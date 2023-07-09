# Υπερφόρτωση (override) μεθόδων
#
#
# Σε ορισμένες περιπτώσεις, η υποκλάση μπορεί να χρειαστεί να τροποποιήσει
# τη συμπεριφορά μιας μεθόδου που κληρονομήθηκε από τη γονική κλάση. Αυτό
# ονομάζεται "υπερφόρτωση" μεθόδου, "method override".
#
# Ας δούμε τι συμβαίνει με την τροποποιημένη μέθοδο "sleep()" στην κλάση
# 'Dog' παρακάτω:

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
        
    def sleep(self):
        print('Ο σκύλος κοιμάται με ανοιχτά τα μάτια')
    

# Σε αυτήν την ενημερωμένη έκδοση της κλάσης 'Dog', έχουμε ξανα-ορίσει τη μέθοδο
# 'sleep()'. Με αυτόν τον τρόπο, έχουμε κάνει override της μεθόδου 'sleep()' που
# κληρονομήθηκε από την κλάση 'Animal'. Τώρα όταν η μέθοδος 'sleep()' καλείται
# σε ένα αντικείμενο 'Dog', θα εκτελεί τον τροποποιημένο κώδικα που είναι συγκε-
# κριμένος για την κλάση 'Dog'.