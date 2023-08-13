# Story Game
#
#
# Το παιχνίδι μας θα είναι ένα παιχνίδι κειμένου. Αυτός ο τύπος παιχνιδιών
# ήταν δημοφιλής πριν πολλά χρόνξια. Τότε που τα γραφικά και η "δράση", δεν
# ήταν δυνατόν να υποστηριχτούν από το hardware.
#
# Πώς λειτουργεί το παιχνίδι:
# Υπάρχει ένα μικρό κείμενο με κενά και ο χρήστης καλείται να συμπληρώσει
# κάποια στοιχεία, τα οποία αργότερα θα συμπληρώσουν τα κενά του προϋπάρχοντος
# κειμένου. Ο χρήστης δεν γνωρίζει που ακριβώς θα μπουν τα στοιχεία που δίνει.
# Ο χρήστης δεν γνωρίζει που ακριβώς θα μπουν τα στοιχεία που δίνει. Αυτό
# άλλωστε είναι και το "διασκεδαστικό" όφελος του παιχνιδιού.
#
#
#
# Στόχος
# ------
# Στόχος μας είναι να φτιάξουμε 3 μικρά σενάρια και να ορίσουμε "κενά" σημεία,
# στα οποία εμείς να ζητάμε από τον χρήστη να μας δίνει στοιχεία και κατόπιν
# όλα αυτά τα στοιχεία, να τυπώνονται στην κονσόλα σαν μια ενιαία ιστορία.
#
# Είναι ένα project σχετικά εύκολο στην υλοποίηση και περισσότερο θα πρέπει
# να σκεφτούμε τις ιστοριούλες, καθώς και τα κενά που θα δημιουργήσουμε, ώστε
# η ιστορία να έχει ενδιαφέρον.
#
# Ο χρήστης που επιλέγει την ιστορία που θέλει να συμπληρώσει, πατώντας στο
# αντίστοιχο κουμπί και κατόπιν, του ζητούνται κάποια δεδομένα, όπως ένα "όνομα"
# ένα "ρήμα" κλπ.
#
# Η ελληνική γλώσσα δεν προσφέρεται για τέτοιου είδους παιχνίδια καθότι έχει πολλές
# πτώσεις, πρόσωπα και ιδιαιτερότητες, με αποτέλεσμα στην τελική ιστορία να υπάρχουν
# γραμματικά λάθη, όμως αυτό μας βάζει να γινόμαστε ακόμα πιο λεπτομερείς και
# ακριβείς σ' αυτό που ζητάμε από τον χρήστη (πχ "συμπληρώστε α' πληθυντικό πρόσωπο"),
# αλλά και στο πως συντάσσουμε την ιστορία.
#
#


#
# Προαπαιτούμενα
# --------------
# Δεν χρειαζόμαστε κάτι περισσότερο απ' αυτό που ήδη έχουμε εγκαταστήσει μέχρι τώρα.
# Όλα τα modules που χρειαζόμαστε είναι ήδη εγκατεστημένα και χρειάζεται απλά να τα
# εισάγουμε.
#


#
# Δομή έργου
# ----------
# Το έργο μας θα έχει την παρακάτω απλή δομή:
#   - Εισγωγή modules
#   - Δημιουργία παραθύρου
#   - Καθορισμός συναρτήσεων
#   - Δημιουργία γραφικού περιβάλλοντος
#


#
# Κατασκευή έργου - Περιγραφή - Σχόλια
# ------------------------------------
#
# Πρώτα από όλα, καθορίζουμε τις ιστοριούλες μία προς μία. Ονομάζουμε τη συνάρτηση που
# θα χρειαστούμε με το όνομα της ιστορίας και φτιάχνουμε ένα print() με το οποίο θα
# τυπώνουμε την ιστορία.
#
# Τώρα, μπορούμε να καθορίσουμε κάποια κενά, στα οποία θα ζητάμε από τον χρήστη να
# συμπληρώσει τα στοιχεία.
#
# Έτσι, καθορίζουμε τις αντίστοιχες μεταβλητές, ζητάμε και παίρνουμε δεδομένα από τον
# χρήστη και με το τελευταίο στοιχείο τυπώνουμε όλη την ιστορία μας. Επαναλαμβάνουμε
# τα βήματα για κάθε ιστορία
#


