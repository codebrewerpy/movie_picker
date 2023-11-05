import tkinter as tk
import random

# Function to check if the user's numbers match the generated numbers
def check_numbers():
    user_numbers = [int(entry1.get()), int(entry2.get()), int(entry3.get()), int(entry4.get()), int(entry5.get()), int(entry6.get())]
    user_joker = int(joker_entry.get())
    
    generated_numbers = random.sample(range(1, 50), 6)
    generated_joker = random.randint(0, 9)
    
    matched_numbers = set(user_numbers).intersection(set(generated_numbers))
    
    result_label.config(text=f"Your Numbers: {user_numbers}\nYour Joker: {user_joker}\nGenerated Numbers: {generated_numbers}\nGenerated Joker: {generated_joker}")
    
    if len(matched_numbers) >= 2 and user_joker == generated_joker:
        result_label.config(text=result_label.cget("text") + "\nCongratulations! You Win!")
    else:
        result_label.config(text=result_label.cget("text") + "\nSorry, you didn't win this time.")

# Create the main window
window = tk.Tk()
window.title("Lucky Numbers Game")

# Create labels and entry fields for user's numbers and joker
tk.Label(window, text="Enter 6 numbers between 1 and 49:").pack()
entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry3 = tk.Entry(window)
entry4 = tk.Entry(window)
entry5 = tk.Entry(window)
entry6 = tk.Entry(window)
entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()
entry5.pack()
entry6.pack()

tk.Label(window, text="Enter a joker number between 0 and 9:").pack()
joker_entry = tk.Entry(window)
joker_entry.pack()

# Create a button to check the numbers
check_button = tk.Button(window, text="Check Numbers", command=check_numbers)
check_button.pack()

# Create a label to display the results
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main loop
window.mainloop()
