import tkinter 
import typingsimu

userinterface = tkinter.Tk()
userinterface.attributes("-fullscreen", True)

cortexTextbox = tkinter.Text(x = 100, y = 100, width= 150, height = 25, background= "gray", font = ("Times New Roman", 30), yscrollcommand=True, borderwidth= 10)
cortexTextbox.pack()
uiTextbox = tkinter.Text(x = 100, y = 100, width= 150, height = 25, background= "white",font = ("Times New Roman", 30), borderwidth=10)
uiTextbox.pack()

typingsimu.typing("Hi My Name is Cortex your assistant in anything Calc 3 how can I help you today?",cortexTextbox)
userinterface.mainloop()