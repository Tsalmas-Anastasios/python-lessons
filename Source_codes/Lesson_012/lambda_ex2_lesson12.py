# exercise 2
#
# Γράψτε ένα πρόγραμμα το οποίο υψώνει εις το τετράγωνο κάθε αριθμό μιας δεδομένης λίστας
# ακεραίων. Κατόπιν υψώνει εις τον κύβο τους ίδιους αριθμούς. Χρησιμοποιήστε lambda function
# καθώς και τη συνάρτηση map(), σαν όρι8σμα της list() (list(map(lambda...))).
# Τυπώστε μία-μία σε ξεχωριστές γραμμές την κάθε λίστα
#
# Η αρχική λίστα των ακεραίων είναι η: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


nums = [i for i in range(1, 11)]
print("Αρχικό array: ", nums)

print("\nNumbers square")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

print("\nNumbers cube")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)
