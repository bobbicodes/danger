import Tkinter as tk
from subprocess import call

button_flag = True

def click01():
    global button_flag
    call('up')

root = tk.Tk()
root.title('Uppy')
frame1 = tk.Frame(root)
frame1.pack(side=tk.TOP, fill=tk.X)

photo1 = tk.PhotoImage(file="up.gif")
button1 = tk.Button(frame1, image=photo1,
    text="Update System", command=click01)
button1.pack(side=tk.LEFT, padx=2, pady=2)
button1.image = photo1

root.mainloop()