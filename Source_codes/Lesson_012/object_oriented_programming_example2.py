# example 2
#
#
# Γράψτε μια κλάση που έχει δύο μεθόδους: get_String και print_String.
# H get_String δέχεται μια συμβολοσειρά από τον χρήστη και η 
# print_String εκτυπώνει τη συμβολοσειρά με κεφαλαία


class IOString():
    def __init__(self):
        self.str1 = ""
        
    def get_String(self):
        self.str1 = input()
        
    def print_String(self):
        print(self.str1.upper())
        
        

str1 = IOString()
str1.get_String()
str1.print_String()


# Παράδειγμα εξόδου
#   fsdfasdf
#   FSDFASDF