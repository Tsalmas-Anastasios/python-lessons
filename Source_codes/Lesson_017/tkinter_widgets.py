# tkinter-widgets (συνέχεια)
#
# 1. Message - Μήνυμα
#    Το Widget Message χρησιμοποιείται για την εμφάνιση πεδίων κειμένου
#    πολλών γραμμών για την αποδοχή τιμών από έναν χρήστη
#
#    Παράδειγμα:
#
from tkinter import *

root = Tk()

var = StringVar()
label = Message(root, textvariable=var, relief = RAISED)

var.set("Message")
label.pack()

root.mainloop()



#
# 2. Radiobutton - Κουμπί 'ραδιοφώνου'
#    Το γραφικό στοιχείο Radiobutton χρησιμοποιείται για την εμφάνιση ενός
#    αριθμούεπιλογών ως κουμπιά επιλογής. Ο χρήστης μπορεί να επιλέξει μόνο
#    μία επιλογή κάθε φορά.
#
#    Παράδειγμα:
#
from tkinter import *

def sel():
    selection = f"You selected the option {str(var.get())}"
    label.config(text = selection)
    

root = Tk()

var = IntVar()
R1 = Radiobutton(root, text="Option 1", variable = var, value = 1, command = sel)
R1.pack(anchor = W)

R2 = Radiobutton(root, text="Option 2", variable = var, value = 2, command = sel)
R2.pack(anchor = W)

R3 = Radiobutton(root, text="Option 3", variable = var, value = 3, command = sel)
R3.pack(anchor = W)

label = Label(root)
label.pack()

root.mainloop()





#
# 3. Scale - Κλίμακα
#    Το γραφικό στοιχείο Scale χρησιμοποιείται για την παροχή ενός γραφικού στοιχείου
#    ρυθμιστικού.
#
#    Παράδειγμα:
from tkinter import *

def sel():
    selection = f"Value = {str(var.get())}"
    label.config(text = selection)
    
    
root = Tk()

var = DoubleVar()
scale = Scale(root, variable = var)
scale.pack(anchor = CENTER)

button = Button(root, text = "Set the value", command = sel)
button.pack(anchor = CENTER)

label = Label(root)
label.pack()

root.mainloop()






#
# 4. Scrollbar - Γραμμή κύλισης
#    Το γραφικό στοιχείο Scrollbar χρησιμοποιείται για την προσθήκη δυνατότητας κύλισης
#    σε διάφορα γραφικά στοιχεία, όπως πλαίσια λίστας.
#
#    Παράδειγμα:
from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side = RIGHT, fill = Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)
for line in range(100):
    mylist.insert(END, f"This is the line number {str(line)}")
    
mylist.pack(side = LEFT, fill = BOTH)
scrollbar.config( command = mylist.view )

root.mainloop()






#
# 5. Text - Κείμενο
#    Το γραφικό στοιχείο του κειμένου χρησιμοποιείται για την εμφάνιση κειμένου σε πολλές
#    γραμμές.
#
#    Παράδειγμα:
from tkinter import *

root = Tk()

text = Text(root)
text.insert(INSERT, "Hello...")
text.insert(END, "Good bye...")
text.pack()
text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="blue", foreground="green")

root.mainloop()





#
# 6. TopLevel - Κορυφαίο επίπεδο
#    Το γραφικό στοιχείο Toplevel χρησιμοποιείται για την παροχή ενός ξεχωριστού κοντέινερ
#    παραθύρου.
#
#    Παράδειγμα:
from tkinter import *

root = Tk()
root.title("hello")

top = Toplevel()
top.title("Python")

top.mainloop()





#
# 7. Spinbox
#    Το γραφικό στοιχείο Spinbox είναι μια παραλλαγή του τυπικού γραφικού στοιχείου Tkinter
#    Entry, το οποίο μπορεί να χρησιμοιποιηθεί για επιλογή από έναν σταθερό αριθμό τιμών.
#
#    Παράδειγμα:
from tkinter import *

master = Tk()

w = Spinbox(master, from_ = 0, to = 10)
w.pack()

master.mainloop()




#
# 8. PanedWindow
#    Ένα PanedWindow είναι ένα γραφικό στοιχείο κοντέινερ που μπορεί να περιέχει οποιονδήποτ
#    αριθμό παραθύρων, διατεταγμένα οριζόντια ή κάθετα.
#
#    Παράδειγμα:
from tkinter import *

m1 = PanedWindow()
m1.pack(fill = BOTH, expand = 1)

left = Entry(m1, bd = 5)
m1.add(left)

m2 = PanedWindow(m1, orient = VERTICAL)
m1.add(m2)

top = Scale(m2, orient = HORIZONTAL)
m2.add(top)

bottom = Button(m2, text = "OK")
m2.add(bottom)

mainloop()






#
# 9. Label frame - Πλαίσιο ετικέτας
#    Ένα πλαίσιο ετικέτας είναι ένα απλό widget κοντέινερ. Ο πρωταρχικός του σκοπός είναι να
#    λειτουργεί ως διαχωριστικό ή δοχείο για πολύπλοκες διατάξεις παραθύρων
#
#    Παράδειγμα:
from tkinter import *

root = Tk()

labelframe = LabelFrame(root, text = "Αυτό είναι ένα label frame")
labelframe.pack(fill="both", expand="yes")

left = Label(labelframe, text = "Μέσα σε ένα LabelFrame")

left.pack()

root.mainloop()




#
# 10. tkMessageBox
#     Αυτή η ενότητα χρησιμοποιείται για την εμφάνιση πλαισίων μηνυμάτων στις εφαρμογές μας.
#
#     Παράδειγμα:
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry('100x100')


def hello():
    messagebox.showinfo("Say Hello", "Hello World")
    
    
B1 = Button(top, text="Say Hello", command = hello)
B1.place(x = 35, y = 50)

top.mainloop()