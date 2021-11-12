from tkinter import *
import pyshorteners
import re
root = Tk()
root.title("Link Shortener")
root.geometry("500x500")


def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    p = re.compile(regex)

    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False


def shorten():
    if shortened_link.get():
        shortened_link.delete(0, END)

    if original_link.get():

        if isValidURL(original_link.get()) == True:

            # convert to tinyurl
            try:
                url = pyshorteners.Shortener().tinyurl.short(original_link.get())
                shortened_link.insert(END, url)
            # reverse url
                print(pyshorteners.Shortener().tinyurl.expand(url))
            except:
                raise pyshorteners.exceptions.ShorteningErrorException(
                    message=None)
        else:
            shortened_link.insert(END, "Invalid Input Url")


Title_label = Label(root, text="Enter link to shorten", font=("Helvetica", 24))
Title_label.pack(pady=20)
original_link = Entry(root, font=("Helvetica", 24))
original_link.pack(pady=20)
button_shorten = Button(root, text="Shorten Link",
                        command=shorten, font=("Helvetica", 15))
button_shorten.pack(pady=20)

output_subtitle = Label(root, text="Shortened Link", font=("Helvetica", 20))
output_subtitle.pack(pady=50)

shortened_link = Entry(root, font=("Helvetica", 22), justify=CENTER,
                       width=30, bd=0, bg="systembuttonface")
shortened_link.pack(pady=8)
root.mainloop()
