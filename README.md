# Raven-Morph-API

Raven Morph API é um projeto inspirado na personagem Raven Darkhölme, também conhecida como Mystique, dos X-Men. Esta API utiliza Flask para fornecer endpoints dinâmicos com base em um arquivo JSON estático. A partir de um arquivo JSON o Raven Morph é capaz de prover uma API estática, bastante util para ambientes de teste.

Esta ferramente procura facilitar os tentes de desenvolvedores que precisam popular dados em frontend sem abrir mão de simular um ambiente real, mantendo a possibilidade de flexibilidade e falicidades de inserção de contaúdos de mockup.

## Funcionalidades

- Leitura dinâmica de um arquivo JSON para criar endpoints baseados nos objetos do JSON.
- Fornecimento de dados estáticos através de uma API simples e fácil de usar.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/raven-api.git
   ```

2. Instale as dependências usando pip:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Certifique-se de ter o arquivo `data.json` com os dados que deseja fornecer pela API.

2. Execute o servidor Flask:

   ```bash
   python app.py
   ```

3. Acesse os endpoints da API em `http://localhost:5000/`.

## Exemplo de JSON

Exemplo de estrutura do arquivo `data.json`:

```json
{
    "saldoInicial": -3205,
    "saldoFinal": 4722,
    "reducaoEconomia": -247,
    "economiaMes": 7927,
    "despesas": [
        {"categoria": "Alimentação", "planejado": 50, "real": 50, "diferenca": 0},
        {"categoria": "Transporte", "planejado": 100, "real": 90, "diferenca": 10}
    ],
    "renda": [
        {"categoria": "Poupança", "planejado": 50, "real": 50, "diferenca": 0},
        {"categoria": "Salário", "planejado": 3000, "real": 3000, "diferenca": 0}
    ]
}
```

Para o exemplo acima, cada objeto no json retornará um respectivo endpoint com seu nome exato e os dados internos a ele, como nos seguintes exemplos:

- http://127.0.0.1:5000/saldoInicial
```json
{
 "saldoInicial": -3205
}
```
- http://127.0.0.1:5000/despesas
```json
{
  "despesas": [
    {
      "categoria": "Alimenta\u00e7\u00e3o",
      "diferenca": 0,
      "planejado": 50,
      "real": 50
    },
    {
      "categoria": "Transporte",
      "diferenca": 10,
      "planejado": 100,
      "real": 90
    }
  ]
}
```
## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou abrir issues se encontrar algum problema ou tiver sugestões.