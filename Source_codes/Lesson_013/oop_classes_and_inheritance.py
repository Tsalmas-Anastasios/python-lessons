# Για να προχωράμε την κατανόησή μας σε σχέση με τις κλάσεις, μπορούμε να πούμε πως
# κλάση είναι ένα πρότυπο το οποίο περιλαμβάνει μεταβλητές και μεθόδους που σχετίζονται
# μεταξύ τους
#
# 
#
#
# Ας δούμε ένα παράδειγμα του πραγματικού κόσμου, στο οποίο μπορούμε να χρησιμοποιήσουμε
# μια και μόνο κλάση. Θα δημιουργήσουμε ένα πρόγραμμα το οποίο να εξυπηρετεί ένα εστιατόριο.
# Θα έχει μια κλάση MyRestaurant με μεταβλητές (χαρακτηριστικά) όπως menu_items, book_table,
# και customer_orders και μεθόδους όπως add_item_to_menu, book_tables και customer_order.
# Αφού δημιουργήσαυμε την κλάση κι ένα στιγμιότυπό της, θα πραγματοποιήσουμε τα παρακάτω:
#   - Προσθήκη στοιχείων στο μενού
#   - Κράτηση τραπεζιού
#   - Παραγγελιοληψία
#   - Εκτύπωση του μενού
#   - Εκτύπωση των κρατήσεων των τραπεζιών
#   - Εκτύπωση των παραγγελιών
#
# Θα χρησιμοποιήσουμε λεξικά και λίστες για να αποθηκεύσουμε τα δεδομένα:
# """
#
#   Θα δημιουργήσουμε ένα πρόγραμμα το οποίο να εξυπηρετεί ένα εστιατόριο.
#   Θα έχει μια κλάση MyRestaurant με μεταβλητές (χαρακτηριστικά) όπως menu_items, book_table
#       και customer_orders και μεθόδους όπως add_item_to_menu, book_tables και customer_order.
#   Αφού δημιουργήσουμε την κλάση κι ένα στιγμιότυπό της, θα πραγματοποιήσουμε τα παρακάτω:
#       Προσθήκη στοιχείων στο μενού
#       Κράτηση τραπεζιού
#       Παραγγελιοληψία
#       Εκτύπωση των κρατήσεων των τραπεζιών
#       Εκτύπωση των παραγγελιών
#
#   Θα χρησιμοποιήσουμε λεξικά και λίστες για να αποθηκεύσουμε τα δεδομένα:
#
# """

class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.book_table = []
        self.customer_orders = []
        
    def add_item_to_menu(self, item, price):
        self.menu_items[item] = price
        
    def book_tables(self, table_number):
        self.book_table.append(table_number)
        
    def customer_order(self, table_number, order):
        self.customer_orders.append({ 'table_number': table_number, 'order': order })
    
    def print_menu_items(self):
        for item, price in self.menu_items.items():
            print("{}: {}".format(item, price))
    
    def print_table_reservations(self):
        for table in self.book_table:
            print('Τραπέζι {}'.format(table))
            
    def print_customer_orders(self):
        for order in self.customer_orders:
            print('Τραπέζι {}: {}'.format(order['table_number'], order['order']))
            


restaurant = Restaurant()


# Προσθήκη στοιχείων στο μενού
restaurant.add_item_to_menu("Αστακομακαρονάδα: ", 9.99)
restaurant.add_item_to_menu("Σαλάτα Casear's: ", 8)
restaurant.add_item_to_menu("Φιλέτο σολωμού: ", 19.99)
restaurant.add_item_to_menu("Τηγανητές πατάτες: ", 3.99)
restaurant.add_item_to_menu("Τσιπούρα: ", 15)

# Κράτηση τραπεζιού
restaurant.book_tables(1)
restaurant.book_tables(2)
restaurant.book_tables(3)

# Orders
restaurant.customer_order(1, "Αστακομακαρονάδα")
restaurant.customer_order(1, "Φιλέτο σολωμού")
restaurant.customer_order(1, "Τσιπούρα")
restaurant.customer_order(1, "Σαλάτα Ceasar' s")

print('\nΔιάσημα πιάτα με τις τιμές τους: ')
restaurant.print_menu_items()
print('\nΚρατημένα τραπέζια στο εστιατόριο: ')
restaurant.print_table_reservations()
print('\nΕκτύπωση παραγγελιών: ')
restaurant.print_customer_orders()



# Έξοδος
#   Διάσημα πιάτα με τις τιμές τους:
#   Αστακομακαρονάδα: 9.99
#   Σαλάτα Ceasar's: 8
#   Φιλέτο σολωμού: 19.99
#   Τηγανητές πατάτες: 3.99
#   Τσιπούρα: 15
#
#   Κρατημένα τραπέζια στο εστιατόριό μας:
#   Τραπέζι 1
#   Τραπέζι 2
#   Τραπέζι 3
#
#   Εκτύπωση παραγγελιών
#   Τραπέζι 1: Αστακομακαρονάδα
#   Τραπέζι 1: Φιλέτο σολωμού
#   Τραπέζι 2: Τσιπούρα
#   Τραπέζι 2: Σαλάτα Ceasar's