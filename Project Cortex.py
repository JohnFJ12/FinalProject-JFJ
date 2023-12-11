import tkinter 
import typingsimu
from sympy import latex

userinterface = tkinter.Tk()
userinterface.attributes("-fullscreen", True)

cortexTextbox = tkinter.Text(width= 150, height = 15, background= "blue", font = ("Times New Roman", 30), yscrollcommand=True, borderwidth= 10)
cortexTextbox.pack()
uiTextbox = tkinter.Text(width= 150, height = 10, background= "black",font = ("Times New Roman", 30), borderwidth=10)
uiTextbox.pack()
uiTxtbutton = tkinter.Button(userinterface, text= "Enter",font = ("Times New Roman", 30), borderwidth=10, command=lambda: calculatorcallers())
uiTxtbutton.pack()
typingsimu.typing("Hi My Name is Cortex your assistant in how can I help you today?",cortexTextbox)

def intuicallers(integralinterface, single, double, triple):
     if single == True: 
          integralinterface.attributes("-fullscreen", True)

          integrals = latex(r"\[ \int f(x) dx \]")
          cortexsgint = tkinter.Label(text = integrals, width= 150, height = 15, background= "blue", font = ("Times New Roman", 30), borderwidth= 10)
          cortexsgint.pack()
def integralui():
     userinterface.destroy()
     integralinterface = tkinter.Tk()
     singleint = tkinter.Button(integralinterface, text= "Single Integral",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = True, double = False, triple = False) and singleint.destroy() and doubleint.destroy() and tripleint.destroy())
     singleint.pack()
     doubleint = tkinter.Button(integralinterface, text= "Double Integral",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = False, double = True, triple = False))
     doubleint.pack()
     tripleint = tkinter.Button(integralinterface, text= "Triple Integral",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = False, double = False, triple = True))
     tripleint.pack()
def dotproductui():
     pass

def crossproductui():
     pass



def calculatorcallers():
    uihelper = uiTextbox.get(1.0, "end-1c")
    if "joke" in uihelper.lower():
         cortexTextbox.delete(1.0, "end-1c")
         uiTextbox.delete(1.0, "end-1c")
         typingsimu.typing("Alright we done to much Calc 3 your right, Lets lighten the mood. ",cortexTextbox)
    elif "integral" in uihelper.lower():
         cortexTextbox.delete(1.0, "end-1c")
         uiTextbox.delete(1.0, "end-1c")
         typingsimu.typing("Alright let me redirct you",cortexTextbox)
         integralui()

userinterface.mainloop()