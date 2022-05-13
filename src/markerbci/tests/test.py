import os
import pathlib
import time
import sys

path_tests = pathlib.Path(__file__).parent.resolve()
sys.path.append(str(path_tests)[0:-5])

import buttonbox

bb = buttonbox.ButtonBoxBci(port="COM4")

bb.sendMarker(val=255)
time.sleep(1)
bb.sendMarker(val=255)
time.sleep(1)
bb.sendMarker(val=255)
time.sleep(1)
bb.sendMarker(val=255)
time.sleep(1)

bb.close()