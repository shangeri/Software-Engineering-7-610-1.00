import sys
import os
import calendar
import re
import csv


def format_date(date_str):
    if not date_str:
        return

    re_month = re.search(r'[a-zA-Z]+', date_str)
    re_day = re.search(r'\d\d', date_str)
    re_year = re.search(r'\d\d\d\d', date_str)
    if any([not ob for ob in [re_day, re_year, re_month]]):
        return

    month = list(calendar.month_name).index(re_month.group().capitalize())
    return '-'.join([re_year.group(), re_day.group().zfill(2), str(month).zfill(2)])


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

    retweets = 0
    dix = {}
    for name, tweet, link, date in reader:
        # check if it is a retweet (starts with RT)
        if re.match(r'RT', tweet):
            retweets += 1
            continue
        date_form = format_date(date)
        if date_form not in dix:
            dix[date_form] = 1
        else:
            dix[date_form] += 1

    writer = csv.writer(output_csv, delimiter=',')
    writer.writerow(['date:', 'tweets:'])
    for date, amount in sorted(dix.items(), key=lambda x: x[0]):
        writer.writerow([date, amount])

    print 'retweets: ' + str(retweets)
    print 'tweets: ' + str(sum(dix.values()))


if __name__ == '__main__':
    main()
