import sqlite3
def EventDetails():
    conn = sqlite3.connect('event_database.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS event_details (event_name TEXT, event_id TEXT PRIMARY KEY, event_date TEXT, event_time TEXT, event_duration Text)")

    cursor.execute('SELECT * FROM event_details')
    event_details = cursor.fetchall()
    
    event_names = []
    event_ids = []
    event_dates = []
    event_times = []
    event_durations = []
        
    conn.close()
    
    for i in event_details:
        event_names.append(i[0])
        event_ids.append(i[1])
        event_dates.append(i[2])
        event_times.append(i[3])
        event_durations.append(i[4])
        
    return event_names, event_ids, event_dates, event_times, event_durations, event_details

def TicketDetails():
    conn = sqlite3.connect('event_database.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS ticket_details (customer_name TEXT, ticket_id TEXT PRIMARY KEY, event_name TEXT, event_id TEXT, event_date TEXT, event_time TEXT, duration Text)")

    cursor.execute('SELECT * FROM ticket_details')
    ticket_details = cursor.fetchall()
    
    customer_names = []
    ticket_ids = []
    event_names = []
    event_ids = []
    event_dates = []
    event_times = []
    event_durations = []
        
    conn.close()
    
    for i in ticket_details:
        customer_names.append(i[0])
        ticket_ids.append(i[1])
        event_names.append(i[2])
        event_ids.append(i[3])
        event_dates.append(i[4])
        event_times.append(i[5])
        event_durations.append(i[6])
        
    return customer_names, ticket_ids, event_names, event_ids, event_dates, event_times, event_durations, ticket_details

def BookTicket(customer_name, ticket_id, event_name):
    
    event_names = EventDetails()[0]
    event_ids = EventDetails()[1]
    event_dates = EventDetails()[2]
    event_times = EventDetails()[3]
    event_durations = EventDetails()[4]
    
    event_index = event_names.index(event_name)
    event_id = event_ids[event_index]
    event_date = event_dates[event_index]
    event_time =  event_times[event_index]
    event_duration =  event_durations[event_index]
    
    try:
        conn = sqlite3.connect("event_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO ticket_details (customer_name, ticket_id, event_name, event_id, event_date, event_time, duration) VALUES (?, ?, ?, ?, ?, ?, ?)", (customer_name, ticket_id, event_name, event_id, event_date, event_time, event_duration))
        conn.commit()
        conn.close()
        return 'Success'
    except sqlite3.Error as e:
        return e
    finally:
        conn.close()
        
def CreateNewEvent(event_name, event_id, event_date, event_time, event_duration):
    try:
        conn = sqlite3.connect("event_database.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO event_details (event_name, event_id, event_date, event_time, event_duration) VALUES (?, ?, ?, ?, ?)", (event_name, event_id, event_date, event_time, event_duration))
        conn.commit()
        conn.close()
        return 'Success'
    except sqlite3.Error as e:
        return e
    finally:
        conn.close()
        
def DeleteTicket(ticket_id):
    try:
        conn = sqlite3.connect("event_database.db")
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ticket_details WHERE ticket_id = ?", (ticket_id,))
        conn.commit()
        conn.close()
        return 'Success'
    except sqlite3.Error as e:
        return e
    finally:
        conn.close()