# Prova 2 - Modulo 8
Repositório voltado para a solução prática realizada durante a prova 2 do módulo 8 de engenharia da computação do Inteli, onde o seguinte era solicitado:

"""
Sua tarefa é montar uma prova de conceito de uma aplicação que utiliza arquiteturas modernas de aprendizado profundo como ferramenta de sintetização de voz, potencialmente agindo como uma ponte valiosa para a comunicação, permitindo que pessoas com desafios na fala, incluindo aquelas no espectro autista, se expressem de maneira mais eficaz em seu cotidiano. Para tal, deve-se desenvolver:

1. Uma interface de terminal. O usuário deve ser capaz de inserir frases para sintetização de forma contínua, sem precisar reinicializar a aplicação cada vez que precisar inserir uma frase.

2. Integração com um modelo de machine learning capaz de sintetização de fala. (Lembre-se que a API da OpenAI está bloqueada durante o período de prova)

3. Reprodução do áudio gerado pelo modelo de sintetização de fala.

Sua entrega de consultoria deve contar com o link do repositório aberto com o código-fonte da PoC desenvolvida. Em seu repositório ainda deve ser possível encontrar instruções claras para execução do projeto. 
"""

## Como executar?
Primeiro, para executar, precisamos possuir o python instalado em nosso sistema, após isso, precisamos digitar o seguinte comando dentro da pasta src para instalar as dependências:

```
pip install -r requirements.txt
```

Com as dependências já baixadas, é possível executar a aplicação digitando:
```
python3 main.py
```

Com isso, é só inserir a frase desejada que o texto será transcrito para aúdio e reproduzido automaticamente.

Caso deseje alterar a linguagem de reprodução, é possível realizar isso alterando a linha 7 do código localizado no main.py.