import psycopg2
 
conn = psycopg2.connect(host="localhost", dbname="lab10", user="postgres",
                        password="1234", port=5432)   
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists snake(
            player_name VARCHAR(255),
            score INTEGER,
            level INTEGER
);
           """)
conn.commit()