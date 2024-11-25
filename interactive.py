class Interactive:
    def __init__(self, input_file):
        self.input_file = input_file
        self.input_countries = list(input('Please enter country: ').split(', '))
        self.countries_statistics = dict()

    def process_countries(self):
        for input_country in self.input_countries:
            self.process_data(input_country)

    def process_data(self, input_country):
        country_data = {
            'first_year': None,
            'first_olympic_location': None,
            'year_statistics': {},
            'best_year': None,
            'worst_year': None,
            'avr_gold': 0,
            'avr_silver': 0,
            'avr_bronze': 0
        }

        with open(self.input_file) as file:
            # Collect in-memory struct for alter analysis
            for line in file:
                # Each iteration is for one line which contains 1 athlete and his country and medal type

                s = line.split('\t')
                team, country, games, year, sport, medal_type = s[6], s[7], s[8], s[9], s[12], s[14].strip()

                # Ignore other countries
                if input_country not in [team, country]:
                    continue

                # Update first year and first olympic location
                if not country_data['first_year'] or int(year) < int(country_data['first_year']):
                    country_data['first_year'] = year
                    country_data['first_olympic_location'] = country

                # Populate new row in year_statistics dict if needed
                if games not in country_data['year_statistics']:
                    country_data['year_statistics'][games] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}

                # Update  medals
                if medal_type != 'NA':
                    country_data['year_statistics'][games][medal_type] += 1

            # Analyze in-memory struct
            total_gold = total_silver = total_bronze = 0
            for key, value in country_data['year_statistics'].items():
                # key: 1992 Winter
                # value: {'Gold': 5, 'Silver': 7, 'Bronze': 2}

                # Populate and update if needed best and worst
                total_medals = value['Gold'] + value['Silver'] + value['Bronze']

                if not country_data['best_year'] or total_medals > country_data['best_year'][2]:
                    country_data['best_year'] = (key, value, total_medals)
                if not country_data['worst_year'] or total_medals < country_data['worst_year'][2]:
                    country_data['worst_year'] = (key, value, total_medals)

                # Update totals, we will calculate average later
                total_gold += value['Gold']
                total_silver += value['Silver']
                total_bronze += value['Bronze']

            total_games = len(country_data['year_statistics'])
            if total_games > 0:
                country_data['avr_gold'] = total_gold // total_games
                country_data['avg_silver'] = total_silver // total_games
                country_data['avg_bronze'] = total_bronze // total_games

        self.countries_statistics[input_country] = country_data

    def print_statistic(self):
        for input_country, data in self.countries_statistics.items():
            if len(data['year_statistics']) == 0:
                print(f'Seems like no such country {input_country} \n \n')

            print(f'In the {data["first_year"]} {input_country} participated in the Olympics for the first time. \n'
                  f'In this year Olympics were held in {data["first_olympic_location"]}. \n'
                  f'Country best Olympics: {data["best_year"]}, \n'
                  f'Country worst Olympics: {data["worst_year"]}.\n'
                  f'In average {input_country} had {data["avr_gold"]} gold medal, '
                  f'{data["avg_silver"]} silver medal, and {data["avg_bronze"]} bronze medal.'
                  f'\n \n')
