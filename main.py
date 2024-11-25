import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file path')
parser.add_argument('--overall', '-o', nargs='+')

args = parser.parse_args()
input_file = args.input_file
overall_input = args.overall

with open('data.tsv', 'r', encoding='utf-8') as file:
    header = file.readline().strip()

    columns = header.split('\t')
    NOC = 7     #header.index('NOC')
    YEARS = 9   #header.index('Year')
    MEDAL = 14  #header.index('Medal')
    TEAM = 6    #header.index('Team')
    if overall_input:
        for o in overall_input:
            years_dict = {}
            file.seek(0)
            header = file.readline()
            for line in file:
                row = line.strip().split('\t')
                if o == row[TEAM]:
                    year = int(row[YEARS])
                    if year in years_dict:
                        years_dict[year] += 1
                    else:
                        years_dict[year] = 1
            max_year_medals = max(years_dict.values())
            for year, medals in years_dict.items():
                if medals == max_year_medals:
                    max_year = year
            print(f"{o} - Year: {max_year}, Medals: {max_year_medals}")