import os
from time import sleep
import pyuac

def main():
    command = 'winget upgrade --accept-source-agreements --all --include-unknown --silent'
    os.system(command)

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        sleep(3)
        pyuac.runAsAdmin()
    else:
        main()
        print("This windows will close in 10 seconds!")
        sleep(10)