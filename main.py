import tkinter as tk
import random
import time

# --- Configuration & Data ---
sentences = [
    "Code is like humor. When you have to explain it, it's bad. Enjoy your typing journey!",
    "The quick brown fox jumps over the lazy dog.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Python makes hard things look easy.",
    "Do you think you can type 100 words per minute? Let's find out, Nuria!"
]

start_time = 0

# --- Functions ---

def start_test():
    global start_time
    sentence_label.config(text=random.choice(sentences))
    start_time = time.time()
    input_entry.delete(0, tk.END)
    input_entry.focus()
    result_label.config(text="Typing...", fg="black")

def end_test():
    global start_time
    duration = time.time() - start_time
    
    user_text = input_entry.get().strip()
    target_text = sentence_label.cget("text")
    
    if user_text == target_text:
        wpm = (len(user_text) / 5) / (duration / 60)
        result_label.config(text=f"Perfect! Speed: {wpm:.2f} WPM", fg="green")
    else:
        # Precision calculation
        correct_chars = sum(1 for c_t, c_u in zip(target_text, user_text) if c_t == c_u)
        accuracy = (correct_chars / len(target_text)) * 100 if target_text else 0
        result_label.config(text=f"Accuracy: {accuracy:.1f}% | Try to be more precise!", fg="orange")

# --- GUI Setup ---
window = tk.Tk()
window.title("Python Speed Typer Pro")
window.geometry("600x450")

# Widgets
title_label = tk.Label(window, text="Typing Speed Test", font=("Helvetica", 24, "bold"))
title_label.pack(pady=20)

sentence_label = tk.Label(window, text="Click Start to begin!", font=("Helvetica", 12), wraplength=500)
sentence_label.pack(pady=20)

input_entry = tk.Entry(window, width=50, font=("Helvetica", 14))
input_entry.pack(pady=10)
input_entry.bind("<Return>", lambda event: end_test())

start_button = tk.Button(window, text="START TEST", command=start_test, bg="blue", fg="white", font=("Helvetica", 10, "bold"))
start_button.pack(pady=20)

result_label = tk.Label(window, text="", font=("Helvetica", 13, "italic"))
result_label.pack(pady=20)

window.mainloop()




