# example 2
#
#
# Φτιάξτε μια κλάση Person και δύο υποκλάσεις: Male & Female.
# Όλες οι κλάσεις έχουν τη μέθοδο "getGender" η οποία μπορεί να τυπώσει "Άνδρας"
# για την κλάση Male και "Γυναίκα" για την κλάση Female.
# Κατόπιν, φτιάξτε 2 αντικείμενα των κλάσεων και ζητήστε τις εκτυπώσεις τους.

class Person():
    def getGender(self):
        return "Unknown"

class Male(Person):
    def getGender(self):
        return "Άνδρας"
    
class Female(Person):
    def getGender(self):
        return "Γυναίκα"
    

george = Male()
maria = Female()
print('Ο Γιώργος είναι ', george.getGender())
print('Η Μαρία είναι ', maria.getGender())