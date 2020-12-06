from tkinter import *
from tkinter.messagebox import *
import json
from tkinter import ttk
import os

CONFIG_PATH = os.path.join(
    os.path.join(os.environ.get("appdata"), "IconAutoChanger"), "config.json"
)


def get_requests():  # returns list of requests in config
    return [
        request for request in json.loads(open(CONFIG_PATH, "r").read())["requests"]
    ]


def rearrange(config, title, direction):  # True = up; #False = down
    for count, request in enumerate(config):
        if request["title"] == title:
            if direction == True and count != 0:
                config.pop(count)
                config.insert(count - 1, request)
            if direction == False and count != len(config):
                config.pop(count)
                config.insert(count + 1, request)
            break
    update_config(config)
    listbox_update()


def listbox_update():  # update listbox
    listboxRequests.delete(0, END)
    for request in get_requests():
        listboxRequests.insert("end", request["title"])


def update_config(config):  # Make changes to config
    config = {"requests": config}

    with open(CONFIG_PATH, "w") as f:
        f.write(json.dumps(config, indent=4))
    return


def search_value(key, value):  # search for request value in config
    for request in get_requests():
        if request[key] == value:
            return request


def ClickNew(config):  # append new item with default values
    suffix = 0
    while True:
        try:
            suffix += 1
            for request in config:
                if request["title"] == "title" + str(suffix):
                    raise TitleAlreadyExistsError(
                        "Title already exists. Duplicates are not allowed."
                    )
            break
        except:
            pass
    config.append(
        {
            "title": "title" + str(suffix),
            "endpoint": "",
            "method": "post",
            "body": {"": ""},
        }
    )
    update_config(config)
    listbox_update()
    showinfo(title="Success", message="Added request successfully.")


def ClickDelete(config, title):  # remove selected item
    for request in config:
        if request["title"] == title:
            config.remove(request)
            break
    update_config(config)
    listbox_update()


def ClickApply(beforetitle, title, endpoint, method, body):  # apply changes to item
    config = get_requests()
    for request in config:
        if request["title"] == title and title != beforetitle:
            showerror(
                title="Error",
                message=f'The title "{title}" already exists. Please use a different one.',
            )
            return
    for request in config:
        if request["title"] == beforetitle:
            config.remove(request)
            break
    config.append(
        {"title": title, "endpoint": endpoint, "method": method, "body": body}
    )
    update_config(config)
    listbox_update()
    showinfo(title="Success", message="Applied changes successfully.")


def Edit(event):  # Show Edit Frame
    selectedTitle = listboxRequests.get(event.widget.curselection()[0])
    editFrame = Frame(tkFenster)
    editFrame.grid(row=0, column=2)
    # Entry Title
    Label(master=editFrame, text="Title:").grid(row=0, column=0)
    titleEntry = Entry(master=editFrame)
    titleEntry.insert(END, selectedTitle)
    titleEntry.grid(row=0, column=1)
    # Entry Endpoint
    Label(master=editFrame, text="Endpoint:").grid(row=1, column=0)
    endpointEntry = Entry(master=editFrame)
    endpointEntry.insert(END, search_value("title", selectedTitle)["endpoint"])
    endpointEntry.grid(row=1, column=1)
    # Entry Method
    Label(master=editFrame, text="Method:").grid(row=2, column=0)
    n = StringVar()
    methodEntry = ttk.Combobox(editFrame, textvariable=n, state="readonly")
    methodEntry["values"] = (
        "GET",
        "POST",
        "PUT",
        "GET",
        "PATCH",
        "DELETE",
    )
    methodEntry.grid(row=2, column=1)
    for x in range(len(methodEntry["values"])):
        if methodEntry["values"][x] == search_value("title", selectedTitle)["method"]:
            methodEntry.current(x)
            break

    # Entry Body
    Label(master=editFrame, text="Body:").grid(row=3, column=0)
    bodyEntry = Text(editFrame, height=20, width=130)
    bodyEntry.insert(
        END,
        json.dumps(
            search_value("title", selectedTitle)["body"], sort_keys=True, indent=4
        ),
    )
    bodyEntry.grid(row=3, column=1)
    # Apply Button
    Button(
        master=tkFenster,
        text="Apply",
        command=lambda: ClickApply(
            listboxRequests.get(event.widget.curselection()[0]),
            titleEntry.get(),
            endpointEntry.get(),
            methodEntry.get(),
            json.loads(bodyEntry.get("1.0", "end-1c")),
        ),
    ).grid(row=1, column=2)
    editFrame.mainloop()


# Creation of root window
tkFenster = Tk()
tkFenster.geometry("1300x500")
tkFenster.iconbitmap("settingsicon.ico")
tkFenster.lift()
tkFenster.title("Settings Changer")


# Listbox of Requests
listboxRequests = Listbox(master=tkFenster, selectmode="browse", exportselection=False)
for request in get_requests():
    listboxRequests.insert("end", request["title"])
listboxRequests.grid(row=0, column=0)
listboxRequests.bind("<<ListboxSelect>>", Edit)
# Buttons
buttonFrame = Frame(master=tkFenster)
buttonFrame.grid(row=0, column=1)
addButton = Button(
    master=buttonFrame, text=" + ", command=lambda: ClickNew(get_requests())
)
addButton.grid(row=1, column=0)
deleteButton = Button(
    master=buttonFrame,
    text=" - ",
    command=lambda: ClickDelete(
        get_requests(), listboxRequests.get(listboxRequests.curselection()[0])
    ),
)
deleteButton.grid(row=2, column=0)
upButton = Button(
    master=buttonFrame,
    text=" ▲ ",
    command=lambda: rearrange(
        get_requests(), listboxRequests.get(listboxRequests.curselection()[0]), True
    ),
)
upButton.grid(row=0, column=0)
downButton = Button(
    master=buttonFrame,
    text=" ▼ ",
    command=lambda: rearrange(
        get_requests(), listboxRequests.get(listboxRequests.curselection()[0]), False
    ),
)

downButton.grid(row=3, column=0)
# mainloop
tkFenster.mainloop()