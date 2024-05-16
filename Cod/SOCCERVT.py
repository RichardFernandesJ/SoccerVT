import random
from time import sleep
import os
#FutVirtual
#inicio
menu = ' '
while menu != 'N':
    print('\033[1;37m=-='*20)
    print('\033[33m                        SoccerVT')
    print('\033[37m=-='*20)
    #Neste jogo vamos ter 2 times por partidas onde vai ser escolhido times aleatorios nas partidas onde eles vão se enfrentar e o usuario vai poder apostar qual vai ganhar ou quantos gols vão ser feitos na partida ao todo ou por cada time.
    times_brasileirao = ['Athletico-MG', 'Atlético-GO' , 'Bahia' , 'Botafogo' , 'Bragantino' , 'Corinthians' , 'Criciúma' , 'Cruzeiro' , 'Cuiabá' , 'Flamengo' , 'Fluminense' , 'Fortaleza' , 'Grêmio' , 'Internacional' , 'Juventude' , 'Palmeiras' , 'São Paulo' , 'Vasco' , 'Vitória']
    multiplicado = [1.05, 1.10 , 1.15 , 1.29 , 1.5, 1.76, 2.0 , 2.23, 2.47 , 2.5, 3.0 , 3.5 , 4.0 , 4.5 , 5.0 , 5.5 , 6.0 , 6.5 , 7.0]
    multiempate = [1.05, 1.10 , 1.15 , 1.29 , 1.5, 1.76, 2.0]
    mult = random.choice(multiplicado)
    multe = random.choice(multiempate)
    timea = random.choice(times_brasileirao)
    timeb = random.choice(times_brasileirao)
    gols_timea = random.randint(0, 7)
    gols_timeb = random.randint(0, 7)
    if timea == timeb:
        while timea == timeb:
            timea = random.choice(times_brasileirao)
            timeb = random.choice(times_brasileirao)
    print('\033[33m                        BRASILEIRÃO')
    print('\033[37m=-='*20)
    print('\033[33m               {}      x      {}'.format(timea.upper(), timeb.upper()))
    print('\033[37m=-='*20)
    #MENU DE APOSTAS
    print('\033[33mMENU DE APOSTAS')
    print('\033[33m[ 1 ]\033[37m PLACAR')
    print('\033[33m[ 2 ]\033[37m GOLS')
    print('\033[33m[ 3 ]\033[37m VITORIA OU EMPATE')
    while True:
        menu = input('Digite: ')
        if menu.isdigit():  
            menu = int(menu)
            if menu < 1 or menu > 3:
                print('\033[1;31mPor favor, digite uma opção válida\033[m')  
            if menu in [1, 2, 3]:
                break
        else:
            print('\033[1;31mPor favor, digite uma opção válida\033[m')  
    # ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR O MENU ATÉ DIGITAR UM NUMERO VALIDO
    print('\033[37m=-=\033[m' * 20)
    os.system('cls')
    #USUARIO ESCOLHER A OPÇÃO 1 APOSTAR NO PLACAR
    if menu == 1:
        print('\033[1;37m=-='*20)
        print('\033[33m                        SoccerVT')
        print('\033[37m=-='*20)
        print('\033[1;33mPLACAR')
        print('\033[37mA ODD do PLACAR esta em \033[1;33m[{}]'.format(mult))
        #VALOR QUE O USUARIO DESEJA APOSTAR
        print('\033[1;37mDeseja apostar quantos R$ no placar ? ')
        #IDENTIFICADOR SE O NUMERO É VALIDO OU É STR ENQUANTO O USUARIO NÃO DIGITA UM NUMERO VALIDO VAI SER REPETIDO A SOLICITAÇÃO 
        while True:
            odd = input('Digite: ')
            if odd.replace('.','').isdigit():
                numb = float(odd)
                break
            else:
                print('\033[31mPor favor, digite um número válido\033[m')
        print('Informe quanto vai ser o placar do jogo entre \n\033[1;33m{} x {}'.format(timea, timeb))
        print('\033[1;37mQuantos gols do \033[1;33m{} ?\033[1;37m'.format(timea))
        #QUANTIDADE DE GOLS DO TIME 1
        #IDENTIFICADOR SE O NUMERO É VALIDO INTEIRO OU É STR ENQUANTO O USUARIO NÃO DIGITA UM NUMERO VALIDO VAI SER REPETIDO A SOLICITAÇÃO 
        while True:
            placartimea = input('Digite: ')
            if placartimea.isdigit():
                resulta = int(placartimea)
                break
            else:
                print('\033[1;31mPor favor, digite um número válido\033[m')
        print('Quantos gols do \033[1;33m{} ?\033[1;37m'.format(timeb))
        #QUANTIDADE DE GOLS DO TIME 2
        while True:
            placartimeb = input('Digite: ')
            if placartimeb.isdigit():
                resultb = int(placartimeb)
                break
            else:
                print('\033[1;31mPor favor, digite um número válido\033[m')
        os.system('cls')
        print('\033[1;37m=-='*20)
        print('\033[33m                        SoccerVT')
        print('\033[37m=-='*20)
        forra = numb * mult
        print('Você apostou R${} no placar \033[1;33m{} {} x {} {} \033[1;37m\npodendo ganhar R${:.2f}, Boa Sorte !!'.format(odd, timea, resulta, resultb, timeb, forra))
        #FORMAS DE MOSTRAR O RESULTADO DA PARTIDA
        print('\033[1;33m[ 1 ] \033[1;37mResultado mostrando Gols')
        print('\033[1;33m[ 2 ] \033[1;37mResultado direto')
        #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR O MENU ATÉ DIGITAR UM NUMERO VALIDO
        while True:
            select = input('Digite: ')
            if select.isdigit():  
                select = int(select)
                if select < 1 or select > 2:
                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                if select in [1, 2]:
                    break
            else:
                print('\033[1;31mPor favor, digite uma opção válida\033[m')
        print('\033[37m=-=\033[m'*20)
        os.system('cls')
        #SE O USUARIO DESEJAR VER OS GOLS DA PARTIDA
        if select == 1:
            #MOSTRAS OS GOLS FEITOS PELO TIME 1
            print('\033[1;37m=-='*20)
            print('\033[33m                        SoccerVT')
            print('\033[37m=-='*20)
            for x in range(gols_timea):
                print('Goool do {}'.format(timea))
                sleep(1)
            #MOSTRA OS GOLS FEITOS PELO TIME 2
            for x in range(gols_timeb):
                print('Goool do {}'.format(timeb))
                sleep(1)
            sleep(3)
            os.system('cls')
        #SE O USUARIO ESCOLHER O RESULTADO DIRETO SO MOSTRA O PLACAR FINAL
        if select == 2:
            print('\033[1;37m=-='*20)
            print('\033[33m                        SoccerVT')
            print('\033[37m=-='*20)
            print('\033[1;33mPALPITE\033[m')
            print('\033[1;33m{} \033[1;37m{} \033[1;33mx \033[1;37m{} \033[1;33m{} \033[1;37m'.format(timea, resulta, resultb, timeb))
            print('\033[37m=-=\033[m' * 20)
            #COMPARADOR DE PLACAR SE FOR IGUAL AO RESULTADO PALPITE CERTO SE NAO PALPITE ERRADO
            if resulta == gols_timea and resultb == gols_timeb:
                print('\033[1;37mQue Belo Palpite você acertou foram depositados na sua conta \033[1;32m+ R${}'.format(forra))
            else:
                print('\033[1;37mNão foi dessa vez, você errou o palpite e perdeu \033[31mR${}'.format(odd))
    #MENU DE GOLS
    if menu == 2:
        print('\033[1;37m=-='*20)
        print('\033[33m                        SoccerVT')
        print('\033[37m=-='*20)
        print('\033[1;33mMENU DE GOLS\033[m')
        print('\033[1;37mDeseja apostar em qual ?')
        print('\033[1;33m[ 1 ] \033[1;37mPalpite de gols do \033[1;33m{}'.format(timea))
        print('\033[1;33m[ 2 ] \033[1;37mPalpite de gols do \033[1;33m{}'.format(timeb))
        print('\033[1;33m[ 3 ] \033[1;37mPalpite de quantos GOLS vão sair na partida entre \n\033[1;33m{} x {}\033[1;37m'.format(timea, timeb))

        while True:
            select = input('Digite: ')
            if select.isdigit():  
                select = int(select)
                #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                if select < 1 or select > 3:
                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                if select in [1, 2, 3]:
                    break
            else:
                print('\033[1;31mPor favor, digite uma opção válida\033[m')  
        #SE O USUARIO ESCOLHER A OPÇÃO 1
        os.system('cls')
        if select == 1:
            print('\033[1;37m=-='*20)
            print('\033[33m                        SoccerVT')
            print('\033[37m=-='*20)
            print('A ODD de palpite de GOLS do \033[1;33m{}\033[1;37m esta em \033[1;33m[{}]'.format(timea, mult))
            print('\033[1;37mDeseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
            #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
            while True:
                odd = input('Digite: ')
                if odd.replace('.','').isdigit():
                    odd = float(odd)
                    break
                else:
                    print('\033[31mPor favor, digite um número válido\033[m')
            forra = mult * odd
            print('Qual é seu palpite ? Quantos GOLS o \033[1;33m{}\033[1;37m vai fazer ?'.format(timea))
            #IDENTIFICA SE É UM NUMERO INTEIRO OU STR
            while True:
                palpite = input('Digite: ')
                if palpite.isdigit():
                    palpite = int(palpite)
                    break
                else:
                    print('\033[1;31mPor favor, digite um número válido\033[m')
            print('Você apostou \033[1;33mR${} \033[1;37mque o \033[1;33m{} \033[1;37mvai fazer \033[1;33m{} \033[1;37mGOLS e \npode receber \033[1;33mR${:.2f} \033[1;37mpelo palpite \033[1;33mBoa Sorte !'.format(odd, timea, palpite, forra))
            sleep(5)
            os.system('cls')
            if palpite == gols_timea:
                print('\033[37m=-=\033[m' * 20)
                print('\033[1;37mQue Belo Palpite você acertou ! \nForam depositados na sua conta \033[322m+ R${}\033[1;37m'.format(forra))
                print('\033[37m=-=\033[m' * 20)
                sleep(5)
                os.system('cls')
            else:
                print('\033[37m=-=\033[m' * 20)
                print('Não foi dessa vez, você errou o palpite e perdeu \033[1;31mR${}'.format(odd))
                print('\033[37m=-=\033[m' * 20)
                sleep(5)
                os.system('cls')
        #SE O USUARIO ESCOLHER A OPÇÃO 2
        if select == 2:
            print('\033[1;37m=-='*20)
            print('\033[33m                        SoccerVT')
            print('\033[37m=-='*20)
            print('A ODD de palpite de GOLS do \033[1;33m{} \033[1;37mesta em \033[1;33m[{}]'.format(timeb, mult))
            print('Deseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')

            #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
            while True:
                odd = input('Digite: ')
                if odd.replace('.','').isdigit():
                    odd = float(odd)
                    break
                else:
                    print('\033[31mPor favor, digite um número válido\033[m')
            forra = mult * odd
            print('Qual é seu palpite ? Quantos GOLS o \033[1;33m{}\033[1;37m vai fazer ?'.format(timeb))

            #IDENTIFICA SE É UM NUMERO INTEIRO OU STR
            while True:
                palpite = input('Digite: ')
                if palpite.isdigit():
                    palpite = int(palpite)
                    break
                else:
                    print('\033[1;31mPor favor, digite um número válido\033[m')
            print('Você apostou \033[1;33mR${}\033[1;37m que o \033[1;33m{}\033[1;37m \nvai fazer \033[1;33m{}\033[1;37m GOLS e pode receber \033[1;33mR${} \033[1;37mpelo palpite \033[1;33mBoa Sorte !\033[1;37m'.format(odd, timeb, palpite, forra))
            sleep(5)
            if palpite == gols_timeb:
                print('\033[37m=-=\033[m' * 20)
                print('Que Belo Palpite você acertou ! \nForam depositados na sua conta \033[1;32m+ R${:.2f}'.format(forra))
                print('\033[37m=-=\033[m' * 20)
                sleep(5)
                os.system('cls')
            else:
                print('\033[37m=-=\033[m' * 20)
                print('Não foi dessa vez, você errou o palpite e perdeu \033[1;31mR${}\033[1;37m'.format(odd))
                print('\033[37m=-=\033[m' * 20)
                sleep(5)
                os.system('cls')
        #SE O USUARIO ESCOLHER A OPÇÃO 3
        if select == 3:
            print('\033[1;37m=-='*20)
            print('\033[33m                        SoccerVT')
            print('\033[37m=-='*20)
            print('A ODD de quantos GOLS vão sair entre \033[1;33m{} x {} \033[1;37m\nesta em \033[1;33m[{}]\033[1;37m'.format(timea, timeb, mult))
            print('Deseja apostar quantos \033[1;33mR$\033[1;37m neste palpite ? ')
        
            #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
            while True:
                    odd = input('Digite: ')
                    if odd.replace('.','').isdigit():
                        odd = float(odd)
                        break
                    else:
                        print('\033[31mPor favor, digite um número válido\033[m')
            forra = mult * odd
            print('Qual é seu palpite ? Informe quantos Gols vão sair entre \033[1;33m{} x {}\033[1;37m'.format(timea, timeb))
            #IDENTIFICA SE É UM NUMERO INTEIRO OU STR
            while True:
                palpite = input('Digite: ')
                if palpite.isdigit():
                    palpite = int(palpite)
                    break
                else:
                    print('\033[1;31mPor favor, digite um número válido\033[m')
            print('Você apostou \033[1;33mR${} \033[1;37mque no jogo entre \033[1;33m{} x {} \033[1;37m\nvai ser feito \033[1;33m{} \033[1;37mGOLS. Podendo receber neste palpite \033[1;33mR${}\033[1;37m'.format(odd, timea, timeb, palpite, forra))
            print('\033[1;37m=-=' * 20)
            sleep(5)
            result = gols_timea + gols_timeb
            if palpite == result:
                print('Que Belo Palpite você acertou ! \nForam depositados na sua conta \033[1;32m+ R${}\033[1;37m'.format(forra))
            else:
                print('\033[1;37mNão foi dessa vez, você errou o palpite e perdeu \033[1;31mR${}'.format(odd))
            sleep(5)
            os.system('cls')
    #MENU DE VITORIA OU EMPATE
    if menu == 3:
        print('\033[1;37m=-='*20)
        print('\033[33m                        SoccerVT')
        print('\033[37m=-='*20)
        print('\033[1;33mMENU VITORIA OU EMPATE\033[1;37m')
        print('''Deseja apostar em qual dos times 
    \033[1;33m[ 1 ]\033[1;37m {} 
    \033[1;33m[ 2 ] \033[1;37m{}
    \033[1;33m[ 3 ] \033[1;37mEMPATE'''.format(timea, timeb))
        
        while True:
            time = input('Digite: ')
            if time.isdigit():  
                time = int(time)
                #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                if time < 1 or time > 3:
                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                if time in [1, 2, 3]:
                    break
            else:
                print('\033[1;31mPor favor, digite uma opção válida\033[m')  
        print('\033[1;37m=-=\033[m' * 20)
        # OPÇÃO 1 VITORIA DO TIME 1 ou VITORIA E EMPATE
        if time == 1:
            print('\033[1;33m[ 1 ] \033[1;37mVitoria do \033[1;33m{}\033[1;37m ODD em \033[1;33m[{}]\033[1;37m'.format(timea, mult))
            print('\033[1;33m[ 2 ] \033[1;37mVitoria do \033[1;33m{} \033[1;37mou Empate ODD em \033[1;33m[{}]\033[1;37m'.format(timea, multe))

            while True:
                palpite = input('Digite: ')
                if palpite.isdigit():  
                    palpite = int(palpite)
                    #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                    if palpite < 1 or palpite > 2:
                        print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                    if palpite in [1, 2]:
                        break
                else:
                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  
            print('\033[1;37m=-=\033[m' * 20)
            #VALOR A APOSTAR SEGUIDO DE RESULTADO DO PALPITE NAS CORES VERDE E VERMELHA
            if palpite == 1:
                print('\033[1;37mDeseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
                #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                while True:
                    odd = input('Digite: ')
                    if odd.replace('.','').isdigit():
                        odd = float(odd)
                        break
                    else:
                        print('\033[31mPor favor, digite um número válido\033[m')
                forra = mult * odd
                #SE O USUARIO ACERTAR O PALPITE DA VITORIA DO TIME 1
                if gols_timea > gols_timeb:
                    print('\033[1;37mVitoria do \033[1;33m{}\033[1;37m'.format(timea))
                    print('Você apostou na Vitoria do \033[1;33m{} \033[1;37m\nACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(timea, forra))
                #SE O USUARIO ERRAR O PALPITE DA VITORIA DO TIME 1
                else:
                    print('\033[1;37mDerrota do \033[1;33m{}'.format(timea))
                    print('Você apostou na Vitoria do \033[1;33m{} \033[1;37me \nERROU o palpite perdendo o valor depositado \033[1;31mR${}'.format(timea, odd))
            #VALOR A APOSTAR SEGUIDO DE VITORIA OU VITORIA E EMPATE DO TIME ESCOLHIDO
            if palpite == 2:
                print('\033[1;37mDeseja apostar quantos \033[1;33mR$\033[1;37m neste palpite ? ')

                while True:
                    odd = input('Digite: ')
                    if odd.replace('.','').isdigit():
                        odd = float(odd)
                        break
                    else:
                        print('\033[31mPor favor, digite um número válido\033[m')
                print('\033[1;37m=-=\033[m' * 20)
                forra = multe * odd
                #VITORIA OU EMPATE DO TIME 1
                if gols_timea > gols_timeb or gols_timea == gols_timeb:
                    #SE O TIME 1 VENCER
                    if gols_timea > gols_timeb:
                        print('\033[1;37mVitoria\033[m do \033[1;33m{}\033[1;37m'.format(timea))
                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. \nACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}'.format(timea, forra))
                    #SE O TIME 1 VENCER OU EMPATAR
                    if gols_timea == gols_timeb:
                        print('\033[33mEMPATE\033[m entre \033[1;33m{} x {}\033[1;37m'.format(timea, timeb))
                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. \nACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}'.format(timea, forra))
                #SE O USUARIO ERRAR O PALPITE
                else:
                    print('\033[1;37mDerrota do \033[1;33m{}\033[1;37m'.format(timea))
                    print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE.  \nERROU o palpite perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(timea,odd))
            os.system('cls')
        #SE O USUARIO ESCOLHER A OPÇÃO 2 VITORIA DO TIME 2 OU VITORIA E EMPATE
        if time == 2:
            print('\033[1;33m[ 1 ] \033[1;37mVitoria do \033[1;33m{} \033[1;37mODD em \033[1;33m[{}]\033[1;37m'.format(timeb, mult))
            print('\033[1;33m[ 2 ] \033[1;37mVitoria do \033[1;33m{} \033[1;37mou Empate ODD em \033[1;33m[{}]\033[1;37m'.format(timeb, multe))

            while True:
                palpite = input('Digite: ')
                if palpite.isdigit():  
                    palpite = int(palpite)
                    #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                    if palpite < 1 or palpite > 2:
                        print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                    if palpite in [1, 2]:
                        break
                else:
                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  

            if palpite == 1:
                print('Deseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
                #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                while True:
                    odd = input('Digite: ')
                    if odd.replace('.','').isdigit():
                        odd = float(odd)
                        break
                    else:
                        print('\033[31mPor favor, digite um número válido\033[m')
                print('\033[1;37m=-=\033[m' * 20)
                forra = mult * odd
                #SE O USUARIO ACERTAR O PALPITE DA VITORIA
                if gols_timeb > gols_timea:
                    print('\033[1;37mVitoria do \033[1;33m{}\033[1;37m'.format(timeb))
                    print('Você apostou na Vitoria do \033[1;33m{} \033[1;37m\nACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(timeb, forra))
                #SE O USUARIO ERRAR O PALPITE
                else:
                    print('\033[1;37mDerrota do \033[1;33m{}\033[1;37m'.format(timeb))
                    print('Você apostou na Vitoria do \033[1;33m{} \033[1;37me \nERROU o palpite perdendo o valor depositado \033[1;31mR${}'.format(timeb,odd))
            # VALOR A APOSTAR SEGUIDO DE VITORIA OU VITORIA E EMPATE DO TIME ESCOLHIDO
            if palpite == 2:
                print('Deseja apostar quantos \033[1;33mR$ neste \033[1;37mpalpite ? ')
                #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                while True:
                    odd = input('Digite: ')
                    if odd.replace('.','').isdigit():
                        odd = float(odd)
                        break
                    else:
                        print('\033[31mPor favor, digite um número válido\033[m')
                print('\033[1;37m=-=\033[m' * 20)
                forra = multe * odd
                if gols_timeb > gols_timea or gols_timeb == gols_timea:
                    #CASO O USUARIO ACERTE A VITORIA
                    if gols_timeb > gols_timea:
                        print('\033[1;37mVitoria do \033[1;33m{}\033[1;37m'.format(timeb))
                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. \nACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}'.format(timeb, forra))
                    #CASO O USUARIO ACERTE O EMPATE
                    if gols_timeb == gols_timea:
                        print('\033[1;37mEMPATE entre \033[1;33m{} x {}\033[1;37m'.format(timeb, timea))
                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. \nACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(timeb, forra))
                #CASO O USUARIO ERRE O PALPITE
                else:
                    print('\033[1;37mDerrota do \033[1;33m{}\033[1;37m'.format(timeb))
                    print(
                        'Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE.  \nERROU o palpite perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(
                            timeb, odd))
            os.system('cls')
        #SE O USUARIO ESCOLHER A OPÇÃO 3 EMPATE
        if time == 3:
            print('\033[1;33mEMPATE \033[1;37mODD \033[1;33m[{}]\033[1;37m'.format(mult))
            print('Deseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
            #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
            while True:
                odd = input('Digite: ')
                if odd.replace('.','').isdigit():
                    odd = float(odd)
                    break
                else:
                    print('\033[31mPor favor, digite um número válido\033[m')
            print('\033[1;37m=-=\033[m' * 20)
            forra = mult * odd
            #MOSTRA SE O USUARIO ACERTAR O EMPATE
            if gols_timea == gols_timeb:
                print('\033[1;37mEMPATE entre \033[1;33m{} x {}\033[1;37m'.format(timeb, timea))
                print('Você apostou no EMPATE. ACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(forra))
            #MOSTRA QUEM VENCEU CASO O USUARIO ERRE O PALPITE
            else:
                if gols_timea > gols_timeb:
                    print('\033[1;33m{} \033[1;37mVenceu '.format(timea))
                    print('Você apostou no EMPATE e acabou perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(odd))
                if gols_timeb > gols_timea:
                    print('\033[1;33m{} \033[1;37mVenceu '.format(timeb))
                    print('Você apostou no EMPATE e acabou perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(odd))
            os.system('cls')
    #RESULTADO DO JOGO FINAL
    print('\033[1;37m=-='*20)
    print('\033[33m                        SoccerVT')
    print('\033[37m=-='*20)
    print('\033[1;37m=-=\033[m'* 20)
    print('\033[1;33mRESULTADO DO JOGO \033[m')
    if gols_timea > gols_timeb:
        print('\033[1;33m{} \033[1;37m{} \n\033[1;33m{} \033[1;37m{}'.format(timea, gols_timea, timeb, gols_timeb))
    if gols_timeb > gols_timea:
        print('\033[1;33m{} \033[1;37m{} \n\033[1;33m{} \033[1;37m{}'.format(timeb, gols_timeb, timea, gols_timea))
    if gols_timea == gols_timeb:
        print('\033[1;33m{} \033[1;37m{} \n\033[1;33m{} \033[1;37m{}'.format(timea, gols_timea, timeb, gols_timeb))
    print('\033[1;37m=-=\033[m'* 20)
    print('Para retornar ao Menu Digite 1')
    while True:
        retmenu = input('Digite: ')
        if retmenu.isdigit():
            retmenu = int(retmenu)
            if retmenu == 1:
                break
            else:
                print('\033[31mDigite um número válido !\033[m')
        else:
            print('\033[31mDigite um número válido !\033[m')
    os.system('cls')

