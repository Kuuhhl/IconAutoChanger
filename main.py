from lcu_driver import Connector
import os

connector = Connector()


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
    print("LCU API is ready to be used.")

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
    configlocation = os.environ.get("appdata") + "\\IDAutoChanger\\config.txt"
    newpath = os.environ.get("appdata") + "\\IDAutoChanger"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    open(configlocation, "x")
    with open(configlocation, "a") as f:
        f.write(
            input("Path to League installation: ") + "\n" + str(int(input("Icon ID: ")))
        )
    raise Exception
except (FileExistsError, Exception):
    while True:
        try:
            main()
            break
        except:
            pass
