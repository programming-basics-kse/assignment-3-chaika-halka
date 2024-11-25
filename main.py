import argparse
from overall import Overall
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('--overall', '-o', nargs='+')

    args = parser.parse_args()
    input_file = args.input_file
    overall_input = args.overall

    if overall_input:
        overall_ = Overall(input_file, overall_input)
        overall_.process_data(overall_input)
        overall_.print_max_year()

if __name__ == '__main__':
    main()