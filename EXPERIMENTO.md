# Experimento de julgamento moral com modelo de linguagem

## 1. Contexto

Este experimento foi desenvolvido para a disciplina **COP512 — Comunicação e Tecnologias Cognitivas**, da Universidade Federal do Rio de Janeiro (UFRJ).

O objetivo é investigar como um modelo de linguagem executado localmente responde a dilemas morais e, especificamente, se a **força pessoal** do dilema altera a frequência de respostas utilitaristas.

Os dilemas são baseados no estudo de Christensen et al. (2014), *Moral judgment reloaded: A moral dilemma validation study*. Nesta etapa, os dilemas são classificados como:

- `personal`: a ação envolve força pessoal;
- `impersonal`: a ação não envolve força pessoal.

Embora os arquivos também possuam informações sobre intencionalidade, a análise atual concentra-se apenas na força pessoal.

## 2. Pergunta de pesquisa

A probabilidade de o modelo produzir uma resposta utilitarista é menor em dilemas pessoais do que em dilemas impessoais?

## 3. Classificação das respostas

Cada dilema pergunta se uma ação deve ou não ser realizada. Para a análise, as respostas são codificadas da seguinte forma:

| Resposta | Classificação | Valor |
| --- | --- | ---: |
| `YES` | Utilitarista | `1` |
| `NO` | Deontológica | `0` |

Essa é uma definição operacional usada no experimento. Ela não afirma que exista uma resposta moral objetivamente correta.

## 4. Hipóteses

**Hipótese nula (H0):** a força pessoal do dilema não altera a probabilidade de uma resposta utilitarista.

\[
p_{personal} = p_{impersonal}
\]

**Hipótese alternativa (H1):** dilemas pessoais produzem uma proporção menor de respostas utilitaristas do que dilemas impessoais.

\[
p_{personal} < p_{impersonal}
\]

## 5. Modelo e condições

O experimento foi executado localmente com:

```text
Modelo: llama3.2:3b
Sistema de execução: Ollama
Temperatura: 0.7
Dilemas: 52
Trials por dilema: 10
```

O prompt, a temperatura, o modelo e o formato esperado da resposta foram mantidos iguais em todos os trials. As sementes variaram entre as repetições.

## 6. Trials e desenho experimental

Um **trial** corresponde a uma apresentação de um dilema ao modelo e à gravação de sua resposta.

Cada um dos 52 dilemas foi apresentado dez vezes. Assim, o experimento produziu:

\[
52\ dilemas \times 10\ trials = 520\ respostas
\]

As repetições permitem observar se o modelo responde sempre da mesma forma ou se sua decisão varia para um mesmo dilema.

As 520 respostas não devem ser consideradas 520 dilemas independentes. Existem apenas 52 dilemas, cada um repetido dez vezes. Essa dependência precisa ser considerada em uma análise estatística futura.

## 7. Dados registrados

Os metadados dos dilemas ficam em `dilemmas_metadata.csv`. Cada linha identifica o arquivo do dilema e suas categorias.

Cada trial é gravado como uma linha em um arquivo JSON Lines dentro de `results/`. O registro inclui:

- identificador do experimento;
- data e hora;
- modelo utilizado;
- identificador e arquivo do dilema;
- força pessoal;
- intencionalidade;
- número da repetição;
- semente e temperatura;
- decisão `YES` ou `NO`;
- classificação utilitarista;
- justificativa;
- resposta original do modelo.

Cada execução cria um arquivo próprio, por exemplo:

```text
results/baseline_2026-09-21_19-42-08.jsonl
```

Isso evita misturar trials de execuções diferentes.

## 8. Como executar

### 8.1 Ativar o ambiente virtual

```bash
source .venv/bin/activate
```

### 8.2 Iniciar o Ollama

Em outro terminal, execute:

```bash
ollama serve
```

Esse terminal deve permanecer aberto durante o experimento.

### 8.3 Confirmar o modelo

