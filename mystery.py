import os
import subprocess

for name in reversed(os.listdir('sus_folder')):
    result = subprocess.run(["python", os.path.join('sus_folder', name)], capture_output=True, text=True).stdout
    if result == "":
        result = f"script failed :("
    print(f'Name: {name}')
    print(f'Result: {result}')
    print('\n')
