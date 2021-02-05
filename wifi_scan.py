import subprocess
# import re
# from time import sleep


def scan_wifi():

    proc = subprocess.Popen("sudo iwlist wlan0 scan | fgrep -B 3 ESSID | cut -d ':' -f 2 | awk '{print$1}'", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    output = stdout.decode()

    list = dict()
    #if error
    if(stderr != b''):
        list['error'] = stderr.decode()
        return list

    for text in output.split('--'):
        line = text.split('\"')
        info = line[0].split()
        ssid = line[1]

        # # if character has unicode(UTF-8)
        # numbers = re.findall('\\\\x[0-9a-fA-F][0-9a-fA-F]', ssid)
        # if len(numbers) > 0:
        #     byte_string = b''
        #     for n in numbers:
        #         sp = string.split(n, 1)
        #         if sp[0] != '':
        #             byte_string += sp[0].encode('utf-8')
        #         string = sp[1]
        #         byte_string += string_to_hex(n).to_bytes(1, byteorder='big')
        #     byte_string += string.encode('utf-8')
        #     ssid = byte_string.decode()

        #frequency parsing
        info[0] = info[0].split('.')[0]
        #quality parsing
        info[1] = info[1].split('=')[1].split('/')[0]

        #if same ssid, different frequency(2g, 5g)
        if ssid in list and list[ssid][0] != info[0]:
            ch_ssid = ssid + '_5G'
            if list[ssid][0] == '5':
                list[ch_ssid] = list[ssid]
            elif info[0] == '5':
                ssid = ch_ssid

        list[ssid] = info

    #sorting by quality
    list = dict(sorted(list.items(), reverse=True, key=lambda x: x[1][1]))
    
    return list


# def string_to_hex(str):
#     if len(str) != 4:
#         return str
#     elif str[:2] != '\\x':
#         return str
#     else:
#         f = char_to_hexnumber(str[2])
#         s = char_to_hexnumber(str[3])
#         if f is not None and s is not None:
#             return f*16+s
#         else:
#             return str


# def char_to_hexnumber(ch):
#     if re.match('[0-9]',ch):
#         return int(ch)
#     elif re.match('[a-f]',ch):
#         return ord(ch)-87
#     elif re.match('[A-F]',ch):
#         return ord(ch)-55
#     elif True:
#         return None
    