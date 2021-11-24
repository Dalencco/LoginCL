import hashlib

class Main:
    def __init__(self):
        usuario = str(input('Ingrese su Nombre de Usuario: '))
        usuarioof = self.scrypt(usuario)
        contraseña = str(input('Ingrese su contraseña: '))
        contraseñaof = self.scrypt(contraseña)
        if self.login(usuario=usuarioof, contraseña=contraseñaof):
            print(f'Inicio de Sesion Correcto con: {usuario}, con los permisos de: {Permiso}')
        else:
            print('Usuario/Contraseña Incorrecta')

    def login(self, usuario, contraseña):
        global Usuarios
        Usuarios = {
            'Usuarios': {
                b'\xca`\xdd\x18\xcdAM\xb6\x15!\x9eGi\xab\x81KTy~\xa8"\xca\xfd\x8f!6\xdb\x94w\x89\xd3B=\xbb\xb9\xed\xee\xa3\x98x\x0f=\x8bx\xfcN\xadmR\xbf\xcb\xc6\xe2tsS&\xc3\x85\x18\xaeW\x01\t': {
                    'Contraseña': b's\xe2rq{}\xb7\x01\x8d\xecm8\x93\xf7\xf5R>[\xf2i\xf1>\x04Und\xbcZ\xe8P\xa4\x8f\xfe\xa5\xfcG\xaf\xcaGt\xfay>\x815\xb4\x9d\x05+\x9e}F\xe8X\x04\xd4\xa01|\xbd^\x03^%',
                    'Permisos': 'root'
                },
                b'J\x16\x1f\xe5\xc9\xdb\xec\x1c\x11\x99@\xe1x5\xf1\xc0b#\xc6\xc2\x07\xfe\xa2\x06\x12\xf8\xe9\xcc\xf2\xc0\x88\x8ey\x9a\x9f\x1ckw\x8b\xa3\xf9V\x9e\x7fg\x03\xe4\xc8a\x02w\xbc\xf3\xb1\xb6Q:&nZ\xaeKX\xb1': {
                    'Contraseña': b'J\x16\x1f\xe5\xc9\xdb\xec\x1c\x11\x99@\xe1x5\xf1\xc0b#\xc6\xc2\x07\xfe\xa2\x06\x12\xf8\xe9\xcc\xf2\xc0\x88\x8ey\x9a\x9f\x1ckw\x8b\xa3\xf9V\x9e\x7fg\x03\xe4\xc8a\x02w\xbc\xf3\xb1\xb6Q:&nZ\xaeKX\xb1',
                    'Permisos': 'user'
                }
            }
        }

        if usuario in Usuarios['Usuarios']:
            if contraseña == Usuarios['Usuarios'][usuario]['Contraseña']:
                global Permiso
                Permiso = Usuarios['Usuarios'][usuario]['Permisos']
                return True
            else:
                return False
        else:
            return False

    def scrypt(self, txt):
        texto = bytes(txt, 'utf-8')
        cifrado = hashlib.scrypt(texto, salt=b'salt', n=2, r=8, p=1)
        return cifrado

if __name__ == '__main__':
    Main()