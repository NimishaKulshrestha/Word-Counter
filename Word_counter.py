import re
import tkinter as tk

def count_words():
    try:
        input_text = input_entry.get("1.0", tk.END).strip()  # Get input text from the text widget
        if not input_text:
            result_label.config(text="Please enter some text", fg="red")
        else:
            words = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|\b[A-Za-z]+\b', input_text)  # Find words including email addresses
            num_words = len(words)  # Count the number of words
            result_label.config(text=f"Number of words: {num_words}", fg="green")
    except Exception as e:
        result_label.config(text=f"Error: {e}", fg="red")

root = tk.Tk()
root.title("Word Counter")

# Labels
input_label = tk.Label(root, text="Enter Text:")
input_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

# Text Entry
input_entry = tk.Text(root, height=5, width=50)
input_entry.grid(row=1, column=0, padx=10, pady=5)

# Button
submit_button = tk.Button(root, text="Count Words", command=count_words, bg="lightblue", fg="black")
submit_button.grid(row=1, column=1, padx=10, pady=5)

root.mainloop()
