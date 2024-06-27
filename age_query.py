from connect_mysql import connect_database

def get_members_in_age_range(start_age, end_age):
    query = "SELECT DISTINCT age FROM members WHERE age BETWEEN %s AND %s"
    cursor.execute(query, (start_age, end_age))
    print("Distinct Ages in Range:")
    for age in cursor.fetchall():
        print(age[0])

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()

        get_members_in_age_range(25, 30)

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        cursor.close()
        conn.close()
