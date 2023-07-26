# exercise 3
#
#
# Φτιάξτε ένα απλό παράθυρο στο tkinter στο οποίο να
# απενεργοποιείτε το resizing του παραθύρου
#


import tkinter as tk

parent = tk.Tk()

parent.title('-Απενεργοποίηση του resizing-')
parent.resizable(0,0)       # απενεργοποίηση του resizing

parent.mainloop()