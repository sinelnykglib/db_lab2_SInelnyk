import psycopg2

username = 'postgres'
password = '23102002Papa'
database = 'Lab_BD'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT TRIM(film_name), count(film_name) FROM dubs GROUP BY film_name
'''

query_2 = '''
SELECT film_name, run_time from movie order by run_time
'''

query_3 = '''
SELECT years, round(AVG(rate),2) from movie GROUP by years order by years
'''


conn = psycopg2.connect(user = username, password = password, dbname = database, host = host, port = port)

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    print('1.')
    cur.execute(query_1)
    for row in cur:
        print(row)

    print('\n2.')
    cur.execute(query_2)
    for row in cur:
        print(row)

    print('\n3.')
    cur.execute(query_3)
    for row in cur:
        print(row)