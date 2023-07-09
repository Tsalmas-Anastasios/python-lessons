# Παράδειγμα Νο. 1
#   Εφαρμογή συναρτήσεων σε όλα τα στοιχεία μιας λίστας:
numbers = [1, 2, 3, 4 , 5]
processed_numbers = list(map(lambda x: x * 2, numbers))
print(processed_numbers)
    # Print: [2, 4, 6, 8, 10]



# Παράδειγμα Νο. 2
#   Φιλτράρισμα στοιχείων μιας λίστας με βάση συγκεκριμένη συνθήκη
numbers = [i for i in range(1, 6)]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)



# Παράδειγμα Νο. 3
#   Ανώνυμη συνάρτηση ως όρισμα σε μια άλλη συνάρτηση
def process_numbers(numbers, func):
    processed_numbers = []
    for num in numbers:
        processed_numbers.append(func(num))
    
    return processed_numbers


numbers = [i for i in range(1, 6)]
result = processed_numbers(numbers, lambda x: x ** 2)
print(result)
    # Print: [1, 4, 9, 16, 25]



# Με τα παραδείγματα βλέπουμε πως οι συναρτήσεις lambda μπορούν να χρησιμοποιηθούν για να κάνουν
# τον κώδικα πιο συνοπτικό, εκφραστικό και ευανάγνωστο σε περιπτώσεις όπου η δημιουργία ονομασμένης
# συνάρτησης δεν είναι απαραίτητη