import argparse
import os
import cv2


def blur_folder(folder, kernel_size, sigma):

    if folder is None:
        print("Folder not provided. Invalid argument")
        exit(1)

    if not os.path.exists(folder):
        print("Folder not found. Invalid argument")
        exit(1)


    blurred_folder = folder +"/blur"
    if not os.path.exists(blurred_folder):
        os.makedirs(blurred_folder)


    for filename in os.listdir(folder):
        image_path = folder + "/" + filename
        image = cv2.imread(image_path)

        try:
            blurred_image = cv2.GaussianBlur(image, [kernel_size, kernel_size], sigma)
        except cv2.error as e:
            print(filename + " is not an image. File wasn't blurred")
            continue

        output_path = get_path_with_updated_filename(image_path, blurred_folder)
        cv2.imwrite(str(output_path), blurred_image)
        print(output_path)




def blur_image(image_path, kernel_size, sigma):

    if image_path is None:
        print("Image path is not provided. Invalid argument")
        exit(1)

    if not os.path.exists(image_path):
        print("Image not found. Invalid argument")
        exit(1)


    image = cv2.imread(image_path)

    blurred_image = cv2.GaussianBlur(image, [kernel_size, kernel_size], sigma)

    output_path = get_path_with_updated_filename(image_path)

    cv2.imwrite(str(output_path), blurred_image)
    print(output_path)



def get_path_with_updated_filename(image_path, subfolder_path=None):
    filename_with_extension = os.path.basename(image_path)
    filename, extension = os.path.splitext(filename_with_extension)
    output_filename = filename+"_blur" + extension


    if subfolder_path is not None:
        base_directory = subfolder_path
    else:
        base_directory = os.path.dirname(image_path)

    output_path = os.path.join(base_directory, output_filename)

    if not os.path.exists(output_path):
        return output_path


    # in case of duplicates
    counter = 1
    while os.path.exists(output_path):
        new_filename = f"{filename}_blur({counter})" + extension
        output_path = os.path.join(base_directory, new_filename)
        counter += 1


    return output_path




def main():

    arg_parser = argparse.ArgumentParser(description='Applies gaussian blur to image or folder of images. '
                                                     'Result is saved in the same folder as image')

    arg_parser.add_argument('--folder', '-f', type=str, default=None, help='Will process all images in specified folder')
    arg_parser.add_argument( "image", nargs='?' , type=str, help='Specifies image to blur')
    arg_parser.add_argument( "kernel_size", type=int, help='Kernel size of gaussian blur')
    arg_parser.add_argument( "sigma", type=float, help='Sigma of blur')


    args = arg_parser.parse_args()

    if args.kernel_size % 2 == 0:
        print("Kernel size must be odd. Invalid argument")
        exit(1)
    if args.kernel_size < 0:
        print("Kernel size must be positive. Invalid argument")
        exit(1)


    if args.folder:
        blur_folder(args.folder, args.kernel_size, args.sigma)
    else:
        blur_image(args.image, args.kernel_size, args.sigma)


if __name__ == '__main__':
    main()


