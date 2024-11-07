from Interface.nadarAble import NadarAble
from Interface.respirarAble import RespirarAble


class Pez (NadarAble,RespirarAble):
    def nadar(self):
        print("Esteban está nadando")
    def respirar(self):
        print("Esteban está Respirando")