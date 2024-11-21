file = open('Olympic Athletes - athlete_events.tsv')
next_line = file.readline()
while next_line:
    # do stuff with line
    print(next_line)
    next_line = file.readline()