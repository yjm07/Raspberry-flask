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

    _list = output.rstrip('\n').split('\n')
    return len(_list)




def print_modi_list():

    num = num_modi_in_usb()

    if num <= 0: return
    
    import modi

    bundle_list = list()
    for i in range(num):
        print(i)
        bundle = modi.MODI()
        bundles = bundle.modules
        for m in bundles:
            if not m.is_up_to_date:
                bundle_list.append((print(m), m.version))
    print (bundle_list)
    
    for b in range(num):
        bundle.close()

