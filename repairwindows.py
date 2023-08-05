import os
from time import sleep
import pyuac

def main():
    command_sfc= 'sfc /scannow'
    command_DISM1 = 'DISM /Online /Cleanup-Image /CheckHealth'
    command_DISM2 = 'DISM /Online /Cleanup-Image /ScanHealth'
    command_DISM3 = 'DISM /Online /Cleanup-Image /RestoreHealth'
    command_chkdsk = 'CHKDSK /f /r /x'

    os.system(command_sfc)
    sleep(1)
    os.system(command_DISM1)
    sleep(1)
    os.system(command_DISM2)
    sleep(1)
    os.system(command_DISM3)
    sleep(1)
    os.system(command_chkdsk)

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        sleep(3)
        pyuac.runAsAdmin()
    else:
        main()










