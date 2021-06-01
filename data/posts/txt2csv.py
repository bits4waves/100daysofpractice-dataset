from datetime import datetime
import csv


CORE = 'violincase-posts-with-it-dates'
TXT = CORE + '.txt'
CSV = CORE + '.csv'


with open (TXT, 'r') as txtfile,\
     open (CSV, 'w') as csvfile:
    csvw = csv.writer(csvfile)
    for line in txtfile:
        # example of a line: 2021-04-10_18-58-11_UTC
        date_str = line.split('_')[0].split('-')
        date_int = tuple((int(x) for x in date_str))
        date = datetime(*date_int)
        csvw.writerow([date])