#
# Εισαγωγή των modules
# --------------------
# Μιας και το παράθυρό μας είναι αρκετά απλό, δεν χρειάζεται καν να εισάγουμε το
# tkinter
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


#
# Δημιουργία του παραθύρου
# ------------------------
# Δημιουργούμε και αρχικοποιούμε το παράθυρο, καθώς και κάποια βασικά widgets του.
# Περιλαμβάνουμε τα themes του ttkbootstrap για ευκολία πειραματισμών:

# themes = cosmo, flaty, journal, litera, lumen, minty, pulse, sandstone
# united, yeti, morph, simplex, cerculean

root = ttk.Window(themename="simplex")  # root είναι το όνομα του παραθύρου μας
root, geometry("380x250")  # Διαστάσεις παραθύρου
root.title("-Δημιουργός Ιστορίας-")  # Ο τίτλος του παιχχνιδιού μας

label1 = ttk.tk.Label(
    root,
    text="Φτιάξε την ιστορία σου \n με τη βοήθεια της Python!",
    font=("Helvetica", 20),
    bootstyle=PRIMARY,
).pack()  # Κείμενο μέσα στο παράθυρο

label2 = ttk.tk.Label(
    root, text="Κάνε κλικ παρακάτω:", font=("Helvetica", 15), bootstyle=PRIMARY
).place(
    x=40, y=80
)  # Κείμενο μέσα στο παράθυρο


#
# Καθορισμός συναρτήσεων
# ----------------------
# Κάθε συνάρτηση είναι μια πλήρης ιστορία και συνδέεται με ένα κουμπί. Θα μπορούσαμε να
# έχουμε περισσότερες ιστορίες ή και μόνο μία. Σε κάθε συνάρτηση βρίσκεται το κύριο μέρος
# του προγράμματός μας.
# Δίνουμε σαφείς οδηγίες στο τι ακριβώς ζητάμε από τον χρήστη.
#
# Πάμε να δούμε τις συναρτήσεις


##################### - ΙΣΤΟΡΙΕΣ - ########################


def photographer():
    animals = input("Εισάγετε όνομα ζώου: ")
    profession = input("Εισάγετε ένα επάγγελμα (στην αιτιατική): ")
    cloth = input("Εισάγετε όνομα υφάσματος: ")
    things = input("Εισάγετε όνομα αντικειμένων: ")
    name = input("Εισάγετε όνομα με άρθρο: ")
    place = input("Εισάγετε τόπο: ")
    verb = input("Εισάγετε ρήμα σε ενεστώτα, γ πληθυντικό: ")
    food = input("Εισάγετε όνομα τροφής: ")
    print(
        "Πες "
        + food
        + ", είπε ο φωτογράφος καθώς το flash άναψε! "
        + name
        + " κι εγώ  πήγαμε στο/στη "
        + place
        + " σήμερα, για να πάρουμε τις φωτογραφίες μας. Η πρώτη φωτογραφία την οποία θέλαμε να δούμε, ήταν αυτή που είμαστε ντυμένοι "
        + animals
        + " παριστάνοντας έναν/μια "
        + profession
        + " .Όταν είδαμε τη δεύτερη φωτογραφία, ήταν ακριβώς αυτό που θέλαμε. Μοιάζαμε και οι δύο με "
        + things
        + " που φοράνε "
        + cloth
        + " και "
        + verb
        + " --ακριβώς ότι είχα στο μυαλό μου"
    )


def butterfly():
    adjective = input("Εισάγετε ένα επίθετο (θηλυκό) : ")
    color = input("Εισάγετε ένα χρώμα : ")
    thing = input("Εισάγετε ένα αντικείμενο :")
    place = input("Εισάγετε μια πόλη : ")
    person = input("Εισάγετε ένα όνομα (αιτιατική): ")
    adjective1 = input("Εισάγετε ένα επίθετο : ")
    insect = input("Εισάγετε ένα έντομο : ")
    food = input("Εισάγετε μια τροφή : ")
    verb = input("Εισάγετε ένα ρήμα (α πληθυντικό): ")

    print(
        "Χθες το βράδυ ονειρεύτηκα ότι ήμουν μια "
        + adjective
        + " πεταλούδα με "
        + color
        + " φτερά που έμοιαζαν με "
        + thing
        + ". Πετούσα για τον/την"
        + place
        + " με τον καλύτερό μου φίλο και τον/την "
        + person
        + " που ήταν ένας/μια "
        + adjective1
        + " "
        + insect
        + " . Φάγαμε λίγο/η "
        + food
        + " μόλις φτάσαμε και αποφασίσαμε να "
        + verb
        + ' και το όνειρο τέλειωσε όταν είπα "Ας '
        + verb
        + '"'
    )


