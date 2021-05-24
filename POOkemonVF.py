from random import randint, choice
from pygame import mixer
from time import sleep

class jogador:  # NIVEL 4
    def __init__(self, nome, player_pokemons, pot):
        self.nome = nome
        self.player_pokemons = player_pokemons
        self.pot = pot

    def troca(self):
        if self == jogador1:
            for i, v in enumerate(self.player_pokemons):
                if i == len(self.player_pokemons) - 1:
                    print(f'{i + 1}. {v.nome}')
                else:
                    print(f'{i + 1}. {v.nome}')
            op = int(input('\033[1;30mEscolha quem entra!\033[m '))
            aliado = self.player_pokemons[op - 1]
            return aliado
        elif self == jogador2:
            inimigo = choice(jogador2.player_pokemons)
            return inimigo

    def selectPokemon(self, oponente):
        pokemons = [bulbassauro, charmander, cyndaquill, treecko, eevee, totodile, squirtle, godmode]
        indices = []
        for i, v in enumerate(pokemons):  # NIVEL 4
            indices.append(i)
        indices.append(len(pokemons))  # O for só faz append até i-1

        for c in range(0, 3):  # PREENCHER SUA LISTA, SEM REPETIR
            for i, v in enumerate(pokemons):
                if i == 0:
                    print()
                print(f'{i + 1}. ', v.nome)
            print(f'{len(pokemons) + 1}.  Aleatório')
            p1 = int(input(f'\nEscolha seu pokemon #{c + 1}: '))
            if p1 - 1 not in indices:
                print('Insira uma opção válida!')
            else:
                if p1 == len(pokemons) + 1:
                    p1 = randint(1, len(pokemons))
            self.player_pokemons.append(pokemons[p1 - 1])
            pokemons.remove(pokemons[p1 - 1])

    def equipeMostra(self, oponente):
        print('Sua equipe: ', end=' ')
        for c in range(0, len(self.player_pokemons)):  # PREENCHER A DO ADVERSÁRIO, SEM REPETIR
            if c == len(self.player_pokemons) - 1:
                print(self.player_pokemons[c].nome, end=' ')
            else:
                print(self.player_pokemons[c].nome, end=', ')
        for c in range(0, 3):
            p = choice(pokemons)
            oponente.player_pokemons.append(p)
            pokemons.remove(p)

        print('\nEquipe adversária: ', end=' ')
        for c in range(0, len(oponente.player_pokemons)):
            if c == len(oponente.player_pokemons) - 1:
                print(oponente.player_pokemons[c].nome, end=' ')
            else:
                print(oponente.player_pokemons[c].nome, end=', ')

    def derrota(self):
        print(f'\033[1;30m{self.nome} chegou a 0 pokemons e perdeu a batalha!\033[m')

    def vitoria(self):
        print(f'\033[1;30m{self.nome} derrotou todos os pokemons adversários e ganhou a batalha!\033[m')


class ataque:  # NIVEL 2
    def __init__(self, nome, tipo, dano, pp):
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.pp = pp
        self.precisao = 92

    def ataqueInfo(self):
        print(f'Dano: {self.dano}')
        print(f'Tipo: {self.tipo}')
        print(f'Quantidade de usos: {self.quantidade}')


