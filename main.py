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

    next_line = file.readline()

    # years = []
    # years_dict = {}
    while next_line:
        row = next_line.strip().split('\t')
        if overall_input:
            for o in overall_input:
                years = []
                years_dict = {}
                if o == row[TEAM]:
                    years.append(row[YEARS])
                for year in years:
                    if year in years_dict:
                        years_dict[year] += 1
                    else:
                        years_dict[year] = 1
            #print(f"{o}{years_dict}")
            next_line = file.readline()


print(years_dict)




