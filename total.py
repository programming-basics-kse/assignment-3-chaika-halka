class Total:
    def __init__(self, input_file, input_year):
        self.input_file = input_file
        self.input_year = input_year
        self.country_medals = {}

    def process_data(self):
        with open(self.input_file) as file:
            next_line = file.readline()
            while next_line:
                s = next_line.split('\t')
                team, year, medal = s[6], s[9], s[14].strip()

                if self.input_year and year == self.input_year and medal != 'NA':
                    if team not in self.country_medals:
                        self.country_medals[team] = {'Gold': 0, 'Silver': 0, 'Bronze': 0}
                    self.country_medals[team][medal] += 1

                next_line = file.readline()

    def print_medals(self):
        print('team  Gold  Silver  Bronze')
        for team in self.country_medals:
            if any(self.country_medals[team][medal] > 0 for medal in ['Gold', 'Silver', 'Bronze']):
                print(f'{team} - '
                      f'{self.country_medals[team]["Gold"]} - '
                      f'{self.country_medals[team]["Silver"]} - '
                      f'{self.country_medals[team]["Bronze"]}')
