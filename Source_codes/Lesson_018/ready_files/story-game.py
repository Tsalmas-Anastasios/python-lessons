import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# themes = cosmo, flatly, journal, litera, lumen, minty, pulse, sandstone,
# united, yeti, morph, simplex, cerculean
root = ttk.Window(themename="simplex") # root είναι το όνομα του παραθύρου μας
root.geometry('380x250') # Διαστάσεις παραθύρου
root.title('- Δημιουργός Ιστορίας -') # Ο τίτλος του παιχνιδιού μας
label1 = ttk.Label(root, text= 'Φτιάξε την ιστορία σου \n με τη βοήθεια της Python!', font = ('Helvetica', 20), bootstyle = PRIMARY).pack() # Κείμενο μέσα στο παράθυρο
label2 = ttk.Label(root, text = 'Κάνε κλικ παρακάτω :', font=('Helvetica', 15), bootstyle = PRIMARY).place(x=40, y=80) # Κείμενο μέσα στο παράθυρο

################- Ιστορίες -##############

def photographer():

    animals= input('Εισάγετε όνομα ζώου : ')
    profession = input('Εισάγετε ένα επάγγελμα (στην αιτιατική): ')
    cloth = input('Εισάγετε όνομα υφάσματος: ')
    things = input('Εισάγετε όνομα αντικειμένων: ')
    name= input('Εισάγετε όνομα με άρθρο: ')
    place = input('Εισάγετε τόπο: ')
    verb = input('Εισάγετε ρήμα σε ενεστώτα, γ πληθυντικό: ')
    food = input('Εισάγετε όνομα τροφής: ')
    print('Πες ' + food + ', είπε ο φωτογράφος καθώς το flash άναψε! ' + name + ' κι εγώ  πήγαμε στο/στη ' + place +' σήμερα, για να πάρουμε τις φωτογραφίες μας. Η πρώτη φωτογραφία την οποία θέλαμε να δούμε, ήταν αυτή που είμαστε ντυμένοι ' + animals + ' παριστάνοντας έναν/μια ' + profession + ' .Όταν είδαμε τη δεύτερη φωτογραφία, ήταν ακριβώς αυτό που θέλαμε. Μοιάζαμε και οι δύο με ' + things + ' που φοράνε ' + cloth + ' και ' + verb + ' --ακριβώς ότι είχα στο μυαλό μου')



def butterfly():
   
    adjective = input('Εισάγετε ένα επίθετο (θηλυκό) : ')
    color = input('Εισάγετε ένα χρώμα : ')
    thing = input('Εισάγετε ένα αντικείμενο :')
    place = input('Εισάγετε μια πόλη : ')
    person= input('Εισάγετε ένα όνομα (αιτιατική): ')
    adjective1 = input('Εισάγετε ένα επίθετο : ')
    insect= input('Εισάγετε ένα έντομο : ')
    food = input('Εισάγετε μια τροφή : ')
    verb = input('Εισάγετε ένα ρήμα (α πληθυντικό): ')

    print('Χθες το βράδυ ονειρεύτηκα ότι ήμουν μια ' +adjective+ ' πεταλούδα με ' + color+ ' φτερά που έμοιαζαν με '+thing+ '. Πετούσα για τον/την' + place+ ' με τον καλύτερό μου φίλο και τον/την '+person+ ' που ήταν ένας/μια '+adjective1+ ' ' +insect +' . Φάγαμε λίγο/η ' +food+ ' μόλις φτάσαμε και αποφασίσαμε να '+verb+ ' και το όνειρο τέλειωσε όταν είπα "Ας ' +verb+ '"')
    


def appleandapple():
    person = input('Εισάγετε ένα όνομα (σε γενική πτώση): ')
    color = input('Εισάγετε ένα χρώμα (πληθυντικός) : ')
    foods = input('Εισάγετε μια τροφή (γενική) : ')
    adjective = input('Εισάγετε ένα επίθετο (ουδέτερο ενικός): ')
    thing = input('Εισάγετε ένα αντικείμενο : ')
    place = input('Εισάγετε μια πόλη : ')
    verb = input('Εισάγετε ένα ρήμα (ενεστώτας, α πληθυντικό): ')
    adverb = input('Εισάγετε ένα επίρρημα : ')
    food = input('Εισάγετε μια τροφή: ')
    things = input('Εισάγετε ένα αντικείμενο : ')

   
    print('Σήμερα πήραμε μήλα από το περιβόλι του/της '+person+ '. Δεν είχα ιδέα πως υπάρχουν πολλές ποικιλίες μήλων. Έφαγα ' +color+ ' μήλα κατευθείαν από το δέντρο και είχαν γεύση '+foods+ '. Μετά είδαμε ένα '+adjective+ ' μήλο που έμοιαζε με ' + thing + '. Όταν η τσάντα μας γέμισε, πήγαμε μια βόλτα στον/στην '+place+ ' και ξαναγυρίσαμε πίσω. Τελειώσαμε τη βόλτα μας αφού πέσαμε (ευτυχώς) σε μια στοίβα άχυρα και μετά έπρεπε να ' +verb+ ' ' +adverb+ '. Δεν κρατιέμαι να φτάσω σπίτι και να μαγειρέψω με τα μήλα. Θα κάνουμε μηλο- '+food+ ' και '+things+' -πιτες!.')  



# Για πιο όμορφα κουμπιά, χρησιμοποιούμε το ttkbootstrap
# ttkbootstrap styles - PRIMARY, SECONDARY, SUCCESS, INFO, WARNING, DANGER, LIGHT, DARK
b1 = ttk.Button(root, text= 'Ο Φωτογράφος', bootstyle = PRIMARY, command = photographer)
b1.pack(side = BOTTOM, padx=5, pady=5)
b2 = ttk.Button(root, text= 'Μήλο και Μήλο', bootstyle = SUCCESS, command = appleandapple)
b2.pack(side = BOTTOM, padx=5, pady=5)
b3 = ttk.Button(root, text= 'Η Πεταλούδα', bootstyle = INFO, command = butterfly)
b3.pack(side = BOTTOM, padx=5, pady=5)

root.mainloop()
