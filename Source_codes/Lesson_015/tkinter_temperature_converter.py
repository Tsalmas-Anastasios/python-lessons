# Δημιουργία μετατροπέα θερμοκρασίας
#
#
# Βασικά, η εφαρμογή έχει ένα label (ετικέτα), ένα πεδίο εισαγωγής αριθμού
# (entry field) και ένα κουμπί (button). Όταν εισάγουμε μια θερμοκρασία σε
# Φαρενάιτ και κάνουμε κλικ στο κουμπί "Μετατροπή" θα μετατραπεί η τιμή στο
# πεδίο εισαγωγής από Φαρενάιτ σε Κελσίου.
#
# Εάν εισαγάγουμε μια τιμή που δεν μπορεί να μετατραπεί σε αριθμό, το πρόγραμμα
# θα εμφανίσει ένα σφάλμα.
#
# Για να δημιουργήσουμε αυτήν την εφαρμογή, ακολουθούμε τα παρακάτω βήματα:
#
#

# 1. Κάνουμε εισαγωγή όλων των απαραίτητων modules:
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

# 2. Δημιουργούμε το παράθυρο root και τις ρυθμίσεις του:
# Παράθυρο root
root = tk.Tk()
root.title('Temperature converter')
root.geometry('300x700')
root.resizable(False, False)

# Δημιουργούμε ένα frame το οποίο κρατάει το πεδίο εισαγωγής αριθμού
frame = ttk.Frame(root)

# Καθορίζουμε μια επιλογή που θα χρησιμοποιείται από όλα τα πεδία
options = { 'padx': 5, 'pady': 5 }

# Καθορίζουμε την ετικέτα (label) το πεδίο εισαγωγής (entry) και το κουμπί. Η
# ετικέτα θα δείξει το αποτέλεσμα μόλις πατηθεί το κουμπί "Μετατροπή"

# Ετικέτα θερμοκρασίας
temperature_label = ttk.Label(frame, text='Fahrenheit')
temperature_label.grid(column = 0, row = 0, sticky = 'W', **options)

# Πεδίο εισαγωγής θερμοκρασίας
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column = 1, row = 0, **options)
temperature_entry.focus()




# Συνάρτηση - Function για το κουμπί μετατροπής
def convert_button_clicked():
    # Διαχείρηση γεγονότος εισαγωγής αριθμού και πατήματος του κουμπιού
    try:
        f = float(temperature.get())
        c = fahrenheit_to_celsius(f)
        result = f'{f} βαθμοί Φαρενάιτ είναι {c:.2f} βαθμοί Κελσίου'
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)

# Κουμπί μετατροπής
convert_button = ttk.Button(frame, text='Μετατροπή')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# Ετικέτα αποτελέσματος
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)


# Τέλος, τοποθετούμε το frame στο παράθυρο root και τρέχουμε τη μέθοδο mainloop()
frame.grid(padx=10, pady=10)
root.mainloop()











# Συνάρτηση - Function που μετατρέπει τη θερμοκρασία
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9
        
        
        