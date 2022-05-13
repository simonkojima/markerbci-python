from markerbci import buttonbox
import time

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