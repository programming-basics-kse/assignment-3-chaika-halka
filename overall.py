class Overall:
    def __init__(self, input_file, overall_input):
        self.input_file = input_file
        self.input_countries = overall_input
        self.years_dict = {}
        self.results = {}
        self.year = ''

    def process_data(self, overall_input):
        with open(self.input_file, 'r', encoding='utf-8') as file:

            if overall_input:
                for country in overall_input:
                    years_dict = {}

                    next_line = file.readline()
                    while next_line:
                        s = splitted = next_line.split('\t')
                        year_f, medal, team = s[9], s[14], s[6]
                        if country == team and medal != 'NA':
                            self.year = year_f
                            if year in years_dict:
                                years_dict[self.year] += 1
                            else:
                                years_dict[self.year] = 1
                        next_line = file.readline()

                    max_year_medals = max(self.years_dict.values())

                    for year, medals in self.years_dict.items():
                        if medals == max_year_medals:
                            max_year = year
                    self.results[country] = (max_year, max_year_medals)

    def print_max_year(self):
        for o, (max_year, max_year_medals) in self.results.items():
            print(f"{o} - Year: {max_year}, Medals: {max_year_medals}")
