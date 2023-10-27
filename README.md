# SEM Image Synthesis from Petrography Images

This repository contains code to synthesize Scanning Electron Microscopy (SEM) images from Polarized Light Microscopy (PLM) images using deep learning techniques like conditional GAN (cGAN) and U-Net.

## Data
The data used is a dataset of images of carbonate concretions from the St Lawrence Estuary in Canada. It contains:

- PLM images in plane polarized light (PPL) 
- PLM images in cross polarized light (XPL)
- SEM images generated using backscattered electron detector (BSD)
- SEM images generated using secondary electron detector (SE) 

The images are provided as 3-channel and 6-channel RGB images for PPL and XPL, and grayscale images for BSD and SE.

## Preprocessing
The `crop_images.py` script is used to crop the large images into smaller crops to create the training data. 
The appropriate preprocessing individual to each method is done in the corresponding notebook.
The crops are saved into separate folders to create the final dataset used for training.

## Models

### cGAN (pix2pix)
The `pix2pix` model from the [pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) repository is used. 

It contains a generator and discriminator based on U-Net architecture.

The model is trained to translate between PPL, XPL and BSD, SE images using adversarial loss and L1 loss.

Training is done using `pip2pix_train.ipynb` notebook.

### U-Net
A standard U-Net model with encoder-decoder structure and skip connections is implemented in `U-net.ipynb`.

It takes 6-channel input (3 from PPL + 3 from XPL) and generates 1-channel SEM image output. It can be adapted to take 3-channel input as well.

The model is trained using binary cross-entropy loss to translate between input and output domains.

## Results

The models are evaluated using MSE, SSIM, PSNR and other metrics.

Adversarial evaluation is also performed using a discriminator model to detect real vs fake SEM images.

Finally, manual evaluation by human experts is conducted to assess synthesized images.

The cGAN model is found to produce more realistic outputs than U-Net, even though the numeric metrics are slightly worse.

## Usage

The code can be used to generate synthesized SEM images from PLM images after training the models on suitable dataset.

This can be helpful for previewing what SEM images might look like for a sample before acquiring actual SEM data.

The models are not meant to replace real SEM imaging but can provide approximate supplemental visualizations.

## References

Omidreza Amrollahinasab, Arash Rabbani (2023): Image translation between Polarized Light Microscopy and Scanning Electron Microscopy via generative adversarial networks

Please cite the papers if you use this code.

## Contributing

Contributions are welcome! Please open an issue or PR if you would like to add a feature or fix a bug.

Python version: 3.8.16 (conda env) is used in this work<br />

suggested structure for the datasets: <br />

>root/ <br />
>>output/ <br />
>>dataset/ <br />
>>>images/ (copy images from crop_1 folder) <br />
>>>masks/ (copy images from crop_3 folder) <br />
  
