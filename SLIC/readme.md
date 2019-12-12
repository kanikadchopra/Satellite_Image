# Simple Linear Iterative Clustering (SLIC)

A project on completing Simple Linear Iterative Clustering on an image. Inputs a .TIF file for satellite imagery or any other image type from given filepath, number of segments, compactness and sigma factors, a list of bands and the output filepath to export the segments results to. 

There is also a generalized function where you input the filepath to the .TIF file, the number of segments for SLIC, the compactness and sigma, bands to consider and an output filepath and it will complete SLIC and export the segments array back as a .TIF file. 

## Steps to Run:
1. Install virtualenv: `pip install virtualenv`
2. Create your virtual environment: `virtualenv slic`
3. Activate your virtual environment: `source slic\bin\activate`
4. Install pip packages: `pip install -r slic_requirements.txt`
5. Create the virtual environment kernel for your jupyter notebook: `ipython kernel install --user --name=satellite_img_slic`
6. Run the jupyter notebook `jupyter notebook`
 
## Files:
- **slic_helper.py:** The helper functions to conduct SLIC on the image and append a suffix to the filepath.
- **slic_main.py:** The command line interface program to connect the slic_helper to the command line.
- **SLIC - Satellite Imagery.ipynb:** Jupyter Notebook to conduct the SLIC attempting with only non-null values in the image and then with the whole image
- **slic_requirements.txt:** Python libraries for installation
