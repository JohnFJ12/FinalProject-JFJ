Modules
I mainly used the Tkinter and Sympy modules for this project. For Sympy, I worked with functions like integrate, parse_expr, cross, dot, and matrix operations. With Tkinter, I learned how to create and close windows, and how to open new ones using buttons. I also used tkinter.Label and tkinter.Tk() to create new windows and tkinter.attributes to set them to fullscreen. Tkinter.Text was super helpful for creating a space to easily retrieve user input.

Challenges
•	Problem 1: Latex Compatibility with Tkinter Textbox
I initially thought I could print formatted integrals in a Tkinter label. After more research, I found that it was possible to display LaTeX in Tkinter, but it required using Matplotlib, which was a bit too complicated for my timeline. So, I worked around it by using ASCII art and .format to approximate integral bounds and make it look as close as possible.
	•	Problem 2: Simulating a Typing Effect for a Chatbot
To simulate a chatbot typing, I needed to print text letter-by-letter, but .sleep() didn’t work well with Tkinter. I fixed this by using tkinter.after(), which let me create a mini typing simulation module. It uses a for loop to insert each character in a text box every 100 ms to mimic typing.
	•	Problem 3: Formatting Sympy’s Cross Product Output
Sympy’s cross function returned a list instead of a nicely formatted vector. I got around this by formatting the output myself—adding “i,” “j,” and “k” to the appropriate indices in the list.

What I Learned

Working with Tkinter and Sympy taught me a lot. I realized I’d barely scratched the surface of what these modules can do, and I’m excited to keep expanding on this project. Surprisingly, I didn’t need a deep understanding of calculus—Sympy handled most of the heavy lifting. Overall, I had a lot of fun with this project and hope to keep building on it!
