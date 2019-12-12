# Band Ratio/Equation Application

A project on applying an equation(s) to the bands referred to in the equation(s) to an image and export it as a single or multi band image depending on the number of equation(s).

There is also a generalized function where you input the filepath to the .TIF file, the equations (**), and the output filepath so it will apply the equation(s) and export the result back as a .TIF file. 

## Steps to Run:
1. Install virtualenv: `pip install virtualenv`
2. Create your virtual environment: `virtualenv bandratio`
3. Activate your virtual environment: `source bandratio\bin\activate`
4. Install pip packages: `pip install -r eqn_requirements.txt`
5. Create the virtual environment kernel for your jupyter notebook: `ipython kernel install --user --name=satellite_img_bandratio`
6. Run the jupyter notebook `jupyter notebook`
 
## Files:
- **Img_Transform_helper.py:** All the helper functions to transform the image and append a suffix to a filepath
- **Img_Transform_main.py:** The command interface file to apply the image transformation
- **Image Transformation.ipynb:** Jupyter notebook to try out the equation application and then the generalized application
- **eqn_requirements.txt:** Python libraries required
