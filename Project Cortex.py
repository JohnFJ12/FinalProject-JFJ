import tkinter 
import typingsimu
from sympy import integrate, symbols, Matrix, Symbol
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
typingsimu.typing("Hi my name is Cortex your assistant in some things Calculus how can I help you today?",cortexTextbox)

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

def dot2D(dotproductinterface):
     def dotproduct2Dcalc():
          a = parse_expr(a1.get("1.0", "end-1c"),evaluate= False)
          b = parse_expr(a2.get("1.0", "end-1c"),evaluate= False)
          c = parse_expr(b1.get("1.0", "end-1c"), evaluate= False)
          d = parse_expr(b2.get("1.0", "end-1c"), evaluate=False)
          avector = Matrix([a,b])
          bvector = Matrix([c,d])
          dotproduct = avector.dot(bvector)
          dotproductformulae = tkinter.Label(dotproductinterface, text = text.format(a = a, b = b, c = c, d = d), background="Black", font = ("Times New Roman", 30))
          dotproductformulae.pack()
          answer = tkinter.Label(dotproductinterface, text = " = " + str(dotproduct), background="Black", font = ("Times New Roman", 30))
          answer.pack()

     for widget in dotproductinterface.winfo_children():
          widget.destroy()
     dotproductinterface.attributes("-fullscreen", True)
     disclaimer = tkinter.Label(dotproductinterface, text = "For formatting reasons I need to have terms in i, j and k, they are pretty much interchangeable with bracket notation", background="Black")
     disclaimer.pack()
     text = "a * b = (({a})i + ({b})j) * (({c})i + ({d})j)"
     dotproductformulae = tkinter.Label(dotproductinterface, text = text.format(a = "a1", b = "a2", c = "b1", d = "b2"), background="Black", font = ("Times New Roman", 30))
     dotproductformulae.pack()

     a1lbl = tkinter.Label(dotproductinterface, text = "What we got for a1", background="Black", font = ("Times New Roman", 30))
     a1lbl.pack()
     a1 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a1.pack()


     a2lbl = tkinter.Label(dotproductinterface, text = "What we got for a2", background="Black", font = ("Times New Roman", 30))
     a2lbl.pack()
     a2 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a2.pack()


     b1lbl = tkinter.Label(dotproductinterface, text = "What we got for b1", background="Black", font = ("Times New Roman", 30))
     b1lbl.pack()
     b1 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b1.pack()

     
     b2lbl = tkinter.Label(dotproductinterface, text = "What we got for b2", background="Black", font = ("Times New Roman", 30))
     b2lbl.pack()
     b2 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b2.pack()
     
     userdone = tkinter.Button(dotproductinterface, text="Done",font = ("Times New Roman", 30), borderwidth=10,command=dotproduct2Dcalc)
     userdone.pack()


def dot3D(dotproductinterface):
     def dotproduct3Dcalc():
          a = parse_expr(a1.get("1.0", "end-1c"),evaluate= False)
          b = parse_expr(a2.get("1.0", "end-1c"),evaluate= False)
          e = parse_expr(a3.get("1.0", "end-1c"),evaluate= False)
          c = parse_expr(b1.get("1.0", "end-1c"), evaluate= False)
          d = parse_expr(b2.get("1.0", "end-1c"), evaluate=False)
          f = parse_expr(b3.get("1.0", "end-1c"),evaluate= False)
          avector = Matrix([a,b,e])
          bvector = Matrix([c,d,f])
          dotproduct = avector.dot(bvector)
          dotproductformulae = tkinter.Label(dotproductinterface, text = text.format(a = a, b = b, c = c, d = d, e = e, f = f), background="Black", font = ("Times New Roman", 30))
          dotproductformulae.pack()
          answer = tkinter.Label(dotproductinterface, text = " = " + str(dotproduct), background="Black", font = ("Times New Roman", 30))
          answer.pack()
     for widget in dotproductinterface.winfo_children():
          widget.destroy()
     dotproductinterface.attributes("-fullscreen", True)
     disclaimer = tkinter.Label(dotproductinterface, text = "For formatting reasons I need to have terms in i, j and k, they are pretty much interchangeable with bracket notation", background="Black")
     disclaimer.pack()
     text = "a * b = (({a})i + ({b})j + ({e})k) * (({c})i + ({d})j+ ({f})k)"
     dotproductformulae = tkinter.Label(dotproductinterface, text = text.format(a = "a1", b = "a2", e = "a3", c = "b1", d = "b2", f = "b3"), background="Black", font = ("Times New Roman", 30))
     dotproductformulae.pack()

     a1lbl = tkinter.Label(dotproductinterface, text = "What we got for a1", background="Black", font = ("Times New Roman", 30))
     a1lbl.pack()
     a1 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a1.pack()


     a2lbl = tkinter.Label(dotproductinterface, text = "What we got for a2", background="Black", font = ("Times New Roman", 30))
     a2lbl.pack()
     a2 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a2.pack()

     a3lbl = tkinter.Label(dotproductinterface, text = "What we got for a3", background="Black", font = ("Times New Roman", 30))
     a3lbl.pack()
     a3 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a3.pack()

     b1lbl = tkinter.Label(dotproductinterface, text = "What we got for b1", background="Black", font = ("Times New Roman", 30))
     b1lbl.pack()
     b1 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b1.pack()

     
     b2lbl = tkinter.Label(dotproductinterface, text = "What we got for b2", background="Black", font = ("Times New Roman", 30))
     b2lbl.pack()
     b2 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b2.pack()
     
     b3lbl = tkinter.Label(dotproductinterface, text = "What we got for b3", background="Black", font = ("Times New Roman", 30))
     b3lbl.pack()
     b3 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b3.pack()
     userdone = tkinter.Button(dotproductinterface, text="Done",font = ("Times New Roman", 30), borderwidth=10,command=dotproduct3Dcalc)
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
     dotproductinterface = tkinter.Tk()
     r2 = tkinter.Button(dotproductinterface, text= "2D Vector",font = ("Times New Roman", 30), borderwidth=10, command=lambda: dot2D(dotproductinterface))
     r2.pack()
     r3 = tkinter.Button(dotproductinterface, text= "3D Vector",font = ("Times New Roman", 30), borderwidth=10, command=lambda: dot3D(dotproductinterface))
     r3.pack()








