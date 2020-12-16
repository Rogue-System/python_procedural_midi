from midi import midicontroller
default = serial0
conn = midicontroller('dev' + str(raw_input(default)))
