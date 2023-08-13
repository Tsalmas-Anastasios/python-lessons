import turtle as tl

# Η χελώνα είναι η μεταβλητή pen
pen = tl.Turtle()
pen.color("blue")
pen.speed(0)

# Ζωγραφική ενός μεγάλου τετραγώνου με 4 τετράγωνα στο εσωτερικό του
def draw_square():
        for side in range(4):
                pen.forward(100)
                pen.right(90)
                for side in range(4):
                        pen.forward(50)
                        pen.right(90)

# Σήκωσε την πένα
pen.penup()
# Πήγαινε πίσω 20 μονάδες
pen.back(20)
# Τοποθέτησε την πένα έτοιμη να γράψει
pen.pendown()

for square in range(80):
     # κλήση της συνάρτησης για σχηματισμό των τετραγώνων
        draw_square()
        #Αφού έχει ολοκληρωθει ένα μεγάλο τετράγωνο με 4 μικρά, πήγαινε μπροστά
        #κατά 5 μονάδες και στρίψε 5 μοίρες
        pen.forward(5)
        pen.left(5)
        
pen.hideturtle()
