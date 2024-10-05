from nomadbook.db import connection as db_connection
from nomadbook.db import usuario as db_usuario

conn = db_connection.get_connection()
#cur = conn.cursor()

# Teste funções:
id = db_usuario.create_usuario(conn, "email2@email.com", "joao25", "joa2o5")
print(id)

#informacoes = db_usuario.get_usuario_by_id(conn, "aa61162a-54d9-41f0-9677-55de398994e9")
#print(informacoes)

# update =  db_usuario.update_usuario(conn, 
#                                     "3484a9f6-f35a-447c-8265-ec9417d40cc7", 
#                                     "update@email.com", 
#                                     "update", 
#                                     "update")

delete = db_usuario.delete_usuario(conn, "d0e933a1-8923-459e-9030-a8eeac677cfd")