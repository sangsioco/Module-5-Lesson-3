from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        new_workoutsessions = ("5", "125", "2024-02-05")

        query = "INSERT INTO workoutsessions (member_id, session_id, session_date) VALUES (%s,%s,%s)"

        cursor.execute(query, new_workoutsessions)
        conn.commit()
        print("Workout session added successfully.")

    finally:
        cursor.close()
        conn.close()

        from connect_mysql import connect_database

