def delayed_print(string):
      import time
      sleep=0.05 ## Isso faz com que o printe seja atrasado por segundo
      for x in string:
            print (x, end="") #É necessario o end="" pois sem ele o programa crash ??
            time.sleep(sleep)
print('.:.:.:.:')

##Game de desenvolvimento por texto

nome = input('Informe seu nome: ')
print('')

delayed_print('Prazer em te conhecer {}. \n Aqui começa uma aventura por linhas de comando e \n'
      ' mesmo que seja apenas uma demonstração \n bem simples, não se engane '
      'esse \n é apenas o começo de uma grande historia, certo...Humm'.format(nome))

print('')
print('')

delayed_print('Opá antes de começar gostaria de avisar os \n '
      'principais comandos, pois como se trata de uma demo \n '
      'os comandos são muito delimitados "sorry". \n '
      'LISTA DE COMANDOS\n'
      ' * olhar em volta\n'
      ' * ir ate porta\n'
      ' * entrar\n'
              '\n')

enter = input('Tecle enter para começar...')

r1 = 'olhar em volta'
r2 = 'ir ate a porta'
r3 = 'entrar'

print('')
print('')

texto = ('Hora atual: 18:00 PM\n'
         '\n'
         'Você se vê em frente a uma casa\n'
         'aparentemente abandonada...')

print("{0:^60}".format(texto))

print('')
print('')

resposta = input('O que vc gostaria de fazer? ')

print('')
print('')

if resposta == r1:
      print('Olhando para a casa em si vc observa que \n'
            'ela tem uma coloração acinzentada, \n'
            'com a tinta toda quebradiça, nela á uma janela \n'
            'fechada por tabuas e suja pela poeira além \n'
            'de uma varanda vazia que se observa uma \n'
            'porta azul e isso lhe chama a atenção')
else:
      resposta = input('Comando invalido \n'
                       'O que vc gostaria de fazer? ')
print('')
print('')

resposta2 = input('O que vc gostaria de fazer? ')

print('')
print('')

if resposta2 == r2:
      print('vc passa pela varanda e chega ate a porta \n'
            'assim parando na frente da mesma...')
else:
      resposta2 = input('Comando invalido \n'
                       'O que vc gostaria de fazer? ')

print('')
print('')

resposta3 = input('O que vc gostaria de fazer? ')

print('')
print('')

if resposta3 == r1:
      print('Meticulosamente você observa a porta \n'
            'e escuta o vento passar por entre sua fresta, \n'
            'você roda a maçaneta e descobre \n'
            'que a mesma se encontra destrancada...')

else:
      resposta3 = input('Comando invalido \n'
                       'O que vc gostaria de fazer? ')

print('')
print('')

resposta3 = input('O que vc gostaria de fazer? ')

print('')
print('')

if resposta3 == r3:
      print('passando pela porta vc se encontra em um cômodo \n'
      'que dá vai a uma que vai a cozinha \n'
      'e uma outra que vai a sala alem, de \n'
      'uma escada que sobe a o segundo andar.')

else:
      resposta3 = input('Comando invalido \n'
                       'O que vc gostaria de fazer? ')

print('')
print('')

print('De repente um estrondo é ouvido \n'
      'e da escada algo vem correndo em sua direção ...')

print('')
print('')

delayed_print('ESSE É O FIM POR ENQUANTO\n'
              'MUITO OBRIGADO POR JOGAR')






