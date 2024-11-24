import argparse

# -total 1988 athlete_events.tsv
#

parser = argparse.ArgumentParser()
parser.add_argument('-total', type=str, help='year for total count', required=False)
parser.add_argument('-interactive', help='output statistics for given country',
                    required=False, action='store_true')
parser.add_argument('input_file', help='input file path')

args = parser.parse_args()

input_file = args.input_file
input_year = args.total
interactive = args.interactive

if input_year:
    with open(input_file) as file:
        country_medals = {}
        next_line = file.readline()

        while next_line:
            s = splitted = next_line.split('\t')
            team, year, medal = s[6], s[9], s[14].replace('\n', '')

            if year == input_year and medal != 'NA':
                if team not in country_medals:
                    country_medals[team] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                country_medals[team][medal] += 1
            next_line = file.readline()

        print('team  Gold  Silver  Bronze')
        for team in country_medals:
            if any(country_medals[team][medal] == 1 for medal in ['Gold', 'Silver', 'Bronze']):
                print(f'{team} - '
                      f'{country_medals[team]["Gold"]} - '
                      f'{country_medals[team]["Silver"]} - '
                      f'{country_medals[team]["Bronze"]}')

if interactive:
    input_file = args.input_file
    input_country = input('Please enter country: ')
    first_year = ''
    year_statistics = dict()

    with open(input_file) as file:
        for line in file:
            s = splitted = line.split('\t')
            team, country, games, year, sport, medal = s[6], s[7], s[8], s[9], s[12], s[14]
            
            if input_country not in [team, country]:
                continue
            if len(first_year) == 0 or int(year) < int(first_year):
                first_year = year

            if games not in year_statistics:
                year_statistics[games] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
            year_statistics[games][medal] += 1