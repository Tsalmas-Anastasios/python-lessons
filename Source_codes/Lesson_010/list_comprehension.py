# όταν έχουμε μία λίστα, ξέρουμε ότι υπάρχει μεγάλη πιθανότητα
# να χρειαστεί να γρα΄ψουμε ένα βρόχο.
# Τις περισσότερες φορές αυτό είναι εντάξει, αλλά η Python μας δίνει την δυνατότητα,
# όταν πρόκειται για κάτι σχετικά απλό, να μπορούμε να χρησιμοποιήσουμε τη
# σύνταξη 'list comprehension', η οποία γράφεται πολύ πιο σύντομα, σε μια γραμμή.
#
# Πρόκειται για λίστες οι οποίες αναπαράγουν τον εαυτό τους με έναν εσωτερικό
# βρόχο. Είναι κοινό χαρακτηριστικό στην Python και συνήθως μοιάζουνε με:
#       x for x in list_of_x



# συνάρτηση η οποία θα πολλαπλασιάζει τα στοιχεία της λίστας που στέλνουμε ως
# παράμετρο και επιστρέφει την λίστα με τα στοιχεία της να είναι διπλασιασμένα
def list_doubler(lst):      # Συνάρτηση που διπλασιάζει τα στοιχεία μιας λίστας
    doubled = []        # Αρχικοποίηση μίας κενής λίστας
    for num in lst:     # Για κάθε αριθμό στη λίστα που έρχεται από τις παραμέτρους
        doubled.append(num * 2) # πρόσθεσε στη νέα λίστα τον διπλάσιό του
    return doubled      # επέστρεψε την λίστα

my_list = [21, 2, 93]
my_doubled_list = list_doubler(my_list)
#######################################
    # ο τρόπος που χρησιμοποιήθηκε εδώ, είναι ο βασικός τρόπος που θα χρηιμοποιούσαμε
    # αν δεν είχαμε τον τρόπο της σύνταξης του 'list comprehension'
    #
    # αυτό έχει ως αποτέλεσμα, η συνάρτηση να γράφεται σε πέντε (5) γραμμές μαζί
    # με τον ορισμό της συνάρτησης (def list_doubler(lst)), έχει μια μεταβλητή με
    # την οποία δεν κάνουμε τίποτα παρά μόνο να προσθέσουμε τα στοιχεία (num) και
    # τέλος επιστρέφει "γεμάτη" από τα νέα στοιχεία. Ο βρόχος 'for', δεν κάνει πολλά
    # απλά πολλαπλασιάζει έναν αριθμό με το 2.
    #
    # Βάσει της παραπάνω περιγραφής, η συγκεκριμένη σύνταξη δεν είναι η κατάλληλη,
    # ενώ εδώ ενδείκνυται η σύνταξη, list comprehension


# 'list comprehension' syntax
my_list = [21, 2, 93]
my_doubled_list = [num * 2 for num in my_list]
    # συντακτικό
    #   list_name = [item_will_be_putted for variable in old_list]

    # οι list comprehension χρησιμοποιούνται για να γλιτώσουμε χώρο στο αρχείο του
    # κώδικα. Επίσης, για να επεξεργαστούμε μια λίστα στα γρήγορα με μια επαναλαμβα-
    # νόμενη εργασία.
    # Τέλος, είναι χρήσιμες στον συναρτησιακό προγραμματισμό
    #
    # όμως σε περίπτωση που όλα όσα θέλουμε να κάνουμε είναι να γίνουν σε μια λίστα,
    # δεν θα μας χρησίμευαν και πολύ. Ευτυχώς μπορούν να χρησιμοποιηθούν με προϋποθέσεις