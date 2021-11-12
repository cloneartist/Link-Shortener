from tkinter import *
root = Tk()
root.title("Link Shortener")
root.geometry("500x500")


def shorten():
    if shorty.get():
        shorty.delete(0, END)


my_label = Label(root, text="Enter link to shorten", font=("Helvetica", 30))
my_label.pack(pady=20)
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)
my_button = Button(root, text="Shorten Link",
                   command=shorten, font=("Helvetica", 24))
my_button.pack(pady=20)

shorty_label = Label(root, text="Shortened Link", font=("Helvetica", 20))
shorty_label.pack(pady=50)

shorty = Entry(root, font=("Helvetica", 22), justify=CENTER)
shorty.pack(pady=8)
root.mainloop()
