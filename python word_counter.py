import tkinter as tk
from tkinter import messagebox

def count_words(text):
    """Count the number of words in the given text."""
    words = text.split()
    return len(words)

def validate_input(text):
    """Validate the user input to ensure it is not empty."""
    if not text.strip():
        return False
    return True

def on_count_button_click():
    """Handle the count button click event."""
    text = input_text.get("1.0", tk.END)
    if validate_input(text):
        word_count = count_words(text)
        result_label.config(text=f"Word Count: {word_count}")
    else:
        messagebox.showerror("Input Error", "Input cannot be empty.")

def on_clear_button_click():
    """Handle the clear button click event."""
    input_text.delete("1.0", tk.END)
    result_label.config(text="Word Count: 0")

# Set up the main application window
app = tk.Tk()
app.title("Word Counter")
app.geometry("400x300")

# Create and place the input text widget
input_label = tk.Label(app, text="Enter a sentence or paragraph:")
input_label.pack(pady=10)
input_text = tk.Text(app, height=10, width=50)
input_text.pack(pady=10)

# Create and place the result label
result_label = tk.Label(app, text="Word Count: 0", font=("Helvetica", 14))
result_label.pack(pady=10)

# Create and place the count button
count_button = tk.Button(app, text="Count Words", command=on_count_button_click)
count_button.pack(pady=5)

# Create and place the clear button
clear_button = tk.Button(app, text="Clear", command=on_clear_button_click)
clear_button.pack(pady=5)

# Run the application
app.mainloop()
