# BlurImage

### Setup
```
source .venv/bin/activate
pip install -r requirements.txt
```
### How it works
```
❯ python3 BlurImage.py --help
usage: BlurImage.py [-h] [--folder FOLDER] [image] kernel_size sigma

Applies gaussian blur to image or folder of images. Result is saved in the same folder as image

positional arguments:
  image                Specifies image to blur
  kernel_size          Kernel size of gaussian blur
  sigma                Sigma of blur

options:
  -h, --help           show this help message and exit
  --folder, -f FOLDER  Will process all images in specified folder
```
