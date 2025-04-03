# Pong em Python

Este é um jogo clássico de Pong desenvolvido em Python utilizando a biblioteca `pygame`. O jogo permite partidas entre dois jogadores e registra as pontuações em um arquivo de texto.

## Sobre o Jogo
Pong é um dos primeiros jogos eletrônicos de arcade criados, lançado originalmente em 1972. Neste remake em Python, dois jogadores controlam raquetes verticais para rebater a bola. O objetivo é marcar pontos ao fazer com que a bola passe pelo adversário.

## Requisitos
Antes de executar o jogo, certifique-se de ter o Python instalado e instale a biblioteca `pygame` se ainda não a tiver:

```sh
pip install pygame
```

## Como Jogar
- **Jogador 1:**
  - Mover para cima: `W`
  - Mover para baixo: `S`
- **Jogador 2:**
  - Mover para cima: `Seta para cima`
  - Mover para baixo: `Seta para baixo`

O objetivo do jogo é marcar pontos fazendo a bola ultrapassar o adversário. A bola rebaterá nas paredes e nas raquetes dos jogadores.

## Como Executar
Para rodar o jogo, siga estes passos:

1. Certifique-se de que o Python está instalado no seu sistema.
2. Instale a biblioteca `pygame` caso ainda não tenha:
   ```sh
   pip install pygame
   ```
3. Execute o script do jogo com o seguinte comando:
   ```sh
   python pong.py
   ```
4. O jogo abrirá em uma nova janela.
5. Dois jogadores podem jogar usando as teclas `W` e `S` (Jogador 1) e as setas direcionais `↑` e `↓` (Jogador 2).
6. Cada vez que um jogador marca um ponto, a bola é reposicionada no centro.

## Registro de Pontuações
As pontuações das partidas são salvas no arquivo `pontuacoes.txt`, onde cada linha representa uma partida no formato:
```
Jogador1 - Jogador2
```
Isso permite que os jogadores acompanhem o histórico de suas partidas.

## Controles e Mecânica
- A bola rebaterá nas paredes e nas raquetes dos jogadores.
- Ao marcar um ponto, a bola reinicia no centro do campo.
- O jogo roda a 60 FPS para uma experiência fluida.
- As raquetes podem se mover para cima e para baixo sem ultrapassar os limites da tela.

## Possíveis Melhorias
Caso queira aprimorar o jogo, aqui estão algumas sugestões:
- **Adicionar um placar mais avançado:** Exibir nomes dos jogadores ou manter um histórico mais detalhado.
- **Melhorar os gráficos:** Incluir animações ou efeitos sonoros.
- **Criar um modo de IA:** Implementar um adversário controlado pelo computador.
- **Ajustar a dificuldade:** Modificar a velocidade da bola conforme o jogo avança.

## Contribuições
Sinta-se à vontade para modificar e melhorar o jogo! Caso queira adicionar novas funcionalidades, faça um fork do repositório e contribua.

Divirta-se jogando Pong! 🏓


