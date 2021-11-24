import os

try:
    import sourcedefender
    import cifrado
except ModuleNotFoundError:
    os.system('pip3 install -r requirements.txt')