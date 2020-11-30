# pyclesperanto
pyclesperanto is a prototype for [clEsperanto](http://clesperanto.net) - a multi-platform multi-language framework for GPU-accelerated image processing. 
It uses [OpenCL kernels](https://github.com/clEsperanto/clij-opencl-kernels/tree/development/src/main/java/net/haesleinhuepf/clij/kernels) from [CLIJ](http://clij.github.io/)

Right now, this is very preliminary.

## Reference
The [full reference](https://clij.github.io/clij2-docs/reference__pyclesperanto) is available as part of the CLIJ2 documentation.

## Installation
* Get a python environment, e.g. via [mini-conda](https://docs.conda.io/en/latest/miniconda.html)
* Install [pyopencl](https://documen.tician.de/pyopencl/).

If installation of pyopencl for Windows fails, consider downloading a precompiled wheel (e.g. from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopencl) ) and installing it manually:

```
pip install pyopencl-2019.1.1+cl12-cp37-cp37m-win_amd64.whl
```

Afterwards, install pyclesperanto:

```
pip install pyclesperanto-prototype
```

### Troubleshooting installation
If you receive an error like 
```
DLL load failed: The specified procedure could not be found.
```
Try downloading and installing a pyopencl with a lower cl version, e.g. cl12 : pyopencl-2020.1+cl12-cp37-cp37m-win_amd64

## Example code
A basic image procressing workflow loads blobs.gif and counts the number of gold particles:

```python
import pyclesperanto_prototype as cle

from skimage.io import imread, imsave

# initialize GPU
cle.select_device("GTX")
print("Used GPU: " + cle.get_device().name)

# load data
image = imread('https://imagej.nih.gov/ij/images/blobs.gif')
print("Loaded image size: " + str(image.shape))

# push image to GPU memory
input = cle.push(image)
print("Image size in GPU: " + str(input.shape))

# process the image
inverted = cle.subtract_image_from_scalar(image, scalar=255)
blurred = cle.gaussian_blur(inverted, sigma_x=1, sigma_y=1)
binary = cle.threshold_otsu(blurred)
labeled = cle.connected_components_labeling_box(binary)

# The maxmium intensity in a label image corresponds to the number of objects
num_labels = cle.maximum_of_all_pixels(labeled)

# print out result
print("Num objects in the image: " + str(num_labels))

# for debugging: print out image
print(labeled)

# for debugging: save image to disc
imsave("result.tif", cle.pull(labeled))
```

## Example gallery 

<table border="0">
<tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_select_GPU.png" width="300"/>

</td><td>

[Select GPU](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/select_GPU.py)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_count_blobs.png" width="300"/>

</td><td>

[Counting blobs](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/count_blobs.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_crop_and_paste_images.png" width="300"/>


</td><td>

[Crop and paste images](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/crop_and_paste_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_inspecting_3d_images.png" width="300"/>

</td><td>

[Inspecting 3D image data](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/inspecting_3d_images.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_multiply_vectors_and_matrices.png" width="300"/>

</td><td>

[Multiply vectors and matrices](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_vectors_and_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_multiply_matrices.png" width="300"/>

</td><td>

[Matrix multiplication](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/multiply_matrices.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_spots_pointlists_matrices_tables.png" width="300"/>

</td><td>

[Working with spots, pointlist and matrices](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/spots_pointlists_matrices_tables.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_voronoi_diagrams.png" width="300"/>

</td><td>

[Voronoi diagrams](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/basics/voronoi_diagrams.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_tribolium_napari.png" width="300"/>

</td><td>

[Tribolium morphometry + Napari](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium.py)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_tribolium_morphometry.png" width="300"/>

</td><td>

[Tribolium morphometry](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/tribolium_morphometry/tribolium_morphometry.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_napari_dask.png" width="300"/>

</td><td>

[Napari+Dask Timelapse processing](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/napari_gui/napari_dask.ipynb)

</td></tr><tr><td>

<img src="https://github.com/pyclesperanto_prototype/tree/master/docs/images/screenshot_particle_analyzer.png" width="300"/>

</td><td>

[Napari Particle Analyser](https://github.com/clEsperanto/pyclesperanto_prototype/tree/master/demo/napari_gui/particle_analyser.py)

</td></tr></table>





## Feedback welcome!
clEsperanto is developed in the open because we believe in the [open source community](https://clij.github.io/clij2-docs/community_guidelines). Feel free to drop feedback as [github issue](https://github.com/clEsperanto/pyclesperanto_prototype/issues) or via [image.sc](https://image.sc)
