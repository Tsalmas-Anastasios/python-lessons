# εφαρμόζουμε τη φόρτωση εικόνας
from pygame.image import load


def load_sprite(name, with_alpha=True):
    path = f"assets/sprites/{name}.png"
    loaded_sprite = load(path)

    if with_alpha:
        return loaded_sprite.convert_alpha()
    else:
        return loaded_sprite.convert()


#
# Σχολιασμός του παραπάνω κώδικα
# ------------------------------
#
# Η γραμμή 1 εισάγει μια μέθοδο που ονομάζεται load() η οποία θα είναι απαραίτητη για την
# ανάγνωση εικόνων αργότερα.
#
# Η γραμμή 4 δημιουργεί μια διαδρομή προς μια εικόνα, υποθέτοντας ότι είναι αποθηκευμένη
# στο φάκελο assets/sprites και ότι είναι αρχείο PNG. Με αυτόν τον τρόπο, θα χρειαστεί να δώσουμε
# μόνο το όνομα του sprite αργότερα.
#
# Η γραμμή 5 φορτώνει την εικόνα χρησιμοποιώντας τη load(). Αυτή η μέθοδος επιστρέφει μια επιφάνεια,
# η οποία είναι ένα ανικείμενο που χρησιμοποιείται από την Pygame για την αναπαράσταση εικόνων.
# Μπορούμε αργότερα να την εισάγουμε στην οθόνη (ή σε άλλη επιφάνεια, αν θέλουμε).
#
# Οι γραμμές 8 & 10 μετατρέπουν την εικόνα σε μορφή ου ταιριάζει καλύτερα στην οθόνη για να επιταχύνει
# τη διαδικασία σχεδίασης. Αυτό γίνεται με τις μεθόδους convert_alpha() και convert(), ανάλογα με το
# αν θέλουμε να χρησιμοποιήσουμε τη διαφάνεια.
#
# Σημείωση
# Γενικά, θα μπορούσαμε απλώς να χρησιμοποιήσουμε την convert_alpha() για όλους τους τύπους εικόνων,
# καθώς αυτή η μέθοδος, μπορεί να χειριστεί επίσης μια εικόνα χωρίς διαφανή pixel. Ωστόσο, η σχεδίαση
# διαφανών εικόνων είναι λίγο πιο αργή από τη σχεδίαση αδιαφανών εικόνων.
