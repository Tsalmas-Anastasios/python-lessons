# Ας μιλήσουμε για τα χαρακτηριστικά. Τα χαρακτηριστικά είναι τα
# γνωρίσματα ή οι πληροφορίες που σχετίζονται με ένα αντικείμενο. Στην
# Python, ορίζουμε χαρακτηριστικά μέσα σε μια κλάση χρησιμοποιώντας τη
# μέθοδο '__init__', γνωστή και ως constructor. Καλείται αυτόματα όταν
# δημιουργείται ένα αντικείμενο από την κλάση.
#
#
# Παράδειγμα
# ----------
# Θα δημιουργήσουμε μια κλάση με το όνομα 'Person' με χαρακτηριστικά όπως το
# 'name' και το 'age'.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
person1 = Person('Maria', 25)

# Ορίσαμε την κλάση 'Person' με τη μέθοδο '__init__' που παίρνει τα 'name' και 'age'
# ως παραμέτρους. Χρησιμοποιούμε τη λέξη-κλειδί 'self' για να αναφερθούμε στο αντικεί-
# μενο που δημιουργείται. Μέσα στη μέθοδο, αντιστοιχίζουμε τις τιμές που περνάνε στα 
# χαρακτηριστικά του αντικειμένου χρησιμοποιώντας τη σύνταξη 'self.attribute_name'
#
# Κατόπιν δημιουργούμε ένα αντικείμενο 'person1' της κλάσης 'Person', περνώντας το όνομα
# 'Maria' και την ηλικία 25 ως ορίσματα. Αυτό θα αρχικοποιήσει το αντικείμενο με τις
# καθορισμένες τιμές των χαρακτηριστικών.