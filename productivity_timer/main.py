from tkinter import *
import pyglet
import datetime
import math


class TimerDisplay(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.label = Label(self, text="Productivity Timer\nHow long do you want your productivity to last?")
        self.btn = Button(self, text="Be Productive!", command=self.toggle_timer)
        self.time_show = StringVar()
        self.time_show.set("<-- Whatcha waitin' for?")
        self.timer_label = Label(self, textvariable=self.time_show)
        self.productivity_time = Scale(self, from_=0, to=60, label="Productive Time")
        self.break_time = Scale(self, from_=0, to=60, label="Break Time") 
        
        self.timer_on = False
        self.timer_sound = pyglet.media.load('gong.mp3', streaming=False)
        self.next_time = datetime.datetime.now()
        self.is_break = False
        
        self.label.grid(row=0, column=0, columnspan=4)
        self.productivity_time.grid(row=1, column=0, columnspan=2)
        self.break_time.grid(row=1, column=2, columnspan=2)
        self.btn.grid(row=2, column=1)
        self.timer_label.grid(row=2, column=2)
        self.update_me()
        
    def toggle_timer(self):
        if self.timer_on:
            self.timer_on = False
            self.btn.configure(relief=RAISED)
        else:
            self.timer_on = True
            self.btn.configure(relief=SUNKEN)
            self.refresh_timer()
            self.is_break = False
            
            
    def update_me(self):  
        if self.timer_on:
            if datetime.datetime.now() > self.next_time:
                self.timer_sound.play()
                self.master.focus_force()
                self.is_break = not self.is_break
                self.refresh_timer()
        self.update_count_lbl()
        self.timer_label.after(1000, self.update_me)
        
            
    def update_count_lbl(self):
        if self.timer_on:
            if self.is_break:
                mini_msg = "On break for: "
            else:
                mini_msg = "Active for: "
            curr_delta = self.next_time - datetime.datetime.now()
            main_msg = mini_msg + str(math.ceil(curr_delta.seconds/60)) + " more min"
        else:
            main_msg = "Timer off"
        self.time_show.set(main_msg)
        
    def refresh_timer(self):
        if not self.is_break:
            self.next_time = datetime.datetime.now() + datetime.timedelta(minutes=self.productivity_time.get())
        else:
            self.next_time = datetime.datetime.now() + datetime.timedelta(minutes=self.break_time.get())



if __name__=="__main__":
    tk = Tk()
    timer_frame = TimerDisplay(tk)
    timer_frame.pack()
    tk.mainloop()

