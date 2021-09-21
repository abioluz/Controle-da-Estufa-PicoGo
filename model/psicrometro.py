class Psicrometro:
    def __init__(self, bulbo_seco:float, bulbo_umido:float, pressao_KPA:float=101.325,ventilacao:str ="N" ) -> float:
        self.bulbo_seco = bulbo_seco 
        self.bulbo_umido = bulbo_umido
        self.ventilacao = ventilacao
        self.pressao_KPA = pressao_KPA
        self.UR = self.get_ru


    def __calcular_ur(self):
        if self.ventilacao == "F":
            return self.__ventilacao_forcada()
        elif self.ventilacao == "N":
            return self.__ventilacao_nao_forcada()
        else:
            raise Exception("Digite somente N ou F")


    def __ventilacao_forcada(self) -> float:
        return self.__psicrometro(0.000667)
        
    def __ventilacao_nao_forcada(self) -> float:
        return self.__psicrometro(0.0008)

    def __psicrometro(self,A) -> float:
        Es1 = 0.6108 * (10**((7.5 * self.bulbo_seco) / (237.3 + self.bulbo_seco)))
        Es2 = 0.6108 *(10**((7.5 * self.bulbo_umido) / (237.3 + self.bulbo_umido)))
        Ea = Es2 - A *self.pressao_KPA * (self.bulbo_seco - self.bulbo_umido)
        return Ea * 100 / Es1

    @property
    def get_ru(self):
        ru = self.__calcular_ur()
        if ru >= 0 and ru <= 100:
            return ru
        else:
            raise Exception("Valor de RU não confere!")

if __name__ == "__main__":

    ps = Psicrometro(23.5,22.5,101.325,"F")
    print(ps.get_ru)