class Pokemon:  # NIVEL 1
    def __init__(self, nome, tipo, nivel, ataques, fraqueza, fortitude, vida, velocidade):
        self.nome = nome
        self.tipo = tipo
        self.ataques = ataques
        self.vida = vida
        self.vidamax = vida
        self.fraqueza = fraqueza
        self.fortitude = fortitude
        self.nivel = nivel
        self.velocidade = velocidade

    def pokeInfo(self):
        print('Nome: ', self.nome)
        print('Tipo: ', self.tipo)
        print('Nivel: ', self.nivel)
        print('Ataques: ', self.ataques)
        print('Fraco contra: ', self.fraqueza)
        print('Forte contra: ', self.fortitude)
        print('Vida: ', self.vida)
        print('Velocidade: ', self.velocidade)

    def infoBatalha(self, oponente):
        print('\033[1;30m=========BATALHA POKEMON=========\033[m')
        print(oponente.nome, end=': ')
        print(f"\033[1;92m{oponente.vida}/{oponente.vidamax}\033[m")
        print(f'Tipo: {oponente.tipo}', end=' | ')
        print(f'Velocidade {oponente.velocidade}')
        print('              \033[1;31mVS\033[m                ')
        print(self.nome, end=': ')
        print(f"\033[1;92m{self.vida}/{self.vidamax}\033[m")
        print(f'Tipo: {self.tipo}', end=' | ')
        print(f'Velocidade {self.velocidade}')
        print('\033[1;30m=================================\033[m')

    def ataque(self, oponente, op):  # atacante, adversário, opção de ataque
        print(f'\n{self.nome} usou {self.ataques[op - 1].nome}')
        acertou = randint(0, 100)
        if acertou < self.ataques[op - 1].precisao:
            if self.ataques[op - 1].pp > 0:
                if self.ataques[op - 1].tipo == oponente.fraqueza:
                    oponente.vida -= (self.ataques[op - 1].dano) * 1.5
                    print('\033[1;33mITS SUPER EFFECTIVE!\033[m\n')
                elif self.ataques[op - 1].tipo == oponente.fortitude:
                    oponente.vida -= (self.ataques[op - 1].dano) * 0.75
                    print('\033[1;30mIts not very effective...\033[m\n')
                else:
                    oponente.vida -= self.ataques[op - 1].dano
                self.ataques[op - 1].pp -= 1
            elif self.ataques[op - 1].pp <= 0:
                self.ataques[op - 1].pp = 0
                print('Você já usou todas as cargas desse ataque! Perdeu sua vez!')
        else:
            print('Errou!')
            self.ataques[op - 1].pp -= 1

    def poçao(self, oponente, jogador, i): # pokemon a ser curado, oponente, jogador usando a poção, indice da opção def
        op = i + 2
        if jogador.pot > 0:
            if self.vida < self.vidamax:
                print(f'\n{self.nome} usou \033[1;31mPoção de HP!\033[m')
                self.vida += 10
                jogador.pot -= 1
            else:
                print('Sua vida já está cheia!')
                while op == i + 2:
                    for i, v in enumerate(self.ataques):
                        print(f'{i + 1}.', v.nome, end=' ')
                        print(f'({v.tipo})', end=' ')
                        print(f'Usos restantes: {v.pp}')
                    op = int(input('Escolha seu movimento! '))
                    self.ataque(oponente, op)
        else:
            print('Você está sem poções!')
            while op == i + 2:
                for i, v in enumerate(self.ataques):
                    print(f'{i + 1}.', v.nome, end=' ')
                    print(f'({v.tipo})', end=' ')
                    print(f'Usos restantes: {v.pp}')
                op = int(input('Escolha seu movimento! '))
                self.ataque(oponente, op)

    def batalha(self, oponente):  # NIVEL 3
        if len(jogador1.player_pokemons) > 0 and len(jogador2.player_pokemons) > 0:
            self.infoBatalha(oponente)
            while len(jogador1.player_pokemons) > 0 and len(jogador2.player_pokemons) > 0:
                atual = self
                inimigo = oponente
                if self.velocidade >= oponente.velocidade:
                    if self.vida > 0:
                        for i, v in enumerate(self.ataques):
                            print(f'{i + 1}.', v.nome, end=' ')
                            print(f'({v.tipo})', end=' ')
                            print(f'Usos restantes: {v.pp}')
                        print(f'{i + 2}. Poção (10 HP) ({jogador1.pot} restantes)')
                        print(f'{i + 3}. Trocar Pokemon')
                        op = int(input('Escolha seu movimento! '))
                        if op == i + 2:
                            self.poçao(oponente, jogador1, i)
                        elif op == i + 3:
                            troca = jogador1.troca()
                            troca.batalha(inimigo)
                        else:
                            self.ataque(oponente, op)
                        if oponente.vida <= 0 and len(jogador2.player_pokemons) > 0:
                            oponente.vida = 0
                            self.infoBatalha(oponente)
                            print(f'{oponente.nome} chegou a 0 pontos de vida! Você ganhou!')
                            jogador2.player_pokemons.remove(inimigo)
                            if len(jogador2.player_pokemons) == 0:
                                return
                                break
                            else:
                                troca = jogador2.troca()
                                atual.batalha(troca)
                    if oponente.vida > 0:
                        if oponente.vida < oponente.vidamax - 10 and jogador2.pot > 0:
                            if jogador2.pot > 0:
                                if oponente.vida < oponente.vidamax:
                                    print(f'\n{oponente.nome} usou \033[1;31mPoção de HP!\033[m\n')
                                    oponente.vida += 10
                                    jogador2.pot -= 1
                        else:
                            ataqueop = randint(1, 2)
                            oponente.ataque(self, ataqueop)
                        if self.vida <= 0 and len(jogador1.player_pokemons) > 0:
                            self.vida = 0
                            self.infoBatalha(oponente)
                            print(f'{atual.nome} chegou a 0 pontos de vida! Você perdeu a rodada!')
                            jogador1.player_pokemons.remove(atual)
                            if len(jogador1.player_pokemons) <= 0:
                                return
                                break
                            else:
                                atual = jogador1.troca()
                                atual.batalha(inimigo)
                        if self.vida > 0 and oponente.vida > 0:
                            self.infoBatalha(oponente)
                else:
                    if oponente.vida > 0:
                        if oponente.vida < oponente.vidamax - 10 and jogador2.pot > 0:
                            if jogador2.pot > 0:
                                if oponente.vida < oponente.vidamax:
                                    print(f'\n{oponente.nome} usou \033[1;31mPoção de HP!\033[m')
                                    oponente.vida += 10
                                    jogador2.pot -= 1
                        else:
                            ataqueop = randint(1, 2)
                            oponente.ataque(self, ataqueop)
                        if self.vida <= 0 and len(jogador1.player_pokemons) > 0:
                            self.vida = 0
                            self.infoBatalha(oponente)
                            print(f'{atual.nome} chegou a 0 pontos de vida! Você perdeu a rodada!')
                            jogador1.player_pokemons.remove(atual)
                            if len(jogador1.player_pokemons) <= 0:
                                return
                                break
                            else:
                                atual = jogador1.troca()
                                atual.batalha(inimigo)
                    if self.vida > 0:
                        for i, v in enumerate(self.ataques):
                            print(f'{i + 1}.', v.nome, end=' ')
                            print(f'({v.tipo})', end=' ')
                            print(f'Usos restantes: {v.pp}')
                        print(f'{i + 2}. Poção (10 HP) ({jogador1.pot} restantes)')
                        print(f'{i + 3}. Trocar Pokemon')
                        op = int(input('Escolha seu movimento! '))
                        if op == i + 2:
                            self.poçao(oponente, jogador1, i)
                        elif op == i + 3:
                            atual = jogador1.troca()
                            atual.batalha(inimigo)
                        else:
                            self.ataque(oponente, op)
                            if oponente.vida <= 0 and len(jogador2.player_pokemons) > 0:
                                oponente.vida = 0
                                self.infoBatalha(oponente)
                                print(f'{oponente.nome} chegou a 0 pontos de vida! Você ganhou!')
                                jogador2.player_pokemons.remove(inimigo)
                                if len(jogador2.player_pokemons) <= 0:
                                    return
                                    break
                                else:
                                    troca = jogador2.troca()
                                    atual.batalha(troca)
                        if self.vida > 0 and oponente.vida > 0:
                            self.infoBatalha(oponente)


