# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 15:58:00 2019

@author: Kanika Chopra

"""

from PCA_helper import transform_image
import argparse

def main():
    ''' 
    Enter the input_fp, n_components, output_fp and band_lst from the Command line and it 
    will perform the transform_image function on the image in the input_fp 
    and export it to the output_fp based on a PCA with n_components. 
    If band_lst is specified, it will only conduct the PCA on the specified 
    bands. 
    
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
    parser = argparse.ArgumentParser(description='PCA for Images')
    parser.add_argument('input-fp', help='The path to the image')
    parser.add_argument('-n', '--n-components', type=int, required=True,
                        help='The number of dimensions to reduce image array to \
                        with PCA')
    parser.add_argument('--output-fp', type=str, default=None,
                        help='The path to export the transformed image')
    parser.add_argument('--band-lst', type=list, default=None,
                        help='The list of bands to apply the PCA to if not all')

    args = parser.parse_args()

    transform_image(input_fp=args.input_fp,
                    n_components=args.n_components,
                    output_fp=args.output_fp,
                    band_lst = args.band_lst)

if __name__ == '__main__':
    main()
