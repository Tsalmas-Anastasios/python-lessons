import tkinter as tk 
from tkinter import ttk 
from tkinter.messagebox import showerror 
# Παράθυρο root  
root = tk.Tk() 
root.title('Μετατροπέας Θερμοκρασίας') 
root.geometry('360x90') 
root.resizable(False, False) 
def fahrenheit_to_celsius(f): 
    # Μετατροπή Φαρενάιτ σε Κελσίου 
    return (f - 32) * 5/9

# Δημιουργία frame 
frame = ttk.Frame(root)

# Ρυθμίσεις του πεδίου 
options = {'padx': 5, 'pady': 5}

# Ετικέτα θερμοκρασίας 
temperature_label = ttk.Label(frame, text='Φαρενάιτ')
temperature_label.grid(column=0, row=0, sticky='W', **options)

# Πεδίο εισαγωγής αριθμού (θερμοκρασίας) 
temperature = tk.StringVar() 
temperature_entry = ttk.Entry(frame, textvariable=temperature)
temperature_entry.grid(column=1, row=0, **options)
temperature_entry.focus()

# Κουμπί μετατροπής 
def convert_button_clicked(): 
 # Διαχείριση γεγονότος εισαγωγής αριθμού και πατήματος του  κουμπιού  
    try:
        f = float(temperature.get()) 
        c = fahrenheit_to_celsius(f) 
        result = f'{f} βαθμοί Φαρενάιτ είναι {c:.2f} βαθμοί Κελσίου'
        result_label.config(text=result) 
    except ValueError as error: 
        showerror(title='Error', message=error)
     
convert_button = ttk.Button(frame, text='Μετατροπή')
convert_button.grid(column=2, row=0, sticky='W', **options)
convert_button.configure(command=convert_button_clicked)

# Ετικέτα αποτελέσματος 
result_label = ttk.Label(frame) 
result_label.grid(row=1, columnspan=3, **options)

# Προσθήκη padding στο frame 
frame.grid(padx=10, pady=10)

# Εκκίνηση εφαρμογής 
root.mainloop()



