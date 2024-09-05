import tkinter as tk
import sys
import io

class CodeExecutorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Code Executor")

        # Erstellen Sie das Textfeld für die Codeeingabe
        self.code_text = tk.Text(root, height=15, width=60)
        self.code_text.pack(pady=10)

        # Erstellen Sie den Ausführen-Button
        self.execute_button = tk.Button(root, text="Execute Code", command=self.execute_code)
        self.execute_button.pack(pady=5)

        # Erstellen Sie das Textfeld für die Ausgabe
        self.output_text = tk.Text(root, height=15, width=60)
        self.output_text.pack(pady=10)
        self.output_text.config(state=tk.DISABLED)

    def execute_code(self):
        # Holen Sie sich den Code aus dem Textfeld
        code = self.code_text.get("1.0", tk.END)
        
        # Leiten Sie stdout um, um die print-Ausgaben zu erfassen
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        
        try:
            # Führen Sie den Code aus
            exec(code, globals())
        except Exception as e:
            # Erfassen Sie alle Fehler
            redirected_output.write(f"Error: {e}")
        finally:
            # Stellen Sie stdout wieder her
            sys.stdout = old_stdout
        
        # Zeigen Sie die Ausgabe im Ausgabefeld an
        output = redirected_output.getvalue()
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output)
        self.output_text.config(state=tk.DISABLED)

# Erstellen Sie das Hauptfenster
root = tk.Tk()
app = CodeExecutorApp(root)
root.mainloop()
