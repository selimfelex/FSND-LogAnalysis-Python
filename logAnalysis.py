import psycopg2
import string

# this SQL statement to print out what are the most
# popular  three articles of all the time acordings to the number of views
# in the news database.


def get_articles():

    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    c.execute("SELECT articles.title AS title , COUNT(log.status) AS num"
              " FROM  articles, log where log.status = '200 OK'"
              " AND log.path LIKE '%' || articles.slug || '%'"
              " GROUP BY title ORDER BY num DESC limit 3; ")
    message1 = c.fetchall()
    print("")
    print("What are the most popular three articles of all time?")
    print("\"" + string.replace(message1[0][0], '/article/', '')+"\" -- "
          + str(message1[0][1]) + " views")
    print("\"" + string.replace(message1[1][0], '/article/', '')+"\" -- "
          + str(message1[1][1]) + " views")
    print("\"" + string.replace(message1[2][0], '/article/', '')+"\" -- "
          + str(message1[2][1]) + " views")
    print("")

    # this is the query of the second quiz
    # Who are the most popular article authors of all time?

    c2 = db.cursor()
    SQL = ("select authors.name as name ,count(log.status)as num"
           " FROM  log, authors , articles"
           " where log.status = '200 OK'"
           " AND  authors.id = articles.author"
           " AND log.path LIKE '%' || articles.slug || '%'"
           " GROUP BY name ORDER BY num DESC;")
    c2.execute(SQL)
    message2 = c2.fetchall()
    # print(message2)
    print("Who are the most popular article authors of all time?")
    print(str(message2[0][0]) + " -- " + str(message2[0][1]) + " views")
    print(str(message2[1][0]) + " -- " + str(message2[1][1]) + " views")
    print(str(message2[2][0]) + " -- " + str(message2[2][1]) + " views")
    print(str(message2[3][0]) + " -- " + str(message2[3][1]) + " views")
    print("")

    # this is the query for the third quiz
    # On which days did more than 1% of requests lead to errors?

    c3 = db.cursor()
    SQL2 = ("SELECT to_char(t1.day,'Mon DD,YYYY')  ,"
            "ROUND((t2.num2*1./t1.num1)*100,2) FROM (SELECT date(time) "
            "AS day , COUNT(status) AS num1 FROM log  GROUP BY day"
            " ORDER BY day) t1"
            " INNER JOIN (SELECT date(time) AS day , COUNT(status) AS num2"
            " FROM log WHERE status='404 NOT FOUND' "
            "GROUP BY day ORDER BY day) t2"
            " ON t1.day = t2.day WHERE (t2.num2*1./t1.num1) > 0.01")
    c3.execute(SQL2)
    message3 = c3.fetchall()
    print("on which days did more than 1/% of requests lead to errors?")
    print(str(message3[0][0]) + " -- " + str(message3[0][1]) + "% error")
    print("")
    db.close()


# then call the function
if __name__ == "__main__":
    get_articles()
