import os
import pandas as pd
from tqdm import tqdm
from glob import glob


def prepare_data(image_dir, subject_list):
    image_paths = glob(image_dir + '/*')

    # store image data in DataFrame
    df_face_image = pd.DataFrame(columns=['image', 'label', 'id'])

    for i, image_path in tqdm(enumerate(image_paths)):
        name
        images = glob.glob(image_path + '/*')
        for image in images:
            df_face_image.loc[len(df_face_image)] = [image, i, name]

    # save DataFrame to binary file
    if save_file_name is None:
        save_file_name = os.path.join(curr_dir, 'image_data.pkl')
    df_face_image.to_pickle(save_file_name)
