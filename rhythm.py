from midi import MidiConnector

serial_path = input("Please specify a serial input (i.e. serial0): ")

def specify_midi_port(arg):
    port = '/dev/' + str(arg)
    return port

midi_device = specify_midi_port(serial_path)
conn = MidiConnector(str(midi_device), timeout = 5)

def major_scale(key)
    pass
def minor_scale(key)
    pass
class phyrigian
    pass
class ionian
    pass
class dorian
    pass
class locrian
    pass
    
