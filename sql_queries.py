# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES
# One of the review requirement is adding primary Key. It is already added here, do you want me to add a constraint NOT NULL for Song play table?

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY NOT NULL, start_time time NOT NULL, user_id int NOT NULL, level varchar, song_id varchar NOT NULL, artist_id varchar NOT NULL, session_id int, location varchar, user_agent text);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY NOT NULL, first_name varchar,last_name varchar, gender char(1), level varchar);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (song_id varchar PRIMARY KEY NOT NULL, title varchar, artist_id varchar NOT NULL, year int, duration numeric);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (artist_id varchar PRIMARY KEY NOT NULL, artist_name varchar, artist_location varchar, lattitude numeric, longitude numeric);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (start_time time PRIMARY KEY NOT NULL, hour int, day int, week int, month int, year int, weekday int);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent )
             VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users (user_id ,
                first_name ,
                last_name ,
                gender ,
                level )
             VALUES(%s, %s, %s, %s, %s) on conflict (user_id) set level = EXCLUDED.level; """)

song_table_insert = ("""INSERT INTO songs (song_id ,
                title ,
                artist_id ,
                year ,
                duration )
             VALUES(%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING """)

artist_table_insert = ("""INSERT INTO artists (artist_id ,
                artist_name ,
                artist_location ,
                lattitude ,
                longitude )
             VALUES(%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""INSERT INTO time (start_time ,
                hour ,
                day ,
                week ,
                month,
                year,
                weekday)
             VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT s.song_id, a.artist_id FROM songs as s
LEFT JOIN artists as a 
ON a.artist_id = s.artist_id
WHERE title = (%s) AND artist_name = (%s) AND duration=(%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]