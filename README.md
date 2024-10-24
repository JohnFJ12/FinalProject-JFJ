
Modules: Basically just incorporated heavily the Tkinter Module and the Sympy Module. Incorporated integrate, parser_expr and cross, dot and matrixes from sympy. From Tkinter I learned heavily how to create a window and close it but at the same time create a new one
with just the use of a button created with tkinter. I also incorporated the tkinter.Label, tkinter.Tk() to create a new window and tkinter.attributes to be able to full screen the window. Tkinter.Text was also important because it allowed me to create a space where I could retrieve the user input easily.

Problem 1: Latex wasn’t exactly compliant with a Tkinter TextBox

I believed that I would be
able to print formatted integrals in a tkinter label I was not so wrong but
it was far more complicated than I believed because I found that it was possible through more research on 
how to display Latex on tkinter but it involved also using matplotlib but it was far to complicated to get to work 
in a short amount of time

Went around this by using ASCII art instead and .format to implement bounds on the integral to get it to look 
as best as possible 

Problem 2: In order to simulate a chatbot typing I had to print letter by letter but .sleep() didnt work well with tkinter

Easily overcame this with the tkinter.after() function which enabled me to create my own
mini typingsimu module which allowed me to traverse the string that is wanted to be displayed in a textbox using a for loop and insert 
it character by character each 100 ms appart to simulate the typing.

Problem 3: Sympy Cross Product printed as a list rather than a formatted vector

Easily overcame this by just formatting a string with the results depending on the index. So for example the x part of the vector would be 
printed alongside i by just doing whatever the crossproduct list name is [0] and + "i" 



Things I learned

I learned a significant amount working with the tkinter module and the sympy module. I believe that I barely touched the surface using the
modules in this project and I hope to learn more as I continue to expand on this project. I thought that some understanding of calculus was required 
to fully bring this project to its fruicion but I was mistaken because Sympy was mostly doing all the work.

Overall, I really enjoyed working through this project and hope to continue to expand it more in the future.
