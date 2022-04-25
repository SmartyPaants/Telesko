class Computer:
    def config(self):
        print('i5, 16GB RAM, 1TB SSD')


com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)
print()
com1.config()
com2.config()