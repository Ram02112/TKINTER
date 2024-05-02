from tkinter import *

window = Tk()
window.title("MILES TO KM CONVERTOR.")
def convert_units():
  miles = float(miles_input.get())
  km = round(miles * 1.609)
  km_label.config(text=f"{km}")

miles_input = Entry()
miles_label = Label(text="Miles")
is_equal_label = Label(text="is equals to")
km_label = Label(text="0")
km_units = Label(text="Kilometers")
calc_btn = Button(text="CALCULATE",command=convert_units)


miles_input.grid(row=1,column=2)
miles_label.grid(row=1,column=3)
is_equal_label.grid(row=2,column=0)
km_label.grid(row=2,column=2)
km_units.grid(row=2,column=3)
calc_btn.grid(row=4,column=2)



window.mainloop()