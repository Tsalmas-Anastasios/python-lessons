from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# themes = cosmo, flatly, journal, litera, lumen, minty, pulse, sandstone,
# united, yeti, morph, simplex, cerculean

import datetime
import time
import winsound


def alarm(set_alarm_timer): # Η παράμετρος εισάγεται από την actual_time()
    while True: # Όσο δεν συμβαίνει τίποτα, τύπωνε στην κονσόλα την ημ/νία και την ώρα
        time.sleep(1) # Ο χρόνος θα μετράει με καθυστέρηση ενός δευτ/του
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Η ημερομηνία είναι:",date) # Εκτύπωση στην κονσόλα (IDLE)
        print(now) # Εκτύπωση στην κονσόλα (IDLE)
        if now == set_alarm_timer: # Όταν η ώρα γίνει ίση με την ώρα που έχει ορίσει ο χρήστης
            print("Ώρα να ξυπνήσεις!") #τύπωσε μήνυμα στην κονσόλα
            # winsound.PlaySound("sound.wav",winsound.SND_ASYNC) # Εδώ έχουμε έναν κλασικό ήχο των Windows
            winsound.PlaySound("D://Cookoo_Home/Λήψεις/mixkit-retro-game-emergency-alarm-1000.wav",winsound.SND_FILENAME) # και κάλεσε τον ήχο του ξυπνητηριού(ήχος που έχουμε κατεβάσει) 
            break # βγες από τον βρόχο (η λειτουργία του ξυπνητηριού ολοκληρώθηκε)



def activate_alarm(): # Παίρνει τον χρόνο αφύπνισης και "καλεί" τη "μηχανή" που θα χτυπήσει το ξυπνητήρι
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer) # # Κλήση της μηχανής του ξυπνητηριού

# Δημιουργία γραφικού περιβάλλοντος
clock = ttk.Window(themename="flatly")
clock.title("Python Alarm Clock")
#clock.iconbitmap(r"python.ico")
clock.geometry("400x200")
time_format=ttk.Label(clock, text= "Εισάγετε την ώρα σε 24ωρη βάση", font=('Helvetica', 15), bootstyle = PRIMARY).pack(side = TOP, padx=5, pady=5)
addTime = ttk.Label(clock, text = "Ώρα   Λεπτά  Δευτερόλεπτα", font=('Helvetica', 12), bootstyle = SUCCESS).pack(side = TOP, padx=5, pady=5)
setYourAlarm = ttk.Label(clock, text = "Να ξυπνήσω στις...", font=('Helvetica', 10), bootstyle = SECONDARY).pack(side = BOTTOM, padx=5, pady=5)


# Οι μεταβλητές που χρειαζόμαστε για το ξυνητήρι (αρχικοποίηση):
hour = StringVar()
min = StringVar()
sec = StringVar()

# Ώρα στην οποία βάζουμε το ξυπνητήρι να χτυπήσει
hourTime= Entry(clock,textvariable = hour, width = 10).place(x=105,y=70)
minTime= Entry(clock,textvariable = min, width = 10).place(x=145,y=70)
secTime = Entry(clock,textvariable = sec, width = 10).place(x=185,y=70)

# Το ξυπνητήρι μπαίνει σε λειτουργία με το πάτημα του κουμπιού
submit = ttk.Button(clock,text = "Βάζω ξυπνητήρι", width = 15, command = activate_alarm).pack(side = BOTTOM, padx=5, pady=5)

clock.mainloop()