```bash
ollama list
```

Se o modelo ainda não estiver instalado:

```bash
ollama pull llama3.2:3b
```

### 8.4 Validar o conjunto de dilemas

```bash
python validate_dataset.py
```

### 8.5 Configurar o experimento

Os principais parâmetros ficam em `config.py`:

```python
MODEL_NAME = "llama3.2:3b"
NUMBER_OF_DILEMMAS = None
REPETITIONS = 10
TEMPERATURE = 0.7
```

`NUMBER_OF_DILEMMAS = None` faz o programa utilizar todos os dilemas disponíveis.

### 8.6 Executar o experimento

```bash
python run_experiment.py
```

Ao final, um novo arquivo `.jsonl` será criado em `results/`.

### 8.7 Analisar os resultados

Informe ao script o arquivo que deve ser analisado:

```bash
python analyze_results.py results/NOME_DO_ARQUIVO.jsonl
```

O script apresenta o total de respostas, a quantidade de respostas utilitaristas em cada grupo, as taxas observadas e a diferença entre os grupos.

## 9. Resultado preliminar

Foram obtidas 520 respostas:

| Grupo | Trials | Respostas utilitaristas | Taxa utilitarista |
| --- | ---: | ---: | ---: |
| Pessoal | 260 | 9 | 3,46% |
| Impessoal | 260 | 15 | 5,77% |

A diferença observada foi:

\[
5{,}77\% - 3{,}46\% = 2{,}31\ pontos\ percentuais
\]

Portanto, a taxa utilitarista foi menor nos dilemas pessoais, na direção prevista por H1.

Entretanto, as 24 respostas utilitaristas ficaram concentradas em apenas quatro dilemas:

| Dilema | Força pessoal | Respostas utilitaristas |
| --- | --- | ---: |
| 30 | Impessoal | 5/10 |
| 31 | Pessoal | 6/10 |
| 38 | Impessoal | 10/10 |
| 51 | Pessoal | 3/10 |

Nos outros 48 dilemas, todos os trials produziram respostas deontológicas.

## 10. Interpretação

O resultado preliminar está na direção prevista pela hipótese alternativa: o modelo apresentou uma taxa utilitarista menor em dilemas pessoais do que em dilemas impessoais.

Contudo, ainda não foi realizado um teste de significância estatística. Portanto, não é possível afirmar que a diferença observada seja um efeito sistemático da força pessoal, nem rejeitar H0. A diferença pode estar relacionada à variação do modelo ou às características particulares dos quatro dilemas que produziram respostas utilitaristas.

A conclusão adequada para esta etapa é:

> A taxa utilitarista foi menor nos dilemas pessoais (3,46%) do que nos impessoais (5,77%), uma diferença de 2,31 pontos percentuais na direção prevista pela hipótese alternativa. Entretanto, como ainda não foi aplicado um teste de significância estatística e as respostas utilitaristas se concentraram em poucos dilemas, o resultado deve ser considerado preliminar.

## 11. Limitações e continuação

- Os trials de um mesmo dilema não são observações totalmente independentes.
- As respostas utilitaristas ficaram concentradas em quatro dilemas.
- O comportamento pode variar com modelo, versão, temperatura, semente e prompt.
- O experimento utilizou apenas um modelo local.
- As classificações `YES` e `NO` são definições operacionais deste conjunto de dilemas.
- Os resultados descrevem o comportamento do modelo nas condições testadas e não demonstram compreensão moral humana.

Como continuação, deve ser aplicado um teste estatístico que considere cada dilema como unidade de análise, como um teste de permutação sobre as taxas agregadas dos 52 dilemas.

## 12. Referência

Christensen, J. F., Flexas, A., Calabrese, M., Gut, N. K., & Gomila, A. (2014). Moral judgment reloaded: A moral dilemma validation study. *Frontiers in Psychology, 5*, Article 607. <https://doi.org/10.3389/fpsyg.2014.00607>
