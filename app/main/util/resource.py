import os
import shutil
from glob import glob


def save_image(imdir, filename, im):
    try:
        im.save(os.path.join(imdir, filename))
    except:
        return False
    return True


def delete_image(imdir, filename):
    try:
        os.remove(os.path.join(imdir, filename))
    except:
        return False
    return True


def delete_images(imdir, staff_id):
    try:
        filenames = glob(os.path.join(imdir, staff_id) + '*')
        for fn in filenames:
            os.remove(os.path.join(imdir, fn))
    except:
        return False
    return True
