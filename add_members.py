from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        new_member = ("Sarah Jane", "8", "18")

        query = "INSERT INTO members (name, id, age) VALUES (%s, %s, %s)"

        cursor.execute(query, new_member)
        conn.commit()
        print("New member added successfully.")

    finally:
        cursor.close()
        conn.close()
0