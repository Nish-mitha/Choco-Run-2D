from tkinter import *
import pymysql
import main_menu

def login():
    window = Tk()
    window.title('Chocolate Run')  # Title
    #window.iconbitmap(r'Images/chocolatei.ico')  # icon here r->raw string
    def center(root):
        root.configure(bg='black')
        # position the window to center
        width = root.winfo_reqwidth()
        height = root.winfo_reqheight()
        right = int(root.winfo_screenwidth() / 2 - width / 2)
        down = int(root.winfo_screenheight() / 2 - height / 2)
        root.geometry('+{}+{}'.format(right - 100, down - 100))

    center(window)
    window.geometry('300x200')
    window.title('Player Login')

    # alertbox
    def alert_window(title, message):
        alert_box = Tk()
        center(alert_box)
        #alert_box.iconbitmap(r'Images/chocolatei.ico')  # icon here r->raw string
        alert_box.title(title)
        alert_box.geometry('250x90')

        def terminate():
            alert_box.destroy()

        alert_label = Label(alert_box, text=message, bg="black", fg="white").place(x=1, y=20)
        alert_button = Button(alert_box, text="  OK  ", activeforeground="white", activebackground="black",
                              command=terminate).place(x=110, y=50)
        alert_box.mainloop()

    # Submit Function
    def submit():
        db = pymysql.connect("localhost", "user", "password10", "choco_run", 3306)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        check_play = "SELECT Player_name,Password FROM users WHERE Player_name ='%s' AND Password='%s'" %(e1.get(),e2.get())
        name=e1.get()
        try:
            # Execute the SQL command
            cursor.execute(check_play)
            result = cursor.rowcount
            if result == 1:
                # Commit your changes in the database
                db.commit()
                window.destroy()
                main_menu.start_menu(name)
            else:
                window.destroy()
                alert_window("INVALID", "PLAYER NAME OR PASSWORD IS INCORRECT")
        except:
            # Rollback in case there is any error
            db.rollback()
            window.destroy()

    player_name = Label(window, text="Player Name", bg="black", fg="white").place(x=20, y=50)  # e1
    password = Label(window, text="Password", bg="black", fg="white").place(x=30, y=100)  # e2
    e1 = Entry(window)
    e1.place(x=110, y=50)
    e2 = Entry(window,show='*')
    e2.place(x=110, y=100)
    submit_btn = Button(window, text="LOGIN", activeforeground="white",
                        activebackground="black", command=submit).place(x=130, y=140)

    window.mainloop()
