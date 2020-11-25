from django.db import models


class Time(models.Model):
    nome = models.CharField(max_length=30)
    sigla = models.CharField(max_length=3)
    imagem = models.ImageField(upload_to=f'image/escudo_times/', blank=True)

    def __str__(self):
        return self.nome


class Player(models.Model):
    nome = models.CharField(max_length=30)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, default=None)
    foto = models.ImageField(upload_to=f'image/%d/%m/%Y/', blank=True)
    posicao = models.CharField(max_length=5)
    preco = models.FloatField()
    media = models.FloatField(default=0)
    jogos = models.IntegerField(default=0)
    gols = models.IntegerField(default=0)
    gol_contra = models.IntegerField(default=0)
    gol_sofrido = models.IntegerField(default=0)
    falta_cometida = models.IntegerField(default=0)
    cartao_amarelo = models.IntegerField(default=0)
    cartao_vermelho = models.IntegerField(default=0)
    assistencias = models.IntegerField(default=0)

    # Pontuacao linha
    finalizacao_no_gol = models.IntegerField(default=0)
    finalizacao_para_fora = models.IntegerField(default=0)
    finalizacao_bloqueadas = models.IntegerField(default=0)
    drible_certo = models.IntegerField(default=0)
    drible_errado = models.IntegerField(default=0)
    toques = models.IntegerField(default=0)
    passes_certos = models.IntegerField(default=0)
    passes_errados = models.IntegerField(default=0)
    passes_decisivos = models.IntegerField(default=0)
    cruzamentos = models.IntegerField(default=0)
    bolas_longas = models.IntegerField(default=0)
    duelos_no_chao_certos = models.IntegerField(default=0)
    duelos_no_chao_errados = models.IntegerField(default=0)
    duelos_aereos_certos = models.IntegerField(default=0)
    duelos_aereos_errados = models.IntegerField(default=0)
    perda_da_posse_de_bola = models.IntegerField(default=0)
    faltas = models.IntegerField(default=0)
    faltas_sofridas = models.IntegerField(default=0)
    cortes = models.IntegerField(default=0)
    chutes_travados = models.IntegerField(default=0)
    interceptacaoes = models.IntegerField(default=0)
    desarmes = models.IntegerField(default=0)
    dribles_sofridos = models.IntegerField(default=0)

    # Pontuacao de goleiro
    defesas = models.IntegerField(default=0)
    socos = models.IntegerField(default=0)
    saida_gol_certos = models.IntegerField(default=0)
    saida_gol_errados = models.IntegerField(default=0)
    bola_aerea_pega = models.IntegerField(default=0)
    defesa_dentro_area = models.IntegerField(default=0)
