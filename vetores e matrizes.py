opcoes = {"1": "Refrigerante de cola",
    "2": "Batata-frita",
    "3": "Barra de cereal",
    "4": "Água",
    "5": "Água com gás",
    "6": "Achocolatado",
    "7": "Bala de Menta",    
}

status = "AGUARDANDO"

while ( status == "AGUARDANDO" ):
  opcao = input( "Digite iniciar para escolher um produto: " )
  if ( opcao != "iniciar" ):
    print( "Você Digitou uma opção inválida, o programa terminou!" )
    status = "FINALIZADO"
  else:
    print( "Escolha um produto: " )
  
    for chave, valor in opcoes.items():
      print( chave + " = " + valor )
  
    print( "ou digite cancelar para retornar ao começo" )

    opcao = input("Digite o código do produto: ")

    if ( opcao != "cancelar") :
      if ( opcao in opcoes ):
        print( "Você escolheu " + opcoes[opcao])
        confirmacao = input( "Digite confirmar para receber o produto: " )
        if (confirmacao == "confirmar"):
          print( "Obrigado por usar nossa máquina!" ) 
      else:
        print("Esse produto não existe") 
    