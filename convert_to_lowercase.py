import os
from itertools import chain
from glob import glob

directory = './'

for filename in os.listdir(directory):
    if filename.endswith(".md"):
        f = open(filename, 'r')
        text = f.read()
        
        lines = [text.lower() for line in filename]
        print((lines[0][0]))
        with open(filename, 'w') as out:
            out.writelines(lines)