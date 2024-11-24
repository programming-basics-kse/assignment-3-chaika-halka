import argparse
from total import Total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-total', type=str, help='year for total count', required=False)
    parser.add_argument('-interactive', help='output statistics for given country',
                        required=False, action='store_true')
    parser.add_argument('input_file', help='input file path')

    args = parser.parse_args()

    input_file = args.input_file
    total_year = args.total
    interactive = args.interactive

    if total_year:
        medal_stats = Total(input_file, total_year)
        medal_stats.process_data()
        medal_stats.print_medals()
    if interactive:
        pass
        # some code


if __name__ == '__main__':
    main()
