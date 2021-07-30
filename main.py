# Simphiwe Sithole, class 1
from tkinter import *
from tkinter import messagebox


class TicketSales:
    def __init__(self, master):
        # THIS IS TO INITIALIZE THE WINDOW
        self.master = master
        self.master.title('Tickets')
        self.master.geometry('400x450')
        self.master.config(bg='#191923')

        # THIS IS THE CELL NUMBER ENTRY SECTION
        self.cell_entry_lable = Label(self.master, text='Enter CellNumber:', bg='red', fg='blue', font="monospace 10")
        self.cell_entry = Entry(self.master, bg='yellow', fg='green', font="monospace 10")
        self.cell_entry_lable.place(x=10, y=10)
        self.cell_entry.place(x=220, y=10)

        # THIS IS THE TICKET TYPE LABEL AND OPTION BOX FOR TICKET TYPE
        self.ticket_label = Label(self.master, text='Choose Ticket Category:', bg='blue', fg='red', font="monospace 10")
        self.options = ['Movie', 'Soccer', 'Theater']
        self.variable = StringVar()
        self.variable.set('Choose Ticket')
        self.ticket_op = OptionMenu(master, self.variable, *self.options)
        self.ticket_op.config(font="monospace 10")
        menu = self.master.nametowidget(self.ticket_op.menuname)
        menu.config(font='monospace 10')
        self.ticket_label.place(x=10, y=50)
        self.ticket_op.place(x=220, y=45)

        # THIS IS THE TICKET NUMBER LABEL AND TICKET NUMBER SPINBOX
        self.ticket_no_label = Label(self.master, text='Number of Tickets Bought:', bg='green', fg='red', font="monospace 10")
        self.ticket_spinbox = Spinbox(self.master, width=10, from_=0, to=100, bg='yellow', fg='blue', font="monospace 10")
        self.ticket_no_label.place(x=10, y=90)
        self.ticket_spinbox.place(x=220, y=90)

        # THIS IS THE BUTTON FOR CALCULATING THE TICKET PRICES
        self.calc_button = Button(self.master, text='Calculate Ticket', command=self.calc_prepayment, font="monospace 10")
        self.clear_button = Button(self.master, text='Clear Entries', command=self.clear, font="monospace 10")
        self.calc_button.place(x=40, y=180)
        self.clear_button.place(x=225, y=180)

        # THIS IS THE PAYMENT INFO
        self.frame = Frame(self.master, width=318, height=180, bg='#BDBF09')
        self.frame.place(x=40, y=230)


        self.amount_pay = Label(self.frame, text='', fg='blue', bg='red', font="monospace 10")
        self.reserve = Label(self.frame, text='', fg='green', bg='yellow', font="monospace 10")
        self.cell_label = Label(self.frame, text='', fg='blue', bg='red', font="monospace 10")
        self.amount_pay.place(x=10, y=30)
        self.reserve.place(x=10, y=70)
        self.cell_label.place(x=10, y=110)

    def calc_prepayment(self):
        # THIS IS TO INITIALIZE THE VARIABLES AND CONSTANTS
        ticket_no = int(self.ticket_spinbox.get())
        vat = 0.14


        try:
            int(self.cell_entry.get())
            if len(self.cell_entry.get()) < 10 or len(self.cell_entry.get()) > 10:
                raise ValueError

            elif self.variable.get() == 'Select Ticket':
                raise ValueError

            elif ticket_no == 0:
                raise ValueError

            # THIS IS FOR THE CALCULATION OF THE SOCCER
            elif self.variable.get() == 'Soccer':
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)


            elif self.variable.get() == 'Movie':
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            # THIS IS TO CALCULATE FOR THE THEATER AND WLL BE CALCULATED IN RANDS
            elif self.variable.get() == 'Theater':
                price = 100
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ('Amount Payable: R{}'.format(price_pay))
                self.amount_pay.config(text=text)

            # THIS IS GONNA DISPLAY THE AMOUNT THAT NEEDS TO BE PAYED
            reserve_text = 'Reservation for {} for {}'.format(self.variable.get(), ticket_no)
            cell_text = 'was done by {}'.format(self.cell_entry.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:
            messagebox.showerror(message='Invalid combination')

    # THIS WILL CLEAR EVERYTHING
    def clear(self):
        self.cell_entry.delete(0, END)
        self.cell_entry.focus()
        self.variable.set('Choose Ticket')
        self.ticket_spinbox.delete(0, END)
        self.ticket_spinbox.insert(0, 0)
        self.amount_pay.config(text='')
        self.reserve.config(text='')
        self.cell_label.config(text='')


root = Tk()
TicketSales(root)   # Instance of class
root.mainloop()
