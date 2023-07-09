print('Lesson 10')
print('Παρακάτω υπάρχουν άλλες συνακτικές επιλογές της εντολής if')

x = 10
y = 11

# shorthand if...else
if x > y: print('x is greater that y')
    # εξήγηση
    #   Γράφουμε την εντολή if σε μία μονο γραμμή, όταν το μπλοκ
    #   εντολών περιέχει αποκλειστικά μία εντολή

# τριαδικός τελεστής
print('X') if x > y else print('=') if x == y else print('y')
    # εξήγηση
    #   Όταν ένα if...elif...else περιέχουν μπλοκ εντολών με μία μόνο γραμμή
    #   μπορούμε να χρησιμοποιήσουμε τον τριαδικό τελεστή προκειμένου να μην
    #   χρειαστεί να επεκτείνουμε τον κώδικά μας και να τον κάνουμε να φαίνεται
    #   κάπως έτσι:
    #       if x > y:
    #           print('X')
    #       elif x == y:
    #           print('=')
    #       else:
    #           print('Y')