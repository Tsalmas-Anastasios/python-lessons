# Exercise 1
#
# Γράψτε ένα προγραμματάκι το οποίο έχει τρία πεδία εισαγωγής:
#   - Όνομα
#   - User ID
#   - Password
# καθώς και ένα κουμπί εισαγωγής 'ΥΠΟΒΟΛΗ'
#

import tkinter as tk

root = tk.Tk()
root.geometry("400x250")

name = tk.Label(root, text="Όνομα").place(x = 30, y = 50)
email = tk.Label(root, text="E-mail").place(x = 30, y = 90)
password = tk.Label(root, text="Password").place(x = 30, y = 130)
submitbtn = tk.Button(root, text = "ΥΠΟΒΟΛΗ", activebackground="green", activeforeground = "blue").place(x = 120, y = 170)

entry1 = tk.Entry(root).place(x = 85, y = 50)
entry2 = tk.Entry(root).place(x = 85, y = 90)
entry3 = tk.Entry(root).place(x = 90, y = 130)

root.mainloop()