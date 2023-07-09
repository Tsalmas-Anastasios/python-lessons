# exercise 1
# 
# Δημιουργήστε μια γονική κλάση "Shape" με μια μέθοδο "area" που επιστρέφει το εμβαδόν
# ενος σχήματος. Στη συνέχεια, δημιουργήστε δύο παιδικές (child) κλάσεις "Rectangle"
# και "Circle" που κληρονομούν την κλάση "Shape" και υλοποοιούν τη μέθοδο "area" με τον
# κατάλληλο τρόπο για κάθε σχήμα.

class Shape:
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * (self.radius ** 2)


# Αυτό που λείπει τώρα από τον κώδικα είναι η δημιουργία αντικειμένων - στιγμιοτύπων των
# κλάσεων μας και ο υπολογισμός των εμβαδών
#

# Δημιουργία παραλληλογράμμου και υπολογισμός εμβαδού
rectangle = Rectangle(5, 10)
rectangle_area = rectangle.area()
print("Το εμβαδόν του παραλληλογράμμου είναι: ", rectangle_area)

# Δημιουργία κύκλου και υπολογισμός εμβαδού
circle = Circle(3)
circle_area = circle.area()
print("Το εμβαδόν του κύκλου είναι: ", circle_area)


# Η έξοδος θα είναι
#   Το εμβαδόν του παραλληλογράμου είναι: 50
#   Το εμβαδόν του κύκλου είναι: 28.2599999999999999999999998
