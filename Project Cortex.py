import tkinter 
import typingsimu

userinterface = tkinter.Tk()
userinterface.attributes("-fullscreen", True)

cortexTextbox = tkinter.Text(width= 150, height = 15, background= "blue", font = ("Times New Roman", 30), yscrollcommand=True, borderwidth= 10)
cortexTextbox.pack()
uiTextbox = tkinter.Text(width= 150, height = 10, background= "black",font = ("Times New Roman", 30), borderwidth=10)
uiTextbox.pack()
uiTxtbutton = tkinter.Button(userinterface, text= "Enter",font = ("Times New Roman", 30), borderwidth=10, command=lambda: calculatorcallers())
uiTxtbutton.pack()
typingsimu.typing("Hi My Name is Cortex your assistant in how can I help you today?",cortexTextbox)

def integralui():
     pass

def dotproductui():
     pass

def crossproductui():
     pass



def calculatorcallers():
    uihelper = uiTextbox.get(1.0, "end-1c")
    if "joke" in uihelper.lower():
         return typingsimu.typing("Alright we done to much Calc 3 your right, Lets lighten the mood. ",cortexTextbox)
 

userinterface.mainloop()