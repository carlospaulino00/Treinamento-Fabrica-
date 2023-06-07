from animal import Animal
from cachorro import Cachorro

animal = Animal('cachorro', 19)
cachorro = Cachorro('sully', 2, 'monstrinho')

animal.emitir_som() 
cachorro.emitir_som() 

animal.movimentar()
cachorro.movimentar() 

cachorro.apresentar()
