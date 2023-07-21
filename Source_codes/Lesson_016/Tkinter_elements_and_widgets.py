# Γραφικά στοιχεία - widgets του Tkinter
#
# Το Tkinter μας παρέχει διάφορα στοιχεία ελέγχου, όπως κουμπιά, ετικέτες και
# πλαίσια κειμένου που χρησιμοποιούνται σε μια εφαρμογή γραφικού περιβάλλοντος.
# Αυτά τα στοιχεία ελέγχου ονομάζονται συνήθως widgets (γραφικά στοιχεία).
#
# Αυτή τη στιγμή υπάρχουν 15 τύποι γραφικών στοιχείων στο Tkinter.
# Ας δούμε αυτά τα widgets καθώς και μια σύντομη περιγραφή παρακάτω:
#
#   - Button, Κουμπί
#     Το γραφικό στοιχείο Button χρησιμοποιείται για την εμφάνιση των κουμπιών
#     εφαρμογή μας.
#       Παράδειγμα:
#           Τo Button widget χρησιμοποιείται για την προσθήκη κουμπιών σε ένα
#           παράθυρο. Κάθε κουμπί μπορεί να εμφανίζει κείμενο ή εικόνες που
#           μεταφέρει το σκοπό των κουμπιών. Μπορούμε να συνδέσουμε μια μέθοδο
#           σε ένα κουμπί που καλείται όταν κάνουμε κλικ στο κουμπί.
#
#       Σύνταξη:
#           w = Button(master, option = value, ... )
#
#       Παράμετροι
#           - master --> το γονικό παράθυρο
#           - Επιλογές --> Ακολουθεί η λίστα με τις πιο συχνά χρησιμοποιούμενες
#                          επιλογές για αυτό το γραφικό στοιχείο. Αυτές οι επιλογές
#                          μπορούν να χρησιμοποιηθούν ως ζεύγη κλειδιού-τιμής που
#                          χωρίζονται με κόμμα.
#                               1. activebackground
#                                   Χρώμα φόντου όταν το κουμπί βρίσκεται κάτω από
#                                   τον κέρσορα.
#                               2. activeforeground
#                                   Χρώμα παρασκηνίου όταν το κουμπί βρίσκεται κάτω
#                                   από τον κέρσορα.
#                               3. bd
#                                   Πλάτος περιγράμματος σε pixel. Η επιλογή είναι 2
#                               4. bg
#                                   Κανονικό χρώμα φόντου
#                               5. command
#                                   Λειτουργία ή μέθοδος που θα κληθεί όταν κάνουμε κλικ
#                                   στο κουμπί.
#                               6. fg
#                                   Κανονικό χρώμα παρασκηνίου (κειμένου)
#                               7. font
#                                   Γραμματοσειρά κειμένου που θα χρησιμοποιηθεί για την
#                                   ετικέτα του κουμπιού.
#                               8. height
#                                   Ύψος του κουμπιού σε γραμμές κειμένου (για κουμπιά
#                                   κειμένου) ή εικονοστιχεία (για εικόνες)
#
#                           Πλήρη σειρά επιλογών, καθώς και συχνά χρησιμοποιούμενων μεθό-
#                           δων με το χειριστήριο, μπορούμε να βρούμε στην τεκμηρίωση της
#                           Python.
#
#       Παράδειγμα δημιουργίας ενός κουμπιού
#

from tkinter import *
from tkinter import messagebox

# Element creation
top = Tk()
top.geometry("100x100")

# Δημιουργία μεθόδου η οποία καλείται με το πάτημα του κουμπιού
def helloCallBack():
    msg = messagebox.showinfo("Hello Python", "Hello world")

# Button element creation
B = Button(top, text="Hello", command=helloCallBack)

# Place the button to the window
B.place(x = 50, y = 50)
top.mainloop()



