print("Lesson 2\n")

first_number = 7
second_number = 3


#if conditions
if first_number > second_number:
    print("The number " + str(first_number) + " is bigger than the number " + str(second_number))
elif first_number < second_number:
    print("The number " + str(second_number) + " is bigger than the number " + str(first_number))
else:
    print("The numbers are equal")
print("\n")


# H python αλλάζει χωρίς χαρακτήρα διαφυγής τις σειρές από μόνη της


x = 'Hello world!'
print(" - Η μεταβλητή x είναι string --> " + x)

y = 10
print(" - Η μεταβλητή y είναι int --> " + str(y))

z = 3.10
print(" - Η μεταβλητή z είναι float-double --> " + str(z))


#πολλαπλή ανάθεση
a, b, c, d = 1, 2, 3, 4

#example
a, b = 1, 2
c = a
d = c + 1
print(a, b, c, d)