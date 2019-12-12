# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:56:45 2019

@author: Kanika Chopra
"""

from kmeans_helper import clustering_image
import argparse

def main():
    ''' 
    Enter the input_fp, n_clusters, output_fp and band_lst from the Command line
    and it will perform the clustering_image function on the image in the 
    input_fp and export it to the output_fp based on a k-means clustering with 
    n_clusters. If band_lst is specified, it will only conduct the k-means 
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
        None, it will print that the New k-means image is stored in the 
        output_fp
        
    @author: Kanika Chopra
    '''
    
    parser = argparse.ArgumentParser(description='K-Means Clustering for Images')
    parser.add_argument('input-fp', help='The path to the image')
    parser.add_argument('-n', '--n-clusters', type=int, required=True,
                        help='The number of clusters for k-means clustering')
    parser.add_argument('--output-fp', type=str, default=None,
                        help='The path to export the single-band clustered image')
    parser.add_argument('--band-lst', type=list, default=None,
                        help='The list of bands to apply the k-means to if not all')

    args = parser.parse_args()
    
    clustering_image(input_fp=args.input_fp,
                    n_clusters=args.n_clusters,
                    output_fp=args.output_fp,
                    band_lst = args.band_lst)
if __name__ == '__main__':
    main()
