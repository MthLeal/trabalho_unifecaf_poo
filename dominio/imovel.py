from abc import ABC, abstractmethod


class Imovel(ABC):

    def __init__(self, valor_base: float = 0.0):
        self.valor_base = valor_base

    @abstractmethod
    def calcular_valor_mensal(self) -> float: ...


class Apartamento(Imovel):
    def __init__(self, quartos=1, garagem=0, possui_criancas=True):
        super().__init__(700.0)
        if 1 > quartos > 2:
            raise ValueError("Quantidade de quartos inválida.")
        if 0 > garagem > 1:
            raise ValueError("Quantidade de garagem inválida.")
        if type(possui_criancas) != bool:
            raise TypeError(
                "Formato inválido para configuração de crianças no apartamento."
            )
        self.quartos = quartos
        self.garagem = garagem
        self.possui_criancas = possui_criancas

    def calcular_valor_mensal(self) -> float:
        valor = self.valor_base + (self.garagem * 300) + ((self.quartos - 1) * 200)
        if not self.possui_criancas:
            valor *= 0.95
        return valor


class Casa(Imovel):
    def __init__(self, quartos=1, garagem=0):
        super().__init__(900)
        if 1 > quartos > 2:
            raise ValueError("Quantidade de quartos inválida.")
        if 0 > garagem > 1:
            raise ValueError("Quantidade de garagem inválida.")
        self.quartos = quartos
        self.garagem = garagem

    def calcular_valor_mensal(self):
        valor = self.valor_base + (self.garagem * 300) + ((self.quartos - 1) * 250)
        return valor


class Estudio(Imovel):
    def __init__(self, vagas_estacionamento=0):
        super().__init__(1200.00)
        if vagas_estacionamento < 0:
            raise ValueError("Quantidade de vagas de estacionamento inválida.")
        self.vagas_estacionamento = vagas_estacionamento

    def calcular_valor_mensal(self):
        valor = self.valor_base
        if self.vagas_estacionamento >= 2:
            valor += 250 + ((self.vagas_estacionamento - 2) * 60.00)
        return valor
