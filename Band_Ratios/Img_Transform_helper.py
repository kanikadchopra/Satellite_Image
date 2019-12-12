# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:18:53 2019

@author: Kanika Chopra
"""

import os
import rasterio as rio
import numpy as np

def transform_image(input_fp, output_fp=None, *equations):
    ''' 
    Transforms an image of format .TIF from the input_fp using the equation 
    given and then exports it to output_fp. 
    
    Args: 
        input_fp (str): The file path to retrieve the .TIF file from 
        output_fp (str): The file path to export the image to once it is 
        transformed.
            None, _transformed will be added to the input filepath (default: None)
        *equations: Variable length argument list of equations to transform the image; image will
        be transformed in this specific order. Must refer to bands as B1, B2, B3, etc. 
        
    Returns:
        None, it will print that the New Transformed Image is stored in the 
        output_fp
        
    @author: Kanika Chopra
    '''
    # Import and open the image
    sat_data = rio.open(input_fp)
    
    # Gather the metadata and collect height and width
    src_meta = sat_data.meta
    height = src_meta['height']
    width = src_meta['width']

    # Read the image
    img = sat_data.read()
    
    # Create a dictionary with all the bands
    bands = {'B%d'%(i+1): img[i] for i in list(range(img.shape[0]))}
    
    # Unpack the dictionary as local variables
    locals().update(bands)
    
    # Evaluate our equations on the bands and append to an overall array
    num_eqns = len(equations)
    
    # Create an empty array to index your results into later
    transformed_array = np.zeros((num_eqns, height, width))
    
    for i in range(num_eqns):
        transformed_array[i] = eval(equations[i])
        print('Equation %d:' % (i+1), equations[i])
    
    # Export the image 
    if output_fp is None:
        output_fp = append_file_suffix(input_fp, 'transformed')
        
    # Recreate the metadata and set count to 1 since we want a single-band image
    dst_meta = src_meta.copy()
    dst_meta['count'] = num_eqns
    
    with rio.open(output_fp, 'w', **dst_meta) as dst:
        dst.write(result)
    
    print('New Image after equation(s) applied stored in ' + output_fp)
    
def append_file_suffix(filepath, suffix=None):
    ''' Appends a suffix to a filepath. 
    Args: 
        filepath (str): The file path to modify. 
        suffix (str): The suffix to be appended to the filepath string 
            None, no suffix is appended (default: None)
    Returns: 
        str: The file path with added suffix
    @author: charles
    '''
    name, ext = os.path.splitext(filepath)
    if suffix is not None: 
        filepath = "{name}_{uid}{ext}".format(name=name, uid=suffix, ext=ext)
        
    return filepath
    