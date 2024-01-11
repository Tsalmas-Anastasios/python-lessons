'''
Γράψτε ένα προγραμματάκι το οποίο να έχει τρία πεδία εισαγωγής:
Όνομα, User ID, και Password, καθώς κι ένα κουμπί εισαγωγής, "ΥΠΟΒΟΛΗ".
'''

import tkinter as tk
root = tk.Tk()
root.geometry("400x250")

# Πεδίο 1
name = tk.Label(root, text = "Όνομα").place(x = 30, y = 50)

# Πεδίο 2
email = tk.Label(root, text = "User ID").place(x = 30, y = 90)

# Πεδίο 3
password =  tk.Label(root, text = "Password").place(x = 30, y = 130)

# Κουμπί υποβολής στοιχειων
sbmitbtn = tk.Button(root, text = "ΥΠΟΒΟΛΗ", activebackground = "green", activeforeground = "white").place(x = 120, y = 170)
entry1 = tk.Entry(root).place(x = 90, y = 50)
entry2 = tk.Entry(root).place(x = 90, y = 90)
entry3 = tk.Entry(root).place(x = 90, y = 130)

# Δημιουργία και επανάληψη παραθύρου
root.mainloop()
