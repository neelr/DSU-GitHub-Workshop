import os

for name in os.listdir('names'):
    print(name.strip('.txt'))