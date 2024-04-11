import psycopg2


class BancoDeDadosPostgres:
    def __init__(
        self, host: str, port: str, database: str, user: str, password: str,
    ) -> None:
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.conexao: psycopg2.connection

    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password,
            )
            print('Conexão estabelecida com sucesso.')
        except psycopg2.Error as e:
            print('Erro ao conectar com banco de dados:', e)

    def desconectar(self):
        if self.conexao:
            self.conexao.close()
            print('Conexão fechada.')

    def executar_query(self, query: str) -> None:
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query)
            self.conexao.commit()
            print('Query executada com sucesso.')
        except psycopg2.Error as e:
            print('Erro ao executar query:', e)


# Exemplo de uso
if __name__ == '__main__':
    host = 'localhost'
    port = '5432'
    database = 'nome_do_banco'
    user = 'usuario'
    password = 'senha'

    banco = BancoDeDadosPostgres(host, port, database, user, password)
    banco.conectar()

    # Criando uma tabela
    create_table_query = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id SERIAL PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """

    banco.executar_query(create_table_query)

    # Inserindo dados na tabela
    insert_query = """
    INSERT INTO usuarios (nome, email) VALUES
    ('João', 'joao@example.com'),
    ('Maria', 'maria@example.com');
    """

    banco.executar_query(insert_query)

    banco.desconectar()
