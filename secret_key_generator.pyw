from datetime import datetime
from tkinter import *

from app.generator import Generator

window = Tk()
gen = Generator()
date = datetime.now()

PRIMARY_COLOR = '#e74c3c'
SECONDARY_COLOR = '#c0392b'


def generate_flask():
    flask_key = str(gen.flask_generator())
    input_user.delete(0, END)
    input_user.insert(0, flask_key)


def generate_django():
    django_key = str(gen.django_generator())
    input_user.delete(0, END)
    input_user.insert(0, django_key)


def clipboard():
    window.clipboard_clear()
    window.clipboard_append(input_user.get())


# TKINTER INTERFACE
content = Frame(window, bg=PRIMARY_COLOR)
title = Label(content,
              text='Secret Key Generator',
              font=('courrier', 20),
              bg=PRIMARY_COLOR,
              fg='white')
title.pack(pady=20)
input_user = Entry(content,
                   width=74)
input_user.pack()

btn_flask = Button(content, text='Generate a secret key for Flask',
                   width=26,
                   relief='flat',
                   command=generate_flask)
btn_flask.pack(pady=10, side=LEFT)

btn_django = Button(content, text='Generate a secret key for Django',
                    width=26,
                    relief='flat',
                    command=generate_django)
btn_django.pack(padx=10, pady=10, side=LEFT)

btn_clipboard = Button(content,
                       width=16,
                       relief='flat',
                       command=clipboard)
img_clipboard = PhotoImage(file='app/clipboard.png').subsample(4, 4)
btn_clipboard.config(image=img_clipboard, width=20, height=20)
btn_clipboard.pack(side=RIGHT)
content.pack(expand=YES)

footer = Frame(window, bg=SECONDARY_COLOR)

lbl_copyright = Label(footer, text=(f'Vincent HOUILLON - {date.year}'),
                      bg=SECONDARY_COLOR,
                      fg='white',
                      font=('courrier', 7, 'italic'))
lbl_copyright.pack(side=LEFT, padx=5)

exit_btn = Button(footer,
                  text='Quit',
                  command=quit,
                  width=12,
                  relief='flat')
exit_btn.pack(side=RIGHT, padx=5, pady=5)
footer.pack(fill='x')


if __name__ == "__main__":
    window.title('Secret Key Generator')
    window.iconbitmap('app/key.ico')
    window.geometry('460x200')
    window.resizable(False, False)
    window.config(bg=PRIMARY_COLOR)
    window.mainloop()
