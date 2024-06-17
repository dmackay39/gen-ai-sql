import psycopg2
import pandas as pd

DB_NAME = "py_database"
DB_USER = "pyuser"
DB_PASS = "pyuser"
DB_HOST = "postgres"
DB_PORT = "5432"
 
def populate_table():
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
    except:
        print("Database not connected successfully")
    cur = conn.cursor()  # creating a cursor
    cur.execute("""
    DROP TABLE IF EXISTS Movies;
    CREATE TABLE Movies
    (
        ID INT   PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        DIRECTOR TEXT NOT NULL,
        RATING INT NOT NULL,
        PROFITS INT NOT NULL
    )
    """)
    conn.commit()
    print("Table Created successfully")
    cur.execute("""
        INSERT INTO Movies (ID,NAME,DIRECTOR,RATING,PROFITS) VALUES
        (0,'Inception','Christopher Nolan',4,370000),
        (1,'Tenet','Christopher Nolan',4,100000), 
        (2,'The Dark Knight','Christopher Nolan',5,1000000),
        (3,'Memento','Christopher Nolan',3,150000),
        (4,'The Fellowship of the Ring','Peter Jackson',5,7000000),
        (5,'The Two Towers','Peter Jackson',5,8000000),
        (6,'The Return of the King','Peter Jackson',5,9000000),
        (7,'Dune part 1','Denis Villeneuve',3,5000000),
        (8,'Dune part 2','Denis Villeneuve',4,6500000),
        (9,'Arrival','Denis Villaneuve',4,4500000),
        (10,'Twister','Jan de Bont',2,500000),
        (11,'The Godfather','Francis Ford Coppola',5,10000000),
        (12,'The Godfather part 2','Francis Ford Coppola',5,50000000),
        (13,'The Godfather part 3','Francis Ford Coppola',2,6000000),
        (14,'The Shawshank Redemption','Frank Darabont',4,8000000),
        (15,'The Good, the Bad, and the Ugly','Sergio Leone',4,3000000),
        (16,'Forrest Gump','Robert Zemeckis',2,600000),
        (17,'The Silence of the Lambs','Jonathan Demme',3,400000),
        (18,'Spirited Away','Hayao Miyazaki',4,5500000),
        (19,'Gladiator','Ridley Scott',5,3400000),
        (20,'Alien','Ridley Scott',3,900000),
        (21,'WALLE','Andrew Stanton',4,8000000),
        (22,'Pulp Fiction','Quentin Tarantino',2,3000000),
        (23,'Kill Bill Vol.1','Quentin Tarantino',4,2500000),
        (24,'Kill Bill Vol.2','Quentin Tarantino',4,2800000),
        (25,'Coco','Lee Unkrich',2,1500000)
    """)
    conn.commit()
    print("Table populated successfully")
    cur.execute("""
        SELECT * FROM Movies;
    """) 
    results = cur.fetchall() 
    print(results) 
    conn.commit()
    conn.close()

def get_all_table_data():
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
    except:
        print("Database not connected successfully")

    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM Movies;
    """)
    results = cur.fetchall() 
    column_names = [i[0] for i in cur.description]
    conn.commit()
    conn.close()
    df = pd.DataFrame(results)
    df.columns = column_names
    return df

def execute_custom_query(query):
    try:
        conn = psycopg2.connect(database=DB_NAME,
                                user=DB_USER,
                                password=DB_PASS,
                                host=DB_HOST,
                                port=DB_PORT)
        print("Database connected successfully")
    except:
        print("Database not connected successfully")
    cur = conn.cursor()
    cur.execute(query)
    
    results = cur.fetchall()
    column_names = [i[0] for i in cur.description]
    conn.commit()
    conn.close()
    df = pd.DataFrame(results)
    df.columns = column_names
    return df