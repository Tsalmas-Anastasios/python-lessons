# exercise 2
#
#
# Δημιουργήστε ένα γραφικό περιβάλλον με ένα παράθυρο στο οποίο
# να θέσετε το προεπιλεγμένο του μέγεθος σε 600x300 και τον τίτλο
# του σε "-Προεπιλεγμένο μέγεθος παραθύρου-" με το tkinter
#

import tkinter as tk

parent = tk.Tk()

parent.title('-Προεπιλεγμένο μέγεθος παραθύρου')
parent.geometry('600x300')

parent.mainloop()