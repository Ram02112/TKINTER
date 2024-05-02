from tkinter import * 
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
FONT = ("Courier",14,"bold")
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  letter_list = [choice(letters) for _ in range(randint(8, 10))]
  symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
  number_list = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = letter_list+symbol_list+number_list
  shuffle(password_list)
  password = "".join(password_list)
  pass_entry.insert(0,password)
  pyperclip.copy(password)
  
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

  website = web_entry.get()
  email = user_entry.get()
  password = pass_entry.get()

  is_ok = messagebox.askokcancel(title=website,message=f"DETAILS === \n EMAIL : {email} \n PASSWORD : {password} \n SAVE?")

  if len(website) == 0 or len(password) == 0 :
    messagebox.showinfo(title="CHECK AGAIN",message="Details can't be empty in order to save")
  else:
    if is_ok:
      with open("data.txt","a") as data_file:
        data_file.write(f"{website} || {email} || {password}")
        web_entry.delete(0,END)
        pass_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("PASSWORD MANAGER")
window.config(padx=80,pady=80)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="../UDEMY/Tkinter/PW_MANAGER/logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)


# --------------------- LABELS ----------------------- #

web_name = Label(text="WEBSITE :",font=FONT)
user_label = Label(text="EMAIL/USERNAME :",font=FONT)
pass_label = Label(text="PASSWORD :",font=FONT)

web_name.grid(row=1,column=0)
user_label.grid(row=2,column=0)
pass_label.grid(row=3,column=0)

# --------------------- ENTRY ----------------------- #

web_entry = Entry(width=55)
web_entry.focus()
user_entry = Entry(width=55)
user_entry.insert(0,"rammurthy0320@gmail.com")
pass_entry = Entry(width=33)

web_entry.grid(row=1,column=1,columnspan=2)
user_entry.grid(row=2,column=1,columnspan=2)
pass_entry.grid(row=3,column=1)

# --------------------- BUTTON ----------------------- #

pwgen_button = Button(text="GENERATE PASSWORD.",command=generate_password)
add_button = Button(text="ADD",width=48,command=save)

pwgen_button.grid(row=3,column=2)
add_button.grid(row=4,column=1,columnspan=2)




window.mainloop()