from connect_mysql import connect_database

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        members_to_remove = (5,)

        query_check = "SELECT * FROM workoutsessions member_id = %s"

        query = "DELETE FROM members WHERE id = %s"
        cursor.execute(query_check, members_to_remove)
        workoutsessions = cursor.fetchall()

        if workoutsessions:
            print("Cannot delete member: Member has workout session scheduled.")
        else:


            cursor.execute(query, members_to_remove)
            conn.commit()
            print("Member removed successfully.")

    finally:
        cursor.close()
        conn.close()
