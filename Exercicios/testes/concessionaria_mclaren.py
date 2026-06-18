# ============================================================
#   CONCESSIONÁRIA McLAREN - Sistema em POO (Python)
#   4 Classes | 5+ Atributos por classe | 4+ Métodos por classe
# ============================================================


# ============================================================
# CLASSE 1: Carro
# Representa um veículo McLaren no estoque
# ============================================================
class Carro:

    # Atributo de classe (compartilhado por todos os carros)
    marca = "McLaren"

    def __init__(self, modelo, ano, preco, cor, velocidade_maxima):
        # Atributo 1
        self.modelo = modelo
        # Atributo 2
        self.ano = ano
        # Atributo 3
        self.preco = preco
        # Atributo 4
        self.cor = cor
        # Atributo 5
        self.velocidade_maxima = velocidade_maxima
        # Atributo extra (controlado internamente)
        self.disponivel = True

    # Método 1 - Exibe todas as informações do carro
    def exibir_detalhes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        print(f"""
     {self.marca} {self.modelo}
     Ano:               {self.ano}
     Cor:               {self.cor}
     Velocidade máx:    {self.velocidade_maxima} km/h
     Preço:             R$ {self.preco:,.2f}
     Status:            {status}
        """)

    # Método 2 - Aplica desconto no preço do carro
    def aplicar_desconto(self, percentual):
        if percentual <= 0 or percentual >= 100:
            print("Percentual de desconto inválido.")
            return
        desconto = self.preco * (percentual / 100)
        self.preco -= desconto
        print(f"Desconto de {percentual}% aplicado! Novo preço: R$ {self.preco:,.2f}")

    # Método 3 - Realiza a venda do carro
    def vender(self):
        if self.disponivel:
            self.disponivel = False
            print(f"{self.marca} {self.modelo} vendido com sucesso!")
            return True
        print(f"Carro indisponível.")
        return False

    # Método 4 - Atualiza o preço do carro
    def atualizar_preco(self, novo_preco):
        if novo_preco <= 0:
            print("Preço inválido.")
            return
        self.preco = novo_preco
        print(f"Preço atualizado para R$ {self.preco:,.2f}")


# ============================================================
# CLASSE 2: Cliente
# Representa um cliente da concessionária
# ============================================================
class Cliente:

    def __init__(self, nome, cpf, email, telefone, saldo):
        # Atributo 1
        self.nome = nome
        # Atributo 2
        self.cpf = cpf
        # Atributo 3
        self.email = email
        # Atributo 4
        self.telefone = telefone
        # Atributo 5
        self.saldo = saldo
        # Atributo extra
        self.carros_comprados = []

    # Método 1 - Exibe os dados do cliente
    def exibir_dados(self):
        print(f"""
        Cliente: {self.nome}
     CPF:      {self.cpf}
     Email:    {self.email}
     Telefone: {self.telefone}
     Saldo:    R$ {self.saldo:,.2f}
     Carros comprados: {len(self.carros_comprados)}
        """)

    # Método 2 - Verifica se o cliente tem saldo para comprar
    def pode_comprar(self, preco):
        if self.saldo >= preco:
            print(f"{self.nome} tem saldo suficiente para a compra.")
            return True
        print(f"Saldo insuficiente. Faltam R$ {preco - self.saldo:,.2f}")
        return False

    # Método 3 - Registra a compra de um carro
    def registrar_compra(self, carro):
        self.saldo -= carro.preco
        self.carros_comprados.append(carro)
        print(f"Compra registrada! Saldo restante: R$ {self.saldo:,.2f}")

    # Método 4 - Lista os carros comprados pelo cliente
    def listar_compras(self):
        if not self.carros_comprados:
            print(f"{self.nome} ainda não comprou nenhum carro.")
            return
        print(f"Carros comprados por {self.nome}:")
        for carro in self.carros_comprados:
            print(f"     → McLaren {carro.modelo} ({carro.ano})")


