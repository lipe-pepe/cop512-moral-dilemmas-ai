# IA e Dilemas Morais

Projeto em Python que utiliza um modelo de linguagem executado localmente para responder a dilemas morais e registrar os resultados para análise.

Desenvolvido para a disciplina **COP512 — Comunicação e Tecnologias Cognitivas**, da **Universidade Federal do Rio de Janeiro (UFRJ)**.

Os dilemas são baseados no estudo *Moral judgment reloaded: A moral dilemma validation study*, de Christensen et al. (2014). O modelo deve escolher entre `YES` e `NO` e fornecer uma justificativa curta em inglês.

O modelo é executado localmente pelo [Ollama](https://ollama.com/), sem necessidade de API externa ou chave de API.

As hipóteses, o desenho experimental, os resultados preliminares e as limitações estão descritos em [`EXPERIMENTO.md`](EXPERIMENTO.md).

## Estrutura do projeto

```text
moral-ai-dilemmas/
├── dilemmas/
├── results/
├── analyze_results.py
├── config.py
├── dataset.py
├── dilemmas_metadata.csv
├── EXPERIMENTO.md
├── model.py
├── prompts.py
├── results.py
├── run_experiment.py
├── validate_dataset.py
└── README.md
```

## Requisitos

- Python 3;
- `pip` e `venv`;
- Ollama;
- modelo `llama3.2:3b`.

## Instalação

Clone o repositório:

```bash
git clone git@github.com:lipe-pepe/cop512-moral-dilemmas-ai.git moral-ai-dilemmas
cd moral-ai-dilemmas
```

No Ubuntu ou WSL, instale o suporte ao ambiente virtual:

```bash
sudo apt update
sudo apt install python3-pip python3-venv
```

Crie e ative o ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale a dependência Python:

```bash
python -m pip install ollama
```

## Ollama

Instale o Ollama no Ubuntu ou WSL:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Baixe o modelo:

```bash
ollama pull llama3.2:3b
```

Em sistemas sem `systemd`, inicie o servidor manualmente em outro terminal:

```bash
ollama serve
```

Mantenha esse terminal aberto durante a execução. Em outro terminal, entre na pasta do projeto e ative novamente o ambiente virtual.

## Configuração

Os principais parâmetros ficam em `config.py`:

```python
MODEL_NAME = "llama3.2:3b"
NUMBER_OF_DILEMMAS = None
REPETITIONS = 10
TEMPERATURE = 0.7
```

`NUMBER_OF_DILEMMAS = None` utiliza todos os dilemas disponíveis.

## Execução

Valide os arquivos e metadados:

```bash
python validate_dataset.py
```

Execute o experimento:

```bash
python run_experiment.py
```

Cada execução cria um arquivo `.jsonl` dentro de `results/`. Cada linha representa uma resposta do modelo a um dilema.

## Análise

Liste os arquivos de resultado:

```bash
ls results
```

Analise a execução desejada:

```bash
python analyze_results.py results/NOME_DO_ARQUIVO.jsonl
```

O script compara as taxas de respostas utilitaristas entre dilemas pessoais e impessoais. Consulte [`EXPERIMENTO.md`](EXPERIMENTO.md) para entender as hipóteses e a interpretação dos resultados.

## Referência

Christensen, J. F., Flexas, A., Calabrese, M., Gut, N. K., & Gomila, A. (2014). Moral judgment reloaded: A moral dilemma validation study. *Frontiers in Psychology, 5*, Article 607. <https://doi.org/10.3389/fpsyg.2014.00607>
