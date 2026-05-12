# Import the libraries
import tkinter as tk
import random
import time

# Setup the main window
window = tk.Tk()
window.title("Speed Typing Test")
window.geometry("500x400") # This sets the size (Width x Height)

# Create a Label for the title or instructions
title_label = tk.Label(window, text="Typing Speed Test", font=("Helvetica", 24))
title_label.pack(pady=10) # pady adds some vertical space

# Create a lists with several sentences options
sentences = [
    "Code is like humor. When you have to explain it, it’s bad. Enjoy your typing journey!",
    "The quick brown fox jumps over the lazy dog.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Python makes hard things look easy."
    "Do you think you can type 100 words per minute? Let's find out, Nuria!"
    ]

# Create a Label for the target sentence
# (This is where the random sentence will go later)

sentence_label = tk.Label(window, text="", wraplength=400)
sentence_label.pack(pady=20)

start_time = 0
end_time = 0

def start_test():
    global start_time
    # 1. Update the sentence
    sentence_label.config(text=random.choice(sentences))
    # 2. Record the current time
    start_time = time.time() 
    # 3. Clear the input box so the user starts fresh
    input_entry.delete(0, tk.END)
    # 4. Clear previous results
    result_label.config(text="Typing...", fg="black")
    # 5. Put the cursor in the entry box automatically
    input_entry.focus()

def end_test():
    global start_time
    end_time = time.time()
    duration = end_time - start_time
    
    user_text = input_entry.get().strip()
    target_text = sentence_label.cget("text")
    
    # Check if it's ok
    if user_text == target_text:
        wpm = (len(user_text) / 5) / (duration / 60)
        result_label.config(text=f"Well done! Speed: {wpm:.2f} WPM", fg="green")
    else:
        # 1. Compare character by character
        correct_chars = 0
        # target_text is the original, user_text is typed by user
        
        # Python tip: zip iterates through both until the shortest one ends
        for char_target, char_user in zip(target_text, user_text):
            if char_target == char_user:
                correct_chars += 1
                
        # 2. Calculate accuracy %
        # Be careful with division by zero! Check if target_text is not empty
        if len(target_text) > 0:
            accuracy = (correct_chars / len(target_text)) * 100
        else:
            accuracy = 0
            
        # 3. Inform the user
        result_label.config(text=f"Errors found. Accuracy: {accuracy:.1f}%", fg="orange")
        pass

start_button = tk.Button(window, text='Start', command=start_test)
start_button.pack(pady=10)

# Create an Entry widget for the user input
input_entry = tk.Entry(window, width=50, font=("Helvetica", 14))
input_entry.pack(pady=10)

# This tells the entry box: "When the Enter key is pressed, run end_test"
input_entry.bind("<Return>", lambda event: end_test())

result_label = tk.Label(window, text="", font=("Helvetica", 12, "italic"))
result_label.pack(pady=20)

# Keep the window running
window.mainloop()




