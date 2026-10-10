# Explicação

O `mutmut show` revelou que ele trocou `>=` por `>` (e `700` por `701`) na regra do score, e `>` por `>=` (e `5000.00` por `5001.0`) na regra da renda; os testes originais só usavam valores longe do limite (850, 500, 8000, 300), então passavam com o código quebrado.
Com 4 mutantes sobreviventes, a cobertura de 100% só provava que as linhas executavam, não que o resultado estava correto.
A Análise do Valor Limite testa exatamente no limite e ao redor dele (699/700/701 e 4999.99/5000.00/5000.01), onde qualquer troca de operador ou de constante muda o resultado e o teste falha.
Assim, os 7 mutantes foram mortos (0 sobreviventes).
