
decimal = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
roman = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
class IntRom:
    def __init__(self,value):
        self.value = value
    def toRoman(self):
        self.value = int(input('>'))
        print(self.value)
        returned = ''
        for i in range(len(decimal)):
            m=self.value//decimal[i]
            for j in range(m):
                returned += roman[i]
            self.value=self.value%decimal[i]
        return returned
example = IntRom(36)
example_rom = example.toRoman()
print(example_rom)
