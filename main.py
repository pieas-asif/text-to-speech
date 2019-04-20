import tkinter as tk
import pyttsx3

def speak(text):
    print("Button Clicked")
    print(text, end='')
    engine = pyttsx3.init()
    engine.setProperty('rate',150)
    engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
    engine.say(text)
    engine.runAndWait()


root = tk.Tk()
root.resizable(width=False, height=False)
root.title("Talk To Me")

canvas = tk.Canvas(root, height=300, width=400, bg="#b3d1ff")
canvas.pack()

frame = tk.Frame(root, bg="#b3d1ff")
frame.place(relx=0.025, rely=0.025, relwidth=0.95, relheight=0.95)

text = tk.Text(frame, height=15, bd=1, bg="#e6e6e6")
text.pack()

button = tk.Button(frame, text="SPEECH", bd=3, bg="#0080ff", fg="#fff", activebackground="#66b3ff", command=lambda: speak(text.get(0.0, 'end')))
button.pack(fill="x")

root.mainloop()
