from lcu_driver import Connector
import os
import time
import json

connector = Connector()


def parse_config():
    return [
        request for request in json.loads(open("config.json", "r").read())["requests"]
    ]


def check_config():
    if os.path.isfile("config.json"):
        return True


async def send_request(connection, endpoint, method, body):
    response = await connection.request(
        method,
        endpoint,
        data=body,
    )
    if response.status == 201:
        print(
            f"Custom request sent:\nEndpoint: {endpoint}\nMethod: {method}\nBody: {body}\n"
        )
    else:
        print(
            f"Unknown problem, Custom request could not be sent.\nStatus Code: {response.status}"
        )


@connector.ws.register("/lol-loot/v1/ready", event_types=("UPDATE",))
async def connect(connection, event):
    for request in parse_config():
        await send_request(
            connection, request["endpoint"], request["method"], request["body"]
        )
    print("Finished sending requests.")


def main():
    if check_config():
        connector.start()
    else:
        os.system("python settings.py")
        exit("No configuration file detected. Opening Settings...")


main()
