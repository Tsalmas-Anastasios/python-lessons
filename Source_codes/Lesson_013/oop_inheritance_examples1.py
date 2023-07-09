# example 1
#
#
# Γνωρίζουμε ήδη ότι μέσω της κληρονομικότητας μια κλάση μπορεί να κληρονομήσει τα
# χαρακτηριστικά (μεταβλητές, μεθόδους) μιας άλλης (γονικής) κλάσης. Με την κληρονο-
# μικότητα λοιπόν, επαναχρησιμοποιούμε κώδικα, με μικρές αλλαγές, συνήθως μικρές προσθήκες.
# Η αρχική κλάση λοιπόν, ονομάζεται γονική (parent class) και η κλάση η οποία κληρονομεί
# απ' αυτήν, υποκλάση (subclass) ή κλάση-παιδί (child class).
# Στον ορισμό μιας υποκλάσης το όνομα της γονικής κλάσης μπαίνει μέσα σε παρενθέσεις σαν
# όρισμα της κλάσης-παιδί
#
#
# Στο παρακάτω παράδειγμα έχουμε ένα πανεπιστήμιο με φοιτητές και καθηγητές. Οι φοιτητές και
# οι καθηγητές έχουν κάποια κοινά χαρακτηριστικά, π.χ όνομα, ηλικία αλλά και κάποια μοναδικά
# χαρακτηριστικά που αφορούν την ιδιότητά τους, όπως είναι ο αριθμός μητρώου για τους φοιτητές
# και ο μισθός για τους καθηγητές. Θα μπορούσαμε να δημιουργήσουμε μια κοινή γονική κλάση
# (University Member), και οι κλάσεις Καθηγητής (Professor) και φοιτητής (Student) να
# κληρονομήσουν από αυτήν:

class UniversityMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Μέλος του Πανεπιστημίου: ', self.name)
    
    def show(self):
        print('Name: "{0}", Age: "{1}"'.format(self.name, self.age))


class Professor(UniversityMember):
    def __init__(self, name, age, salary):
        UniversityMember.__init__(self, name, age)
        self.salary = salary
        print('Καθηγητής/τρια:', self.name)
    
    def show(self):
        UniversityMember.show(self)
        print('Μισθός: ', self.salary)


class Student(UniversityMember):
    def __init__(self, name, age, ar):
        UniversityMember.__init__(self, name, age)
        self.ar = ar
        print('Φοιτητής/τρια: ', self.name)
    
    def show(self):
        UniversityMember.show(self)
        print('ΑΜ: ', self.ar)



p = Professor('Κωνσταντίνου Γεωργίου', 48, 1700)
p.show()
s = Student('Tsalmas Anastasios', 19, 342)
s.show()
        