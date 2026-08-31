# IA e Dilemas Morais

Projeto em Python que utiliza um modelo de linguagem executado localmente para tomar decisões diante de dilemas morais.

Este projeto foi desenvolvido para a disciplina **COP512 — Comunicação e Tecnologias Cognitivas**, da **Universidade Federal do Rio de Janeiro (UFRJ)**.

## Sobre o projeto

O programa apresenta um dilema moral a um modelo de inteligência artificial e solicita que ele decida se realizaria ou não a ação proposta no cenário.

Os dilemas utilizados são baseados no estudo:

> Christensen, J. F., Flexas, A., Calabrese, M., Gut, N. K., & Gomila, A. (2014). *Moral judgment reloaded: A moral dilemma validation study*. Frontiers in Psychology, 5, 607.

O estudo apresenta um conjunto revisado e validado de dilemas morais, desenvolvido para investigar como diferentes características de uma situação podem influenciar o julgamento moral.

Neste projeto, o dilema selecionado é lido de um arquivo de texto e enviado para um modelo de linguagem. O modelo deve:

* escolher exatamente entre `YES` e `NO`;
* responder em inglês;
* fornecer uma justificativa curta;
* não criar uma solução alternativa fora das opções do dilema.

O modelo é executado localmente por meio do [Ollama](https://ollama.com/). Portanto, o projeto não depende de uma API externa nem exige uma chave de API.

## Estrutura do projeto

```text
moral-ai-dilemmas/
├── dilemmas/
│   ├── dilemma_01.txt
│   ├── dilemma_02.txt
│   └── ...
├── main.py
├── .gitignore
└── README.md
```

Cada arquivo dentro da pasta `dilemmas/` contém um dilema moral completo, incluindo sua pergunta final.

## Requisitos

Antes de executar o projeto, é necessário ter:

* Python 3 instalado;
* `pip` e `venv` instalados;
* Ollama instalado;
* modelo `llama3.2:3b` baixado.

## Instalação

### 1. Clonar o repositório

```bash
git clone git@github.com:lipe-pepe/cop512-moral-dilemmas-ai.git
cd moral-ai-dilemmas
```
### 2. Instalar os recursos necessários do Python

No Ubuntu ou WSL:

```bash
sudo apt update
sudo apt install python3-pip python3-venv
```

### 3. Criar um ambiente virtual

Dentro da pasta do projeto, execute:

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

```bash
source .venv/bin/activate
```

Depois da ativação, o terminal deverá exibir `(.venv)` antes do comando.

### 4. Instalar as dependências do projeto

Com o ambiente virtual ativado, execute:

```bash
python -m pip install ollama
```

## Instalação do Ollama

No Ubuntu ou WSL, instale o Ollama usando:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Confirme se a instalação foi concluída:

```bash
ollama --version
```

## Inicialização do Ollama

O servidor do Ollama precisa estar em execução antes de iniciar o programa em Python.

### Ubuntu com systemd

Inicie o serviço:

```bash
sudo systemctl start ollama
```

Verifique o status:

```bash
systemctl status ollama
```

Se o status mostrar `active (running)`, o Ollama está funcionando.

### WSL ou sistemas sem systemd

Inicie o servidor manualmente:

```bash
ollama serve
```

Mantenha esse terminal aberto enquanto utiliza o projeto.

Abra outro terminal, entre novamente na pasta do projeto e ative o ambiente virtual:

```bash
cd moral-ai-dilemmas
source .venv/bin/activate
```

## Download do modelo local

Baixe o modelo utilizado pelo projeto:

```bash
ollama pull llama3.2:3b
```

Confirme se o modelo está disponível:

```bash
ollama list
```

Também é possível testá-lo diretamente:

```bash
ollama run llama3.2:3b
```

Para encerrar a conversa direta com o modelo, utilize:

```text
/bye
```

## Seleção do dilema

O dilema é selecionado diretamente no arquivo `main.py`.

Encontre a variável:

```python
DILEMMA_FILE = "dilemma_01.txt"
```

Para testar outro dilema, altere seu valor para o nome de outro arquivo presente na pasta `dilemmas/`:

```python
DILEMMA_FILE = "dilemma_02.txt"
```

O nome informado precisa corresponder exatamente ao nome de um arquivo existente.

## Execução do projeto

Antes da execução, verifique se:

1. o Ollama está em funcionamento;
2. o modelo `llama3.2:3b` foi baixado;
3. o ambiente virtual do Python está ativado;
4. o arquivo do dilema selecionado existe.

Execute o programa:

```bash
python main.py
```

O programa irá:

1. ler o dilema selecionado;
2. montar as instruções para o modelo;
3. enviar o dilema ao modelo local;
4. exibir a decisão e a justificativa geradas.

A saída deverá seguir este formato:

```text
Decision: YES
Justification: A short explanation of the model's decision.
```

ou:

```text
Decision: NO
Justification: A short explanation of the model's decision.
```

Embora o README esteja em português, as respostas do modelo são apresentadas em inglês.

## Executando novamente

Ao abrir um novo terminal, ative novamente o ambiente virtual:

```bash
source .venv/bin/activate
```

Se o Ollama não estiver sendo executado automaticamente, abra outro terminal e inicie o servidor:

```bash
ollama serve
```

Depois, execute o projeto:

```bash
python main.py
```

## Considerações importantes

O programa não identifica uma resposta moral objetivamente correta. Sua saída representa uma decisão gerada por um modelo de linguagem de acordo com seu treinamento e com as instruções fornecidas no prompt.

Modelos, prompts ou execuções diferentes podem produzir decisões diferentes. Portanto, os resultados devem ser tratados como material para o estudo de inteligência artificial e julgamento moral, e não como orientações éticas definitivas.

## Referência

Christensen, J. F., Flexas, A., Calabrese, M., Gut, N. K., & Gomila, A. (2014). Moral judgment reloaded: A moral dilemma validation study. *Frontiers in Psychology, 5*, Article 607. https://doi.org/10.3389/fpsyg.2014.00607
