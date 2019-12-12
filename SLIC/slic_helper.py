# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:10:29 2019

@author: Kanika Chopra
"""

# Import the libraries
from skimage.segmentation import slic
from skimage.util import img_as_float
import rasterio as rio
import numpy as np
import os

def slic_image(input_fp, n_segments, compactness=10.0, sigma=1.0, band_lst=None, output_fp=None):
    '''
    Insert description here
    
    Args: 
        input_fp (str): The file path to retrieve the .TIF file from 
        n_segments (int): The (approximate) number of labels in the segmented 
        output image.
        compactness (float): The compactness of the segments; balances color
        proximity and space proximity so higher values give more weight to 
        space proximity making superpixels cubic/square.
            (default: 10.0)
        sigma (float): Width of Gaussian smoothing kernel for pre-processing for 
        each dimension of the image. Zero means no smoothing.
            (default: 1.0)
        band_lst (lst): The list of bands in the image that you want to transform.
            None, all of the bands will be used.
            (default: None)
        output_fp (str): The file path to export the image to once it is 
        transformed
            None, _slic + n_segments will be added to the input filepath 
            (default: None)
            
    Returns:
        None, it will print that the new segments image is stored in the 
        output_fp 
    
    @author: Kanika Chopra
        
    '''
    # Read in the input filepath
    sat_data = rio.open(input_fp)
    
    # Get the metadata
    src_meta = sat_data.metadata
    
    if band_lst is not None:
        img = img_as_float(sat_data.read(band_lst))
    else:
        img = img_as_float(sat_data.read())
        
    # Transform image to be in the format for Scikit-Image: (height, width, n_bands)
    new_image = np.moveaxis(img, 0, -1)
    
    # get SLIC segments
    segments = slic(new_image, n_segments=n_segments, compactness=compactness, 
                    sigma=sigma)
    
    # Add a new dimension to the segments and reshape to (n_bands, height, width)
    final_segments = segments[:, :, np.newaxis]
    final_segments = np.moveaxis(final_segments, -1, 0)
    
    # Change the dtype to int32 so that rasterio can export it 
    final_segments = final_segments.astype('int32')
    
    # Create destination metadata and update information
    dst_meta = src_meta.copy()
    dst_meta['count'] = 1 
    dst_meta['dtype'] = str(final_segments.dtype)
    
    # Export the image 
    if output_fp is None:
        output_fp = append_file_suffix(input_fp, 'slic' + str(n_segments))
        
    # Open a new file in 'write' mode and unpack (**) the destination metadata
    with rio.open(output_fp, 'w', **dst_meta) as dst:
        dst.write(final_segments)
    print("Segments from SLIC with " + str(n_segments) + " saved in " + output_fp)


    
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
    

