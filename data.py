import sqlite3

db_path = "pa.db"

# This function conencts to the DB and returns a conn and cur objects
def connect_to_db(path):
    conn = sqlite3.connect(path)
    # Converting tuples to dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# This function returns pets by pet_type
def read_student_by_house(house):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM students WHERE house = ?'
    value = house
    results = cur.execute(query,(value,)).fetchall()
    conn.close()
    return results

def read_student_by_student_id(student_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM students WHERE id = ?'
    value = student_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result
