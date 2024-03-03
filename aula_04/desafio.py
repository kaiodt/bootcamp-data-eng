##############################################################################
# Bootcamp de Python, SQL e Git para Engenharia de Dados                     #
# Aula 04 - Type Hint, Tipos Complexos (Dicionários vs. DataFrames vs.       #
#           Tabelas vs. Excel) e Funções                                     #
##############################################################################

# Desafio ####################################################################
#                                                                            #
# * Refatorar o código do desafio desenvolvido na Aula 03 usando dicionário, #
#   funções e tipagem.                                                       #
#                                                                            #
##############################################################################

BASE_SALLARY = 1000


def get_user_name() -> str:
    """
    Solicita o nome do usuário e realiza testes de validade.
    """

    # Solicitar nome do usuário
    name = input("Digite seu nome: ")

    # Não aceitar um nome vazio
    if len(name) == 0:
        raise ValueError("Você não digitou o seu nome.")
    
    # Não aceitar apenas espaços no nome
    elif name.isspace():
        raise ValueError("Você digitou apenas espaços no seu nome.")

    # Aceitar apenas letras (espaços entre os nomes são permitidos)
    elif not name.replace(" ", "").isalpha():
        raise ValueError("Use apenas letras no seu nome.")
    
    else:
        return name


def get_user_sallary() -> float:
    """
    Solicita o salário do usuário e realiza testes de validade.
    """

    # Solicitar salário
    sallary = float(input("Digite seu salário: "))

    # Não aceitar salário negativo
    if sallary < 0:
        raise ValueError("Insira um salário positivo.", True)
    else:
        return sallary


def get_user_bonus() -> float:
    """
    Solicita o bônus do usuário e realiza testes de validade.
    """

    # Solicitar bônus
    bonus = float(input("Digite seu bonus: "))

    # Não aceitar bônus menor que 1
    if bonus < 1:
        raise ValueError("Insira um bônus maior ou igual a um.", True)
    else:
        return bonus


def calc_final_bonus(base_sallary: float, sallary: float, bonus: float = 1.):
    """
    Calcula o bônus final do usuário.
    """

    return base_sallary + sallary * bonus


def info_string(user_info: dict[str, str | float]):
    return f"Olá {user_info['name']}, confira seu resultado:\n" + \
           f"Salário: R$ {user_info['sallary']:.2f}\n" + \
           f"Bônus: {user_info['bonus']:.2f}\n" + \
           f"Bônus Final: R$ {user_info['final_bonus']:.2f}\n"


# Dicionário com as informações do usuário
user_info = {}

# Obter o nome do usuário
while True:
    try:
        user_info["name"] = get_user_name()

    except ValueError as e:
        print(f"\n[ERRO] {e}")
        print("Tente novamente.\n")

    else:
        break

print()

# Obter o salário do usuário
while True:
    try:
        user_info["sallary"] = get_user_sallary()

    except ValueError as e:
        if len(e.args) > 1:
            print(f"\n[ERRO] {e.args[0]}")
        else:
            print("\n[ERRO] O valor inserido é inválido.")
        
        print("Tente novamente.\n")

    else:
        break

print()

# Obter o bônus do usuário
while True:
    try:
        user_info["bonus"] = get_user_bonus()

    except ValueError as e:
        if len(e.args) > 1:
            print(f"\n[ERRO] {e.args[0]}")
        else:
            print("\n[ERRO] O valor inserido é inválido.")
        
        print("Tente novamente.\n")
    
    else:
        break

print()

# Cálculo do bônus final
user_info["final_bonus"] = calc_final_bonus(
    base_sallary=BASE_SALLARY,
    sallary=user_info["sallary"],
    bonus=user_info["bonus"]
)

print(info_string(user_info))

