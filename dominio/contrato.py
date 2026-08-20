from dominio.imovel import Imovel


class Contrato:
    def __init__(self, imovel: Imovel, valor_base: float=2000.0, parcelas: int=5):
        if parcelas < 1:
            raise ValueError('Parcelas devem ser de 1 a 5')
        self.imovel = imovel
        self.valor_base = valor_base
        self.parcelas = parcelas



    def calcular_parcela_base(self) -> float:
        return round(self.valor_base / self.parcelas, 2)

    def listar_parcelas_contrato(self) -> list:
        valor_parcela = self.calcular_parcela_base()
        lista_parcelas = [valor_parcela if i <= self.parcelas else 0 for i in range(1, 13)]
        return lista_parcelas

    def listar_valores_alugueis(self) -> list[float]:
        valores = []
        for mes in range(1, 13):
            valor = self.imovel.calcular_valor_mensal()
            if mes <= self.parcelas:
                valor += round(self.valor_base / self.parcelas, 2)
            valores.append(valor)
        return valores