def crossproductui():
     def crossproductcalc():
          a = parse_expr(a1.get("1.0", "end-1c"),evaluate= False)
          b = parse_expr(a2.get("1.0", "end-1c"),evaluate= False)
          e = parse_expr(a3.get("1.0", "end-1c"),evaluate= False)
          c = parse_expr(b1.get("1.0", "end-1c"), evaluate= False)
          d = parse_expr(b2.get("1.0", "end-1c"), evaluate=False)
          f = parse_expr(b3.get("1.0", "end-1c"),evaluate= False)
          avector = Matrix([a,b,e])
          bvector = Matrix([c,d,f])
          crossproduct = avector.cross(bvector)
          vecans = str(crossproduct[0]) + "i" + str(crossproduct[1]) + "j" + str(crossproduct[2]) + "k"
          crossproductformulae = tkinter.Label(userinterface, text = text.format(a = "a1", b = "a2", e = "a3", c = "b1", d = "b2", f = "b3"), background="Black", font = ("Times New Roman", 30))
          crossproductformulae.pack()
          answerlabel = tkinter.Label(userinterface, text = vecans, background="Black", font = ("Times New Roman", 30))
          answerlabel.pack()
     for widget in userinterface.winfo_children():
          widget.destroy()
     disclaimer = tkinter.Label(userinterface, text = "For formatting reasons I need to have terms in i, j and k, they are pretty much interchangeable with bracket notation", background="Black")
     disclaimer.pack()
     text = "a X b = (({b})({f})- ({e})({d}))i + (({e})({c})- ({a})({f}))j + (({a})({d}) - ({b})({c}))k"
     crossproductformulae = tkinter.Label(userinterface, text = text.format(a = "a1", b = "a2", e = "a3", c = "b1", d = "b2", f = "b3"), background="Black", font = ("Times New Roman", 30))
     crossproductformulae.pack()
     a1lbl = tkinter.Label(userinterface, text = "What we got for a1", background="Black", font = ("Times New Roman", 30))
     a1lbl.pack()
     a1 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a1.pack()


     a2lbl = tkinter.Label(userinterface, text = "What we got for a2", background="Black", font = ("Times New Roman", 30))
     a2lbl.pack()
     a2 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a2.pack()

     a3lbl = tkinter.Label(userinterface, text = "What we got for a3", background="Black", font = ("Times New Roman", 30))
     a3lbl.pack()
     a3 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     a3.pack()

     b1lbl = tkinter.Label(userinterface, text = "What we got for b1", background="Black", font = ("Times New Roman", 30))
     b1lbl.pack()
     b1 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b1.pack()

     
     b2lbl = tkinter.Label(userinterface, text = "What we got for b2", background="Black", font = ("Times New Roman", 30))
     b2lbl.pack()
     b2 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b2.pack()
     
     b3lbl = tkinter.Label(userinterface, text = "What we got for b3", background="Black", font = ("Times New Roman", 30))
     b3lbl.pack()
     b3 =  tkinter.Text(width= 150 , height = 0, background= "blue",font = ("Times New Roman", 30), borderwidth=10)
     b3.pack()
     userdone = tkinter.Button(userinterface, text="Done",font = ("Times New Roman", 30), borderwidth=10,command=crossproductcalc)
     userdone.pack()

     



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
         typingsimu.typing("Alright, let me redirect you to the integral calculator page. One Second.....",cortexTextbox)
         typingsimu.typing(".........Redirecting",cortexTextbox)
         integralui()
    elif "dot product" in uihelper.lower():
         cortexTextbox.delete(1.0, "end-1c")
         uiTextbox.delete(1.0, "end-1c")
         typingsimu.typing("Alright, let me redirect you to the dot product calculator page. One Second.....",cortexTextbox)
         typingsimu.typing(".........Redirecting",cortexTextbox)
         dotproductui()
    elif "cross product" in uihelper.lower():
         cortexTextbox.delete(1.0, "end-1c")
         uiTextbox.delete(1.0, "end-1c")
         typingsimu.typing("Alright, let me redirect you to the cross product calculator page. One Second.....",cortexTextbox)
         typingsimu.typing(".........Redirecting",cortexTextbox)
         crossproductui()

userinterface.mainloop()