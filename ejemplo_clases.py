from copy import deepcopy

#motor
class motor:
    def __init__(self, potencia,
                 cilindros_motor):
        self.potencia = potencia
        self.cilindros_motor = cilindros_motor

class llanta:
    def __init__(self, tamanno,
                 color_llanta):
        self.tamanno = tamanno
        self.color_llanta = color_llanta

class asientos:
    def __init__(self,material_asiento,
                 color_asiento):
        self.material_asiento = material_asiento
        self.color_asiento = color_asiento

class carro(object):
    def __init__(self, potencia,
                 cilindros_motor,
                 tamanno,
                 color_llanta,
                 material_asiento,
                 color_asiento
                 ):
        self.el_motor = motor(potencia,cilindros_motor)
        self.la_llanta = llanta(tamanno, color_llanta)
        self.el_asiento = asientos(material_asiento, color_asiento)

    def __eq__(self, other):
        return self.el_motor.cilindros_motor == other.el_motor.cilindros_motor

    def __add__(self, other):
        potencia_final = self.el_motor.potencia + other.el_motor.potencia
        otro = deepcopy(self)
        otro.el_motor.potencia = potencia_final
        return otro

mi_carro = carro(potencia=1000,
                 cilindros_motor=4,
                 tamanno=17,
                 color_llanta='negro',
                 material_asiento='cuero',
                 color_asiento='negro'
                 )
otro_carro = carro(potencia=2000,
                 cilindros_motor=4,
                 tamanno=14,
                 color_llanta='rojo',
                 material_asiento='vinil',
                 color_asiento='azul'
                 )

carro_modificado = mi_carro + otro_carro
pass