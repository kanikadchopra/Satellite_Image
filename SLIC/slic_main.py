# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:46:19 2019

@author: Kanika Chopra
"""

from slic_helper import slic_image
import argparse

def main():
    ''' 
    Enter the input_fp, n_segments, compactness, sigma, band_lst and output_fp 
    from the Command line and it will perform SLIC to segment the image from 
    input_fp with approximately n_segments using the compactness and sigma 
    parameters and export it to output_fp. If band_lst is specified, it will 
    only conduct SLIC on the specified bands. 
    
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

    parser = argparse.ArgumentParser(description='SLIC for Image Segmentation')
    
    parser.add_argument('input-fp', help='The path to the image')
    parser.add_argument('-n', '--n-segments', type=int, required=True,
                        help='The number of segments for SLIC')
    parser.add_argument('-n', '--compactness', type=float, default=10.0,
                        help='Compactness of the superpixels')
    parser.add_argument('n', '--sigma', type=float, default=1.0,
                        help='Smoothness of the superpixels')
    parser.add_argument('--band-lst', type=list, default=None,
                        help='The list of bands to apply the SLIC to if not all')
    parser.add_argument('--output-fp', type=str, default=None,
                        help='The path to export the single-band segments image')

    args = parser.parse_args()
    
    slic_image(input_fp=args.input_fp,
                n_segments=args.n_segments,
                compactness=args.compactness,
                sigma=args.sigma,
                band_lst=args.band_lst,
                output_fp=args.output_fp)
    
if __name__ == '__main__':
    main()
