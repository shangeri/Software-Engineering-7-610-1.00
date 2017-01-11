import sys
import os
import csv
import re
import string
import datetime
import calendar


def format_date(date_str, format_str='%b %d %Y %H:%M'):
    # tries to work even when the format of the date string is different
    # in another file...

    # will be simplified...

    d0 = string.translate(date_str, None, ',"')
    d1 = d0.split()

    try:
        del d1[d1.index('at')]
    except IndexError:
        pass

    month_lst = filter(lambda y: y.capitalize() in calendar.month_name, d1)
    month_ind = list(calendar.month_name).index(month_lst[0])
    day_year_lst = filter(lambda y: y.isdigit(), d1)
    time_lst = [x for x in d1 if x not in month_lst and x not in day_year_lst]

    month_abbr = calendar.month_abbr[month_ind]
    day = [s for s in day_year_lst if len(s) <= 2][0]
    year = [s for s in day_year_lst if len(s) == 4][0]
    time_12 = datetime.datetime.strptime(time_lst[0], '%I:%M%p')
    time_24 = time_12.strftime('%H:%M')
    return ' '.join([month_abbr, day, year, time_24, '\n'])



def main():
    if len(sys.argv) != 2:
        prog = os.path.basename(sys.argv[0])
        # different in windows probably
        print('usage: ./{0} <csv_file>'.format(prog))
        sys.exit(1)

    try:
        csv_file = open(sys.argv[1], 'r')
        ll = len(sys.argv[1]) - 4
        output_name = sys.argv[1][0:ll] + '_new.csv'
        output = open(output_name, 'w')
    except IOError:
        print('cant open {0}'.format(sys.argv[1]))
        sys.exit(1)

    # will be extended ... 
    for line in csv_file:
        line_split = line.split('\t')[0:4]
        line_split[3] = format_date(line_split[3])
        output.write('\t'.join(line_split))

    csv_file.close()
    output.close()


if __name__ == '__main__':
    main()

