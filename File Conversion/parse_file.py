import sys
import os
import string
import calendar
import itertools
import csv


def format_date(date_str, format_str='%b %d %Y %H:%M'):
    """ month name must be grammatically correct english,
        could be fixed with regular expressions """
    if not date_str:
        return

    d0 = string.translate(date_str, None, ',"')
    d1 = d0.split()

    try:
        del d1[d1.index('at')]
    except:
        pass

    month_lst = filter(lambda y: y.capitalize() in calendar.month_name, d1)
    if not month_lst:
        return
    month = month_lst[0].capitalize()
    month_ind = list(calendar.month_name).index(month)
    day_year_lst = filter(lambda y: y.isdigit(), d1)

    day = [s for s in day_year_lst if len(s) <= 2][0]
    year = [s for s in day_year_lst if len(s) == 4][0]

    return '-'.join([year, day, str(month_ind).zfill(2)])


def main():
    """ if a line of the file does not have a seperator between
        the username and the tweet, the line will be discarded!"""
    if len(sys.argv) != 2:
        # probably different in windows
        prog = os.path.basename(sys.argv[0])
        print('usage: python2 {0} <csv_file>'.format(prog))
        sys.exit(1)

    try:
        csv_file = open(sys.argv[1], 'r')
        ll = len(sys.argv[1]) - 4
        output_name = sys.argv[1][0:ll] + '_new.csv'
        output = open(output_name, 'w')
        output.write('date:\t\ttweets:\n')
        discarded_name = sys.argv[1][0:ll] + '_discarded.txt'
        discarded = open(discarded_name, 'w')
    except IOError:
        print('can not open {0}'.format(sys.argv[1]))
        sys.exit(1)

    # very ugly code, because of the ugly input format!
    tw = {}
    for line in csv_file:
        line1 = line.split('\t')[0:4]
        if not len(line1) == 4:
            discarded.write(line)
            continue
        if not len(line1[0]) > 2:
            discarded.write(line)
            continue
        if line1[0][1] != '@':
            discarded.write(line)
            continue
        if len(line1) != 4:
            discarded.write(line)
            continue
        if line1[1] not in tw:
            tw[line1[1]] = format_date(line1[3])

    dix = {}
    tweets = zip(tw.values(), tw.keys())
    for date, tweet in filter(lambda x: x[0], tweets):
        if date not in dix:
            dix[date] = 1
        else:
            dix[date] += 1

    for k, t in dix.items():
        output.write('\t'.join([k, str(t), '\n']))

    # ascii output at the moment
    csv_file.close()
    output.close()
    discarded.close()


if __name__ == '__main__':
    main()
