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

    next_line = file.readline()

    years = []

    while next_line:
        row = next_line.strip().split('\t')
    # do stuff with line
        if overall_input:
            for o in overall_input:
                if o == row[NOC]:               #?
                    years.append(row[YEARS])
        next_line = file.readline()

print(years)




