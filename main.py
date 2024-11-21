import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-total', type=str, help='year for total count', required=False)
parser.add_argument('input_file', help='input file path')

args = parser.parse_args()

input_file = args.input_file
input_year = args.total

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
            print(f'{team} - {country_medals[team]["Gold"]} - {country_medals[team]["Silver"]} - {country_medals[team]["Bronze"]}')
