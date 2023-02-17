import os
import cv2

def crop_image(image, crop_factor):
    height, width = image.shape[:2]
    crop_width = int(width / crop_factor)
    crops = [image[:, i*crop_width:(i+1)*crop_width] for i in range(crop_factor)]
    return crops

# specify the path to your images folder
images_folder = "Export"

# specify the number of crops to be made per image
crop_factor = 4

for i in range(1, 223):
    filename = f"A_{str(i).zfill(4)}.png"
    image_path = os.path.join(images_folder, filename)
    image = cv2.imread(image_path)

    # crop the image horizontally into 4 parts
    crops = crop_image(image, crop_factor)

    # save each crop in separate folders
    for j in range(crop_factor):
        crop = crops[j]
        crop_folder = f"crop_{j+1}"
        crop_path = os.path.join(crop_folder, filename)

        if not os.path.exists(crop_folder):
            os.makedirs(crop_folder)

        cv2.imwrite(crop_path, crop)
