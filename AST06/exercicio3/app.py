class ProcessadorDeAcoes:
    def validar_dados(self, dados: dict) -> bool:
        """Simula a validação dos dados."""
        return True

    def salvar_dados(self, dados: dict) -> bool:
        """Simula o salvamento dos dados."""
        return True

    def executar_processo(self, dados: dict) -> str:
        """Executa o processo: valida e, se ok, salva os dados, nessa ordem."""
        if self.validar_dados(dados):
            if self.salvar_dados(dados):
                return "Processo executado com sucesso."
            return "Falha ao salvar os dados."
        return "Falha na validação dos dados."
