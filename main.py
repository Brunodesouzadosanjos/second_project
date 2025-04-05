from dataclasses import dataclass
@dataclass

class Sistema:
    saldo: float


    def exibir_saldo(self):
        print(self.saldo)

    def adicionar_receita(self):
        valor = float(input('Adicione um valor: '))
        self.saldo = self.saldo+valor

    def adicionar_dispesa(self):
        valor = float(input('Adicione um valor: '))
        self.saldo = self.saldo-valor


sis = Sistema(saldo=0)

while True == True:
   
    escolha = input('Deseja adicionar receita[R] ou despesa[D] ou exibir saldo[E]: ')
    if escolha == 'R' or escolha == 'r':
        sis.adicionar_receita()
    elif escolha == 'D':
        sis.adicionar_dispesa()
    elif escolha == 'E':
        sis.exibir_saldo()