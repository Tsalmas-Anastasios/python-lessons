#
# Εισαγωγή στο ttkbootstrap
#
# Όσοι γνωρίζουμε το bootstrap, θα γνωρίζουμε ότι πρόκειται για ένα css
# framework, το οποίο είναι αρκετά δημοφιλές στο διαδίκτυο και κυρίως στους
# front-end developers.
#
# To ttkbootstrap λοπόν είναι μια "συνεργασία" του ttk με το bootstrap το
# οποίο μας εξασφαλίζει όλα τα καλά εμφανισιακά χαρακτηριστικά του bootstrap.
#
# Για να ξεκινήσουμε λοιπόν, πρέπει να κατεβάσουμε την αντίστοιχη βιβλιοθήκη,
# την οποία κατόπιν θα μπορούμε να κάνουμε import.
# 
# Στα Windows, ανοίγουμε το command line και δίνουμε την εντολή
#           pip install ttkbootstrap
#
#
# Ας το γνωρίσουμε:
# Αντί να χρησιμοποιούμε μεγάλες δηλώσεις ttk, μπορούμε με μικρότερες και
# απλούστερες δηλώσεις να έχουμε ένα καλύτερο εμφανισιακά αποτέλεσμα:
#
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = tkk.Window(themename="superhero")

b1 = ttk.Button(root, text = "Submit", bootstyle="success")
b1.pack(side=LEFT, padx=5, pady=10)

b2 = ttk.Button(root, text="Submit", bootstyle="info-outline") 
b2.pack(side=LEFT, padx=5, pady=10) 

root.mainloop()

#
# Το νέο API είναι ελαστικό και οι παρακάτω δηλώσεις έχουν όλες το ίδο
# αποτέλεσμα, δίνοντάς μας έτσι μεγάλη ευελιξία και πολύ λιγότερα σφάλματα:
#           bootstyle = "info-outline"
#           bootstyle = "info outline"
#           bootstyle = ("info", "outline")
#           bootstyle = (INFO, OUTLINE)
#
# Για πλήρη αναφορά στα χαρακτηριστικά και τις δυνατότητες του ttkbootstrap
# μπορεί κάππιος να ψάξει σε βάθος στην τεκμηρίωσή του και στο GiHub
#       Τεκμηρίωση: https://ttkbootstrap.readthedocs.io/en/latest/
#       GitHub: https://github.com/israel-dryer/ttkbootstrap
#
# Για την ακρίβεια, τα χαρακτηριστικά του είναι:
#   - Ενσωματωμένα themes
#     Πάνω από δώδεκα dark & light themes
#
#   - Προκαθορισμένα στυλ
#     Έτοιμα widgets με στυλ όπως κουμπιά με στρόγγυλες γωνίες ή με διακεκομμένο
#     περίγραμμα
#
#   - Απλή χρήση με λέξεις κλειδιά
#     Εφαρμογή χρωμάτων και τύπων χρησιμοποιώντας λέξεις κλειδιά όπως primary
#     και striped αντί για την κλασική προσέγγιση του
#                   primary.Striped.Horizontal.TProgressbar.
#     Αν κάποιος έχει χρησιμοποιήσει το Bootstrap για web development, θα του είναι
#     ήδη προσφιλής η χρήση των κλάσεων της css.
#
#   - Πολλά νέα widgets
#     To ttkbootstrap έρχεται με πολλά σύγχρονα και με εξαιρετική εμφάνιση widgets
#     όπως τα: Meter, DateEntry και Floodgauge. Επιπροσθέτως, οι διάλογοι είναι
#     τώρα εμπλουτισμένοι με themes και πλήρως παραμετροποιήσιμοι.
#
#   - Ενσωματωμένος δημιουργός θεμάτων
#     Με το ttkbootstrap μπορούμε πλέον σχετικά εύκολα να δημιουργήσουμε και να φορτώσουμε
#     τα δικά μας θέματα.