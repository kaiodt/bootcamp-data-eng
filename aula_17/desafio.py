from sqlalchemy import (
    Column,
    Float,
    ForeignKey,
    Integer,
    String,
    create_engine,
    func,
)
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Fornecedor(Base):
    __tablename__ = 'fornecedores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(20))
    email = Column(String(50))
    endereco = Column(String(100))


class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    descricao = Column(String(200))
    preco = Column(Float)
    fornecedor_id = Column(Integer, ForeignKey('fornecedores.id'))

    fornecedor = relationship('Fornecedor')


engine = create_engine('sqlite:///:memory:')

# Criando tabelas
Base.metadata.create_all(engine)

# Criando sessão
Session = sessionmaker(engine)

# Inserindo fornecedores
try:
    with Session() as session:
        fornecedores = [
            Fornecedor(
                nome='Fornecedor A',
                telefone='12345678',
                email='contato@a.com',
                endereco='Endereço A',
            ),
            Fornecedor(
                nome='Fornecedor B',
                telefone='87654321',
                email='contato@b.com',
                endereco='Endereço B',
            ),
            Fornecedor(
                nome='Fornecedor C',
                telefone='12348765',
                email='contato@c.com',
                endereco='Endereço C',
            ),
            Fornecedor(
                nome='Fornecedor D',
                telefone='56781234',
                email='contato@d.com',
                endereco='Endereço D',
            ),
            Fornecedor(
                nome='Fornecedor E',
                telefone='43217865',
                email='contato@e.com',
                endereco='Endereço E',
            ),
        ]
        session.add_all(fornecedores)
        session.commit()
        print('Fornecedores inseridos com sucesso.')
except SQLAlchemyError as e:
    print('Erro ao inserir fornecedores:')
    print(e)

# Inserindo produtos
try:
    with Session() as session:
        produtos = [
            Produto(
                nome='Produto 1',
                descricao='Descrição do Produto 1',
                preco=100.10,
                fornecedor_id=1,
            ),
            Produto(
                nome='Produto 2',
                descricao='Descrição do Produto 2',
                preco=200.20,
                fornecedor_id=2,
            ),
            Produto(
                nome='Produto 3',
                descricao='Descrição do Produto 3',
                preco=300.30,
                fornecedor_id=3,
            ),
            Produto(
                nome='Produto 4',
                descricao='Descrição do Produto 4',
                preco=400.40,
                fornecedor_id=4,
            ),
            Produto(
                nome='Produto 5',
                descricao='Descrição do Produto 5',
                preco=500.50,
                fornecedor_id=5,
            ),
        ]
        session.add_all(produtos)
        session.commit()
        print('Produtos inseridos com sucesso.')
except SQLAlchemyError as e:
    print('Erro ao inserir produtos:')
    print(e)

# Consultando os produtos inseridos
with Session() as session:
    for produto in session.query(Produto).all():
        if produto:
            print(
                f'Produto: {produto.nome}, '
                f'Fornecedor: {produto.fornecedor.nome}',
            )

# Query com JOIN e GROUP BY
with Session() as session:
    resultado = (
        session
        .query(
            Fornecedor.nome,
            func.sum(Produto.preco).label('preco_total'),
        )
        .join(
            Produto, Fornecedor.id == Produto.fornecedor_id,
        )
        .group_by(
            Fornecedor.nome,
        )
        .all()
    )

    if resultado:
        for fornecedor, preco_total in resultado:
            print(f'Fornecedor: {fornecedor}, Preço Total: {preco_total:.2f}')
