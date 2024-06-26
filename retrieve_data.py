from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        query = """SELECT m.id, m.name, m.age
                   FROM members m, members a
                   WHERE m. id = a.id"""

        cursor.execute(query)

        for members in cursor.fetchall():
            print(members)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
