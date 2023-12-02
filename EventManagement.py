from tkinter import *

from Book import Book 
from CreateEvent import CreateEvent
from ViewTickets import ViewTickets
from ViewEvents import ViewEvents
from CancelTicket import CancelTicket

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f'{width}x{height}+{x}+{y}')

top = Tk()
top.title('Event Management')

# Set background color
top.configure(bg='white')

# Create buttons
btn_book = Button(top, text='Book Ticket', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: Book())
btn_create = Button(top, text='Create Event', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: CreateEvent())
btn_view_tickets = Button(top, text='View Tickets', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: ViewTickets())
btn_view_events = Button(top, text='View Events', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: ViewEvents())
btn_cancel_ticket = Button(top, text='Cancel Ticket', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: CancelTicket())
btn_quit_app = Button(top, text='Quit App', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: top.destroy())

# Pack buttons
btn_book.pack(pady=10)
btn_create.pack(pady=10)
btn_view_tickets.pack(pady=10)
btn_view_events.pack(pady=10)
btn_cancel_ticket.pack(pady=10)
btn_quit_app.pack(pady=10)

# # Create and pack label
# label_thank_you = Label(top, text='Thank you', font=('Arial', 24), bg='green', fg='white')
# label_thank_you.pack(pady=10)

# Center the window on the screen
center_window(top, 415, 450)

top.mainloop()
