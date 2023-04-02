peso_veiculo = float(input('Qual peso do veículo? '))
quant_rodas = int(input('Quantas rodas o veiculo possui? '))
quant_pessoas = int(input('Até quantas pessoas o veiculo pode carregar? '))
categoria = str

if quant_rodas <= 3:
  print('A categoria do veículo é: A')
elif quant_rodas == 4 and quant_pessoas < 8 and peso_veiculo < 3500:
  print('A categoria do veiculo é: B')
elif quant_rodas >= 4 and peso_veiculo >3500 and peso_veiculo <6000:
  print('A categoria do veiculo é: C')
elif quant_rodas >= 4 and quant_pessoas < 8:
  print('A categoria do veiculo é: D')
elif quant_rodas >= 4 and peso_veiculo >= 6000:
  print('A categoria do veiculo: E')
else:
  print('Categoria não encontrada.')
