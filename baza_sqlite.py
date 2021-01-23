from tkinter import *
#from PIL import ImageTK,Image
import sqlite3

# tutaj zmiana ostatnia do sprawdzenia - piatek 19:32
# xxx
# jeszcze jedna zmiana

root = Tk()
root.title('tytul aplikacji')
root.geometry("1024x1000")


# Create Submit Function For database
def submit():
    conn = sqlite3.connect('marek.db')
    c = conn.cursor()
    conn.commit()
    conn.close()
    # Clear The Text Boxes
    f_name.delete(0,END)
    f_imie.delete(0,END)
    f_dataur.delete(0,END)


# Create Query Function For database
def query():
    conn = sqlite3.connect('marek.db')
    c = conn.cursor()

    c.execute("SELECT *,id FROM user")
    records = c.fetchall()
    # print(records)

    # Loop Thru Results
    print_records = ''
    for record in records:
        print_records += str(record[1]) + " " + str(record[2]) + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=5, column=0, columnspan=2)


    conn.commit()
    conn.close()




# Create Text Boxes
f_name = Entry(root,width=30)
f_name.grid(row=0, column=1, padx=20)
f_imie = Entry(root,width=30)
f_imie.grid(row=1, column=1, padx=20)
f_dataur = Entry(root,width=30)
f_dataur.grid(row=2, column=1, padx=20)

# Create Text Box Labels
f_name_label = Label (root, text="Nazwisko")
f_name_label.grid(row=0, column=0)
f_imie_label = Label (root, text="Imie")
f_imie_label.grid(row=1, column=0)
f_dataur_label = Label (root, text="Data ur.")
f_dataur_label.grid(row=2, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Create Query Button
submit_btn = Button(root, text="Show Records", command=query)
submit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=137)








#query = c.execute('SELECT * FROM user')



root.mainloop()


# conn = sqlite3.connect('marek.db')

# cursor = conn.cursor()

# query = cursor.execute('SELECT * FROM user')

# results = query.fetchall()

# for xxx in results:
#     print(xxx[1] + " " + xxx[2])

