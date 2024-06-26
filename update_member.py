from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        update_member = ("30", "5")

        query = "UPDATE members set age = %s where id = %s"

        cursor.execute(query, update_member)
        conn.commit()
        print("Members details updated successfully.")

    finally:
        cursor.close()
        conn.close()
