from funcionario import Funcionario
from gerente import Gerente

funcionario1 = Funcionario("João", 5000.0)

funcionario1.imprimir_informacoes()

gerente1 = Gerente("Maria", 8000.0, "Vendas")

gerente1.imprimir_informacoes()

gerente1.dar_aumento(10)

gerente1.imprimir_informacoes()
