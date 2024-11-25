import argparse
from total import Total
from interactive import Interactive
from medals import Medals


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-total', type=str, help='year for total count', required=False)
    parser.add_argument('-interactive', help='output statistics for given country',
                        required=False, action='store_true')
    parser.add_argument('input_file', help='input file path')
    parser.add_argument('--medals', '-m', nargs=2,  required=False)



    args = parser.parse_args()

    input_file = args.input_file
    total_year = args.total
    interactive = args.interactive
    medals_input = args.medals


    if total_year:
        # -total 1988 athlete_events.tsv
        medal_stats = Total(input_file, total_year)
        medal_stats.process_data()
        medal_stats.print_medals()
    if interactive:
        # -interactive (USA, Afghanistan, FIN, EST)
        stats = Interactive(input_file)
        stats.process_countries()
        stats.print_statistic()
    if medals_input:
        overall_ = Medals(input_file, medals_input)
        overall_.process_data(medals_input)
        overall_.print_results()


if __name__ == '__main__':
    main()
