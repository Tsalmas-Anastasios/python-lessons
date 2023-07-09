# Μόλις δημιουργήσουμε ένα αντίκειμενο, μπορούμε να έχουμε πρόσβαση
# στα γνωρίσματά του χρησιμοποιώντας την σημείωση με τελεία
#           'αντικείμενο.χαρακτηριστικό'
# Ας δοκιμάσουμε να έχουμε πρόσβαση στα χαρακτηριστικά του 'person1'.
#
#   print(person1.name)
#   print(person2.age)
#
# Εκτελώντας αυτόν τον κώδικα, μπορούμε να δούμε ότι μπορούμε να έχουμε
# πρόσβαση και να εκτυπώσουμε τις τιμές των γνωρισμάτων 'name' και 'age'
# για το 'person1'. Τα χαρακτηριστικά παρέχουν έναν τρόπο αποθήκευσης και
# ανάκτησης δεδομένων που σχετίζονται με ένα αντικείμενο.
#
# Εκτός από τα χαρακτηριστικά, τα αντικείμενα μπορούν επίσης να έχουν μεθόδους,
# που είναι συναρτήσεις που ορίζονται μέσα σε μια κλάση. Οι μέθοδοι μπορούν να
# εκτελούν λειτουργίες στα δεδομένα του αντικειμένου ή να πραγματοιποιούν
# συγκεκριμένες ενέργειες. Ας προσθέσουμε μια μέθοδο στην κλάση 'Person' μας.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f'Γεια σας, το όνομά μου είναι {self.name}.')



person1 = Person('Maria', 25)
person1.greet()

# Σε αυτήν την έκδοση της κλάσης 'Person', προσθέσαμε μια μέθοδο 'greet()' που
# εκτυπωνει ένα μήνυμα χαιρετισμού μαζί με το όνομα του προσώπου. Παρατηρήστε ότι
# η παράμετρος 'self' χρησιμοποιείται μέσα στη μέθοδο για να έχουμε πρόσβαση στα 
# χαρακτηριστικά του αντικειμένου. Μπορούμε να καλέσουμε τη μέθοδο 'greet()' στο
# αντικείμενο 'person1' και να εκτυπώσουμε το σχετικό μήνυμα χαιρετισμού.
#
# Συνοψίζοντας, τα χαρακτηριστικά αναπαριστούν τα δεδομένα που σχετίζονται με ένα
# αντικείμενο, ενώ οι μέθοδοι παρέχουν λειτουργίες και ενέργειες που μπορούν να
# εκτελέσουν τα αντικείμενα.
#
# Τώρα, όταν καλούμε τη μέθοδο 'greet' στο αντικείμενο 'person1', θα εκτυπωθεί το
# μήνυμα χαιρετισμού, συμπεριλαμβανομένου του ονόματος του ατόμου.