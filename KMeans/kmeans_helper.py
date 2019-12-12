# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:20:52 2019

@author: Kanika Chopra
"""

import os
import rasterio as rio
import numpy as np

from sklearn.preprocessing import scale
from sklearn.cluster import KMeans

def clustering_image(input_fp, n_clusters, output_fp=None, band_lst=None):
    ''' 
    Takes an image of the format .TIF from the input_fp and conducts k-means 
    clustering with n_clusters to get a single-band image outputting into the 
    output_fp. If band_lst is specified, it will only conduct the k-means 
    clustering on the specified bands.
    
    
    Args: 
        input_fp (str): The file path to retrieve the .TIF file from 
        n_clusters (int): The number of clusters for k-means clustering
        output_fp (str): The file path to export the image to once it is 
        transformed
            None, _kmeans + n_clusters will be added to the input filepath 
            (default: None)
        band_lst (lst): The list of bands in the image that you want to transform
            None, all of the bands will be used. 
            (default: None)
    Returns:
        None, it will print that the New Kmeans image is stored in the 
        output_fp
        
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
        
       
    # We convert (n_bands, height, width) to an array of shape (n_pixel, n_bands)
    flattened_img = img.reshape(n_bands, -1)
    flattened_img = flattened_img.T
    n_pixels = flattened_img.shape[0]
    
    # Create an empty array for the results
    KMeans_results = np.ones(n_pixels) * -1 

    # Collecting the Data that only has the non-nulls
    null_mask = np.isnan(flattened_img).all(axis=1)
    notnull_array = flattened_img[~null_mask]
    
    # K-Means Clustering with the non Null array
    results = kmeans(notnull_array, n_clusters, n_pixels)
    
    # Replacing the correct rows of the KMeans_results with the clustering
    KMeans_results[~null_mask] = results
    
    # Reshaping data to a single-band image (1, height, width)
    KMeans_results = KMeans_results.reshape(1, height, width)

    # Export the image 
    if output_fp is None:
        output_fp = append_file_suffix(input_fp, 'kmeans' + str(n_clusters))
    
    # Update destination metadata
    dst_meta = src_meta.copy()
    dst_meta['dtype'] = 'float64'
    dst_meta['nodata'] = -1
    dst_meta['count'] = 1 

    with rio.open(output_fp, 'w', **dst_meta) as dst:
        dst.write(KMeans_results)
    
    
    print('New Image after K-Means Clustering stored in ' + output_fp)
    
    
def kmeans(array, n_clusters, n_pixels):
    '''
    Standardizes the array and performs K-Means Clustering with n_clusters 
    
    Args: 
        array (np.array): The array for K-Means Clustering (has no Nulls).
        n_clusters (int): The number of clusters to organize the data into 
        when clustering.
        n_pixels (int): The number of pixels in the satellite image.
        
    Returns:
        An array after the K-Means Clustering where the values are cluster values 
        from (0, 1, 2, ..., n_clusters-1)
            
    @author: Kanika Chopra
    '''

    # Standardize the array 
    std_array = scale(array, axis=0)
    
    # K-Means Clustering
    Kmean = KMeans(n_clusters = n_clusters, init='k-means++')
    Kmean.fit(std_array)
    
    X_clustered = Kmean.labels_    
    
    return X_clustered 

    
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
    