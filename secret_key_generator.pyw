from datetime import datetime
from tkinter import *
from tkinter import colorchooser, messagebox

from app.config import UserSettings
from app.generator import Generator


class SecretKeyGenerator:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Secret Key Generator')
        self.user_settings = UserSettings.get_settings()
        if (sys.platform.startswith('win')):
            self.parent.iconbitmap('app/img/icon.ico')
            self.parent.minsize(480, 240)
            self.FONT = 'Segoe UI'
        else:
            logo = PhotoImage(file='app/img/icon.gif')
            self.parent.call('wm', 'iconphoto', self.parent._w, logo)
            self.parent.minsize(580, 220)
            self.FONT = 'Droid Sans Mono'
        self.parent.config(bg=self.user_settings['BG_COLOR'], padx=20)
        self.var_entry = StringVar()
        self.img_clipboard = PhotoImage(
            file='app/img/clipboard.png').subsample(2, 2)
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

    def set_mode(self, event):
        mode = messagebox.askokcancel(title='choice mode',
                                      message='Confirm the change mode?')
        if mode:
            if self.user_settings['MODE'] == 'light':
                UserSettings.write_settings('mode', 'dark')
                refresh()
            else:
                UserSettings.write_settings('mode', 'light')
                refresh()

    def set_color(self, event):
        color = colorchooser.askcolor(initialcolor='#e74c3c',
                                      title='Color accent')
        UserSettings.write_settings('accent_color', color[1])
        refresh()

    def initialize(self):
        # SETTINGS
        pw_settings = PanedWindow(
            self.parent, bg=self.user_settings['BG_COLOR'])
        pw_settings.pack(fill='x')

        lbl_settings = Label(pw_settings, text='accent color',
                             bg=self.user_settings['BG_COLOR'],
                             fg=self.user_settings['ACCENT_COLOR'],
                             font=(self.FONT, 7, 'bold'))
        lbl_settings.bind('<Button-1>', self.set_color)
        lbl_settings.pack(side=RIGHT)

        lbl_mode = Label(pw_settings, text=f"mode: {self.user_settings['MODE']}",
                         bg=self.user_settings['BG_COLOR'],
                         fg=self.user_settings['CR_COLOR'],
                         font=(self.FONT, 7, 'bold'))
        lbl_mode.bind('<Button-1>', self.set_mode)
        lbl_mode.pack(side=RIGHT, padx=5)

        # HEADER
        pw_header = PanedWindow(bg=self.user_settings['BG_COLOR'])
        pw_header.pack(fill='x')

        lbl_title = Label(pw_header,
                          text='Secret Key Generator',
                          font=(self.FONT, 24),
                          bg=self.user_settings['BG_COLOR'],
                          fg=self.user_settings['ACCENT_COLOR'],
                          anchor='w')
        lbl_title.pack(fill='x', pady=(5, 0))

        lbl_subtitle = Label(pw_header,
                             text='Secret Key Generator for Flask and Django made with Python 3.',
                             font=(self.FONT, 11),
                             bg=self.user_settings['BG_COLOR'],
                             fg=self.user_settings['FG_COLOR'],
                             anchor='w')
        lbl_subtitle.pack(side=LEFT)
        pw_header.pack(fill='x')

        # FORM
        pw_form = PanedWindow(bg=self.user_settings['BG_COLOR'])
        input_user = Entry(pw_form,
                           relief=FLAT,
                           bg='#DDDDDD',
                           font=(self.FONT, 10))
        input_user.config(textvariable=self.var_entry)
        input_user.pack(fill='x', pady=(10, 0))

        btn_flask = Button(pw_form, text='Generate a secret key for Flask',
                           width=26,
                           relief=FLAT,
                           command=self.generate_flask,
                           bg=self.user_settings['ACCENT_COLOR'])
        btn_flask.pack(pady=10, side=LEFT)

        btn_django = Button(pw_form, text='Generate a secret key for Django',
                            width=26,
                            relief=FLAT,
                            bg=self.user_settings['ACCENT_COLOR'],
                            command=self.generate_django)
        btn_django.pack(padx=14, pady=10, side=LEFT)

        btn_clipboard = Button(pw_form,
                               relief=FLAT,
                               bg=self.user_settings['ACCENT_COLOR'],
                               command=self.clipboard)

        btn_clipboard.config(image=self.img_clipboard, width=20, height=20)
        btn_clipboard.pack(side=RIGHT)
        pw_form.pack(fill='both')

        # FOOTER
        pw_footer = PanedWindow(bg=self.user_settings['BG_COLOR'])
        lbl_copyright = Label(pw_footer, text=(f'Vincent Houillon ({self.date.year})'),
                              bg=self.user_settings['BG_COLOR'],
                              fg=self.user_settings['CR_COLOR'],
                              font=(self.FONT, 7, 'bold'))
        lbl_copyright.pack(side=LEFT, padx=5)

        btn_border = Frame(pw_footer,
                           highlightbackground=self.user_settings['ACCENT_COLOR'],
                           highlightcolor=self.user_settings['ACCENT_COLOR'],
                           highlightthickness=2,
                           bg=self.user_settings['BG_COLOR'],
                           bd=0)

        btn_quit = Button(btn_border,
                          text='Quit',
                          width=24,
                          height=1,
                          relief=FLAT,
                          border=0,
                          bg=self.user_settings['BG_COLOR'],
                          highlightbackground=self.user_settings['BG_COLOR'],
                          activebackground=self.user_settings['ACCENT_COLOR'],
                          fg=self.user_settings['FG_COLOR'],
                          command=quit)

        btn_border.pack(side=RIGHT, pady=10)
        btn_quit.pack(side=RIGHT, padx=0, pady=0)
        pw_footer.pack(fill='x', side=BOTTOM)


def main():
    global root
    root = Tk()
    app = SecretKeyGenerator(root)
    root.mainloop()


if __name__ == "__main__":
    def refresh():
        root.destroy()
        main()
    main()
