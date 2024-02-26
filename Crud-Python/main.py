import mysql.connector 

#pip install mysql-connector-python

conexao = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="230390",
    database='bd_crud_python'
)

try:
    cursor = conexao.cursor()

    # INSERT
    # cmd_inserir = 'INSERT INTO tabela_vendas(nome_produto, valor) VALUES ("jabuticaba", 30)' #armazenei um comando em uma variavel
    # cursor.execute(cmd_inserir) #executa o comando
    # conexao.commit() #confirma a o comando, editando o bd

    # SELECT
    # cmd_select =  'SELECT * FROM tabela_vendas'
    # cursor.execute(cmd_select)
    # resultado = cursor.fetchall()
    # print(resultado)

    # UPDATE
    # nValor = 17
    # cmd_update = f'UPDATE tabela_vendas SET valor = {nValor} WHERE nome_produto ="jaca"'
    # cursor.execute(cmd_update)
    # conexao.commit()

    # DELETE
    # nome_produto = "jabuticaba"
    # cmd_deletar = f'DELETE FROM tabela_vendas WHERE nome_produto = "{nome_produto}"'
    # cursor.execute(cmd_deletar)
    # conexao.commit()


    cursor.close()
    conexao.close()

except Exception as e:
    print(f"Erro: {e}")