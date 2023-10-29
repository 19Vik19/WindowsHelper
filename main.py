import os

def main():
    while True:
        print("WindowsOptimizerTool:")
        print("1. Update all Programs       winget")
        print("2. Repair Windows            sfc /scannow + DISM + CHKDSK")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            os.system("python updateall.py")
        elif choice == "2":
            os.system("python repairwindows.py")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
