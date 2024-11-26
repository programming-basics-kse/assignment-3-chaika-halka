class Overall:
    def __init__(self, input_file, overall_input):
        self.input_file = input_file
        self.input_countries = overall_input
        self.years_dict = {}

    def process_data(self, overall_input):
        with open('data.tsv', 'r', encoding='utf-8') as file:
            header = file.readline().strip()

            columns = header.split('\t')
            NOC = 7  # header.index('NOC')
            YEARS = 9  # header.index('Year')
            MEDAL = 14  # header.index('Medal')
            TEAM = 6  # header.index('Team')
            results = {}
            if overall_input:
                for o in overall_input:
                    years_dict = {}
                    file.seek(0)
                    header = file.readline()
                    for line in file:
                        row = line.strip().split('\t')
                        if o == row[TEAM]:
                            if row[MEDAL] != 'NA':
                                year = int(row[YEARS])
                            if year in years_dict:
                                years_dict[year] += 1
                            else:
                                years_dict[year] = 1
                    max_year_medals = max(self.years_dict.values())
                    for year, medals in self.years_dict.items():
                        if medals == max_year_medals:
                            max_year = year
                    results[o] = (max_year, max_year_medals)
        return results

    def print_max_year(self):
        results = self.process_data()
        for o, (max_year, max_year_medals) in results.items():
            print(f"{o} - Year: {max_year}, Medals: {max_year_medals}")
