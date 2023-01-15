from tkinter import *
import pymysql
import main_menu

def register():
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
    window.geometry('300x300')
    window.title('Player Registration')

    # alertbox
    def alert_window(title, message):
        alert_box = Tk()
        center(alert_box)
        alert_box.title(title)
        #alert_box.iconbitmap(r'Images/chocolatei.ico')  # icon here r->raw string
        alert_box.geometry('250x90')

        def terminate():
            alert_box.destroy()

        alert_label = Label(alert_box, text=message, bg="black", fg="white").place(x=45, y=20)
        alert_button = Button(alert_box, text="  OK  ", activeforeground="white", activebackground="black",
                              command=terminate).place(x=110, y=50)
        alert_box.mainloop()

    # Submit Function
    def submit():
        db = pymysql.connect("localhost", "user", "password10", "choco_run", 3306)
        # prepare a cursor object using cursor() method
        cursor = db.cursor()
        sql = "INSERT INTO users(Player_name,Password, name)  VALUES ('%s', '%s', '%s')" % (
            e2.get(), e3.get(), e1.get())
        check_new = "SELECT Player_name FROM users WHERE Player_name ='%s'" % (e2.get())
        name=e2.get()
        try:
            # Execute the SQL command
            cursor.execute(check_new)
            result = cursor.rowcount
            value = cursor.fetchall()
            if result == 0:
                cursor.execute(sql)
                # Commit your changes in the database
                db.commit()
                window.destroy()
                main_menu.start_menu(name)
            else:
                window.destroy()
                alert_window("INVALID", "PLAYER   ALREADY   EXISTS ")
        except:
            # Rollback in case there is any error
            db.rollback()
            window.destroy()

    name = Label(window, text="Name", bg="black", fg="white").place(x=30, y=50)  # e1
    player_name = Label(window, text="Player Name", bg="black", fg="white").place(x=20, y=100)  # e2
    password = Label(window, text="Password", bg="black", fg="white").place(x=30, y=150)  # e3
    e1 = Entry(window)
    e1.place(x=110, y=50)
    e2 = Entry(window)
    e2.place(x=110, y=100)
    e3 = Entry(window, show='*')
    e3.place(x=110, y=150)
    submit_btn = Button(window, text="Submit", activeforeground="white",
                        activebackground="black", command=submit).place(x=130, y=200)

    window.mainloop()
