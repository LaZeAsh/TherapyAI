import tkinter as tk
window = tk.Tk()

btn = tk.Button(window, text = "Button", fg = 'blue')
btn.place(x = 80, y = 100)

window.title('TherapyAI')
window.geometry("300x200+10+20")
window.mainloop()

