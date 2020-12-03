import pygame

def lePlaylistDeArquivo(NomeArq):
    arquivo = open(NomeArq, 'r')
    linhas = []
    for linha in arquivo:
        linhaLida = linha.strip().split('#')
        linhas.append(linhaLida)
        arquivo.close
    return linhas

def salvar_novasmsc(playlist,nomeArq):
    arquivo=open(nomeArq,'w')
    for banda, musica, genero in playlist:
        linha=banda+'#'+musica+'#'+genero+'\n'
        arquivo.write(linha)
    arquivo.close()

def listar_playlist(playlist):
    for lista in playlist:
        if lista[0]=='':
            break
        else:
            print(f'Banda: {lista[0]} Música: {lista[1]} Gênero: {lista[2]}')


def pesquisa_musica_por_genero(genero_pesq):
    for msc in playlist:
        if (msc[2] == genero_pesq):
            print(f'{msc [1]}')


def tocar_musica_playlist(musica_tocar):
    print('='*30)
    print("Inicio do Player de Músicas")
    print("="*30)
    pygame.mixer.init()
    pygame.mixer.music.load(musica_tocar)
    pygame.mixer.music.play()

    cont = False
    while(cont == False):
        opcoes_playlist = int(input('''
        Digite uma opção:
        1.Aperte para pausar
        2.Aperte para retomar
        3.Aperte para trocar a música
        4.Aperte para sair 
        digite a opção: '''))
        if (opcoes_playlist == 1):
            pygame.mixer.music.pause()
        if (opcoes_playlist == 2):
            pygame.mixer.music.unpause()
        if (opcoes_playlist == 3):
            msc_tocar = input('Digite o nome da música: ')
            msc_tocar2=msc_tocar+'.mp3'
            pygame.mixer.stop()
            pygame.mixer.music.load(msc_tocar2)
            pygame.mixer.music.play()
        if (opcoes_playlist == 4):
            cont = True


#PROGRAMA PRINCIPAL
print('='*30)
print("Inicio do Programa")
print("="*30)
playlist = lePlaylistDeArquivo('playlistMusicas.txt')
numColunas = len(playlist[0])
numLinhas = len(playlist) 

acabou = False
while (acabou == False):
    opcao = int(input(f'''Digite uma opção:\n
    1.Listar músicas da playlist
    2.Pesquisar música por gênero
    3.Cadastrar música
    4.Tocar uma música
    5.Salvar dados
    6.Sair
    digite a opção: '''))
    if (opcao == 1):
        listar_playlist(playlist)
    elif (opcao == 2):
        genero_pesq = input('Qual o gênero a pesquisar: ')
        pesquisa_musica_por_genero(genero_pesq)
    elif (opcao == 3):
        banda = input('Digite o nome da banda: \n')
        msc = input('Digite o nome da música: \n')
        genero = input('Digite o gênero da música: ')
        lista = [banda, msc, genero]
        playlist.append(lista)
    elif (opcao == 4):
        play1 = input('Digite o nome da música que você deseja ouvir: ')
        play2 = play1+'.mp3'
        tocar_musica_playlist(play2)
    elif (opcao==5):
        salvar_novasmsc(playlist,'playlistMusicas.txt')
    elif (opcao==6):
        print('FIM DO PROGRAMA')
        acabou = True