# Lista de Pokemon's
# objeto ataque = ataque('Nome', 'Tipo', Dano, PP(Número de usos por partida)
tackle = ataque('Tackle', '\033[1;30mNormal\033[m', 5, 50)
vinewp = ataque('Vine Whip', '\033[1;32mGrama\033[m', 15, 3)
ember = ataque('Ember', '\033[1;31mFogo\033[m', 15, 3)
razorl = ataque('Razor Leaf', '\033[1;32mGrama\033[m', 15, 3)
tailw = ataque('Tail Whip', '\033[1;30mNormal\033[m', 10, 50)
watergun = ataque('Water Gun', '\033[1;34mÁgua\033[m', 15, 3)
bubbles = ataque('Bubbles', '\033[1;34mÁgua\033[m', 15, 3)
godata = ataque('IK', '\033[1;31mFogo\033[m', 100, 500)

# objeto pokemon = Pokemon('Nome', 'Tipo', Nível, objetos ataquem, 'Fraqueza', 'Fortitude', Vida, Velocidade
bulbassauro = Pokemon('Bulbassauro', '\033[1;32mGrama\033[m', 1, [tackle, vinewp], '\033[1;31mFogo\033[m', '\033[1;34mÁgua\033[m', 49, 19)
charmander = Pokemon('Charmander', '\033[1;31mFogo\033[m', 1, [tackle, ember], '\033[1;34mÁgua\033[m', '\033[1;32mGrama\033[m', 48, 12)
cyndaquill = Pokemon('Cyndaquill', '\033[1;31mFogo\033[m', 1, [tackle, ember], '\033[1;34mÁgua\033[m', '\033[1;32mGrama\033[m', 50, 20)
treecko = Pokemon('Treecko', '\033[1;32mGrama\033[m', 1, [tackle, razorl], '\033[1;31mFogo\033[m', '\033[1;34mÁgua\033[m', 51, 16)
eevee = Pokemon('Eevee', '\033[1;30mNormal\033[m', 1, [tackle, tailw], 'N/A', 'N/A', 45, 17)
totodile = Pokemon('Totodile', '\033[1;34mÁgua\033[m', 1, [tackle, watergun], '\033[1;32mGrama\033[m', '\033[1;31mFogo\033[m', 46, 10)
squirtle = Pokemon('Squirtle', '\033[1;34mÁgua\033[m', 1, [tackle, bubbles], '\033[1;32mGrama\033[m', '\033[1;31mFogo\033[m', 48, 20)
godmode = Pokemon('GodMode', '\033[1;31mFogo\033[m', 0, [godata, bubbles], '\033[1;31mFogo\033[m', '\033[1;31mFogo\033[m', 600, 100)

# objeto jogador = jogador('Nome', Pokemons, Número de Poções
jogador1 = jogador('Você', [], 3)
jogador2 = jogador('Ash Ketchum', [], 3)

pokemons = [bulbassauro, charmander, cyndaquill, treecko, eevee, totodile, squirtle, godmode]
indices = []

jogador1.selectPokemon(jogador2)
jogador1.equipeMostra(jogador2)
print()
atual = jogador1.troca()
inimigo = choice(jogador2.player_pokemons)
mixer.init()
mixer.music.load('prbm.mp3')
mixer.music.play()
mixer.music.set_volume(0.1)
sleep(1.0)
atual.batalha(inimigo)
if len(jogador1.player_pokemons) == 0:
    jogador2.vitoria()
    jogador1.derrota()
elif len(jogador2.player_pokemons) == 0:
    mixer.init()
    mixer.music.load('win.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.1)
    sleep(0.5)
    jogador1.vitoria()
    jogador2.derrota()
    delay = input('\n\033[1;30mPressione qualquer tecla para sair!\033[m')


