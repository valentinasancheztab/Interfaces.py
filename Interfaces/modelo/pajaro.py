from Interface.respirarAble import RespirarAble
from Interface.terrestreAble import TerrestreAble
from Interface.volarAble import VolarAble


class Pajaro (VolarAble,TerrestreAble,RespirarAble):
    def volar(self):
        print('Pablo vuela')
    def respirar(self):
        print('Pablo respira')
    def terrestre(self):
        print('Pablo se desplaza')