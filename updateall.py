import os

def main():
    command = 'winget upgrade --accept-source-agreements --all --include-unknown --silent'
    os.system(command)

if __name__ == "__main__":
    main()