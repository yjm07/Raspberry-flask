import subprocess
from time import sleep


def num_modi_in_usb():

    proc = subprocess.Popen("lsusb | grep 2fde:0002", 
                             shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    output = stdout.decode()

    # if error
    if stderr != b'':
        return stderr.decode()

    if len(output) == 0:
        return 0

    _list = output.split("\n")
    return len(_list) - 1


def print_modi_list():

    num = num_modi_in_usb()

    if num <= 0: return
    
    import modi

    bundle_list = []
    for i in range(num):
        bundle = modi.MODI()
        bundles = bundle.modules
        bundle_list.append(bundles)
    print (bundle_list)