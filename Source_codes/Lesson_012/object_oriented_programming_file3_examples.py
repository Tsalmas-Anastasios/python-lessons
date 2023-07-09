# Παραδείγματα και εφαρμογές
#
#
# 1. Παράδειγμα 1: Κλάση Car
#       Ας δημιουργήσουμε μια κλάση με όνομα "Car" που θα αναπαριστά ένα
#       αυτοκίνητο. Ορίζουμε τα χαρακτηριστικά όπως το μοντέλο (model), τo
#       χρώμα (color) και την ταχύτητα (speed), καθώς και μεθόδους όπως την
#       επιτάχυνση (accelerate) και το φρενάρισμα (brake).
#
#
#
#
# Ορισμός της κλάσης Car
class Car:
    def __init__(self, model, color):
        # Χαρακτηριστικά της κλάσης car
        self.model = model
        self.color = color
        self.speed = 0
        
    def accelerate(self, increment):
        # Μέθοδος για επιτάχυνση του αυτοκινήτου
        self.speed += increment
        
    def brake(self, decrement):
        # Μέθοδος για φρενάρισμα του αυτοκινήτου
        if self.speed >= decrement:
            self.speed -= decrement
        else:
            self.speed = 0



#
#
# 2. Παράδειγμα 2: Κλάση φοιτητής
#           Ας δημιουργήσουμε μια κλάση με όνομα "Student" που θα αναπαριστά
#           ένα φοιτητή. Ορίζουμε τα χαρακτηριστικά όπως το όνομα, το επώνυμο
#           και τον βαθμό, καθώς και μεθόδους όπως ο υπολογισμός του μέσου όρου
#           και η εκτύπωση των στοιχείων του φοιτητή
#
#
#
#
# Ορισμός της κλάσης Student
class Student:
    def __init__(self, name, surname):
        # Χαρακτηριστικά της κλάσης Student
        self.name = name
        self.surname = surname
        self.grade = 0
        
    def calculate_average(self, grades):
        # Μέθοδος για υπολογισμό μέσου όρου βαθμολογίας
        total = sum(grades)
        self.grade = total / len(grades)
        
    def print_info(self):
        # Μέθοδος για εκτύπωση πληροφοριών φοιτητή
        print("Name: ", self.name)
        print("Surname: ", self.surname)
        print("Grade: ", self.grade)
        