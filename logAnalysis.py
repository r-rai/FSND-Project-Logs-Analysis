#!/usr/bin/env python2.7

import psycopg2

DATABASE = "news"

# parent function which will call all question functions


def run():
    """ Start the reporting tool """
    print ""
    answer_question_1()

    print "\n"
    answer_question_2()

    print "\n"
    answer_question_3()

# function for question 1


def answer_question_1():
    print "Q1. What are the most popular three articles of all time?\n"
    rows = get_three_most_popular_articles()
    for row in rows:
        print "%s - %d views" % (row[0], row[1])

# function for question 2


def answer_question_2():
    print "Q2. Who are the most popular article authors of all time?\n"
    rows = get_most_popular_authors()
    for row in rows:
        print "%s - %d views" % (row[0], row[1])

# function for question 3


def answer_question_3():
    print "Q3. On which days did more than 1% of requests lead to errors?\n"
    rows = get_days_with_higher_errors()
    for row in rows:
        print "%s - %s errors" % (row[0], row[1])

# function to fetch 3 most popular authors from database


def get_three_most_popular_articles():
    db = psycopg2.connect(database=DATABASE)
    cursor = db.cursor()
    cursor.execute("""select articles.title, count(log.id) as total from articles
                   left join log on log.path=('/article/' || articles.slug)
                   group by articles.title order by
                   total desc
                   limit 3""")
    return cursor.fetchall()
    db.close()

# function to fetch most popular authors from DB


def get_most_popular_authors():
    db = psycopg2.connect(database=DATABASE)
    cursor = db.cursor()
    cursor.execute("""select authors.name, count(log.id) from authors left join
                   articles on articles.author=authors.id left join log on
                   log.path=('/article/' || articles.slug)
                   group by authors.name
                   order by count desc""")
    return cursor.fetchall()
    db.close()

# function to fetch days with higher errors


def get_days_with_higher_errors():
    db = psycopg2.connect(database=DATABASE)
    cursor = db.cursor()
    cursor.execute("""select
                   to_char(errors_by_day.date, 'Month DD, YYYY') as date,
                   to_char(((errors_by_day.count:: decimal
                   /requests_by_day.count::decimal)*100)
                    ,'9.99')
                    || '%' as percentage
                    from
                        (select date(time),count(*) from log
                                    group by date(time)) as requests_by_day,
                        (select date(time),count(*) from log
                                    where status != '200 OK'
                                    group by date(time)) as errors_by_day
                    where
                        requests_by_day.date = errors_by_day.date
                        and ((errors_by_day.count::decimal
                                /requests_by_day.count::decimal)*100) > 1;""")
    return cursor.fetchall()
    db.close()
run()
