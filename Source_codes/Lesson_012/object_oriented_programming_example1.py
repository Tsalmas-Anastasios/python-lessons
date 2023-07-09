# Example 1
#
# Γράψτε ένα πρόγραμμα για να δημιουργήσετε δύο κενές κλάσεις, Student και Marks.
# Τώρα δημιουργήστε μερικά στιγμιότυπα και ελέγξτε αν είναι στιγμιότυπα των εν λόγω
# κλάσεων ή όχι. Επίσης, ελέγξτε εάν οι εν λόγω κλάσεις είναι υποκλάσεις της ενσωματωμένης
# (built-in) κλάσης object ή όχι (θα χρησιμοποιήσουμε τις συναρτήσεις isinstance()) και
# issubclass() για τους παραπάνω ελέγχους

class Student:
    pass

class Marks:
    pass

student1 = Student()
marks1 = Marks()

print(isinstance(student1, Student))                # TRUE
print(isinstance(marks1, Marks))                    # TRUE
print(isinstance(student1, Marks))                  # FALSE
print(isinstance(marks1, Student))                  # FALSE