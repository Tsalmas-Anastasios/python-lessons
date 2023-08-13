import turtle
import random

p_one = turtle.Turtle()
p_one.color("purple")
p_one.shape("turtle")
p_one.penup()
p_one.goto(-200,100)
p_two = p_one.clone()
p_two.color("orange")
p_two.penup()
p_two.goto(-200,-100)

p_one.goto(300,60)
p_one.pendown()
p_one.circle(40)
p_one.penup()
p_one.goto(-200,100)
p_two.goto(300,-140)
p_two.pendown()
p_two.circle(40)
p_two.penup()
p_two.goto(-200,-100)


die = [1,2,3,4,5,6]
for i in range(20):
    if p_one.pos() >= (300,100):
            print("Ο Πρώτος Παίκτης Κέρδισε!")
            break
    elif p_two.pos() >= (300,-100):
            print("Ο Δεύτερος Παίκτης Κέρδισε!")
            break
    else:
            p_one_turn = input("Πατήστε το 'Enter' για να ρίξετε το ζάρι ")
            die_outcome = random.choice(die)
            print("Φέρατε: ")
            print(die_outcome)
            print("Ο αριθμός των βημάτων είναι: ")
            print(20*die_outcome)
            p_one.fd(20*die_outcome)
            p_two_turn = input("Πατήστε το 'Enter' για να ρίξετε το ζάρι ")
            die_outcome = random.choice(die)
            print("Φέρατε: ")
            print(die_outcome)
            print("Ο αριθμός των βημάτων είναι: ")
            print(20*die_outcome)
            p_two.fd(20*die_outcome)

