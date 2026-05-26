class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def mostrar_temp(self):
        return f'Temperatura: {round(self.celsius, 1)}°C'
    
    @classmethod
    def de_fahrenheit(cls, fahrenheit: float):
        fah_para_cel = ((fahrenheit - 32) * 5) / 9
        return cls(fah_para_cel)
    
    @classmethod
    def de_kelvin(cls, kelvin):
        kel_para_cel = kelvin - 273.1
        return cls(kel_para_cel)
    
t1 = Temperatura(40)
print(t1.mostrar_temp())

print()

t2 = Temperatura.de_fahrenheit(77)
print(t2.mostrar_temp())

print()

t3 = Temperatura.de_kelvin(300)
print(t3.mostrar_temp())