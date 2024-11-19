import customtkinter as ctk
from tkinter import filedialog, messagebox
import time
from threading import Thread

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def simulate_bypass(file_path, progress_bar, status_label):
    if not file_path:
        status_label.configure(text="Aucun fichier sélectionné !")
        return

    progress_bar.set(0)
    status_label.configure(text="Début du processus...")
    steps = [
        f"Analyse du fichier : {file_path}...",
        "Désactivation des services...",
        "Modification du registre...",
        "Suppression des règles...",
    ]
    
    for i, step in enumerate(steps, 1):
        time.sleep(2)
        status_label.configure(text=step)
        progress_bar.set(i / len(steps))
    
    status_label.configure(text="Bypass echouer")
    messagebox.showinfo("Succès", f"Le fichier '{file_path}' a été traité avec echec")

def start_simulation(progress_bar, status_label, file_path_var):
    thread = Thread(target=simulate_bypass, args=(file_path_var.get(), progress_bar, status_label))
    thread.start()

def select_file(file_path_var, status_label):
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier")
    if file_path:
        file_path_var.set(file_path)
        status_label.configure(text=f"Fichier sélectionné : {file_path}")
    else:
        status_label.configure(text="Aucun fichier sélectionné")

app = ctk.CTk()
app.title("Windows Defender Bypass Tool")
app.geometry("500x350")

file_path_var = ctk.StringVar()

status_label = ctk.CTkLabel(app, text="Prêt à commencer", font=("Arial", 14))
status_label.pack(pady=20)

progress_bar = ctk.CTkProgressBar(app, width=400)
progress_bar.pack(pady=10)
progress_bar.set(0)

select_button = ctk.CTkButton(app, text="Sélectionner un fichier", command=lambda: select_file(file_path_var, status_label))
select_button.pack(pady=10)

start_button = ctk.CTkButton(app, text="Démarrer le Bypass", command=lambda: start_simulation(progress_bar, status_label, file_path_var))
start_button.pack(pady=20)

app.mainloop()
