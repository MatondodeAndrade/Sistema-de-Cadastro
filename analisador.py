import estatisticas as est
import relatorio

# Carregar dados
dados = est.carregar_dados("dados/sensores.npy")
print(dados.shape)
# Calcular estatísticas
temp = est.media_coluna(dados, 0)
umid = est.media_coluna(dados, 1)
press = est.media_coluna(dados, 2)

# Mostrar relatório
print(relatorio.gerar_relatorio(temp, umid, press))

