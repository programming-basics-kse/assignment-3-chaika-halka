import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-total',type=str, help="year for total count", required=False)
parser.add_argument('input_file', help='input file path')

args = parser.parse_args()

input_file = args.input_file
input_country = args.total

with open(input_file) as file:
    next_line = file.readline()
    while next_line:
        s = splitted = next_line.split('\t')
        next_line = file.readline()
