import os
import logging as log

log.info("LaTeX Project Cleaner")
rd = input("LaTeX project root directory: ")

for dirpath, dirnames, filenames in os.walk(rd):
    for filename in [f for f in filenames if f.endswith(".aux")]:
        os.remove(os.path.join(dirpath, filename))