def appleandapple():
    person = input("Εισάγετε ένα όνομα (σε γενική πτώση): ")
    color = input("Εισάγετε ένα χρώμα (πληθυντικός) : ")
    foods = input("Εισάγετε μια τροφή (γενική) : ")
    adjective = input("Εισάγετε ένα επίθετο (ουδέτερο ενικός): ")
    thing = input("Εισάγετε ένα αντικείμενο : ")
    place = input("Εισάγετε μια πόλη : ")
    verb = input("Εισάγετε ένα ρήμα (ενεστώτας, α πληθυντικό): ")
    adverb = input("Εισάγετε ένα επίρρημα : ")
    food = input("Εισάγετε μια τροφή: ")
    things = input("Εισάγετε ένα αντικείμενο : ")

    print(
        "Σήμερα πήραμε μήλα από το περιβόλι του/της "
        + person
        + ". Δεν είχα ιδέα πως υπάρχουν πολλές ποικιλίες μήλων. Έφαγα "
        + color
        + " μήλα κατευθείαν από το δέντρο και είχαν γεύση "
        + foods
        + ". Μετά είδαμε ένα "
        + adjective
        + " μήλο που έμοιαζε με "
        + thing
        + ". Όταν η τσάντα μας γέμισε, πήγαμε μια βόλτα στον/στην "
        + place
        + " και ξαναγυρίσαμε πίσω. Τελειώσαμε τη βόλτα μας αφού πέσαμε (ευτυχώς) σε μια στοίβα άχυρα και μετά έπρεπε να "
        + verb
        + " "
        + adverb
        + ". Δεν κρατιέμαι να φτάσω σπίτι και να μαγειρέψω με τα μήλα. Θα κάνουμε μηλο- "
        + food
        + " και "
        + things
        + " -πιτες!."
    )


#
# Καθορισμός υπόλοιπων γραφικών στοιχείων (κουμπιών)
# --------------------------------------------------
# Το μόνο που μας λείπει τώρα είναι τα κουμπιά. Όπως είπαμε, κάθε κουμπί
# είναι η αρχή μιας ιστορίας την οποία με το πάτημά του, επιλέγει ο χρήστης.
# Περιλαμβάνουμε το σύνολο των στυλ του ttkbootstrap για πειραματισμό. Πάμε
# λοιπόν να τα φτιάξουμε:

# Για πιο όμορφα κουμπιά, χρησιμοποιούμε ttkbootstrap
# ttkbootstrap styles - PRIMARY, SECONDARY, SUCCESS, INFO, WARNING, DANGER, LIGHT
# DARK

b1 = ttk.tk.Button(root, text="Ο φωτογράφος", bootstyle=PRIMARY, command=photographer)
b1.pack(side=BOTTOM, padx=5, pady=5)
b2 = ttk.Button(root, text="Μήλο και Μήλο", bootstyle=SUCCESS, command=appleandapple)
b2.pack(side=BOTTOM, padx=5, pady=5)
b3 = ttk.Button(root, text="Η Πεταλούδα", bootstyle=INFO, command=butterfly)
b3.pack(side=BOTTOM, padx=5, pady=5)

root.mainloop()


#
# ΤΟ ΠΑΙΧΝΙΔΙ ΜΑΣ ΕΙΝΑΙ ΕΤΟΙΜΟ


#
# Τι μάθαμε?
# ----------
# Χρησιμοποιήσαμε το Tkinter καθώς και το ttkbootstrap, αποκτώντας όλο και περισσότερη
# εμπειρία.
#
# Ξεσκονίσαμε τις γνώσεις μας για την εισαγωγή κειμένου από τον χρήστη καθώς και για
# εκτύπωση.
#
# Σκεφτήκαμε πώς να δομήσουμε το πρόγραμμά μας καθώς και ποιες ιστορίες να δημιουργήσουμε.


#
#