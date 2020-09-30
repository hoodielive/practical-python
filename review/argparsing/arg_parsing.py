import argparse

def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description = "A simple argument parser to show Nick",
        epilog = "Usage."
    )

    parser.add_argument('-x', action="store", required=True, help='Help text for option X')
    parser.add_argument('-y', help='Help text for option Y', default=False)
    parser.add_argument('-z', help='Help text for option Z', type=int)

if __name__ == '__main__':
    get_args()
