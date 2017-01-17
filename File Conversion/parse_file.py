import sys
import os
import calendar
import re
import datetime
import csv


def format_date(date_str):
    if not date_str:
        return 'err'

    re_month = re.search(r'[a-zA-Z]+', date_str)
    re_day = re.search(r'\d\d', date_str)
    re_year = re.search(r'\d\d\d\d', date_str)

    # if True: either Day, Month or Year could not been parsed
    if any([not ob for ob in [re_day, re_year, re_month]]):
        return 'err'

    month = list(calendar.month_name).index(re_month.group().capitalize())
    year = int(re_year.group())
    day = int(re_day.group())

    # [5, 6] for Saturday, Sunday
    if datetime.datetime(year, month, day).weekday() in [5, 6]:
        return 'we'
    else:
        return '-'.join([re_year.group(), re_day.group().zfill(2), str(month).zfill(2)])


def parse_file(reader):
    dix = {'RT': 0, 'err': 0, 'we': 0}
    for name, tweet, link, date in reader:
        # check if it is a retweet (starts with RT)
        if re.match(r'RT', tweet):
            dix['RT'] += 1
        else:
            date_form = format_date(date)
            if date_form not in dix:
                dix[date_form] = 1
            else:
                dix[date_form] += 1
    return dix


def main():
    if len(sys.argv) != 2:
        prog = os.path.basename(sys.argv[0])
        print('usage: python2 {0} <csv_file>'.format(prog))
        sys.exit(1)
    try:
        input_csv = open(sys.argv[1], 'r')
        fname, fext = os.path.splitext(sys.argv[1])
        reader = csv.reader(input_csv)
        output_csv = open(fname + '_parsed.csv', 'w')
    except IOError:
        print('can not open {0}'.format(sys.argv[1]))
        sys.exit(1)

    writer = csv.writer(output_csv, delimiter=',')
    writer.writerow(['date:', 'tweets:'])
    dix = parse_file(reader)
    dix_sort = sorted(dix.items(), key=lambda x: x[0], reverse=True)
    for date, amount in dix_sort[3:]:
        writer.writerow([date, amount])

    print('Total Tweets:\t\t{0}'.format(sum(dix.values())))
    print('Tweets on Weekends:\t{0}'.format(dix_sort[0][1]))
    print('Retweets:\t\t{0}'.format(dix_sort[2][1]))
    print('Errors while parsing:\t{0}'.format(dix_sort[1][1]))


if __name__ == '__main__':
    main()
