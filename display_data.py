import sqlite3

def display_data():
    conn = sqlite3.connect('event_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM event_details")
    data = cursor.fetchall()

    for row in data:
        print(row)

    conn.close()

# Call the function to display the data
display_data()
