# Aula 06 - Aula de Revisão e Dúvidas

## Temas Abordados

### Guia de Estilo Oficial do Python - PEP 8

- É importante manter um **padrão de estilo de código**, principalmente quando trabalhamos em um **projeto** **colaborativo** ou quando precisamos pensar em **acessibilidade**.

- A [**PEP 8**](https://pep8.org/) é o **guia** de **estilo** **recomendado** pelo próprio **Python**.

- Em termos de **padrões** de **estilo**, são **definidos**:

    - **Ordenação** dos **imports**.
    - Uso de **`'`** ou **`"`** para delimitar **strings**.
    - Número **máximo** de **caracteres** em cada **linha**.
    - Formas de **quebra** de **linha**.

- Existem **ferramentas** que nos auxiliam a **verificar** se o **código** escrito **atende** aos **padrões** da **PEP 8** ou algum **outro** que podemos **definir**.

- Além disso, também existem **ferramentas** que podem **formatar** automaticamente o **código** de forma a seguir os **padrões** da **PEP 8** ou outro **personalizado**.

### Configurando um Projeto para Usar Ferramentas de Formatação de Código

- Para configurar um projeto para usar as ferramentas que fazem a **análise** e **formatação** do **código**, vamos usar o [Poetry](https://python-poetry.org/).

- Após criar um **diretório** para o **projeto**, usamos o seguinte comando para **iniciar** o **Poetry**:

    ```bash
    poetry init
    ```

- Em seguida, vamos **instalar** as seguintes **ferramentas**:

    - [black](https://black.readthedocs.io/en/stable/?badge=stable) ou ([blue](https://blue.readthedocs.io/en/latest/))
    - [isort](https://pycqa.github.io/isort/)
    - [flake8](https://flake8.pycqa.org/en/latest/)

- Para isso, usamos o comando:

    ```bash
    poetry add black isort flake8
    ```

---

- Para **conciliar** as três **ferramentas**, é preciso **configurá-las**.

- Na raiz do projeto, crie o arquivo `.flake8` com a seguinte configuração:

    ```toml
    [flake8]
    max-line-length = 89
    extend-ignore = E203, E701
    ```

- Adicionalmente, edite o arquivo `pyproject.toml` adicionando o seguinte:

    ```toml
    [tool.isort]
    profile = "black"
    ```

### Pre-Commit

- Outra **ferramenta** interessante é o [pre-commit](https://pre-commit.com/), que nos permite **configurar** nosso **ambiente** para que, a cada vez que fizermos um **commit**, determinadas **ações** sejam **executadas**.

- Para **instalar** o **pre-commit**, usamos o comando:

    ```bash
    poetry add pre-commit
    ```

- Existem vários **hooks** disponíveis, que podem ser acessados neste [link](https://pre-commit.com/hooks.html).

- Por exemplo, podemos **configurar** o **pre-commit** para que **rode** as **ferramentas** citadas acima (**black**, **isort** e **flake8**), bem como outras **verificações**.

- Para isso, criamos o arquivo `.pre-commit-config.yaml` na raiz do projeto:

    ```yaml
    repos:
      - repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v4.5.0
        hooks:
          - id: trailing-whitespace
            args: [--markdown-linebreak-ext=md]
          - id: end-of-file-fixer
          - id: check-yaml
          - id: check-toml
          - id: detect-private-key
          - id: check-added-large-files

      - repo: https://github.com/psf/black-pre-commit-mirror
        rev: 24.1.1
        hooks:
          - id: black
            language_version: python3.11

      - repo: https://github.com/pycqa/isort
        rev: 5.13.2
        hooks:
          - id: isort
            name: isort (python)

      - repo: https://github.com/pycqa/flake8
        rev: 7.0.0
        hooks:
          - id: flake8
    ```

- Então, **instalamos** os **hooks** escolhidos com o comando:

    ```bash
    pre-commit install
    ```

- Após **incluir** esse **arquivo** em um **commit**, a cada **novo** **commit**, os **hooks** definidos serão **executados** antes de completar o commit.

- Outros **hooks** **interessantes**:

    - [bandit](https://bandit.readthedocs.io/en/latest/)
    - [commitizen](https://commitizen-tools.github.io/commitizen/)
