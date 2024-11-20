import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-output', help='output file path', required=False)
parser.add_argument('input_file', help='input file path')
parser.add_argument('input_country', help='country')
parser.add_argument('input_year', help='year')

args = parser.parse_args()

input_file = args.input_file
input_country = args.input_country
output_file = args.output

with open(input_file) as file:
    next_line = file.readline()
    while next_line:
        ...
        next_line = file.readline()