#
#   - Canvas, Καμβάς
#     Το widget Canvas χρησιμοποιείται για τη σχεδιάση σχημάτων, όπως γραμμές, οβάλ, πολύγωνα
#     και ορθογώνια.
#       Σύνταξη:
#           w = Canvas(master, option = value, ... )
#
#       Παράμετροι
#           - master --> Το γονικό παράθυρο
#           - Επιλογές --> Ακολουθεί η λίστα με τις πιο συχνά χρησιμοποιούμενες επιλογές για
#                          αυτό το γραφικό στοιχείο. Αυτές οι επιλογές μπορούν να χρησιμοποι-
#                          ηθούν ως ζεύγη κλειδιού-τιμής που χωρίζονται με κόμμα.
#                               1. bd
#                                  Πλάτος περιγράμματος σε pixel. Η προεπιλογή είναι 2
#                               2. bg
#                                  Κανονικό χρώμα φόντου
#                               3. confine
#                                  Αν είναι true (default value), ο καμβάς δεν μπορεί να βγει
#                                  έξω από την περιοχή του scrolling
#                               4. scrollregion
#                                  Ένα tuple (w, n, e, s) το οποίο καθορίζει πόσο μεγάλη περιοχή
#                                  του καμβά μπορεί να γίνει scrolled:
#                                       w = αριστερή πλευρά
#                                       n = η πάνω πλευρά
#                                       e = δεξιά πλευρά
#                                       s = κάτω πλευρά
#                               5. width
#                                  Το μέγεθος του καμβά στον άξονα των X.
#
#                          Πλήρη σειρά επιλογών, καθώς και συχνά χρησιμοποιούμενων μεθόδων με το
#                          χειριστήριο, μπορούμε να βρούμε στην τεκμηρίωση της Python.
#
#                          Υποστηρίζονται τα παρακάτω αντικείμενα:
#                               - arc
#                                 Δημιουργεί ένα τόξο το οποίο μπορεί να είναι χορδή ή μια απλή
#                                 καμπύλη.
#                                       coord = 10, 50, 240, 210
#                                       arc = canvas.create_arc(coord, start = 0, extent = 150, fill = "blue")
#                               - image
#                                 Δημιουργεί ένα αντικείμενο εικόνας, το οποίο μπορεί να είναι ένα στιγμιότυπο
#                                 της κλάσης BitmapImage ή της PhotoImage
#                                       filename = PhotoImage(file = "sunshine.gif")
#                                       image = canvas.create_image(50, 50, anchor = NE, image = filename)
#                               - line
#                                 Δημιουργεί μια γραμμή
#                                       line = canvas.create_line(x0, y0, x1, y1, ... , xn, yn, options)
#                               - oval
#                                 Δημιουργεί έναν κύκλο ή μια έλλειψη στις δεδομένες συντεταγμένες. Παίρνει δύο
#                                 ζεύγη συντεταγμένων. Την επάνω αριστερή και την κάτω δεξιά γωνία του τετραγώνου
#                                 που εμπεριέχει το οβάλ.
#                                       oval = canvas.create_oval(x0, y0, x1, y1, options)
#                               - polygon
#                                 Δημιουργεί ένα πολύγωνο αντικείμενο οπυ πρέπει να έχει το λιγότερο τρείς ευθείες
#                                       polygon = canvas.create_polygon(x0, y0, x1, y1, ... , xn, yn, options)
#
#
#       Παράδειγμα υλοποίησης - δημιουργίας καμβά
#

from tkinter import *
from tkinter import messagebox

top = Tk()

c = Canvas(top, bg = "blue", height= 250, width = 300)
coord = 10, 50, 240, 210
arc = c.create(coord, start = 0, extent = 150, fill = "red")
line = c.create(10, 10, 200, 200, fill = 'white')
c.pack()

top.mainloop()






