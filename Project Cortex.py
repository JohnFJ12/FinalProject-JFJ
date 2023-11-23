import tkinter 

userinterface = tkinter.Tk()
userinterface.attributes("-fullscreen", True)


welcomeprompt = tkinter.Label(text = "Hi I am Cortex")
welcomeprompt.place(x = 100, y =userinterface.winfo_width()-1000)

userinterface.mainloop()