print('Μάθημα 9ο')
print('Άνοιγμα, ανάγνωση και εγγραφή δυαδικών αρχείων')

# τα δυαδικά αρχεία αναφέρονται σε οποιοδήποτε αρχείο που
# δεν περιέχει κείμενο, όπως εικόνα ή βίντεο. Για να δουλέψουμε
# με δυαδικά αρχεία, χρησιμοποιούμε απλώς τη λειτουργεία - mode
# 'rb' ή 'wb'.

inputFile = open('myimage.txt', 'r')         # open the file
outputFile = open('myoutputimage.txt', 'w')      # open or create a file to write

# .
# .
# .