import argparse
import os
from os import PathLike

import cv2

# WIP
def blur_folder(folder, kernel_size, sigma):
    print("Processing folder {}".format(folder))
    # for filename in os.listdir(folder)
    #
    # print(image)


def blur_image(image_path, kernel_size, sigma):

    if image_path is None:
        print("Image path is not provided. Invalid argument")
        exit(1)

    if kernel_size % 2 == 0:
        print("Kernel size must be odd. Invalid argument")
        exit(1)
    if kernel_size < 0:
        print("Kernel size must be positive. Invalid argument")
        exit(1)

    if not os.path.exists(image_path):
        print("Image not found. Invalid argument")
        exit(1)


    image = cv2.imread(image_path)

    blurred_image = cv2.GaussianBlur(image, [kernel_size, kernel_size], sigma)



    output_path = get_new_filename(image_path)

    cv2.imwrite(str(output_path), blurred_image)
    print(output_path)


def get_new_filename(image_path):
    filename_with_extension = os.path.basename(image_path)
    filename, extension = os.path.splitext(filename_with_extension)
    output_filename = "blur_"+filename + extension

    base_directory = os.path.dirname(image_path)
    output_path = os.path.join(base_directory, output_filename)

    if not os.path.exists(output_path):
        return output_path


    # in case of duplicates
    counter = 1
    while os.path.exists(output_path):
        new_filename = f"blur_{filename}({counter})" + extension
        output_path = os.path.join(base_directory, new_filename)
        counter += 1


    return output_path






def main():

    arg_parser = argparse.ArgumentParser(description='Applies gaussian blur to image or folder of images. '
                                                     'Result is saved in the same folder as image')

    arg_parser.add_argument('--folder', '-f', type=str, default=None, help='Will process all images in specified folder. WIP')
    arg_parser.add_argument( "image", nargs='?' , type=str, help='Specifies image to blur')
    arg_parser.add_argument( "kernel_size", type=int, help='Kernel size of gaussian blur')
    arg_parser.add_argument( "sigma", type=int, help='Sigma of blur')


    args = arg_parser.parse_args()


    if args.folder:
        blur_folder(args.folder, args.kernel_size, args.sigma)
    else:
        blur_image(args.image, args.kernel_size, args.sigma)


if __name__ == '__main__':
    main()


