import tkinter as tk
from tkinter import messagebox

# Statusvariable, um festzustellen, ob der Inject-Button gedrückt wurde
inject_button_pressed = False

# Funktion, die beim Klicken des Execute-Buttons ausgeführt wird
def on_execute_click():
    global inject_button_pressed
    if not inject_button_pressed:
        messagebox.showwarning("Error", "Its not Injected.")
        return
    
    code = textbox_large.get("1.0", tk.END)  # Den gesamten Inhalt der großen Textbox abrufen
    try:
        exec(code, globals())  # Den Python-Code ausführen
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

# Funktion, die beim Klicken des Clear-Buttons ausgeführt wird
def on_clear_click():
    textbox_large.delete("1.0", tk.END)  # Löscht den gesamten Inhalt der großen Textbox

# Funktion, die beim Klicken des Inject-Buttons ausgeführt wird
def on_inject_click():
    global inject_button_pressed
    inject_button_pressed = True
    print("Successful Injected")

# Funktion zum Aktualisieren der Zeilennummern
def update_line_numbers(event=None):
    line_numbers.config(state='normal')
    line_numbers.delete('1.0', tk.END)
    
    # Holen der Zeilennummern und Füllen des Line Numbers Textfelds
    line_count = int(textbox_large.index('end-1c').split('.')[0])
    line_numbers_text = ''.join(f"{i+1}\n" for i in range(line_count))
    line_numbers.insert('1.0', line_numbers_text)
    line_numbers.config(state='disabled')

# Hauptfenster erstellen
root = tk.Tk()
root.title("Executer for Cheat Launcher")

# Fenstergröße einstellen und fixieren
root.geometry("600x315")
root.resizable(False, False)  # Fenstergröße kann nicht geändert werden

# Frame für die Buttons erstellen und unten platzieren
frame_button = tk.Frame(root)
frame_button.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

# Execute-Button hinzufügen
execute_button = tk.Button(frame_button, text="Execute", command=on_execute_click, font=("Arial", 12))
execute_button.pack(side=tk.LEFT, padx=5)

# Clear-Button hinzufügen
clear_button = tk.Button(frame_button, text="Clear", command=on_clear_click, font=("Arial", 12))
clear_button.pack(side=tk.LEFT, padx=5)

# Inject-Button hinzufügen
inject_button = tk.Button(frame_button, text="Inject", command=on_inject_click, font=("Arial", 12))
inject_button.pack(side=tk.RIGHT, padx=5)

# Frame für die Textboxen erstellen und oben platzieren
frame_textboxes = tk.Frame(root)
frame_textboxes.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Frame für Zeilennummern erstellen
frame_line_numbers = tk.Frame(frame_textboxes)
frame_line_numbers.pack(side=tk.LEFT, fill=tk.Y)

# Zeilennummern-Textbox hinzufügen
line_numbers = tk.Text(frame_line_numbers, width=5, padx=2, takefocus=0, borderwidth=0, background='#f0f0f0', state='disabled', font=("Arial", 12))
line_numbers.pack(side=tk.LEFT, fill=tk.Y)

# Große Textbox hinzufügen
textbox_large = tk.Text(frame_textboxes, wrap=tk.NONE, width=40, height=20, font=("Arial", 12))
textbox_large.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
textbox_large.bind('<KeyRelease>', update_line_numbers)
textbox_large.bind('<MouseWheel>', update_line_numbers)

# Kleine Textbox hinzufügen
textbox_small = tk.Text(frame_textboxes, width=20, height=20, font=("Arial", 12))
textbox_small.pack(side=tk.RIGHT, fill=tk.BOTH)
textbox_small.config(state=tk.DISABLED)  # Die Textbox im Lesemodus setzen

# Initialen Text in den Textboxen setzen
initial_text_large = "#Python Cheat Launcher\nprint(\"Hello World!\")\n"
textbox_large.insert("1.0", initial_text_large)

initial_text_small = "                    Info\n\n     Its a Executer for the\n Cheat Launcher. You can\n  get a special command.\n    Here is the command:\n\n\n\n\n\n\n  Made by 321RemagYT"
textbox_small.config(state=tk.NORMAL)  # Temporär aktivieren, um Text zu setzen
textbox_small.insert("1.0", initial_text_small)
textbox_small.config(state=tk.DISABLED)  # Zurück in den Lesemodus versetzen

# Die GUI-Schleife starten
root.attributes('-topmost', True)
update_line_numbers()  # Initiales Setzen der Zeilennummern
root.mainloop()
