import random
import string
from tkinter import *
# ---------------
def popmsg(final):
    popup = Tk()
    text = Text(popup,height=2, width=30)
    text.pack()
    text.insert(END,final)
    popup.mainloop()
# ---------------
def generate():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    ssymbols = ['!','@','%','^','&','*']
    password_length = slider.get()
    bucket = []
    final = []
# ---------------
    #if sum(lower_selected.get()+upper_selected.get()+numbers_selected.get()+ssymbols_selected.get()) = 0:
    #    popmsg('Please check one') # checks to see if at least one checkbox is checked
    if lower_selected.get():
        for letter in lower:
            bucket.append(letter)

    if upper_selected.get():
        for letter in upper:
            bucket.append(letter)

    if numbers_selected.get():
        for number in numbers:
            bucket.append(number)

    if ssymbols_selected.get():
        for symbol in ssymbols:
            bucket.append(symbol)
# getting a random character as many times as input from password_length
    for i in range(password_length):
        final.append(random.choice(bucket))
# ---------------
    popmsg(''.join(final))
    print(''.join(final))  # prints the final list of characters in string form
# ---------------
root = Tk()
root.geometry("300x300")
# ---------------
lower_selected = IntVar()
upper_selected = IntVar()
numbers_selected = IntVar()
ssymbols_selected = IntVar()

cb_lower = Checkbutton(root, text = "Lowercase", variable=lower_selected)
cb_upper = Checkbutton(root, text = "Uppercase", variable=upper_selected)
cb_numbers = Checkbutton(root, text = "Numbers", variable=numbers_selected)
cb_ssymbols = Checkbutton(root, text = "Special Symbols", variable=ssymbols_selected)
# ---------------
slider = Scale(root, from_=0, to=36, orient=HORIZONTAL)
btn_generatepw = Button(root,text="Generate Password",command=generate)
# ---------------
cb_lower.pack()
cb_upper.pack()
cb_numbers.pack()
cb_ssymbols.pack()
slider.pack()
btn_generatepw.pack()
# ---------------
mainloop()

# remember that atleast one checkbox needs to be ticked
