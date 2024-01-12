import ctypes
import argparse
from PIL import Image
import array

# load the c library
sobel_lib = ctypes.CDLL('./lib.so')

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog='pyedge', 
        description='sobel edge detection tool (python and c)'
    )

    parser.add_argument(
        'input', 
        type=str, 
        help='path to the input image file'
    )

    parser.add_argument(
        'output', 
        type=str, 
        help='path to the output image file'
    )

    parser.add_argument(
        '--verbose', 
        action='store_true', 
        help='enable verbose mode'
    )

    return parser.parse_args()

def load_image(file_path):
    # open the input image using pillow
    image = Image.open(file_path)

    # convert the image to grayscale
    image = image.convert('L')

    # get pixel data as a standard python array
    pixels_array = array.array('B', image.tobytes())

    return pixels_array, image.width, image.height

def save_image(file_path, result_image):
    # save the result image using pillow
    result_image.save(file_path)

def main():
    # parse command line arguments
    args = parse_arguments();

    # load the input image
    input_array, width, height = load_image(args.input)

    # create `ctypes`` pointer to the input image data

    # create result array and pointer

    # prepare c function signatures


    # optionally print verbose information
    if args.verbose:
        print(f'sobel edge detection applied to {args.input}.\nResult saved to {args.output}')

if __name__ == '__main__':
    main()
