from lcu_driver import Connector
import os
from tkinter import *
from tkinter import filedialog


connector = Connector()


def get_league_path():
    master = Tk()
    master.withdraw()
    leaguedir = filedialog.askopenfilename(
        parent=master,
        initialdir=os.getcwd(),
        title="Please select your League of Legends Client executable",
        filetypes=[("Executable files", "*.exe")],
    )
    master.destroy()
    return leaguedir
    master.mainloop()


async def set_icon(connection):
    # random number of a chinese icon
    with open(configlocation, "r") as f:
        iconid = int(f.readlines()[1].strip())
    # make the request to set the icon
    icon = await connection.request("put", "/lol-chat/v1/me", data={"icon": iconid})

    # if HTTP status code is 201 the icon was applied successfully
    if icon.status == 201:
        print(f"Chinese icon number {iconid} was set correctly.")
    else:
        print("Unknown problem, the icon was not set.")
    await connector.stop()


# fired when LCU API is ready to be used
@connector.ready
async def connect(connection):

    # check if the user is already logged into his account
    summoner = await connection.request("get", "/lol-summoner/v1/current-summoner")
    if summoner.status != 200:
        raise
    else:
        await set_icon(connection)


# starts the connector
def main():
    with open(configlocation, "r") as f:
        os.startfile(f.readlines()[0].strip())
    connector.start()


try:
    newpath = os.path.join(os.environ.get("appdata"), "IDAutoChanger")
    configlocation = os.path.join(newpath, "config.txt")
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    open(configlocation, "x")
    with open(configlocation, "a") as f:
        f.write(get_league_path() + "\n" + "501")
    raise Exception
except (FileExistsError, Exception):
    while True:
        try:
            main()
            break
        except:
            pass
