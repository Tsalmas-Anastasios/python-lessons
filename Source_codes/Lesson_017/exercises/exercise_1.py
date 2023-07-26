# exercise 1
#
#
# Δημιουργήστε ένα γραφικό περιβάλλον με το tkinter, το οποίο να
# περιέχει ένα label και να αλλάξετε τη γραμματοσειρά σε Arial Bold,
# καθώς και το μέγεθός της σε 70 και να την κάνετε σε μορφή bold
# (έντονη)
#
#

import tkinter as tk

parent = tk.Tk()

parent.title("-Αλλαγή label στο tkinter")
my_label = tk.Label(parent, text="Γεια", font=("Arial Bold", 70))
my_label.grid(column = 0, row = 0)

parent.mainloop()