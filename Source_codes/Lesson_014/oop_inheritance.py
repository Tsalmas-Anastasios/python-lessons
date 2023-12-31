# Κληρονομικότητα
#
# Επισκόπιση - Ορισμός
# --------------------
# Η κληρονομικότητα είναι ένας μηχανισμός στον αντικειμενοστραφή προγραμματισμό
# που επιτρέπει σε μια κλάση (η κλάση-κόρη ή υποκλάση) να κληρονομεί τα χαρακτη-
# ριστικά και τη συμπεριφορά από μια άλλη κλάση (την κλάση-μητέρα ή υπερκλάση).
# Η κλάση-κόρη μπορεί στη συνέχεια να επεκτείνει ή να τροποποιήσει τα κληρονομη-
# μένα χαρακτηριστικά και μεθόδους ανάλογα με τις ανάγκες της.
#
# Ας δούμε ένα απλό παράδειγμα.
# Ας υποθέσουμε ότι έχουμε μια κλάση που ονομάζεται "Animal" με χαρακτηριστικά
# όπως "name" και "age", καθώς και μεθόδους όπως "food()" και "sleep()". Τώρα,
# θέλουμε να δημιουργήσουμε μια πιο συγκεκριμένη κλάση, ας πούμε "Dog", η οποία
# μοιράζεται μερικά κοινά χαρακτηριστικά με το "Animal", αλλά έχει επίσης δικά
# της μοναδικά χαρακτηριστικά και μεθόδους.
#
# Δημιουργία υποκλάσης
# --------------------
# Για να δημιουργήσουμε μια υποκλάση στην Python, καθορίζουμε την υπερκλάση στον
# ορισμό της υποκλάσης. Ας δούμε πώς λειτουργεί αυτό με το παρακάτω παράδειγμα.
#

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def eat(self):
        print('Animal is eating')
    
    def sleep(self):
        print('The animal is sleeping')

class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def bark(self):
        print('Ο σκύλος γαβγίζει')
        
        
# Έχουμε καθορίσει την κλάση "Animal" με τα χαρακτηριστικά "name" και "age", καθώς
# εκαι τις μεθόδους "food()" και "sleep()".
#
# Στην συνέχεια, δημιουργούμε την κλάση "Dog" ως υποκλάση της "Animal" δηλώνοντας την
# "Animal" μέσα στις παρενθέσεις μετά το όνομα της κλάσης.
#
# Η κλάση "Dog" έχει δικό της γνώρισμα με το όνομα "breed", το οποίο συμπεριλαμβάνουμε
# στον κατασκευαστή χρησιμοποιώντας 'init'. Χρησιμοποιούμε τη συνάρτηση 'super()' για
# να καλέσουμε τον κατασκευαστή της υπερκλάσης και να περάσουμε τις απαραίτητες παρα-
# μέτρους. Αυτό μας επιτρέπει να κληρονομήσουμε και να αρχικοποιήσουμε τα χαρακτηρι-
# στικά 'name' και 'age' από την κλάση 'Animal'.