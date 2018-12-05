import subprocess
import os
import platform
import sqlite3
import shutil
import requests

def get_input(day):
    try:
        file = open("{}.txt".format(day))
        return file.read()
    except FileNotFoundError:
        return download_input(day)

def download_input(day):
    sys = platform.system()
    firefox_dir = ""
    if sys == "Windows":
        appdata = os.getenv("APPDATA")
        firefox_dir = os.path.join(appdata, "Mozilla", "Firefox", "Profiles")
    elif sys == "Darwin":
        firefox_dir = os.path.expanduser(os.path.join("~", "Library", "Application Support", "Firefox", "Profiles"))

    dirs = os.listdir(firefox_dir)
    profile = dirs[0]

    profile_dir = os.path.join(firefox_dir, profile)
    cookies_orig = os.path.join(profile_dir, "cookies.sqlite")
    cookies_file = os.path.join(profile_dir, "cookies-copy.sqlite")

    shutil.copy(cookies_orig, cookies_file)

    conn = sqlite3.connect(cookies_file)
    cur = conn.cursor()
    cur.execute("SELECT value FROM moz_cookies WHERE baseDomain = 'adventofcode.com'")
    results = cur.fetchall()
    session = results[0][0]

    conn.close()
    os.remove(cookies_file)

    url = "https://adventofcode.com/2018/day/{}/input".format(day)
    cookies = {"session":session}
    resp = requests.get(url, cookies=cookies)
    data = resp.text.strip()

    file = open("{}.txt".format(day), "x")
    file.write(data)

    return data
