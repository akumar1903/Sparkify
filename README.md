Project Title - Data Modeling with Postgres
--------------------------------------------

Design of a dimenional data model in PostgreSQL with fact and dimension tables loaded through an ETL pipeline executed via Python Scripts.

# Introduction
Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. Sparkify team would analyze the songs and events data to understand who the users are and what songs they are currently listening to.

# Motivation
The motivation behind the project is to maintain and create a running analysis of songs streamed by users and their request by capturing the data in a data warehouse.  Currently, Sparkify don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

# Purpose of the Datamodel
The purpose of the data model is to analyze the user behaviour in song selection, listening and understand the users who use Sparkify App.

The datamodel consists of 4 dimension tables and 1 fact table. The dimension tables are songs, users, artists and time. Fact table has all the keys and user data (level, location and user agent)

Songs table - Captures the details of song title, year and duration of a song.

Users table - Captures the details of user (name, gender and level of subscription) who is listening to the song

Artists table - Captures the details of artist who played the song like name, location and GIS coordinates

Time dim - Dimension table created to capture the duration and time of song play

Fact table (Song play) - captures all the primary keys creating a PK-FK relationship.

Through the above star schema Sparkify can get answer to many questions some of which are like - 
1. Details of the user who is listening to which all artist song?
2. Duration of the song played by users
3. Playing frequency and audit details

# File List
- create_tables.py - consists of python query to drop and create tables
- sql_queries.py - Insert and create table query been run from create tables
- etl.ipynb - iPython notebook for executing commands
- test.ipnyb - iPython notebook for executing commands and testing the ETL flow
- etl.py - Python file to feed data to tables by executing the run queries

# Data List
- Event data from users captured in json files
- Song data about various songs and artists

# Why Datamodeling and ETL pipeline
------------------------------------

There are various reasons datamodeling is designed and used in the way it is designed.

1. Structured Storage of all the transaction data in one location
2. Enable a write intensive schema to capture the streaming data through app
3. OLAP from the data model to slice and dice the data for better information
4. Adhoc queries and views

Python is used as ETL for extracting, transforming and loading data into the tables. Python is a flexible and versatile tool and is also open sourced. It is ideal for handling large data sets and their transformations through python notebooks, consoles and terminals.

# Screenshots of tables

![songplay table](https://i.imgur.com/a4e4Qim.jpg)
![Users table](https://i.imgur.com/GpDsGph.jpg)
![Song Table](https://i.imgur.com/TVCO492.jpg)
![Artist Table](https://i.imgur.com/TVCO492.jpg)
![Time table](https://i.imgur.com/50dMGBg.jpg)