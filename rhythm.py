from midi import MidiConnector
serial_path = input("Please specify a serial input (i.e. serial0): ")
def specify_midi_port(arg):
    port = 'dev/' + str(arg)
    return port
    print(port)
midi_device = specify_midi_port(serial_path)
conn = MidiConnector(str(midi_device), timeout = 5)
