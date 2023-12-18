from typing import Annotated, Union
from fastapi import FastAPI, Body, HTTPException, status

app = FastAPI()

# dictionary para armazenar os dados dos usuários
user_dict = {}
id = 1

# endpoint para criar um novo registro usuário (user)
@app.post('/user')
async def criar_user(email: Annotated[str, Body()], name:  Annotated[str, Body()], password: Annotated[str, Body()]):
    global id
    
    user = {}
    user['id'] = id
    user['email'] = email
    user['name'] = name
    user['password'] = password
        
    user_dict[id] = user
    id+=1
    
    return user

# endpoint para ler todos os registros de usuários (user)
@app.get('/user')
async def ler_users():
    return list(user_dict.values())

# endpoint para ler um registro usuário (user) específico
@app.get('/user/{id}')
async def ler_user_especifico(id: int):
    if id not in user_dict :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
        )
        
    return user_dict[id]

# endpoint para atualizar um registro usuário (user)
@app.put('/user/{id}')
async def atualizar_user(id: int, email: Annotated[str, Body()], name:  Annotated[str, Body()], password: Annotated[str, Body()]):
    user = {}
    user['id'] = id
    user['email'] = email
    user['name'] = name
    user['password'] = password
    
    user_dict[id] = user
    
    return user

# endpoint para remover um registro usuário (user)
@app.delete('/user/{id}')
async def remover_user_especifico(id: int):
    if id not in user_dict :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado"
        )
        
    del user_dict[id]
    
    return {'message' : f'Usuário ID={id} removido com sucesso!'}