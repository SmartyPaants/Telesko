class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram
    def config(self):
        print('Configurations for are: CPU is', self.cpu, 'and RAM is', self.ram)


com1 = Computer('i5', '16GB RAM')
com2 = Computer('Ryzen 3', '8GB RAM')
com1.config()
com2.config()