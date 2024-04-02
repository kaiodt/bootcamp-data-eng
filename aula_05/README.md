# Aula 05 - Projeto 01 - Leitura e Escrita de Arquivos: Lendo 1 Bilhão de Linhas

## Projeto 01 - Leitura de 1 Bilhão de Linhas

- O objetivo deste projeto é demonstrar como **processar eficientemente** um **arquivo de dados massivo** contendo **1 bilhão de linhas (~14 GB)**, especificamente para **calcular estatísticas** envolvendo **agregação** e **ordenação**, que são **operações pesadas**, utilizando **Python**.

- Este desafio foi inspirado no [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originalmente proposto para Java.

- O arquivo de dados consiste em **medições de temperatura** de várias **estações meteorológicas**.

	- Cada registro segue o **formato** `<string: nome da estação>;<double: medição>`, com a temperatura sendo apresentada com precisão de uma casa decimal.

- Aqui estão dez linhas de exemplo do arquivo:
	```
	Hamburg;12.0
	Bulawayo;8.9
	Palembang;38.8
	St. Johns;15.2
	Cracow;12.6
	Bridgetown;26.9
	Istanbul;6.2
	Roseau;34.4
	Conakry;31.2
	Istanbul;23.0
	```

- O desafio é desenvolver um programa Python capaz de ler esse arquivo e calcular a **temperatura mínima**, **média** (arredondada para uma casa decimal) e **máxima** para **cada estação**, exibindo os resultados em uma **tabela ordenada** por **nome da estação**.

- Um exemplo de parte da saída é mostrado abaixo:

    | **station**   | **min_temperature** | **mean_temperature** | **max_temperature** |
    | :------------ | :-----------------: | :------------------: | :-----------------: |
    | Abha          |        -31.1        |         18.0         |        66.5         |
    | Abidjan       |        -25.9        |         26.0         |        74.6         |
    | Abéché        |        -19.8        |         29.4         |        79.9         |
    | Accra         |        -24.8        |         26.4         |        76.3         |
    | Addis Ababa   |        -31.8        |         16.0         |        63.9         |
    | Adelaide      |        -31.8        |         17.3         |        71.5         |
    | Aden          |        -19.6        |         29.1         |        78.3         |
    | Ahvaz         |        -24.0        |         25.4         |        72.6         |
    | Albuquerque   |        -35.0        |         14.0         |        61.9         |
    | Alexandra     |        -40.1        |         11.0         |        67.9         |
    | ...           |         ...         |         ...          |         ...         |
    | Yangon        |        -23.6        |         27.5         |        77.3         |
    | Yaoundé       |        -26.2        |         23.8         |        73.4         |
    | Yellowknife   |        -53.4        |         -4.3         |        46.7         |
    | Yerevan       |        -38.6        |         12.4         |        62.8         |
    | Yinchuan      |        -45.2        |         9.0          |        56.9         |
    | Zagreb        |        -39.2        |         10.7         |        58.1         |
    | Zanzibar City |        -26.5        |         26.0         |        75.2         |
    | Zürich        |        -42.0        |         9.3          |        63.6         |
    | Ürümqi        |        -42.1        |         7.4          |        56.7         |
    | İzmir         |        -34.4        |         17.9         |        67.9         |

## Desafio

- Clonar o repositório do [projeto](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python).

- Rodar o código utilizando `pyenv`, `poetry` e VS Code.

- Instalar as dependências.

- Rodar todos os testes.

- Após isso, aplicar algum dos conteúdos que vimos até agora (estruturas de dados, Type Hint, estruturas condicionais, `try-catch`, funções, etc) e propor uma melhoria no projeto através de um Pull Request (PR).

## Resultados

- Os testes foram executados em um laptop com processador Intel Core i7-12700H 2.30 GHz com 24 GB de memória RAM.

- Após rodar todos os testes com o arquivo de 1 bilhão de linhas, obtiveram-se os seguintes resultados:

    | Ferramenta      |  Tempo  |
    | :-------------- | :------ |
    | Python          | 22m 44s |
    | Python + Pandas | 04m 55s |
    | Python + Dask   | 03m 23s |
    | Python + Polars | 21.62s  |
    | Python + DuckDB | 13.58s  |

## Conclusão

- Os resultados apresentados evidenciam a eficácia de diferentes bibliotecas Python em relação à tarefa de manipulaçlão de grandes volumes de dados.

- O uso apenas das funcionalidades presentes no **Python** demandou mais de **20 minutos** para concluir a tarefa.

- Para usar a biblioteca **Pandas**, foi necessário utilizar o processamento em lotes (*batch*), aumentando a complexidade do código. Porém, o tempo em relação ao Python puro reduziu para cerca de **5 minutos**.

- Já as bibliotecas **Dask**, **Polars** e **DuckDB** ofereceram maior praticidade de implementação, pois já possuem capacidade inerente de distribuir os dados em "lotes em streaming".

- O destaque ficou com a biblioteca **DuckDB**, que concluiu a atividade em apenas **13.58 segundos**, demonstrando extrema eficiência no processamento de grandes volumes de dados.