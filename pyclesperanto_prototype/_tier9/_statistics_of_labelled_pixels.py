from skimage.measure import regionprops

from .._tier0 import Image
from .._tier0 import create_none
from .._tier0 import plugin_function
from .._tier0 import pull_zyx

@plugin_function(output_creator=create_none)
def statistics_of_labelled_pixels(input_image : Image, input_label_map : Image):

    label_image = pull_zyx(input_label_map).astype(int)
    intensity_image = pull_zyx(input_image)

    props = regionprops(label_image, intensity_image=intensity_image, cache=True)
    return props

