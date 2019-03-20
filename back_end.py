import sqlite3


def con():
    conn = sqlite3.connect('mymovies.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, name VARCHAR NOT NULL,released VARCHAR NOT NULL, runtime VARCHAR NOT NULL)")
    conn.commit()
    conn.close()


def adds(name, released, runtime):
    conn = sqlite3.connect('mymovies.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO movies(name,released, runtime) VALUES(?,?,?)", (name, released, runtime))
    conn.commit()
    conn.close()


def get_movies():
    conn = sqlite3.connect('mymovies.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies")
    all_movies = cur.fetchall()
    conn.close()
    return all_movies


def delete_item(id):
    conn = sqlite3.connect('mymovies.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM movies WHERE id=?", (id,))
    conn.commit()
    conn.close()


def updte(name, released, runtime, id):
    conn = sqlite3.connect('mymovies.db')
    cur = conn.cursor()
    cur.execute("UPDATE movies SET name=?, released=?, runtime=? WHERE id=?", (name, released, runtime, id))
    conn.commit()
    conn.close()


def search(name, released='', runtime=''):
    conn = sqlite3.connect('mymovies.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM movies WHERE name=? OR released=? OR runtime=?", (name, released, runtime))
    search_results = cur.fetchall()
    conn.close()
    return search_results


# Calls
con()
# adds("IT", "Unknown", "About 3 hours")
# delete_item(5)
# updte("The Red Room", 2019, "About 2 hours and a half", 2)
# print(search('The Red Room'))
# print(get_movies())



