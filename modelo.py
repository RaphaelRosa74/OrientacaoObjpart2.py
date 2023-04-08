class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self._likes} Likes'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f' {self._nome} - {self.ano} - {self.temporadas} temp - {self._likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)


vingadores = Filme("Vingadores", 2010, 120)
sandman = Serie("Sandman", 2022, 1)
gg = Filme("Gente Grande", 2010, 100)
got = Serie("Game of Thrones", 2013, 9)

vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
sandman.dar_likes()
sandman.dar_likes()
gg.dar_likes()
gg.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()
got.dar_likes()

filmes_e_series = [vingadores, sandman, gg, got]
play_fds = Playlist("Fim de Semana", filmes_e_series)

print(f"Tamanho da playlist: {len(play_fds)}")

for programa in play_fds:
    print(programa)