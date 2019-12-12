# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 16:24:12 2019

@author: Kanika Chopra
"""
import os
import rasterio as rio
import numpy as np

from sklearn.preprocessing import scale
from sklearn.decomposition import PCA as sklearnPCA

def transform_image(input_fp, n_components, output_fp=None, band_lst=None):
    ''' 
    Transforms an image of format .TIF from the input_fp using a Principal 
    Component Analysis with n_components and exports it to output_fp.
    
    Args: 
        input_fp (str): The file path to retrieve the .TIF file from 
        n_components (int): The number of components to modify the image array 
        to using PCA.
        output_fp (str): The file path to export the image to once it is 
        transformed.
            None, _PCA will be added to the input filepath (default: None)
        band_lst (lst): The list of bands in the image that you want to transform
            None, all of the bands will be used or n_components if specified
            
    Returns:
        None, it will print that the New PCA Image is stored in the output_fp
        
    @author: Kanika Chopra
    '''
    # Import and open the image
    sat_data = rio.open(input_fp)
    
    # Collect important data from metadata of original image
    src_meta = sat_data.meta
    n_bands = src_meta['count']
    height = src_meta['height']
    width = src_meta['width']
    
    # Read the image
    if band_lst is not None:
        img = sat_data.read(band_lst)
        n_bands = len(band_lst)
    else:
        img = sat_data.read()
        
    print('Image has been read in')
        
    # Set the components if it is None to either number of bands or the length
    # of the band list 
    if n_components is None:
        n_components = n_bands 
        
    # We convert (n_bands, height, width) to an array of shape (n_pixel, n_bands)
    flattened_img = img.reshape(n_bands, -1)
    flattened_img = flattened_img.T
    
    # Collecting the Data that only has the non-nulls
    notnull_array = flattened_img[~np.isnan(flattened_img).all(axis=1)]
    
    # Create an empty array for the results
    PCA_results = np.empty(flattened_img.shape)
    
    # Principal Component Analysis with the NonNull array
    result = pca_analysis(notnull_array, n_components) 
    
    # Replacing the correct rows of the PCA_results with the PCA results and NaNs
    null_idx = np.isnan(flattened_img).any(axis=1)
    PCA_results[null_idx] = flattened_img[null_idx]
    
    notnull_idx = ~np.isnan(flattened_img).any(axis=1)
    PCA_results[notnull_idx] = result[~np.isnan(result).any(axis=1)]
    
    # Reshaping the data back into the original image shape so we can export it 
    PCA_results = PCA_results.T
    PCA_results = PCA_results.reshape(n_bands, height, width)
    
    # Export the image 
    if output_fp is None:
        output_fp = append_file_suffix(input_fp, 'PCA_' + str(n_bands))
        
    dst_meta = src_meta.copy()
    with rio.open(output_fp, 'w', **dst_meta) as dst:
        dst.write(PCA_results)
    
    
    print('New Image after PCA stored in ' + output_fp)
    

def pca_analysis(array, n_components):
    '''
    Standardizes an array and performs a Principal Component Analysis with
    n_components.
    
    Args: 
        array (np.array): The array for the PCA 
        n_components (int): The number of dimensions of the transformed array 
        after PCA
    
    Returns:
        An array after the PCA analysis with dimensions of n_components 
    
    @author: Kanika Chopra
    '''
    
    # Standardize the array
    std_array = scale(array, axis=0)
    
    # Principal Component Analysis
    sklearn_pca = sklearnPCA(n_components=n_components)
    result = sklearn_pca.fit_transform(std_array)
    
    return result
    
    
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
    