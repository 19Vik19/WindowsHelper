import os

command = 'winget upgrade --accept-source-agreements --all --include-unknown --silent'
os.system(command)