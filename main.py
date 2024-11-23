import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input file path')
parser.add_argument('--medals', '-m', nargs=2,  required=False)

args = parser.parse_args()
input_file = args.input_file
medals_input = args.medals

with open('data.tsv', 'r', encoding='utf-8') as file:
    header = file.readline().strip()

    columns = header.split('\t')
    NOC = 7     #header.index('NOC')
    YEARS = 9   #header.index('Year')
    TEAMS = 6   #header.index('Team')
    NAME = 1    #header.index('Name')
    SPORT = 12  #header.index('Sport')
    MEDAL = 14  #header.index('Medal')

    results = []

    next_line = file.readline()
    while next_line:
        row = next_line.strip().split('\t')
    # do stuff with line
        if medals_input:
            country = medals_input[0]
            year = medals_input[1]

            if (row[NOC] == country and row[YEARS] == year) or (row[TEAMS] == country and row[YEARS] == year):
                results.append(f"{row[NAME]}     {row[SPORT]}    {row[MEDAL]}")
            # else:
            #     print('incorrect input')
            #     break
        next_line = file.readline()

if not results:
    print('not found')
    exit()
else:
    if len(results) >= 10:
        for r in results[:10]:
            print(f"{r}")
    else:
        for r in results[:len(results)]:
            print(f"{r}")


gold_medals = 0
silver_medals = 0
bronze_medals = 0
for res in results:
    if "Gold" in res:
        gold_medals += 1
    elif 'Silver' in res:
        silver_medals += 1
    elif 'Bronze' in res:
        bronze_medals += 1

print(f"{country} in {year} had {gold_medals} gold medals, {silver_medals} silver medals and {bronze_medals} bronze medals")






