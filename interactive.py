class Interactive:
    def __init__(self, input_file):
        self.input_file = input_file
        self.input_country = input('Please enter country: ')
        self.first_year = ''
        self.first_olympic_location = ''
        self.year_statistics = dict()

        self.best_year = None
        self.worst_year = None

        self.avr_gold = 0
        self.avr_silver = 0
        self.avr_bronze = 0

    def process_data(self):
        with open(self.input_file) as file:
            # Collect in-memory struct for alter analyis
            for line in file:
                # Each iteration is for one line which contains 1 athlete and his country and medal type

                s = line.split('\t')
                team, country, games, year, sport, medal_type = s[6], s[7], s[8], s[9], s[12], s[14].strip()

                # Ignore other countries
                if self.input_country not in [team, country]:
                    continue

                # Update first year and first olympic location
                if len(self.first_year) == 0 or int(year) < int(self.first_year):
                    self.first_year = year
                    self.first_olympic_location = country

                # Populate new row in year_statistics dict if needed
                if games not in self.year_statistics:
                    self.year_statistics[games] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}

                # Update  medals
                if medal_type != 'NA':
                    self.year_statistics[games][medal_type] += 1

            # Analyze in-memory struct
            total_gold = total_silver = total_bronze = 0
            for key in self.year_statistics:
                value = self.year_statistics[key]
                # key '2005 Winter'
                # value {'Gold': 5, 'Silver': 7, 'Bronze': 2}

                # Populate and update if needed best and worse
                total_medals = value['Gold'] + value['Silver'] + value['Bronze']
                if not self.best_year:
                    self.best_year = (key, value, total_medals)
                if not self.worst_year:
                    self.worst_year = (key, value, total_medals)
                if total_medals > self.best_year[2]:
                    self.best_year = (key, value, total_medals)
                if total_medals < self.worst_year[2]:
                    self.worst_year = (key, value, total_medals)

                # Update totals, we will calculate average later
                total_gold += value['Gold']
                total_silver += value['Silver']
                total_bronze += value['Bronze']

            self.avr_gold = total_gold // len(self.year_statistics)
            self.avg_silver = total_silver // len(self.year_statistics)
            self.avg_bronze = total_bronze // len(self.year_statistics)

    def print_statistic(self):
        if len(self.year_statistics) == 0:
            print('Seems like no such country')

        print(f'In the {self.first_year} {self.input_country} participated in the Olympics for the first time. \n'
              f'In this year Olympics were held in {self.first_olympic_location}. \n'
              f'Country best Olympics: {self.best_year}, \n'
              f'Country worst Olympics: {self.worst_year}.\n'
              f'In average {self.input_country} had {self.avr_gold} gold medal, {self.avg_silver} silver medal, and {self.avg_bronze} bronze medal.')
