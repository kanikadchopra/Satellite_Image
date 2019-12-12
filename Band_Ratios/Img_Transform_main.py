# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:27:47 2019

@author: Kanika Chopra
"""

from Img_Transform_helper import transform_image
import argparse

def main():
    ''' 
    Enter the input_fp, equation and output_fp from the Command line and it 
    will perform the transform_image function on the image in the input_fp 
    and export it to the output_fp by applying the equation to the given bands
    
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
    parser = argparse.ArgumentParser(description='Equation applied for Images')
    parser.add_argument('input-fp', help='The path to the image')
    parser.add_argument('--output-fp', type=str, default=None,
                        help='The path to export the transformed image')
    parser.add_argument('--equations', nargs='*', type=str, required= True, 
                        help='The equations to apply to the bands in the image')

    args = parser.parse_args()

    transform_image(input_fp=args.input_fp,
                    equation=args.equation,
                    output_fp=args.output_fp)

if __name__ == '__main__':
    main()