#
#
# Checkbutton - Control button
#
# Το γραφικό στοιχείο Checkbutton χρησιμοποιείται για την εμφάνιση ενός αριθμού επιλογών
# ως πλαίσια ελέγχου. Ο χρήστης μπορεί να επιλέξει πολλές επιλογές ταυτόχρονα
#
#   Σύνταξη:
#       w = Checkbutton(master, option, ...)
#
#   Παράμετροι
#       - master --> Το γονικό παράθυρο
#       - Επιλογές --> Ακολουθεί η λίστα με τις πιο συχνά χρησιμοποιούμενες επιλογές για
#                      αυτό το γραφικό στοιχείο. Αυτές οι επιλογές μπορούν να χρησιμοποι-
#                      ηθούν ως ζεύγη κλειδιού-τιμής που χωρίζονται με κόμμα
#                           1. activebackground
#                              Χρώμα φόντου όταν το κουμπί βρίσκεται κάτω από τον κέρσορα
#                           2. activeforeground
#                              Χρώμα παρασκηνίου όταν το κουμπί βρίσκεται κάτω από τον
#                              κέρσορα
#                           3. bd
#                              Πλάτος περιγράμματος σε pixel. Η προεπιλογή είναι 2
#                           4. bg
#                              Κανονικό χρώμα φόντου
#                           5. command
#                              Λειτουργία ή μέθοδος που θα κληθεί όταν κάνουμε κλικ στο
#                              κουμπί
#                           6. fg
#                              Κανονικό χρώμα παρασκηνίου (κειμένου)
#                           7. font
#                              Γραμματοσειρά κειμένου που θα χρησιμοποιηθεί για την ετικέτα
#                              του κουμπιού
#                           8. height
#                              Ύψος του κουμπιού σε γραμμές κειμένου (για κουμπιά κειμένου)
#                              ή εικονοστοιχεία (για εικόνες).
#                           9. bitmap
#                              Απεικόνιση μιας μονόχρωμης εικόνας στο κουμπί
#                           10. image
#                              Απεικόνιση μιας γραφικής εικόνας στο κουμπί
#
#                       Μια πλήρη σειρά επιλογών, καθώς και συχνά χρησιμοποιούμενων μεθόδων
#                       με το χειριστήριο, μπορούμε να βρούμε στην τεκμηρίωση της Python
#
#
#   Ένα παράδειγμα δημιουργίας checkbutton
#
#

from tkinter import *
import tkinter

top = Tk()

CheckVar1 = IntVar()
CheckVar2 = IntVar()
c1 = Checkbutton(top, text = "Music", variable = CheckVar1, \
                onvalue = 1, offvalue = 0, height = 5, \
                width = 20)
c2 = Checkbutton(top, text = "Video", variable = CheckVar2, \
                onvalue = 1, offvalue = 0, height = 5, \
                width = 20)
c1.pack()
c2.pack()

top.mainloop()


#
#
# Entry - Είσοδος
#
# Το γραφικό στοιχείο Entry χρησιμοποιείται για την εμφάνιση ενός πεδίου κειμένου
# μιας γραμμής για την αποδοχή τιμών από έναν χρήστη.
#
# Η σύνταξη και οι παράμετροι είναι παρόμοια και μπορούμε να τα αναζητήσουμε (σε
# περίπτωση μη επάρκειας όσων διαθέτουμε) στην τεκμηρίωση της Python
#
# Ένα παράδειγμα είναι:
#
#

from tkinter import *

top = Tk()

L1 = Label(top, text = "Όνομα χρήστη")
L1.pack(side = LEFT)
E1 = Entry(top, bd = 5)
E1.pack(side = RIGHT)

top.mainloop()


#
#
# Frame - Πλαίσιο
#
# Το γραφικό στοιχείο Frame χρησιμοποιείται ως γραφικό στοιχείο κοντέινερ για την
# οργάνωση άλλων γραφικών στοιχείων.
#
# Παράδειγμα
#
#

from tkinter import *

root = Tk()

frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

