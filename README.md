# 📊 Análise de Perfil de Clientes com Pandas e Plotly

Este projeto realiza uma **análise exploratória de dados (EDA)** a partir de uma base de clientes, utilizando **Python**, **Pandas** e **Plotly** para identificar padrões e traçar o **perfil ideal de clientes** com base em notas de avaliação.

O foco é entender **quais características influenciam a nota do cliente (1–100)** por meio de estatísticas descritivas e visualizações interativas.

---

## 🧰 Tecnologias Utilizadas

* **Python 3.9+**
* **Pandas** – Limpeza e análise de dados
* **Plotly Express** – Visualização de dados interativa

---

## 📁 Estrutura do Projeto

```bash
📦 analise-clientes
 ┣ 📄 analise_clientes.py
 ┣ 📄 clientes.csv
 ┗ 📄 README.md
```

---

## 📌 Base de Dados (`clientes.csv`)

* Codificação: `latin`
* Separador: `;`

### Principais Colunas Utilizadas

| Coluna                  | Descrição                      |
| ----------------------- | ------------------------------ |
| ClienteID               | Identificador único do cliente |
| Idade                   | Idade do cliente               |
| Profissão               | Área profissional              |
| Salário Anual (R$)      | Renda anual                    |
| Experiência de Trabalho | Tempo de experiência           |
| Tamanho Família         | Quantidade de pessoas          |
| Origem                  | Tipo de compra                 |
| Nota (1-100)            | Avaliação do cliente           |

---

## 🧹 Tratamento de Dados

O script executa as seguintes etapas:

1. Leitura do arquivo CSV
2. Remoção de coluna inválida (`Unnamed: 8`)
3. Conversão da coluna **Salário Anual (R$)** para tipo numérico
4. Tratamento de valores inválidos (`errors='coerce'`)
5. Remoção de valores nulos
6. Análise estatística com `.describe()`

---

## 📈 Análise Exploratória (EDA)

Para cada coluna (exceto `ClienteID` e `Nota (1-100)`), o script gera:

* 📊 **Histogramas interativos**
* 📐 Média da nota do cliente por faixa de valores
* 🔢 Agrupamento automático com `nbins=16`

Exemplo de visualização:

```python
px.histogram(
    tabela,
    x=coluna,
    y='Nota (1-100)',
    histfunc='avg',
    text_auto=True
)
```

> Os gráficos são exibidos automaticamente no navegador.

---

## 🎯 Perfil Ideal de Clientes (Insights)

Com base na análise dos dados, foi possível identificar o seguinte perfil ideal:

* 🏷️ **Origem**: Compras em promoção apresentam leve queda na nota
* 🎂 **Idade**: Clientes acima de **15 anos**
* 💰 **Salário**: Média salarial **não impacta diretamente** na nota
* 🎭 **Profissão**: Áreas de **entretenimento e artes** possuem melhores avaliações
* 🛠️ **Experiência**: Entre **10 e 15 anos** de experiência
* 👨‍👩‍👧‍👦 **Tamanho da família**: Até **7 pessoas**

---

## 🚀 Como Executar

```bash
pip install pandas plotly
python analise_clientes.py
```

---

## 📊 Aplicações Práticas

* 📌 Segmentação de clientes
* 📌 Apoio à tomada de decisão comercial
* 📌 Estratégias de marketing direcionadas
* 📌 Análise de comportamento do consumidor

---

## 👨‍💻 Autor

**Jefferson Santos**
Analista de Dados | Python | Data Analytics

🔗 Conecte-se comigo no LinkedIn e acompanhe mais projetos no GitHub.

---

## ⭐ Contribuição

Se este projeto foi útil para você, deixe uma ⭐ no repositório!
