import os
import sqlite3
from typing import Literal

import psycopg2


class BancoDeDados:
    def __init__(self, tipo_banco: Literal['sqlite', 'postgres']) -> None:
        self.tipo_banco = tipo_banco.lower()
        self.conexao = None

    def conectar(self):
        if self.tipo_banco == 'sqlite':
            try:
                nome_arquivo = os.getenv('NOME_ARQUIVO_SQLITE')
                self.conexao = sqlite3.connect(nome_arquivo)
                print('Conexão SQLite estabelecida com sucesso.')
            except sqlite3.Error as e:
                print('Erro ao conectar com banco de dados SQLite:', e)
        elif self.tipo_banco == 'postgres':
            try:
                host = os.getenv('HOST_PG')
                port = os.getenv('PORT_PG')
                database = os.getenv('DATABASE_PG')
                user = os.getenv('USER_PG')
                password = os.getenv('PASSWORD_PG')

                self.conexao = psycopg2.connect(
                    host=host,
                    port=port,
                    database=database,
                    user=user,
                    password=password,
                )

                print('Conexão PostgreSQL estabelecida com sucesso.')

            except psycopg2.Error as e:
                print('Erro ao conectar com banco de dados PostgreSQL:', e)
        else:
            print(f'Banco de dados "{self.tipo_banco}" não suportado.')

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            if self.tipo_banco == 'sqlite':
                print('Conexão SQLite fechada.')
            elif self.tipo_banco == 'postgres':
                print('Conexão PostgreSQL fechada.')

    def executar_query(self, query: str) -> None:
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print('Query executada com sucesso.')
        except (sqlite3.Error, psycopg2.Error) as e:
            print('Erro ao executar query:', e)


# Exemplo de uso
if __name__ == '__main__':
    tipo_banco = os.getenv('TIPO_BANCO')  # 'sqlite' ou 'postgres'

    banco = BancoDeDados(tipo_banco)
    banco.conectar()

    # Exemplo de criação de tabela
    create_table_query = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """

    banco.executar_query(create_table_query)

    # Exemplo de inserção de dados
    insert_query = """
    INSERT INTO usuarios (nome, email) VALUES
    ('João', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """

    banco.executar_query(insert_query)

    banco.desconectar()
