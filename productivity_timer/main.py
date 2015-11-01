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
        
        self.timer_on = False
        self.timer_sound = pyglet.media.load('gong.mp3', streaming=False)
        self.next_time = datetime.datetime.now()
        
        self.label.grid(row=0, column=0, columnspan=4)
        self.productivity_time = IntVar()
        Radiobutton(self, text="15 min", variable=self.productivity_time, value=15).grid(row=1, column=0)
        Radiobutton(self, text="30 min", variable=self.productivity_time, value=30).grid(row=1, column=1)
        Radiobutton(self, text="45 min", variable=self.productivity_time, value=45).grid(row=1, column=2)
        Radiobutton(self, text="60 min", variable=self.productivity_time, value=60).grid(row=1, column=3)
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
            
            
    def update_me(self):  
        if self.timer_on:
            if datetime.datetime.now() > self.next_time:
                self.timer_sound.play()
                self.master.focus_force()
                self.refresh_timer()
            self.update_count_lbl()
        self.timer_label.after(1000, self.update_me)
        
            
    def update_count_lbl(self):
        curr_delta = self.next_time - datetime.datetime.now()
        self.time_show.set("Time left: " + str(math.ceil(curr_delta.seconds/60)))
        
    def refresh_timer(self):
        self.next_time = datetime.datetime.now() + datetime.timedelta(minutes=self.productivity_time.get())
        
        



#main
tk = Tk()
timer_frame = TimerDisplay(tk)
timer_frame.pack()
tk.mainloop()

