from .unet import *




def get_model(**kwargs):
    return UNet(**kwargs)