import re, os
from time import sleep
import subprocess


def get_wlan_ip():
    print('scripts.py : check_wifi start')
    cmd = "ifconfig wlan0 | awk '$1 ~ /^inet/ {print $2}'"
    cmd += "| awk '$1 ~/^[1-9]/ {print $0}'"
    ip_addr = os.popen(cmd).read()
    print(ip_addr.split('\n'))
    return ip_addr.split('\n')[0]


def get_ssid_list():
    MyOut = subprocess.Popen(['sudo', 'sh', os.path.dirname(os.path.abspath(__file__)) + '/shell_scripts/scan_ssid.sh', '.'],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT)
    stdout,stderr = MyOut.communicate()
    string = stdout.decode()
    print(stderr)

    # if character has unicode(UTF-8)
    numbers = re.findall('\\\\x[0-9a-fA-F][0-9a-fA-F]', string)
    if len(numbers) > 0:
        byte_string = b''
        for n in numbers:
            sp = string.split(n, 1)
            if sp[0] != '':
                byte_string += sp[0].encode('utf-8')
            string = sp[1]
            print("n" + n)
            byte_string += string_to_hex(n).to_bytes(1, byteorder='big')
        byte_string += string.encode('utf-8')
        print(byte_string.decode())
        return byte_string.decode()
    else:
        print(stdout.decode())
        return stdout.decode()


def string_to_hex(str):
    if len(str) != 4:
        return str
    elif str[:2] != '\\x':
        return str
    else:
        f = char_to_hexnumber(str[2])
        s = char_to_hexnumber(str[3])
        if f is not None and s is not None:
            return f*16+s
        else:
            return str


def char_to_hexnumber(ch):
    if re.match('[0-9]',ch):
        return int(ch)
    elif re.match('[a-f]',ch):
        return ord(ch)-87
    elif re.match('[A-F]',ch):
        return ord(ch)-55
    elif True:
        return None


def check_wifi():
    print('scripts.py : check_wifi start')
    ssid = os.popen("sudo iwconfig wlan0 | grep 'ESSID' \
                    | awk -F\\\" '{print$2}'").read().replace("\n","")
    print(ssid)
    print("done")

    numbers = re.findall('\\\\x[0-9a-fA-F][0-9a-fA-F]', ssid)

    # if character has unicode(UTF-8)
    if len(numbers) > 0:
        byte_string = b''
        for n in numbers:
            sp = ssid.split(n, 1)
            if sp[0] != '':
                byte_string += sp[0].encode('utf-8')
            ssid = sp[1]
            byte_string += string_to_hex(n).to_bytes(1, byteorder='big')
        byte_string += ssid.encode('utf-8')
        print(byte_string.decode())
        ssid = byte_string.decode()

    if len(ssid) <= 1:
        MyOut2 = subprocess.Popen(['sudo', 'killall', 'dhclient'])

        return False, "None"
    return True, ssid
    print('scripts.py : check_wifi end')


if __name__ =='__main__':
    # print(get_wlan_ip())
    get_ssid_list()
    # check_wifi()