import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        prog="pyedge", 
        description="sobel edge detection tool (python and c)"
    )

    #...

    return parser.parse_args();

def main():
    # parse command line arguments
    args = parse_arguments();

    #...

if __name__ == '__main__':
    main()
