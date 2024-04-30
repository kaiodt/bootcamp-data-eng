from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, sessionmaker

# Usando a abordagem declarativa
Base = declarative_base()


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)


# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)
print('Conexão com SQLite estabelecida.')

# Criar as tabelas no banco de dados
Base.metadata.create_all(engine)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session = Session()

# Adicionando um registro de usuário
# Aqui, não estamos usando um gerenciador de contexto (NÃO RECOMENDADO!)
new_user = Usuario(nome='Kaio', idade=30)
session.add(new_user)
session.commit()
print('Usuário inserido com sucesso.')

# Idealmente, é necessário garantir que as transações foram concluídas e
# encerrar a sessão no final
try:
    new_user = Usuario(nome='Maria', idade=28)
    session.add(new_user)
    session.commit()
    print('Usuário inserido com sucesso.')
except SQLAlchemyError as e:
    session.rollback()
    print('Erro ao inserir usuário.')
    print(e)
finally:
    session.close()

# Entretanto, a forma recomendada é usar um gerenciador de contexto
try:
    with Session() as session:
        new_user = Usuario(nome='João', idade=35)
        session.add(new_user)
        session.commit()
        print('Usuário inserido com sucesso.')
except SQLAlchemyError as e:
    print('Erro ao inserir usuário.')
    print(e)

# Fazendo uma consulta na tabela
with Session() as session:
    user = session.query(Usuario).filter_by(nome='Kaio').first()
    if user:
        print(f'Usuário encontrado: {user.nome}, Idade: {user.idade}')
    else:
        print('Usuário não encontrado')
