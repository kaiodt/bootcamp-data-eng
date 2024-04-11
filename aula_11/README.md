# Aula 11 - Introdução à POO

- Nesta aula, faremos uma **introdução** à **Programação Orientada a Objetos** (**POO**) em **Python**, passando pelos **quatro** **pilares** de **Abstração**, **Encapsulamento**, **Herança** e **Polimorfismo**.


## Programação Orientada a Objetos (POO)

- A **Programação Orientada a Objetos** (**POO**) é um **paradigma de programação** que se baseia no conceito de "**objetos**", que podem conter **dados** na forma de **campos** (também conhecidos como **atributos** ou **propriedades**) e **códigos** na forma de **procedimentos** (**métodos** ou **funções**).

- Os **objetos** são **instâncias** de **classes**, que definem as **estruturas** e **comportamentos** dos **objetos**. 


### Pilares da POO

#### Abstração

- **Abstração** permite **modelar** **objetos** do mundo real de **forma simplificada**, identificando suas **características essenciais** e **comportamentos relevantes**.

- Ajuda a **reduzir** a **complexidade**, tornando o **código** mais **compreensível** e **reutilizável**.


#### Encapsulamento

- **Encapsulamento** é o princípio de **ocultar** os **detalhes** de **implementação** de um objeto e **permitir** o **acesso** apenas por meio de uma **interface** **bem definida**.

- Isso promove a **segurança**, pois **restringe** o **acesso** direto aos **dados internos** de um objeto, **permitindo** apenas **operações autorizadas**.


#### Herança


- **Herança** permite que uma **classe** (ou tipo) de objeto **herde** **atributos** e **métodos** de **outra classe**.

- Permite **reutilizar** código, promovendo a **extensibilidade** e a **organização** **hierárquica** de classes.


#### Polimorfismo

- **Polimorfismo** permite que **objetos** de **diferentes classes** sejam **tratados** de forma **uniforme**.

- Isso é alcançado por meio de **sobrecarga de método** (métodos com o **mesmo nome**, mas com **diferentes implementações**) e **substituição de método** (métodos com a **mesma assinatura** em **classes diferentes**).


### Vantagens e Desvantagens da POO

#### Vantagens

- **Reutilização** de código facilitada pela **herança** e pelo **polimorfismo**.

- Maior **modularidade** e **manutenibilidade** devido à **encapsulação** e **abstração**.

- Mais **próximo** do **mundo real**, **facilitando** a **modelagem** de sistemas complexos.

- **Desenvolvimento** mais **orientado** a **objetos**, favorecendo o trabalho em equipe e a **colaboração**.


#### Desvantagens

- Pode ser **mais complexo** de **entender** e **implementar**, especialmente para iniciantes.

- **Overhead** de **desempenho** em comparação com a **programação procedural** para algumas operações.

- Requer **planejamento** **cuidadoso** e **design de classes eficiente** para **evitar** problemas de **hierarquia** excessivamente **complexa**.


## Programação Procedural

- A **programação procedural** é um **paradigma de programação** que organiza o código em torno de **funções** e **procedimentos**.


### Conceitos da Programação Procedural

#### Procedimentos e Funções

-  A estrutura principal é baseada em **funções** e **procedimentos** que **manipulam** **dados**.

- Os **dados** são **passados** ​​entre as **funções** por meio de **parâmetros** e **retorno** de **valores**.


#### Top-Down Design

- O **código** é **estruturado** de **cima para baixo**, dividindo-o em **funções** **menores** e mais **gerenciáveis**.


## Programação Funcional

- A **programação funcional** é outro **paradigma de programação** que se concentra na **avaliação** de **funções matemáticas** e na **aplicação** de **funções** para **transformar dados**.


### Conceitos da Programação Funcional

#### Funções como Cidadãos de Primeira Classe

- Em **programação funcional**, as **funções** são tratadas como **cidadãos de primeira classe**, o que significa que podem ser **atribuídas a variáveis**, **passadas como argumentos** para outras funções e **retornadas como valores** de outras funções.

- Isso permite uma **abordagem** mais **modular** e **flexível** para escrever código.


#### Imutabilidade de Dados

