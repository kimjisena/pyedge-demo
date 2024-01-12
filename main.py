import argparse
#...(pipenv install Pillow)

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
    
    image = None
    #...
    pixels_array = None

    return pixels_array, image.width, image.height

def save_image(file_path, result_image):
    #...
    pass

def main():
    # parse command line arguments
    args = parse_arguments();

    #...

    # optionally print verbose information
    if args.verbose:
        print(f'sobel edge detection applied to {args.input}.\nResult saved to {args.output}')

if __name__ == '__main__':
    main()
