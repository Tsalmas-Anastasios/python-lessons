print("Lesson 9")
print("Lesson object: file management (.txt files & more) - write")

# open the .txt file
f = open('myfile.txt', 'w')         # --> open the requested file
        # open() function:
            # two arguments: 1. the file path
            #                2. the open mode ('w'->write, 'r'->read)
            #
            #
            # Αν το αρχείο που επιθυμούμε να ανοίξουμε υπάρχει ήδη, τότε τα δεδομένα του
            # αρχείου αυτού διαγράφονται-σβήνονται και στην συνέχεια δημιουργούνται οι
            # νέες εγγραφές. (τα παλιά δεδομένα, αντικαθίστατε από τα νέα)
            #
            # Αν το αρχείο δεν υπάρχει, τότε απλά δημιουργείται και είναι ετοίμο για να
            # γράψουμε δεδομένα σε αυτό.
            #
            # Το path που χρησιμοποιύμε στην συνάτρτηση προκειμένου να ανοίξουμε το αρχείο,
            # πρέπει να προϋπάρχει, διαφορετικά θα εμφανιστεί μήνυμα λάθους. Δεν αναφερόμα-
            # στε στην τελική κατάληξη, που είναι το αρχείο, αλλά στο υπόλοιπο μονοπάτι.



line1 = 'Σ\' αυτό το μάθημά μας θα διαχειριστούμε αρχεία κειμένου\n'
f.write(line1)          # write new line in the end of the opened file

line2 = '(text files), τα οποία δεν είναι τίποτε άλλο παρά\n'
f.write(line2)          # write new line (line2) in the end of the opened file

line3 = 'μια σειρά από χαρακτήρες (συμβολοσειρές) που είναι\n'
f.write(line3)          # write new line (line3) in the end of the opened file

line4 = 'αποθηκευμένοι σε ένα μόνιμο μέσο αποθήκευσης.\n'
f.write(line4)          # write new line (line4) in the end of the opened file

# Συνάρτηση write
# Με τη μέθοδο αυτή μπορούμε να γράψουμε δεδομένα σε ένα αρχείο ή σε ένα αντικείμενο
# αρχείου που δημιουργέιται από την συνάρτηση open
# Το/Τα ορίσματά της, θα πρέπει να ειναι συμβολοσειρές. Έτσι, αν θέλουμε να γράψουμε
# ένα δεδομένο που να έχει διαφορετικό τύπο από string, θα πρέπει πρώτα να το μετατρέ-
# ψουμε σε string (χρησιμοποιώντας τις τεχνικές casting) και στην συνέχεια να εγγράψουμε
# αυτή την τιμή στο αρχείο.

f.close()               # --> close the file that we opened it before
# Η συνάρτηση close() χρησιμοποιείται για να κλείσουμε ένα αρχείο. Αυτό δηλώνει ότι,
# η επεξεργασία του έχει ολοκληρωθεί και δεν θα χρειαστούμε άλλο να το επεξεργασοτούμε,
# είτε να το αναγνώσουμε είτε να εγγράψουμε κάτι σε αυτό.