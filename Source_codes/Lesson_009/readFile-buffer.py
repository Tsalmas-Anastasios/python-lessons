# μερικές φορές για να μην δεσμεύουμε χώρο στην μνήμη,
# μπορεί να θέλουμε να διαβάσουμε ένα αρχείο με το μέγεθος ενός buffer.
# Για να επιτευχθεί αυτό, χρησιμοποιούμε την συνάρτηση read(), κι όχι
# τη readline(), με την οποία μπορούμε να καθορίσουμε το μέγεθος του
# buffer.

inputfile = open('myfile.txt', 'r')             # open file: myfile.txt
outputfile = open('newOutputFile.txt', 'w')
# open file newOutputFile.txt - if not exists then create it

msg = inputfile.read(10)
    # .read(byte_number)    --> Διαβάζει το αρχείο σύμφωνα με τον αριθμό των
    #                           bytes που δηλώνουμε το byte_number. Αφού διαβάσει τα
    #                           πρώτα byte_number bytes, συνεχίζει στα επόμενα

while len(msg):
    # Συνθήκη 'while len(msg)'
    #   ελέγχει το μήκος της μεταβλητής msg. Στην ουσία είναι true όσο το μήκος της
    #   συγκεκριμένης μεταβλητής δεν είναι 0 (αφού 0=FALSE)
    #   Μόλις το μήκος της μεταβλητής msg - len(msg) γίνει 0, σημαίνει ότι η ανάγνωση του
    #   του αρχείου έχει ολοκληρωθεί. Άρα, μόλις ολοκληρωθεί η ανάγνωση του αρχείου, έχει
    #   γίνει 0 ή False η τιμή της μεταβλητής msg

    outputfile.write(msg)
        # δήλωση outputfile.write(msg)
        # Αυτό σημαίνει ότι γράφει στο αρχείο που έχει γίνει open ή create
        # το περιεχόμενο της μεταβλητής msg

    msg = inputfile.read(10)
        # διαβάζονται ξανά τα περιεχόμενα του αρχείου σε αριθμός bytes βάσει του αριθμού
        # που έχουμε δώσει στις παρενθέσεις.
    
    # συνεχίζεται ο βρόχος while μέχρις ότου η συνθήκη len(msg) να έχει πάρει τιμή
    # 0, που προγραμματιστικά σημαίνει FALSE

inputfile.close()          # close opened file: inputfile = open('myfile.txt', 'r')
outputfile.close()         # close opened file: outputfile = open('newOutputFile.txt', 'w')