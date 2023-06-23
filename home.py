import mysql.connector

# Estabelecer conexão com o banco de dados
connection = mysql.connector.connect(
    host='', # Sua host
    user='', # Seu usuário
    password='', # Sua senha
    database='' # Seu banco de dados
)

# Verificar se a conexão foi estabelecida com sucesso
if connection.is_connected():
    db_info = connection.get_server_info()
    print("Conectado ao banco de dados MySQL", db_info)
    cursor = connection.cursor()

# Fechar a conexão com o banco de dados
if connection.is_connected():
    cursor.close()
    connection.close()
    print("Conexão com o banco de dados encerrada")

# CREATE
'''
name_product = "chocolate"
value = "9"
command = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{name_product}", {value})'
cursor.execute(command)
connection.commit()  # commit das alterações no banco de dados
'''

# READ
'''
command = f'SELECT * FROM vendas'
cursor.execute(command)
result = cursor.fetchall()  # ler o banco de dados
print(result)
'''

# UPDATE
'''
name_product = "coca"
value = 6
command = f'UPDATE vendas SET valor = {value} WHERE nome_produto = "{name_product}"'
cursor.execute(command)
connection.commit()  # commit das alterações no banco de dados
'''

# DELETE
'''
name_product = "chocolate"
command = f'DELETE FROM vendas WHERE nome_produto = "{name_product}"'
cursor.execute(command)
connection.commit()  # commit das alterações no banco de dados
'''