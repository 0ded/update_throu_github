import sys
import os
import requests
import utils
import json


def get_remote_ver():
    return json.loads(requests.get(utils.get_json("config_update.json")["git_link_ver"]).text)["ver"]


def get_local_ver():
    return utils.get_json("version.json")["ver"]


def backup():
    try:
        os.mkdir("bku")
    except(FileExistsError):
        pass
    link = utils.get_json("config_update.json")["git_link"]
    ignores = utils.get_json("config_update.json")["ignore"]
    for i in ignores:
        os.replace(i, "bku/" + i)
    os.system("git clone " + link + "./remote")
    for i in os.listdir("./remote"):
        try:
            os.replace("remote/" + i, i)
        except(PermissionError):
            pass
    for i in ignores:
        os.replace("bku/" + i, i)
    os.rmdir("bku")
    os.rmdir("remote")



backup()
