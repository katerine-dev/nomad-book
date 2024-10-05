from nomadbook.db import connection as db_connection
from nomadbook.db import usuario as db_usuario
from nomadbook.db import viagem as db_viagem

conn = db_connection.get_connection()
#cur = conn.cursor()

# Teste funções:
# id = db_usuario.create_usuario(conn, "email2@email.com", "joao25", "joa2o5")
# print(id)

# informacoes = db_usuario.get_usuario_by_id(conn, "aa61162a-54d9-41f0-9677-55de398994e9")
# print(informacoes)

# update =  db_usuario.update_usuario(conn, 
#                                     "3484a9f6-f35a-447c-8265-ec9417d40cc7", 
#                                     "update@email.com", 
#                                     "update", 
#                                     "update")

# delete = db_usuario.delete_usuario(conn, "d0e933a1-8923-459e-9030-a8eeac677cfd")

# Teste funções:
#id = db_viagem.create_viagem(conn, "testedas", "tesderteafdfewf", "b72cfdf5-2382-43b1-b19d-78b29812df5e")
#print(id)

#informacoes = db_viagem.get_viagem_by_id(conn, "f8a2278c-28ef-43a5-9484-0a61149f474b")
#print(informacoes)

# update =  db_viagem.update_viagem(conn,
#                                   "f8a2278c-28ef-43a5-9484-0a61149f474b",
#                                   "testedadsadasds",
#                                    "tesderteafdfdsdawdqwdqwdqwdqwdwqwf")

#delete = db_viagem.delete_viagem(conn, "f8a2278c-28ef-43a5-9484-0a61149f474b")


