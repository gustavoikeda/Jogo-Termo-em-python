# Clone do Jogo Termo em Python

Este projeto é uma recriação do jogo Termo, desenvolvida em Python para ser executada no terminal. O objetivo do jogo é adivinhar uma palavra secreta de 5 letras em até 6 tentativas, com feedback visual que orienta o jogador após cada tentativa:

- 🟩 Letra correta no lugar certo (verde)
- 🟨 Letra presente na palavra, mas na posição errada
- ⬜ Letra não existente na palavra

O programa utiliza a biblioteca termcolor para aplicar cores no terminal e um arquivo .txt contendo palavras válidas com 5 letras.

# ✅ Funcionalidades
- Validação de entrada: apenas palavras com 5 letras e presentes no dicionário.
- Feedback colorido após cada tentativa.
- Lógica completa de verificação com suporte a letras repetidas

# 🛠 Tecnologias
- Python 3
- termcolor (para dar cor às letras)
- Arquivo .txt como dicionário de palavras

# 📥 Instalação
Instale a dependência:

```
pip install termcolor
```
