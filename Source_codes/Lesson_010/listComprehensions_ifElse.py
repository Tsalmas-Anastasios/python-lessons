# η list comprehension μας προσφέρει μια συντομότερη σύνταξη όταν
# θέλουμε να δημιουργήσουμε μια νέα λίστα με βάσει τις τιμές μιας
# υπάρχουσας λίστας

# χωρίς list comprehension γράφουμε
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
newlist = []

for x in fruits:        # για κάθε λέξη-όρισμα του array
    if 'a' in x:        # αν το 'a' υπάρχει μέσα στο όρισμα που περιέχει το x
        newlist.append(x)   # βάλε το όρισμα x μέσα στην νέα λίστα

print(newlist)      # τύπωσε την νέα λίστα

# με list comprehension
fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

newlist = [x for x in fruits if 'a' in x]
    # [x for x in fruits if 'a' in x]
    # βάλε το x όπου το x είναι ένα όρισμα (γραμμικά) της λίστας fruits
    # υπό την συνθήκη ότι μέσα στην τιμή της x υπάρχει το γράμμα 'a'
    #
    #
    # γενική σύνταξη
    # list_name = [item_will_be_putted for variable in old_list if condition]
    # νέα_λίστα = [ενέργεια_σε_στοιχείο for στοιχείο in λίστα if συνθήκη == TRUE]

print(newlist)