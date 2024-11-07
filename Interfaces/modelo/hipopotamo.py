from Interface.nadarAble import NadarAble
from Interface.respirarAble import RespirarAble
from Interface.terrestreAble import TerrestreAble


class Hipopotamo (RespirarAble,NadarAble,TerrestreAble):
    def respirar(self):
        print('Lucas respira')
    def nadar(self):
        print('Lucas nada')
    def terrestre(self):
        print('Lucas se desplaza ')
