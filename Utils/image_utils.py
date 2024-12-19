from PIL import Image, ImageFile, ImageOps
from pathlib import Path
import os
import math
import shutil


def resize_image(img_path: Path, out_img_path: Path, width: int, height: int) -> None:
    image = Image.open(img_path)

    # NOTE: Formatting the file name for better clarity
    out_path = out_img_path.with_name(file.name.replace('[ORIGINAL]', '[RESIZED]'))

    resized_image = image.resize((width, height))
    resized_image.save(out_path)


def rotate_image(img_path: Path, out_img_path: Path) -> None:
    image = Image.open(img_path)

    # Rotates from 10° to 350° by a step of 10°
    for angle in range(10, 360, 10):

        # NOTE: Formatting the file name for better clarity
        out_path = out_img_path.with_name(out_img_path.name.replace('[RESIZED]', f'[ROTATED {angle}°]'))

        rotated_image = image.rotate(angle, expand=True)
        rotated_image.save(out_path)


# Código que vai pro Colab

DATASET_PATH = Path('./Dataset')
MODIFIED_DATASET_PATH = Path('./Modified Dataset')

GALAXIES_FOLDER = Path(DATASET_PATH / 'Galaxies/')
MODIFIED_GALAXIES_FOLDER = Path(MODIFIED_DATASET_PATH / 'Galaxies/')

PLANETS_FOLDER = Path(DATASET_PATH / 'Planets/')
MODIFIED_PLANETS_FOLDER = Path(MODIFIED_DATASET_PATH / 'Planets/')




should_resize: int = len(os.listdir(GALAXIES_FOLDER))
resized_count: int = 0
# NOTE: Resizes all galaxies images from 'Dataset/Galaxies' to 'Modified Dataset/Galaxies' 
for file in os.listdir(GALAXIES_FOLDER):
    file = Path(file)
    
    resize_image(
        img_path=Path(GALAXIES_FOLDER / file),
        out_img_path=Path(MODIFIED_GALAXIES_FOLDER / file),
        width=750,
        height=750,
    )

    resized_count += 1
    print(f'Successfully resized:   {file.name}!')

else:
    print(f'\n[INFO] - - -> Resized a total of: {resized_count} files. Should have resized: {should_resize} files.\n')


should_resize: int = len(os.listdir(PLANETS_FOLDER))
resized_count: int = 0
# NOTE: Resizes all planets images from 'Dataset/Planets' to 'Modified Dataset/Planets' 
for file in os.listdir(PLANETS_FOLDER):
    file = Path(file)
    
    resize_image(
        img_path=Path(PLANETS_FOLDER / file),
        out_img_path=Path(MODIFIED_PLANETS_FOLDER / file),
        width=750,
        height=750,
    )

    resized_count += 1
    print(f'Successfully resized:   {file.name}!')
    
else:
    print(f'\n[INFO] - - -> Resized a total of: {resized_count} files. Should have resized: {should_resize} files.\n')




should_rotate: int = len(os.listdir(MODIFIED_GALAXIES_FOLDER))
rotated_count: int = 0
# Performs a data augmentation
for file in os.listdir(MODIFIED_GALAXIES_FOLDER):
    file = Path(file)

    rotate_image(
        img_path=Path(MODIFIED_GALAXIES_FOLDER / file),
        out_img_path=Path(MODIFIED_GALAXIES_FOLDER / file)
    )

    print(f'Successfully rotated {file.name}!')
else:
    print(f'\n[INFO] - - -> Rotated a total of: {resized_count} files. Should have rotated: {should_resize} files.')


should_rotate: int = len(os.listdir(MODIFIED_PLANETS_FOLDER))
rotated_count: int = 0
# Performs a data augmentation
for file in os.listdir(MODIFIED_PLANETS_FOLDER):
    file = Path(file)

    rotate_image(
        img_path=Path(MODIFIED_PLANETS_FOLDER / file),
        out_img_path=Path(MODIFIED_PLANETS_FOLDER / file)
    )

    print(f'Successfully rotated {file.name}!')
else:
    print(f'\n[INFO] - - -> Rotated a total of: {resized_count} files. Should have rotated: {should_resize} files.')
