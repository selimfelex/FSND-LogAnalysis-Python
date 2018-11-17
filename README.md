# FSND Logs Analysis Project1

## Project Description
- this projects aims to run Psql quiries from python code to practice on database connections and
  use database adapters like psycopg2.

## Project_Specification
 - this project has a database called news , which has 3 tables 
 1- authors , which has authors id, name, bio .
 2- articles , which has id , author, title, slug, lead, body, time.
 4- log , which has id, path, ip, method, status ,time .
 - so those tables should answer the follwing 3 quistions.

## Questions
1. What are the most popular three articles of all time?
  you can optain the number of times that article was visited by counting the path in log table which is 
  related to the text in articles.slug so the most visited will have the most count records in the log.  

2. Who are the most popular article authors of all time?
  acordin to the first quistion you have the count of each article visits , so you can have the author name from authors by authors.id = articles.author to connect other two tables to obtain author's name.

3. On which days did more than 1% of requests lead to errors?
  you can collect the log ration by counting the log status = '200 OK' and errors from log.status 
  = "404 NOT FOUND" and divid on each on and see the ration condition to get the dat and reformat it
  with Mon DD,yyyy as requested. 

## Requirements
* Python 2.7.12
* psycopg2
* Postgresql 9.5.14

## How to run

* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* run the python file 
```
* python3 LogAnalysis.py
```