## Introduction

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

The task is to build an ETL Pipeline that extracts data from S3, stage it in Redshift and then transform data into a set of Dimensional and Fact Tables for their analytics Team to continue finding Insights to what songs their users are listening to.


## Context

Application of Data warehouse and AWS to build an ETL Pipeline for a database hosted on Redshift. I have to load data from S3 to staging tables on Redshift and execute SQL Statements that create fact and dimension tables from these staging tables.


## Project Datasets
The S3 links for each data:
- Song Data Path --> s3://udacity-dend/song_data 
- Log Data Path --> s3://udacity-dend/log_data 
- Log Data JSON Path --> s3://udacity-dend/log_json_path.json

# Song Dataset

This data is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song.

> {"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}


# Log Dataset

Log files in JSON format. These simulate activity logs from a music streaming app based on specified configurations.

> {"artist":"Slipknot","auth":"Logged In","firstName":"Aiden","gender":"M","itemInSession":0,"lastName":"Ramirez","length":192.57424,"level":"paid","location":"New York-Newark-Jersey City, NY-NJ-PA","method":"PUT","page":"NextSong","registration":1540283578796.0,"sessionId":19,"song":null,"status":200,"ts":1541639510796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}


## Schema

I have used Star Schema for this database. The reason I used this schema is because of the fact that this project can be sufficiently managed by it. I  have structured data, which is not huge and I feel the need to perform joins on this data. So, I have used star schema. 
It has one main fact table containing all the measures associated to each event (user song plays) and foreign keys, and 4 dimensional tables, each with a primary key that is connected to the corresponding foreign key in the fact table.


# Fact Table

> songplays - records in log data associated with song plays i.e. records with page NextSong

- songplay_id int PRIMARY KEY: ID of each user song play
- start_time datestamp: Timestamp of beggining of user activity
- user_id int: ID of user
- level  varchar: User level (free or paid)
- song_id varchar: ID of Song played
- artist_id varchar: ID of Artist of the song played
- session_id int: ID of the user Session
- location varchar: User location
- user_agent varchar: Agent used by user to access Sparkify platform

# Dimension Tables

> users - users of the app

- user_id int PRIMARY KEY: ID of user
- first_name varchar: Name of user
- last_name varchar: Last Name of user
- gender char(1): Gender of user (M or F)
- level varchar: User level 

> songs - songs in music database

- song_id varchar PRIMARY KEY: ID of Song
- title varchar: Title of Song
- artist_id varchar NOT NULL: ID of song Artist
- year int: Year of song release
- duration decimal: Song duration in milliseconds

> artists - artists in music database

- artist_id varchar PRIMARY KEY: ID of Artist
- name varchar: Name of Artist
- location varchar: Name of Artist city
- lattitude float8: Lattitude location of artist
- longitude float8: Longitude location of artist

> time - timestamps of records in songplays broken down into specific units

- start_time timestamp PRIMARY KEY: Timestamp of row
- hour int: Hour associated to start_time
- day int: Day associated to start_time
- week int: Week of year associated to start_time
- month int: Month associated to start_time
- year int: Year associated to start_time
- weekday int: Name of week day associated to start_time

## Project files

1. create_tables.py - drops and creates tables for the star schema in Redshift. 

2. etl.py - loads data from S3 into staging tables on Redshift and then process that data into analytics tables on Redshift.

3. sql_queries.py - contains all  sql queries, and is imported into the last two files above.

4. README.md - provides discussion on the project.

## Steps followed to completion

# Create Table Schemas

1. Design schemas for fact and dimension tables.
2. Write a SQL CREATE statement for each of these tables in sql_queries.py.
3. Complete the logic in create_tables.py to connect to the database and create these tables.
4. Write SQL DROP statements to drop tables in the beginning of create_tables.py if the tables already exist. This way, we can run create_tables.py whenever we want to reset your database and test  ETL pipeline.
5. Launch the redshift cluster and create an IAM role that has read access to S3.
6. Add redshift database and IAM role info to dwh.cfg.
7. Test by running create_tables.py and checking the table schemas in redshift database. We can use Query Editor in the AWS Redshift console for this.

# Build ETL Pipeline

1. Implement the logic in etl.py to load data from S3 to staging tables on Redshift.
2. Implement the logic in etl.py to load data from staging tables to analytics tables on Redshift.
3. Test by running etl.py after running create_tables.py and running the analytic queries on Redshift database to compare results with the expected results.
4. Delete redshift cluster when finished.

