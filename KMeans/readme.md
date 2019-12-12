# K-Means Clustering
A project to conduct K-Means Clustering on Satellite Images and create a CLI program for generalized K-Means Clustering. Inputs a .TIF file from given filepath and then using a given number of clusters, it will output a export a single-band image after conducting K-Means Clustering with the number of clusters.
There is also a generalized function where you input the filepath to the .TIF file, the number of clusters for the K-Means Clustering, and it will complete the steps and export the transformed image. 

## Steps to Run:
1. Install virtualenv: `pip install virtualenv`
2. Create your virtual environment: `virtualenv kmeans`
3. Activate your virtual environment: `source kmeans\bin\activate`
4. Install pip packages: `pip install -r requirements.txt`
5. Create the virtual environment kernel for your jupyter notebook: `ipython kernel install --user --name=satellites_img_kmeans`
6. Run the jupyter notebook `jupyter notebook`

## Main Files:
- **K-Means Clustering.ipynb:** Jupyter Notebook to conduct the K-Means Clustering on the satellite image and go through the process; generalized function at the end.
- **kmeans_helper.py:** The helper functions to conduct K-Means Clustering on the image and append a suffix to the filepath.
- **kmeans_main.py:** The command line interface program to connect the kmeans_helper to the command line.
- **requirements.txt:** Python libraries for installation

## Other Files:
- **KMeans Clustering - Satellite Image.ipynb:** Jupyter notebook on a different Satellite Image with no Nulls conducting K-Means Clustering 
- **KMeans Clustering - Wholesale Data:** Jupyter notebook conducting K-Means Clustering on wholesale data; experimenting with another set of data. 
