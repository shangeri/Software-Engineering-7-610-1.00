import sys
import os
import string
import calendar
import re
import io
import codecs
import itertools
import csv


def format_date(date_str):
    """ month name must be grammatically correct english,
        could be fixed with regular expressions """
    if not date_str:
        return
    #d0 = string.translate(date_str, None, ',"')
    d0 = re.sub('"|,', '', date_str)
    #d0 = string.replace(date_str, ',', '')
    d1 = d0.split()
    months = calendar.month_name

    month_lst = filter(lambda y: y.capitalize() in calendar.month_name, d1)
    if not month_lst:
        #print 'month: ' + d0
        return
    month = month_lst[0].capitalize()
    month_ind = list(calendar.month_name).index(month)
    day_year_lst = filter(lambda y: y.isdigit(), d1)
    if not day_year_lst:
        #print 'day year ' + date_str
        return

    try:
        day = [s for s in day_year_lst if len(s) <= 2][0]
    except:
        return
    try:
        year = [s for s in day_year_lst if len(s) == 4][0]
    except:
        #print 'no year ' + date_str
        return

    return '-'.join([year, day, str(month_ind).zfill(2)])


def split_line(line):
    """ makes 4 separated columns with a proper separator,
        based on the assumption that the twitter link exists """
    #line = line.encode('utf-8').strip()
    username = re.search(r'@[a-zA-Z0-9_]+', line)
    if not username:
        return

    twitter_link = r'http[s]?://twitter.com/[a-zA-Z0-9_]+/status/[0-9]+'
    tw_link = re.search(twitter_link, line)
    if not tw_link:
        return

    un_ind = line.index(username.group())
    tw_ind = line.index(tw_link.group())
    tweet_ind = len(username.group()) + un_ind
    tweet = line[tweet_ind:tw_ind]
    date_ind = len(tw_link.group()) + tw_ind
    date_str = line[date_ind:].strip(';,\t\n\r\n')
    date_str = string.replace(date_str, ';', '')
    un_strip = username.group().strip(' ;\t')
    un_strip = string.replace(un_strip, ';', '')
    tw_strip = tweet.strip(' ;\t')
    tw_strip = string.replace(tw_strip, ';', '')
    li_strip = tw_link.group().strip(' ;\t')
    li_strip = string.replace(li_strip, ';', '')
    return ';'.join([un_strip, tw_strip, li_strip, date_str])


def main():
    """ if a line of the file does not have a separator between
        the username and the tweet, the line will be discarded!"""
    if len(sys.argv) != 2:
        prog = os.path.basename(sys.argv[0])
        print('usage: python2 {0} <csv_file>'.format(prog))
        sys.exit(1)

    try:
        in_file = open(sys.argv[1], 'r')
        ll = len(sys.argv[1]) - 4
        output_name = sys.argv[1][0:ll] + '_new.csv'
        output = open(output_name, 'w')
        output.write('date:\t\ttweets:\n')
        discarded_name = sys.argv[1][0:ll] + '_discarded.txt'
        discarded = open(discarded_name, 'w')
        format_name = sys.argv[1][0:ll] + '_format_error.txt'
        format_error = open(format_name, 'w')
    except IOError:
        print('can not open {0}'.format(sys.argv[1]))
        sys.exit(1)

    rt = 0
    tweets = {}
    retweet = 0
    for line in in_file:
        if re.search(r'RT', line):
            rt += line.count('RT')
        sp = split_line(line)
        if not sp:
            format_error.write(line)
            continue
        sp0 = sp.split(';')
        try:
            tweet = sp0[1]
            date = sp0[3]
        except:
            continue

        if tweet not in tweets:
            fd = format_date(date)
            if fd:
                tweets[tweet] = format_date(date)
            else:
                discarded.write(line)
        else:
            retweet += 1

    tweets = zip(tweets.values(), tweets.keys())
    tweets = filter(lambda x: x[0], tweets)
    dix = {}
    for date, tweet in tweets:
        if date not in dix:
            dix[date] = 1
        else:
            dix[date] += 1

    dix['date'] = 'tweets'
    with open('output.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(dix.items())

    for date, amount in dix.items():
        output.write(date + '\t' + str(amount) + '\n')

    # ascii output at the moment
    in_file.close()
    output.close()
    discarded.close()
    print('retweet = %i' % retweet)
    print('rt = %i' % rt)


if __name__ == '__main__':
    main()

