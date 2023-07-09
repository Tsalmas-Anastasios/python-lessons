# exercise 3
#
#
# Δημιουργήστε μια γονική κλάση "Vehicle" με μια μέθοδο "drive" που εκτυπώνει
# ένα μήνυμα. Στη συνέχεια, δημιουργήστε δύο παιδικές κλάσεις "Car" και
# "Motorcycle" που κληρονομούν από την κλάση "Vehicle" και υλοποιούν τη μέθοδο
# "drive" με τον κατάλληλο τρόπο για κάθε όχημα

class Vehicle:
    def drive(self):
        pass
    

class Car(Vehicle):
    def drive(self):
        print("We drive the CAR now")

class Motorcycle(Vehicle):
    def drive(self):
        print("We drive the MOTORCYCLE now")


# Δημιουργία στιγμιοτύπων και κλήση μεθόδων
car = Car()
car.drive()

motorcycle = Motorcycle()
motorcycle.drive()