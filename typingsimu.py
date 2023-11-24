import tkinter 
def typing(output, textbox):
    for i in output:
        textbox.after(100, textbox.insert(tkinter.END, i))