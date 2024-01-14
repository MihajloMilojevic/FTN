from sys import platform
import os

def get_desktop(): 
    if platform == "win32":
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    else:
        desktop = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop') 
    return desktop