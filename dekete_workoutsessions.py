from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        session_id_to_remove = (765, )

        query = "DELETE FROM workoutsessions WHERE session_id = %s"

        cursor.execute(query, session_id_to_remove)
        conn.commit()
        print("Session ID removed successfully.")

    finally:
        cursor.close()
        conn.close()
0