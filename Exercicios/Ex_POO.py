class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.disponivel = True  # começa disponível

    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Vendido"
        print(f"{self.marca} {self.modelo} ({self.ano}) - R${self.preco:.2f} [{status}]")

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)
        print(f"Desconto de {percentual}% aplicado. Novo preço: R${self.preco:.2f}")

    def vender(self):
        if self.disponivel:
            self.disponivel = False
            print(f"{self.marca} {self.modelo} vendido com sucesso!")
            return True
        print("Carro já foi vendido.")
        return False


class Concessionaria:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def adicionar_carro(self, carro):
        self.carros.append(carro)
        print(f"Carro {carro.marca} {carro.modelo} adicionado ao estoque.")

    def listar_carros(self):
        print(f"\n=== Estoque da {self.nome} ===")
        for carro in self.carros:
            carro.exibir_detalhes()

    def buscar_por_marca(self, marca):
        resultado = [c for c in self.carros if c.marca.lower() == marca.lower()]
        return resultado

    def realizar_venda(self, marca, modelo):
        for carro in self.carros:
            if carro.marca == marca and carro.modelo == modelo:
                return carro.vender()
        print("Carro não encontrado.")
        return False

    def filtrar_disponiveis(self):
        return [c for c in self.carros if c.disponivel]


# Main
if __name__ == "__main__":
    loja = Concessionaria("AutoCenter SP")

    carro1 = Carro("Toyota", "Corolla", 2023, 120000)
    carro2 = Carro("Honda", "Civic", 2022, 110000)
    carro3 = Carro("Toyota", "Yaris", 2024, 90000)

    loja.adicionar_carro(carro1)
    loja.adicionar_carro(carro2)
    loja.adicionar_carro(carro3)

    loja.listar_carros()

    carro1.aplicar_desconto(10)

    loja.realizar_venda("Toyota", "Corolla")

    print("\n--- Disponíveis após venda ---")
    for c in loja.filtrar_disponiveis():
        c.exibir_detalhes()