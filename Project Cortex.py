import tkinter 
import typingsimu
from sympy import integrate, symbols, matrix_symbols, Symbol
from sympy.parsing.sympy_parser import parse_expr, standard_transformations,\
implicit_multiplication_application
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
     def singleintcalc():
          
          transformations = (standard_transformations + (implicit_multiplication_application,))
          x = Symbol("x")
          abo = aboundtb.get(1.0, "end-1c")
          bbo = bboundtb.get(1.0, "end-1c")
          abbound = parse_expr(abo, evaluate=False)
          bbbound = parse_expr(bbo, evaluate=False)
          function = functiontb.get(1.0,"end-1c")
          func = parse_expr(function, transformations=transformations)
          answer = integrate(func,(x,abbound, bbbound))
          integraldisplay = tkinter.Label(integralinterface, justify = "left", text = text.format(a= abbound, b = bbbound, f = func) , font = ("Times New Roman", 30))
          integraldisplay.pack()
          emptyspacelbl = tkinter.Label(integralinterface, justify = "left", text = " ", font = ("Times New Roman", 30))
          emptyspacelbl.pack()
          answerlbl = tkinter.Label(integralinterface, justify = "left", text = " =  "+ str(answer), font = ("Times New Roman", 30))
          answerlbl.pack()
     integralinterface.attributes("-fullscreen", True)
     text = r"""                  {b}
                 /\ 
                |
                | {f} dx
                |
               \/
                 {a}"""
     if single == True: 
          for widget in integralinterface.winfo_children():
               widget.destroy()
          x = symbols("x")
          integraldisplay = tkinter.Label(integralinterface, justify = "left", text = text.format(a= "a", b = "b", f = "f(x)"),font = ("Times New Roman", 30))
          integraldisplay.pack()
          aboundlbl = tkinter.Label(integralinterface, text = "a Bound",background="white")
          aboundlbl.pack()
          aboundtb = tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
          aboundtb.pack()

          bboundlbl = tkinter.Label(integralinterface, text = "b Bound", background="white")
          bboundlbl.pack()
          bboundtb = tkinter.Text(width= 150, height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
          bboundtb.pack()

          functionlbl = tkinter.Label(integralinterface, text = "function",background="white")
          functionlbl.pack()
          functiontb = tkinter.Text(width= 150, height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
          functiontb.pack()
          a = aboundtb.get(1.0, "end-1c")
          b = bboundtb.get(1.0,"end-1c")
          func = functiontb.get(1.0,"end-1c")
          userdone = tkinter.Button(integralinterface, text="done",font = ("Times New Roman", 30), borderwidth=10,command=singleintcalc)
          userdone.pack()

def integralui():
     userinterface.destroy()
     integralinterface = tkinter.Tk()
     singleint = tkinter.Button(integralinterface, text= "Single Integral",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = True, double = False, triple = False))
     singleint.pack()
     doubleint = tkinter.Button(integralinterface, text= "Double Integral",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = False, double = True, triple = False))
     doubleint.pack()
     tripleint = tkinter.Button(integralinterface, text= "Triple Integral",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = False, double = False, triple = True))
     tripleint.pack()
def dotproductui():
     userinterface.destroy()
     integralinterface = tkinter.Tk()
     r2 = tkinter.Button(integralinterface, text= "2D Vector",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = True, double = False, triple = False))
     r2.pack()
     r3 = tkinter.Button(integralinterface, text= "3D Vector",font = ("Times New Roman", 30), borderwidth=10, command=lambda: intuicallers(integralinterface, single = False, double = True, triple = False))
     r3.pack()
def crossproductui():
     pass



def calculatorcallers():
    uihelper = uiTextbox.get(1.0, "end-1c")
    if "joke" in uihelper.lower():
         cortexTextbox.delete(1.0, "end-1c")
         uiTextbox.delete(1.0, "end-1c")
         typingsimu.typing("Alright we done to much Calculus your right, Lets lighten the mood. Why did the skeleton not go to prom his senior year and not want to either?",cortexTextbox)
         typingsimu.typing("\n",cortexTextbox)
         typingsimu.typing("\n",cortexTextbox)
         typingsimu.typing("\n",cortexTextbox)
         typingsimu.typing("because he had NOBODY to go with, LOLOLOLOLOLOLOLOL ",cortexTextbox)
    elif "integral" in uihelper.lower():
         cortexTextbox.delete(1.0, "end-1c")
         uiTextbox.delete(1.0, "end-1c")
         typingsimu.typing("Alright, Let me redirect you to the integral calculator page. One Second.....",cortexTextbox)
         typingsimu.typing(".........Redirecting",cortexTextbox)
         integralui()
    elif "dot product" in uihelper.lower():
         cortexTextbox.delete(1.0, "end-1c")
         uiTextbox.delete(1.0, "end-1c")
         typingsimu.typing("Alright, Let me redirect you to the integral calculator page. One Second.....",cortexTextbox)
         typingsimu.typing(".........Redirecting",cortexTextbox)
         dotproductui()

userinterface.mainloop()