# Exercise 2
#
# Γράψτε ένα πρόγραμμα χρησιμοποιώντας το tkinter module, το οποίο
# πρέπει να δημιουργεί ένα checkbutton με κείμενο:
# "Τσεκάρισμα όταν είναι True". Χρησιμοποιείστε μια μεταβλητή boolean
# για να διευκολυνθείτε
#
#

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_boolean_var = tk.BooleanVar()

my_checkbutton = ttk.Checkbutton(
    text = "Τσεκάρισμα όταν είναι true",
    variable = my_boolean_var
)
my_checkbutton.pack()

root.mainloop()