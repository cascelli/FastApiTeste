# Projeto de teste de REST API server com FastAPI

''' 
- Criar um ambiente virtual 'venv' na pasta do projeto : python -m venv venv ##
- Dar um play no arquivo vazio main.py para ativar o venv no projeto
- Abrir o command palette (CTRL + SHIFT + P) (icone da engrenagem do VSCode)
  - Procurar por "Selected Interpreter" 
  - Selecionar o veenv do projeto ao invés da pasta de instalação do python na maquina
- Instalar as bibliotecas necessárias do projeto : 
    pip install uvicorn
    pip install fastapi
'''

# Imports :
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Cria uma classe que herda de BaseModel
class Inputs(BaseModel):
    # Define as propriedades da classe
    inp: int
    inp2: str 

@app.get("/exemplo")
def example() -> str:
    return "Olá mundo FastAPI REST App !"

@app.post("/exemplo_2")
def example_2(inputs: Inputs) -> str:
    # codigo diverso
    # ...
    # ...
    # retorna string
    return inputs.inp2


# Habilita modo de inicializacao padrao do python
# Quando a gente executar este modulo como modulo principal
if __name__ == "__main__":
    uvicorn.run(app, port=8000) # Roda o servidor da API na porta 8000
