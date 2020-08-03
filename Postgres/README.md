## Overview

In this project, I am going to build a Postgres database with tables designed to optimize queries on song play analysis.


## Context

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

My role is to create a database schema and ETL pipeline for this analysis. 

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

1. test.ipynb - displays the first few rows of each table to check the database.

2. create_tables.py - drops and creates tables. 

3. etl.ipynb - reads and processes a single file from song_data and log_data and loads the data into  tables. This notebook contains detailed instructions on the ETL process for each of the tables.

4. etl.py - reads and processes files from song_data and log_data and loads them into  tables.

5. sql_queries.py - contains all  sql queries, and is imported into the last three files above.

6. README.md - provides discussion on the project.

## Steps followed to completion

1. Fill the DROP, CREATE and INSERT query statements in sql_queries.py

2. Save it and run python create_tables.py in console or in jupyter notebook. This will create the tables.

3. Use test.ipynb  to interactively verify that all tables were created correctly.

4. Completed etl.ipynb to create the blueprint of the pipeline to process and insert all data into the tables.

5. Fill the etl.py once the base steps are verified

6. Run etl.py in console or in notebook, and verify results by running test.ipynb