# ============================================================
# CLASSE 3: Vendedor
# Representa um funcionário vendedor da concessionária
# ============================================================
class Vendedor:

    def __init__(self, nome, matricula, salario_base, especialidade, anos_experiencia):
        # Atributo 1
        self.nome = nome
        # Atributo 2
        self.matricula = matricula
        # Atributo 3
        self.salario_base = salario_base
        # Atributo 4
        self.especialidade = especialidade
        # Atributo 5
        self.anos_experiencia = anos_experiencia
        # Atributo extra
        self.vendas_realizadas = 0

    # Método 1 - Exibe os dados do vendedor
    def exibir_dados(self):
        print(f"""
     Vendedor: {self.nome}
     Matrícula:      {self.matricula}
     Especialidade:  {self.especialidade}
     Experiência:    {self.anos_experiencia} anos
     Salário base:   R$ {self.salario_base:,.2f}
     Vendas feitas:  {self.vendas_realizadas}
        """)

    # Método 2 - Calcula o salário com comissão (2% por venda)
    def calcular_salario(self):
        comissao = self.vendas_realizadas * (self.salario_base * 0.02)
        total = self.salario_base + comissao
        print(f"Salário de {self.nome}: R$ {total:,.2f} (base + comissão)")
        return total

    # Método 3 - Registra uma venda realizada pelo vendedor
    def registrar_venda(self):
        self.vendas_realizadas += 1
        print(f"Venda registrada! Total de vendas de {self.nome}: {self.vendas_realizadas}")

    # Método 4 - Verifica se o vendedor é sênior (5+ anos)
    def verificar_senioridade(self):
        if self.anos_experiencia >= 5:
            print(f"{self.nome} é um vendedor SÊNIOR.")
        else:
            print(f"{self.nome} é um vendedor JÚNIOR.")


# ============================================================
# CLASSE 4: Concessionaria
# Gerencia todo o sistema da loja McLaren
# ============================================================
class Concessionaria:

    def __init__(self, nome, cidade, cnpj, telefone, ano_fundacao):
        # Atributo 1
        self.nome = nome
        # Atributo 2
        self.cidade = cidade
        # Atributo 3
        self.cnpj = cnpj
        # Atributo 4
        self.telefone = telefone
        # Atributo 5
        self.ano_fundacao = ano_fundacao
        # Atributos extras
        self.estoque = []
        self.vendedores = []
        self.clientes = []

    # Método 1 - Adiciona um carro ao estoque
    def adicionar_carro(self, carro):
        self.estoque.append(carro)
        print(f"McLaren {carro.modelo} adicionado ao estoque.")

    # Método 2 - Lista todos os carros disponíveis
    def listar_disponiveis(self):
        disponiveis = [c for c in self.estoque if c.disponivel]
        if not disponiveis:
            print("Nenhum carro disponível no momento.")
            return
        print(f"\n Carros disponíveis na {self.nome}:")
        for carro in disponiveis:
            carro.exibir_detalhes()

    # Método 3 - Realiza a venda completa (cliente + vendedor + carro)
    def realizar_venda(self, cliente, vendedor, modelo):
        print(f"\n Iniciando venda do McLaren {modelo} para {cliente.nome}...")

        # Procura o carro no estoque
        carro_encontrado = None
        for carro in self.estoque:
            if carro.modelo == modelo and carro.disponivel:
                carro_encontrado = carro
                break

        if not carro_encontrado:
            print(f"McLaren {modelo} não encontrado ou indisponível.")
            return

        # Verifica se o cliente tem saldo
        if not cliente.pode_comprar(carro_encontrado.preco):
            return

        # Realiza a venda
        carro_encontrado.vender()
        cliente.registrar_compra(carro_encontrado)
        vendedor.registrar_venda()
        print(f"Venda concluída por {vendedor.nome}!")

    # Método 4 - Exibe o resumo geral da concessionária
    def exibir_resumo(self):
        disponiveis = len([c for c in self.estoque if c.disponivel])
        vendidos = len(self.estoque) - disponiveis
        print(f"""
        {self.nome}
     Cidade:         {self.cidade}
     CNPJ:           {self.cnpj}
     Telefone:       {self.telefone}
     Fundada em:     {self.ano_fundacao}
     Total estoque:  {len(self.estoque)} carros
     Disponíveis:    {disponiveis}
     Vendidos:       {vendidos}
     Vendedores:     {len(self.vendedores)}
     Clientes:       {len(self.clientes)}
        """)


