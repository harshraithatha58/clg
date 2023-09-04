from tkinter import *

main_root = Tk()
A = 450
B = 450
main_root.geometry("800x500")
main_root.minsize("800","500")
main_root.maxsize("800","500")
main_root.title("Harsh Raithatha")

photo = PhotoImage(file="image.png")
image_label = Label(image=photo)
image_label.pack()

main_label = Label(text="Harsh Raithatha")
main_label.pack()

main_root.mainloop()

