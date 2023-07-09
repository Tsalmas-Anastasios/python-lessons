# example 2
#
#
# Συνεχίζουμε με το παρακάτω παράδειγμα για την κατανόηση των κλάσεων.
# Ας υποθέσουμε ότι έχουμε μια κλάση που ονομάζεται Staff. Αυτή η κλάση μπορεί
# χρησιμοποιηθεί ώστε να αποθηκεύει όλες τις σχετικές πληροφορίες σχετικά με το
# προσωπικό σε μια εταιρία. Μέσα στην κλάση, μπορούμε να δηλώσουμε δύο μεταβλητές
# για να αποθηκεύσουμε το όνομα και τη θέση του υπαλλήλου. Επιπλέον, μπορούμε
# επίσης να κωδικοποιήσουμε μια μέθοδο που ονομάζεται calculPay() για να υπολο-
# γίζουμε τον μισθό του προσωπικού.
#
# Ας δούμε πώς θα τοι κάνουμε αυτό.
#

class Staff:
    def __init__(self, pPosition, pName, pPay):
        self.position = pPosition
        self.name = pName
        self.pay = pPay
        print('Δημιουργία του αντικειμένου "Προσωπικό"')
        
    def __str__(self):
        return 'Θέση = %s, Name = %s, Pay = %d' % (self.position,
                                                   self.name, self.pay)
    
    def calculatePay(self):
        hours = int(input('\nΕισάγετε τις ώρες εργασίας σας %s: ' % (self.name)))
        hourlyRate = int(input('\nΕισάγετε το ωρομίσθιό σας %s: ' % (self.name)))
        self.pay = hours * hourlyRate
        
        return self.pay
    

# Στον παραοπάνω κώδικα, πρώτα ορίζουμε μια κλάση με το όνομα Staff γράφοντας class Staff:
#
# Στη συνέχεια, ορίζουμε μια ειδική μέθοδο με το όνομα __init__ για την κλάση. Αυτό
# ονομάζεται αρχικοποιητής της κλάσης. Πάντα την ονομάζουμε init με δύο κάτω παύλες
# μπροστά και πίσω.
#
# Η Python διαθέτει ένα μεγάλο αριθμό ειδικών μεθόδων. Όλες οι ειδικές μέθοδοι έχουν δύο
# κάτω παύλες μπροστά και πίσω από τα ονόματά τους.
#
# Ένας αρχικοποιητής καλείται κάθε φορά που δημιουργείται ένα αντικείμενο της κλάσης.
# Για να αρχικοποιήσει τις μεταβλητές (δηλαδή να τους δώσει αρχικές τιμές) στην
# κλάση.
#
# Στην κλάση μας έχουμε τρεις μεταβλητές: position, name και pay
# Οι μεταβλητές αυτές ονομάζονται μεταβλητές στιγμιοτύπων, αντίθετα από τις τοπικές
# μεταβλητές και τις μεταβλητές κλάσης. Οι μεταβλητές στιγμιοτύπων είναι μεταβλητεές που
# προγούνται από μια λέξη - κλειδί self.
#
# Θα διερευνήσουμε την έννοια του self λίγο αργότερα. Για τώρα, απλά ας γνωρίζουμε ότι
# όταν θέλουμε να αναφερθούμε σε μεταβλητές σιτγμιοτύπου στην κλάση, πρέπει να προσθέσουμε
# το self μπροστά από τα ονόματα μεταβλητών. Επιπλέον, οι περισσότερες μέθοδοι σε μια
# κλάση έχουν το self ως πρώτη παράμετρο.
#
# Οι τρεις παρακάτω δηλώσεις αναθέτουν τις τρεις παραμέτρους της μεθόδου __init__
# (pPosition, pName & pPay) στις μεταβλητές στιγμιοτύπου για να τις αρχικοποιήσουν.
#
#   self.position = pPosition
#   self.name = pName
#   self.pay = pPay
#
# Μετά την αρχικοποίηση των τριών μεταβλητών στιγμιοτύπου, εκτυπώνουμε ένα απλό μήνυμα
#           'Δημιουργία του αντικειμένου "Προσωπικό"'.
# Αυτό είναι όλο όσο αναφορά τον αρχικοποιητή
#
# Το να γράψουμε έναν αρχικοποιητή είναι προαιρετικό αν δεν επιθυμούμε να αρχικοποιήσουμε
# τις μεταβλητές στιγμιοτύπου κατά τη δημιουργία του αντικειμένου. Μπορούμε πάντα να τις
# αρχικοποιήσουμε αργότερα.
#
# Ας προχωρήσουμε στην επόμενη μέθοδο '__str__'
# Η __str__ είναι μια άλλη ειδική μέθοδος που συνήθως περιλαμβάνεται όταν κατασκευάζουμε μια
# κλάση. Τη χρησιμοποιούμε για να επιστρέψουμε μια αναγνώριση από άνθρωπο συμβολοσειρά που
# αναπαριστά την κλάση.
#
# Στο παράδειγμά μας, απλά επιστρέφουμε μια συμβολοσειρά που παρέχει τις τιμές των τριών
# μεταβλητών. Θα δούμε πώς χρησιμοποιούμε αυτήν την μέθοδο αργότερα.
#
# Ας προχωρήσουμε τώρα στη μέθοδο calculatePay(). Η calculatePay() είναι μια μέθοδος που
# χρησιμοποιείται για τον υπολογισμό του μισθού ενός μέλους του προσωπικού. Θα παρατηρήσουμε
# ότι είναι πολύ παρόμοια με μια συνάρτηση, εκτός από την παράμετρο self.
#
# Μια μέθοδος είναι σχεδόν ταυτόσημη με μια σνάρτηση εκτός από το γεγονός ότι μια μέθοδος
# βρίσκεται μέσα σε μια κλάση και οι περισσότερες μέθοδοι έχουν τη self ως παράμετρο.
#
# Μέσα στη μέθοδο calculatePay(), πρώτα ζητάμε από τον χρήστη να εισάγει τον αριθμό των εργατοωρών
# που εργάστηκε. Στη συνέχεια, ζητάμε το ωρομίσθιό του και υπολογίζουμε τον μισθό βάσει αυτών των
# δύο τιμών.
# Στη συνέχεια, αναθέτουμε το αποτέλεσμα στη μεταβλητή στιγμιοτύπου self.pay και επιστρέφουμε
# την τιμή του self.pay.
#
# Παρατηρούμε ότι σε αυτήν την μέθοδο, δεν προσθέτουμε το self μπροστά από κάποιες μεταβλητές
# (όπως prompt, hours και hourlyRate). Αυτό συμβαίνει επειδή αυτές οι μεταβλητές είναι
# τοπικές και υπάρχουν μόνο μέσα στη μέθοδο calculatePay().
# Δεν χρειάζεται να προσθέτουμε το self μπροστά από τις τοπικές μεταβλητές.
#
# Η κλάση μας λοιπόν έχει τα ακόλουθα στοιχεία:
#
# Μεταβλητές στιγμιοτύπου:
#   position
#   name
#   pay
#
# Μέθοδοι
#   __init__
#   __str__
#   calculatePay()