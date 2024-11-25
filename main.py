import argparse
from medals import Medals
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('--medals', '-m', nargs=2,  required=False)

    args = parser.parse_args()
    input_file = args.input_file
    medals_input = args.medals

    if medals_input:
        overall_ = Medals(input_file, medals_input)
        overall_.process_data(medals_input)
        overall_.print_results()

if __name__ == '__main__':
    main()
