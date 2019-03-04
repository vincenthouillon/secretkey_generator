from datetime import datetime
from tkinter import *

import app.settings as constants
from app.generator import Generator


class SecretKeyGenerator:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Secret Key Generator')
        self.parent.iconbitmap('app/img/key.ico')
        self.parent.geometry('480x220')
        self.parent.minsize(480, 220)
        self.parent.config(bg=constants.BG_COLOR, padx=20)
        self.var_entry = StringVar()
        self.img_clipboard = PhotoImage(file='app/img/clipboard.png').subsample(2, 2)
        self.date = datetime.now()
        self.gen = Generator()
        self.initialize()

    def generate_flask(self):
        flask_key = str(self.gen.flask_generator())
        self.var_entry.set('')
        self.var_entry.set(flask_key)

    def generate_django(self):
        django_key = str(self.gen.django_generator())
        self.var_entry.set('')
        self.var_entry.set(django_key)

    def clipboard(self):
        self.parent.clipboard_clear()
        self.parent.clipboard_append(self.var_entry.get())

    def initialize(self):

        # HEADER
        pw_header = PanedWindow(bg=constants.BG_COLOR)
        pw_header.pack(fill='x')

        lbl_title = Label(pw_header,
                          text='Secret Key Generator',
                          font=(constants.FONT, 24),
                          bg=constants.BG_COLOR,
                          fg=constants.PRIMARY_COLOR,
                          anchor='w')
        lbl_title.pack(fill='x', pady=(10, 0))

        lbl_subtitle = Label(pw_header,
                             text='Secret Key Generator for Flask and Django made with Python 3.',
                             font=(constants.FONT, 11),
                             bg=constants.BG_COLOR,
                             fg=constants.FG_COLOR,
                             anchor='w')
        lbl_subtitle.pack(side=LEFT)
        pw_header.pack(fill='x')

        pw_form = PanedWindow(bg=constants.BG_COLOR)
        input_user = Entry(pw_form,
                           relief=FLAT,
                           bg='#DDDDDD',
                           font=(constants.FONT, 10))
        input_user.config(textvariable=self.var_entry)
        input_user.pack(fill='x', pady=(10,0))

        btn_flask = Button(pw_form, text='Generate a secret key for Flask',
                           width=26,
                           relief='flat',
                           command=self.generate_flask,
                           bg=constants.PRIMARY_COLOR)
        btn_flask.pack(pady=10, side=LEFT)

        btn_django = Button(pw_form, text='Generate a secret key for Django',
                            width=26,
                            relief='flat',
                            bg=constants.PRIMARY_COLOR,
                            command=self.generate_django)
        btn_django.pack(padx=14, pady=10, side=LEFT)

        btn_clipboard = Button(pw_form,
                               relief='flat',
                               bg=constants.PRIMARY_COLOR,
                               command=self.clipboard)
        
        btn_clipboard.config(image=self.img_clipboard, width=20, height=20)
        btn_clipboard.pack(side=RIGHT)
        pw_form.pack(fill='both')

        pw_footer = PanedWindow(bg=constants.BG_COLOR)
        lbl_copyright = Label(pw_footer, text=(f'Vincent Houillon - {self.date.year}'),
                              bg=constants.BG_COLOR,
                              fg=constants.SECONDARY_COLOR,
                              font=(constants.FONT, 7, 'bold'))
        lbl_copyright.pack(side=LEFT, padx=5)

        btn_border = Frame(pw_footer,
                           highlightbackground=constants.PRIMARY_COLOR,
                           highlightcolor=constants.PRIMARY_COLOR,
                           highlightthickness=2,
                           bg=constants.BG_COLOR,
                           bd=0)

        btn_quit = Button(btn_border,
                          text='Quit',
                          width=24,
                          height=1,
                          relief='flat',
                          border=0,
                          bg=constants.BG_COLOR,
                          highlightbackground=constants.BG_COLOR,
                          activebackground=constants.PRIMARY_COLOR,
                          command=quit)

        btn_border.pack(side=RIGHT, pady=10)
        btn_quit.pack(side=RIGHT, padx=0, pady=0)
        pw_footer.pack(fill='x', side=BOTTOM)


if __name__ == "__main__":
    root = Tk()
    app = SecretKeyGenerator(root)
    root.mainloop()
