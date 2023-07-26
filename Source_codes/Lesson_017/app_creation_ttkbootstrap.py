# Δημιουργία εφαρμογής
#
# Γνωρίζοντας ήδη το ttk, η κλασική προσέγγιση θα ήταν να τα κάνουμε όλα όπως
# ληδη γνωρίζουμε με τη διαφορά, να εισάγουμε το ttkbootstrap αντί για το ttk
# και να χρησιμοποιήσουμε το bootstyle αντί για το boot, καθώς και να εισάγουμε
# τις ¨σταθερές" (constants) του bootstrap.
# Δηλαδή:
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tk.Tk()

b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS) 
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE)) 
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()



#
# Νέα προσέγγιση
#
# Το ίδιο αποτέλεσμα μπορούμε να έχουμε χρησιμοποιώντας τη νέα κλάση Window.
# Στην αρχή, η διαφορά μοιάζει μικρή, όμως αυτή η κλάση χρησιμοποιεί ειδικές
# παραμέτρους για να ορίζει πολλά από τα χαρακτηριστικά, ενώ με την κλασική προσέγγιση
# με την κλάση Tk, θα χρειαζόμασταν μεθόδους. Επίσης, το στυλιζαρισμένο αντικείμενο,
# ενσωματώνεται στο παράθυρο αυτόματα, όπως θα δούμε παρακάτω:
#
import ttkboottstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

b1 = ttk.Button(root, text="Button 1", bootstyle=SUCCESS) 
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Button 2", bootstyle=(INFO, OUTLINE)) 
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()






#
# Επιλογή theme
#
# To default theme είναι το litera, αλλά μπορούμε να θέσουμε όποιο άλλο θεωρούμε
# για να ξεκινήσουμε, επιλέγοντας έναν από τους παρακάτω τρόπους:
#
import ttkbootstrap as ttk

# κλασική προσέγγιση
root = ttk.Tk()
style = ttk.Style("darkly")

# Νέα προσέγγιση
root = ttk.Window(thyemename="darkly")

#
# Στο ttkbootstrap υπάρχουνε δεκάδες προκαθορισμένα στυλ, τα οποία εφαρμόζονται χρησι-
# μοποίωντας λέξεις κλειδιά, που παραμετροποιούν και τον τύπο και το χρώμα του widget.
# Για την ακρίβεια, το χρώμα καθορίζεται κάθε φορά από την επιλογή του αντίστοιχου theme.
#
# Σαν παράδειγμα, χρησιμοποιώντας τη λέξη κλειδί outline, δημιουργούμε ένα κουμπί με
# τύπο outline (περίγραμμα), αλλά χρησιμοποιώντας επίσης τη λέξη κλειδί info θα αλλάξει
# το χρώμα του περιγράμματος και του κειμένου.
#
# Πάμε να δούμε τα χρώματα για κάθε κουμπί:
#
import ttkbootstrap as ttk
from ttkbootstrap.constants import * 

root = ttk.Window()

b1 = ttk.Button(root, text='primary', bootstyle=PRIMARY) 
b1.pack(side=LEFT, padx=5, pady=5)

b2 = ttk.Button(root, text='secondary', bootstyle=SECONDARY) 
b2.pack(side=LEFT, padx=5, pady=5)

b3 = ttk.Button(root, text='success', bootstyle=SUCCESS) 
b3.pack(side=LEFT, padx=5, pady=5)

b4 = ttk.Button(root, text='info', bootstyle=INFO) 
b4.pack(side=LEFT, padx=5, pady=5)

b5 = ttk.Button(root, text='warning', bootstyle=WARNING) 
b5.pack(side=LEFT, padx=5, pady=5) 

b6 = ttk.Button(root, text='danger', bootstyle=DANGER) 
b6.pack(side=LEFT, padx=5, pady=5)

b7 = ttk.Button(root, text='light', bootstyle=LIGHT) 
b7.pack(side=LEFT, padx=5, pady=5)

b8 = ttk.Button(root, text='dark', bootstyle=DARK) 
b8.pack(side=LEFT, padx=5, pady=5)

root.mainloop()


#
# Ας δούμε τώρα πόσο πιο απλά θα μπορούσαμε να έχουμε δημιουργήσει όλα
# αυτά τα κουμπιά, χρησιμοποιώντσς το αντικείμενο Style.colors το οποίο
# εμπεριέχει όλα τα χρώματα του theme και το οποίο επίσης είναι ένας
# iterator.
#
# Δηλαδή:
#
import ttkbootstrap as ttk
from ttkbootstrap.constants import * 

root = ttk.Window()

for color in root.style.colors:
    b = ttk.Button(root, text=color, bootstyle=color)
    b.pack(side=LEFT, padx=5, pady=5)
    
#
# Η λέξη κλειδί μπορεί να ελέγξει τον τύπο του widget που παρουσιάζεται.
# Ας δούμε στο επόμενο παράδειγμα ένα solid και ένα outline κουμπί. Είναι
# και τα δύο κουμπιά, διαφορετικών όμως τύπων:
import ttkbootstrap as ttk
from ttkbootstrap.constants import * 


root = ttk.Window()

b1 = ttk.Button(root, text="Solid Button", bootstyle=SUCCESS) 
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Outline Button", bootstyle=(SUCCESS, OUTLINE))
b2.pack(side=LEFT, padx=5, pady=10)

root.mainloop()


#
# Όπως βλέπουμε, προσθέτοντας τη λέξη κλειδί outline, το κουμπί μετατρέπεται από
# solid σε outline.