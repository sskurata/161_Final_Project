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

# This function retrieves 1 pet by pet_id
def read_pet_by_pet_id(pet_id):
    conn, cur = connect_to_db(db_path)
    query = 'SELECT * FROM pets WHERE id = ?'
    value = pet_id
    result = cur.execute(query,(value,)).fetchone()
    conn.close()
    return result