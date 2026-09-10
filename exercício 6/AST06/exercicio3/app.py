class ProcessadorDeAcoes:
    """
    Precisa executar duas etapas em ordem estrita: primeiro
    validar_dados, depois salvar_dados. A ordem e crucial para
    evitar salvar dados invalidos.
    """

    def validar_dados(self, dados: dict) -> bool:
        return True

    def salvar_dados(self, dados: dict) -> bool:
        return True

    def executar_processo(self, dados: dict) -> str:
        if self.validar_dados(dados):
            self.salvar_dados(dados)
            return "Processo executado com sucesso"
        return "Falha na validacao dos dados"
