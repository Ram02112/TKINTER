from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
TEXT = "✔"
reps = 0
timer_window = None

# ---------------------------- TIMER RESET ------------------------------- # 
def count_reset():
  window.after_cancel(timer_window)
  canvas.itemconfig(timer_text,text="00:00")
  timer.config(text="TIMER")
  check_mark.config(text="")
  global reps
  reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
  global reps
  reps+=1
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60
  if reps % 8 == 0 :
    count_down(long_break_sec)
    timer.config(text="BREAK",fg=RED)
  elif reps % 2 == 0:
    count_down(short_break_sec)
    timer.config(text="BREAK",fg=PINK)
  else:
    count_down(work_sec)
    timer.config(text="WORK",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
  count_min = math.floor(count/60)
  count_sec = count % 60
  if count_sec < 10:
    count_sec = f"0{count_sec}"
  canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
  if count>0:
    global timer_window
    timer_window = window.after(1000,count_down,count-1)
  else:
    start_count()
    mark = ""
    for _ in range(reps//2):
      mark+=TEXT
    check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

tomato_img = PhotoImage(file="../UDEMY/Tkinter/Pomodoro/tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

timer = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
timer.grid(row=0,column=1)

start = Button(text="Start",highlightthickness=0,padx=15,pady=8,font=(FONT_NAME,14,"bold"),command=start_count)
reset = Button(text="reset",highlightthickness=0,padx=15,pady=8,font=(FONT_NAME,14,"bold"),command=count_reset)

start.grid(row=2,column=0)
reset.grid(row=2,column=2)


check_mark = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,16))
check_mark.grid(row=3,column=1)


window.mainloop()