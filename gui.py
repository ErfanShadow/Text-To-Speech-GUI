import tkinter as tk
import pyttsx3

# Initialize window
window = tk.Tk()
window.title("Text To Speech GUI")
window.resizable(width=False, height=False)
window.configure(bg='purple')

# Function to perform text-to-speech
def speak():
    text = entry.get()
    try:
        rate = int(entry2.get())
    except ValueError:
        rate = 200  # Default rate
    bot = pyttsx3.init()
    bot.setProperty('rate', rate)
    bot.say(text)
    bot.runAndWait()
def quit():
    window.destroy()
# Title label
label = tk.Label(window, text='Python Text To Speech GUI',
                font='arial 16 bold', fg='white', bg='purple')
label.pack(fill=tk.X, pady=10)

# Text entry label
label2 = tk.Label(window, text='Write Your Own Text:',
                font='Arial', fg='white', bg='purple')
label2.pack(fill=tk.X)

entry = tk.Entry(window, font='Arial')
entry.pack(fill=tk.X, ipadx=50, ipady=100)

# Settings section
label3 = tk.Label(window, text='Settings:', font='arial 14 bold', fg='white', bg='purple')
label3.pack(fill=tk.X, pady=(10, 0))

# Rate setting
label5 = tk.Label(window, text='Rate (default ~200):', font='arial', fg='white', bg='purple')
label5.pack(fill=tk.X)

entry2 = tk.Entry(window, font='Arial')
entry2.pack(fill=tk.X, padx=10, pady=5)

#Buttons frame
btn_frame = tk.Frame(window, bg='purple')
btn_frame.pack(pady=10)

# Close button
button = tk.Button(btn_frame, text="EXIT", command=quit, font='arial 12 bold', bg='black', fg='white')
button.pack(side=tk.LEFT, padx=5)

# Speak button
button2 = tk.Button(btn_frame, text="SPEAK", command=speak, font='arial 12 bold', bg='black', fg='white')
button2.pack(side=tk.LEFT, padx=5)

window.mainloop()
