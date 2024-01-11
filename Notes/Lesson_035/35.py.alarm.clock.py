from tkinter import *
import datetime
import time
import winsound
from winsound import Beep

def alarm(set_alarm_timer):
    while True: # Όσο δεν συμβαίνει τίποτα, τύπωνε στην κονσόλα την ημ/νία και την ώρα
        time.sleep(1)# Ο χρόνος θα μετράει με καθυστέρηση ενός δευτ/του
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:", date)# Εκτύπωση στην κονσόλα (IDLE)
        print(now)
        if now == set_alarm_timer:# Όταν η ώρα γίνει ίση με την ώρα που έχει ορίσει ο χρήστης
            print("Time to Wake up")
            #winsound.PlaySound("alarm_sound.wav", winsound.SND_ASYNC)
            Beep(1200, 500)
            break

def stop_alarm():
    winsound.PlaySound(None, winsound.SND_PURGE)
    
def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(set_alarm_timer)

# Δημιουργία γραφικού περιβάλλοντος
clock = Tk()
clock.title("Python Alarm Clock")
clock.iconbitmap(r"python_new.ico")# Βάζουμε το δικό μας εικονίδιο στο παράθυρο

clock.geometry("400x250")

# 1η ετικέτα
set_alarm_label = Label(clock, text="Να ξυπνήσω στις...", font=('Helvetica', 15))
set_alarm_label.pack(side=TOP, padx=15, pady=5)

# 2η ετικέτα
time_format = Label(clock, text="Εισάγετε την ώρα σε 24ωρη βάση", font=('Helvetica', 12))
time_format.pack(side=TOP, padx=5, pady=5)

# 3η ετικέτα
add_time_label = Label(clock, text="Ώρα  Λεπτά  Δευτερόλεπτα", font=('Helvetica', 10))
add_time_label.pack(side=TOP, padx=5, pady=5)

# Οι μεταβλητές για να αρχικοποιήσουμε το ρολόι μας(initialization):
hour = StringVar()
minute = StringVar()
second = StringVar()

# Πεδία εισαγωγής
hour_time = Entry(clock, textvariable=hour, bg="pink", width=15)
hour_time.place(x=110, y=110)

minute_time = Entry(clock, textvariable=minute, bg="pink", width=15)
minute_time.place(x=150, y=110)

second_time = Entry(clock, textvariable=second, bg="pink", width=15)
second_time.place(x=200, y=110)

# Κουμπί για να ληφθεί η ώρα του χρήστη από το πρόγραμμα:
submit_button = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time)
submit_button.place(x=100, y=180)

# Κουμπί στοπ
stop_button = Button(clock, text="Stop Alarm", fg="blue", width=10, command=stop_alarm)
stop_button.place(x=210, y=180)

clock.mainloop()
