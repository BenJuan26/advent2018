import subprocess
import os

def get_input(day):
    try:
        file = open("{}.txt".format(day))
        return file.read()
    except FileNotFoundError:
        profiles_dir = os.path.expanduser(r"~/Library/Application\ Support/Firefox/Profiles")

        proc = subprocess.run(["ls {}".format(profiles_dir)], stdout=subprocess.PIPE, check=True, shell=True)
        profile = proc.stdout
        profile = profile.decode('ASCII').strip()

        cookies_dir = "{}/{}".format(profiles_dir, profile)

        subprocess.run(["cp {0}/cookies.sqlite {0}/cookies-copy.sqlite".format(cookies_dir)], check=True, shell=True)
        proc = subprocess.run(["echo \"SELECT value FROM moz_cookies WHERE baseDomain = 'adventofcode.com'\" | sqlite3 {}/cookies-copy.sqlite".format(cookies_dir)], stdout=subprocess.PIPE, shell=True, check=True)
        session = proc.stdout.decode('ASCII').strip()
        subprocess.run(["rm {}/cookies-copy.sqlite*".format(cookies_dir)], shell=True, check=True)

        proc = subprocess.run(["curl -s https://adventofcode.com/2018/day/{}/input --cookie session={}".format(day, session)], stdout=subprocess.PIPE, shell=True, check=True)
        data = proc.stdout.decode('ASCII').strip()

        file = open("{}.txt".format(day), "x")
        file.write(data)

        return data