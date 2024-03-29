from tkinter import *
root=Tk()

#Connection Functions

#Seat Booking
def seat_booking():
    root.destroy()
    import Booking_page

#Check booked Seat
def check_booked():
    root.destroy()
    import Checking_booked_seat

#Add Bus Details
def add_bd():
    root.destroy()
    import ADD_BUS_PAGE

#Main Heading
h=root.winfo_screenheight()
w=root.winfo_screenwidth()
root.geometry("%dx%d+0+0"%(w,h))
bus=PhotoImage(file="./assets/Bus_for_project.png")
Label(root,image=bus).grid(row=0, column=0, columnspan=10, padx=w//3)
Label(root, text="Online Bus Booking System", bg="Light Blue", fg="Red", font=("Arial Bold", 40)).grid(row=1, column=0, columnspan=10, pady=10, padx=w//3)
B=Button(root,text="Seat Booking", bg="PaleGreen1" , font=("Arial Bold", 25), command=seat_booking).grid(row=3,column=3, padx=30, pady=100)
B=Button(root,text="Check booked Seat", bg="Green2", font=("Arial Bold", 25), command=check_booked).grid(row=3,column=4, padx=30, pady=100)
B=Button(root,text="Add Bus Details", bg="Green", font=("Arial Bold", 25), command=add_bd).grid(row=3,column=5, padx=30, pady=100)
Label(root,text="For Admin Only", fg="Red", font=("Arial Bold", 18)).grid(row=4,column=5)
# root.grid_columnconfigure(1, weight=1)
root.mainloop()