# ============================================================
# MAIN - Execução do programa
# ============================================================
if __name__ == "__main__":

    print("=" * 55)
    print("CONCESSIONÁRIA McLAREN")
    print("=" * 55)

    # --- Criando a Concessionária ---
    loja = Concessionaria(
        nome="McLaren São Paulo",
        cidade="São Paulo - SP",
        cnpj="12.345.678/0001-99",
        telefone="(11) 4002-8922",
        ano_fundacao=2015
    )

    # --- Criando os Carros ---
    carro1 = Carro("720S",   2023, 2_100_000, "Laranja Papaya", 341)
    carro2 = Carro("765LT",  2023, 3_400_000, "Cinza Stealth",  330)
    carro3 = Carro("Artura", 2024, 1_800_000, "Azul Elétrico",  330)
    carro4 = Carro("P1",     2022, 9_500_000, "Preto Carbono",  350)

    # --- Adicionando carros ao estoque ---
    print("\n ADICIONANDO CARROS AO ESTOQUE:")
    loja.adicionar_carro(carro1)
    loja.adicionar_carro(carro2)
    loja.adicionar_carro(carro3)
    loja.adicionar_carro(carro4)

    # --- Criando Vendedores ---
    vendedor1 = Vendedor("Carlos Silva",  "V001", 8_000, "Supercarros",  7)
    vendedor2 = Vendedor("Ana Ferreira",  "V002", 7_500, "Hipercars",    3)

    loja.vendedores.append(vendedor1)
    loja.vendedores.append(vendedor2)

    # --- Criando Clientes ---
    cliente1 = Cliente("Bruno Mendes",  "111.222.333-44", "bruno@email.com",  "(11)99999-1111", 4_000_000)
    cliente2 = Cliente("Julia Rocha",   "555.666.777-88", "julia@email.com",  "(11)99999-2222", 2_000_000)

    loja.clientes.append(cliente1)
    loja.clientes.append(cliente2)

    # --- Listando carros disponíveis ---
    print("\n ESTOQUE DISPONÍVEL:")
    loja.listar_disponiveis()

    # --- Aplicando desconto ---
    print("APLICANDO DESCONTO NO 720S:")
    carro1.aplicar_desconto(5)

    # --- Exibindo dados dos vendedores ---
    print("\n DADOS DOS VENDEDORES:")
    vendedor1.exibir_dados()
    vendedor2.exibir_dados()
    vendedor1.verificar_senioridade()
    vendedor2.verificar_senioridade()

    # --- Realizando vendas ---
    print("\n REALIZANDO VENDAS:")
    loja.realizar_venda(cliente1, vendedor1, "765LT")
    loja.realizar_venda(cliente2, vendedor2, "Artura")
    loja.realizar_venda(cliente2, vendedor2, "P1")  # Saldo insuficiente

    # --- Histórico de compras dos clientes ---
    print("\n HISTÓRICO DE COMPRAS:")
    cliente1.listar_compras()
    cliente2.listar_compras()

    # --- Salário dos vendedores após vendas ---
    print("\n SALÁRIOS APÓS VENDAS:")
    vendedor1.calcular_salario()
    vendedor2.calcular_salario()

    # --- Resumo final da concessionária ---
    print("\n RESUMO FINAL DA CONCESSIONÁRIA:")
    loja.exibir_resumo()

    print("=" * 55)
    print("FIM DO SISTEMA")
    print("=" * 55)
