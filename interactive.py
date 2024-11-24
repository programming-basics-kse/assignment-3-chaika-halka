class Interactive:
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