- Na **programação funcional**, os **dados** são **imutáveis**, o que significa que uma vez criados, eles não podem ser alterados.

- Em vez disso, **operações** em **dados imutáveis** ​​**criam novos dados**. Isso ajuda a **evitar** **efeitos colaterais** e facilita o raciocínio sobre o comportamento do programa.


#### Funções Puras

- As **funções** na programação funcional são consideradas "**puras**" se **retornarem** o **mesmo resultado** para os **mesmos argumentos** e **não** tiverem **efeitos colaterais observáveis**.


#### Funções de Ordem Superior

- **Funções de ordem superior** são funções que **aceitam** outras **funções** como **argumentos** ou **retornam** outras **funções** como **resultados**.

- Isso permite uma **abstração** **poderosa** e a capacidade de escrever **código** mais **genérico** e **reutilizável**.


#### Recursão

- **Recursão** é uma **técnica importante** na programação funcional, onde uma **função** **chama a si mesma** para resolver um problema menor.

- Isso é usado em vez de **loops iterativos**.


## POO em Python


- O **Python** **suporta** **fortemente** a **POO**.

- A seguir, tem-se uma visão geral de como a POO é implementada em Python.


### Classes e Métodos

- Em Python, **definimos** uma **classe** usando a **palavra-chave** **`class`**.

- Uma **classe** é como um **modelo** para criar objetos. Por exemplo:

	```python
	class Carro:
	    def __init__(self, marca, modelo):
	        self.marca = marca
	        self.modelo = modelo
	
	    def dirigir(self):
	        print('O carro está em movimento.')
	
	# Criando um objeto (instância) da classe Carro
	meu_carro = Carro('Toyota', 'Corolla')
	
	# Chamando o método 'dirigir'
	meu_carro.dirigir()

	# Output:
	# O carro está em movimento.
	```

- **`__init__`**: Este é o método **construtor** usado para **inicializar** **objetos**. É **chamado** **automaticamente** quando um **novo objeto** da classe é **criado**.

- **`self`**: É uma **referência** ao **próprio objeto** e é usado para **acessar** **variáveis** de **instância** e **métodos** dentro da classe.


### Atributos e Métodos

- **Atributos**: São variáveis pertencentes a uma classe ou objeto.

- **Métodos**: São funções definidas dentro da classe que podem operar nos atributos do objeto.


### Herança

- Uma classe pode **herdar** **atributos** e **métodos** de outra classe. Por exemplo:

	```python
	class Veiculo:
	    def __init__(self, marca, modelo):
	        self.marca = marca
	        self.modelo = modelo
	
	    def ligar(self):
	        print('Veículo ligado.')
	
	class Carro(Veiculo):
	    def dirigir(self):
	        print('O carro está em movimento.')
	
	meu_carro = Carro('Toyota', 'Corolla')
	meu_carro.ligar()  # Chamando o método da classe base

	# Output:
	# Veículo ligado.
	```

### Encapsulamento

- Em **Python**, o **encapsulamento** é alcançado usando **convenções de nomenclatura**.

- **Atributos** e **métodos** podem ser **públicos** (acessíveis em qualquer lugar), **protegidos** (acessíveis apenas na própria classe e suas subclasses) ou **privados** (acessíveis apenas na própria classe).

- Por **convenção**, os membros **privados** são **prefixados** com um underscore **`_`** e os membros **protegidos** são **prefixados** com um dois underscores **`__`** (**dunder**).


### Polimorfismo

- **Métodos** com o **mesmo nome** podem ser **definidos** em **classes diferentes** e podem ter **comportamentos diferentes**. Por exemplo:

	```python
	class Animal:
	    def fazer_som(self):
	        pass
	
	class Cachorro(Animal):
	    def fazer_som(self):
	        print('Au au!')
	
	class Gato(Animal):
	    def fazer_som(self):
	        print('Miau!')
	
	def fazer_barulho(animal):
	    animal.fazer_som()
	
	cachorro = Cachorro()
	gato = Gato()
	
	fazer_barulho(cachorro)  # Output: Au au!
	fazer_barulho(gato)      # Output: Miau!
	```
