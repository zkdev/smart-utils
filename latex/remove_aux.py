import os
import common.ezlog as ezlog

logger = ezlog.get_logger()

rd = input("LaTeX project root directory: ")

logger.info('removing aux files')
for dirpath, dirnames, filenames in os.walk(rd):
    for filename in [f for f in filenames if f.endswith(".aux")]:
        os.remove(os.path.join(dirpath, filename))
logger.info('aux files removed')
