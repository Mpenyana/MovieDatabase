from tkinter import *
import back_end

# Functions::::::::::::::::


def show_selected(event):
    index = li.curselection()
    global selected_film_id
    selected_film_id = li.get(index)[0]
    name.delete(0, END)
    name.insert(0, li.get(index)[1])
    release.delete(0, END)
    release.insert(0, li.get(index)[2])
    run.delete(0, END)
    run.insert(0, li.get(index)[3])


def view_command():
    li.delete(0, END)
    for all_movies in back_end.get_movies():
        li.insert(END, all_movies)


def add_command():
    success = '.... Was added to the database'
    try:
        if name_text.get().__len__() > 0 or release_text.get() > 0 or run_text.get() > 0:
            li.delete(0, END)
            back_end.adds(name_text.get(), release_text.get(), run_text.get())
            li.insert(END, (name_text.get(), release_text.get(), run_text.get(), success))
    except TypeError:
        pass


def delete_command():
    back_end.delete_item(selected_film_id)
    li.delete(0, END)
    li.insert(END, "Item was deleted")

def update_command():
    ini2 = li.curselection()
    information = li.get(ini2)
    back_end.updte(name.get(), release.get(), run.get(), information[0])

window = Tk()

window.wm_title("Movie Database")

# Labels::::::
n_label = Label(window, text='Name')
n_label.grid(row=0, column=1)
rel_label = Label(window, text='Release Date')
rel_label.grid(row=0, column=2)
run_label = Label(window, text='Run Time')
run_label.grid(row=0, column=3)

# Entries::::::
name_text = StringVar()
name = Entry(window, text=name_text)
name.grid(row=1, column=1)
release_text = StringVar()
release = Entry(window, text=release_text)
release.grid(row=1, column=2)
run_text = StringVar()
run = Entry(window, text=run_text)
run.grid(row=1, column=3)

# Buttons::::::::
view_button = Button(window, width=15, text='View Collection', background='pink', command=view_command)
view_button.grid(row=3, column=0)
add_button = Button(window, width=15, text='Add To List', background='pink', command=add_command)
add_button.grid(row=3, column=1)
delete_button = Button(window, width=15, text='Delete', background='pink', command=delete_command)
delete_button.grid(row=3, column=2)
update_button = Button(window, width=15, text='Update Info', background='pink', command= update_command)
update_button.grid(row=3, column=3)
close_button = Button(window, width=15, text='Exit', background='red', command=window.destroy)
close_button.grid(row=3, column=4)

# listBox::::::
li = Listbox(window, width=120, background='#9defd3')
li.grid(row=4, column=0, columnspan=5)
sbar = Scrollbar(window)
sbar.grid(row=4, column=6)

li.bind('<<ListboxSelect>>', show_selected)

window.mainloop()
