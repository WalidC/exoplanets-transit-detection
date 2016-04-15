# Exoplanets transit detection 

A Python program that analyzes 3D FITS images (with the time parameter) from the Spitzer Telescope and outputs a light-curve (Brightness vs Time) of a certain star, enabling the detection of transiting exoplanets in front of the star using the Astropy and Matplotlib libraries.
### Required libraries
The program relies on two important libraries :

* [Astropy] - Python Library for Astronomy applications
* [Matplotlib] - A plotting library

### How to run
```
python FITSpitzer.py /directory/inputfile.fits /directory/output.pdf
```

### Where to get FITS images
The IRAC provides a dataset containing 10 Spitzer observations of XO-3b.

You can select the dataset of your choice from the [IPAC (Infrared Processing and Analysis Center) servers](http://sha.ipac.caltech.edu/applications/Spitzer/SHA/#id=SearchByRequestID&RequestClass=ServerRequest&DoSearch=true&SearchByRequestID.field.requestID=46467072,%2046471424,%2046467840,%2046471168,%2046470144,%2046470912,%2046467584,%2046470656,%2046469376,%2046470400,%2046466816,%2046469632,%2046468864,%2046469120,%2046469888,%2046468608,%2046467328,%2046468352,%2046471680,%2046468096&SearchByRequestID.field.includeSameConstraints=_none_&MoreOptions.field.prodtype=aor&shortDesc=AORKEY&isBookmarkAble=true&isDrillDownRoot=true&isSearchResult=true)
### Future improvements
  - Include PDF generation of the light-curves
  - Work on the GUI
  - Implement automatic FITS files download from the [IRSA (InfraRed Science Archive)](https://irsa.ipac.caltech.edu/frontpage/)


### Version
1.1


[//]: # 
   [Astropy]: <http://www.astropy.org/>
   [Matplotlib]: <http://matplotlib.org/>
   