redbutton = Button(frame, text = "Red", fg = "red")
redbutton.pack(side = LEFT)

greenbutton = Button(frame, text = "Green", fg = "green")
greenbutton.pack(side = LEFT)

bluebutton = Button(frame, text = "Blue", fg = "blue")
bluebutton.pack(side = LEFT)

blackbutton = Button(bottomframe, text = "Black", fg="Black")
blackbutton.pack(side = BOTTOM)

root.mainloop()



#
#
# Label - Ετικέτα (Επιγραφή)
#
# Το γραφικό στοιχείο Label χρησιμοποιείται για την παροχή λεζάντας μιας γραμμής για
# άλλα γραφικά στοιχεία. Μπορεί επίσης να περιέχει εικόνες.
#
# Παράδειγμα:
#
#

from tkinter import *

root = Tk()

var = StringVar()
label = Label(root, textvariable = var, relief = RAISED)

var.set("Hello!")
label.pack()

root.mainloop()



#
#
# Listbox - Πλαίσιο λίστας
#
# Το γραφικό στοιχείο Listbox χρησιμοποιείται για την παροχή μιας λίστας επιλογών σε έναν
# χρήστη.
#
#
# Παράδειγμα
#
#

from tkinter import *
import tkinter

top = Tk()

Lb1 = Listbox(top)
Lb1.insert(1, "Python")
Lb1.insert(1, "Perl")
Lb1.insert(1, "C")
Lb1.insert(1, "PHP")
Lb1.insert(1, "Java")
Lb1.insert(1, "Ruby")

Lb1.pack()

top.mainloop()



#
#
# Menubutton - Κουμπί μενού
#
# Το γραφικό στοιχείο Menubutton χρησιμοποιείται για την εμφάνιση μενού στην εφαρμογή μας.
#
# Παράδειγμα
#
#

from tkinter import *
import tkinter

top = Tk()

mb = Menubutton(top, text="Σάλτσες", relief= RAISED)
mb.grid()
mb.menu = Menu(mb, tearoff = 0)
mb["menu"] = mb.menu

mayoVar = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton(label = "Μαγιονέζα", variable = mayoVar)
mb.menu.add_checkbutton(label = "Ketchup", variable = ketchVar)

mb.pack()

top.mainloop()


#
#
# Menu - Μενού
#
# Το γραφικό στοιχείο Μενού χρησιμοποιείται για την παροχή διάφορων εντολών σε έναν
# χρήστη. Αυτές οι εντολές περιέχονται στο Menubutton
#
# Παράδειγμα
#
#

from tkinter import *

def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text = "Do nothing button")
    button.pack()
    


root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "Νέο", command = donothing)
filemenu.add_command(label = "Άνοιγμα", command = donothing)
filemenu.add_command(label = "Αποθήκευση", command = donothing)
filemenu.add_command(label = "Αποθήκευση ως...", command = donothing)
filemenu.add_command(label = "Κλείσιμο", command = donothing)

filemenu.add_separator()

filemenu.add_command(label = "Έξοδος", command = root.quit)
menubar.add_cascade(label="Αρχείο", menu = filemenu)

editmenu = Menu(menubar, tearoff = 0)
editmenu.add_command(label="Αναίρεση", command = donothing)
editmenu.add_separator()

editmenu.add_command(label="Αποκοπή", command=donothing)
editmenu.add_command(label="Αντιγραφή", command=donothing)
editmenu.add_command(label="Επικόλληση", command=donothing)
editmenu.add_command(label="Διαγραφή", command=donothing)
editmenu.add_command(label="Επιλογή όλων", command=donothing)

menubar.add_cascade(label="Επεξεργασία", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="Αρχείο Οδηγιών", command=donothing)
helpmenu.add_command(label="Περί...", command=donothing)
helpmenu.add_command(label="Βοήθεια", command=donothing)

root.config(menu=menubar)
root.mainloop()
