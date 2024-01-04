# Projeto de teste de REST API com FastAPI

''' 
- Criar um ambiente virtual 'venv' na pasta do projeto : python -m venv venv ##
- Dar um play no arquivo vazio main.py para ativar o venv no projeto
- Abrir o command palette (CTRL + SHIFT + P) (icone da engrenagem do VSCode)
  - Procurar por "Selected Interpreter" 
  - Selecionar o veenv do projeto ao invés da pasta de instalação do python na maquina
- Instalar as bibliotecas necessárias do projeto : 
   pip install pyside6
   pip install requests
   pip install pandas
   pip install openpyxl
   pip install pyinstaller
- Converter arquivos para o python
   - Arquivo icons.qrc :
      pyside6-rcc icons.qrc -o icons_rc.py
   - Arquivo cadastro.ui :
      pyside6-uic cadastro.ui -o ui_main.py
      Obs : Usando pyside2 no lugar de pyside6 - nao funcionou no Windows 7
      pyside2-uic cadastro.ui -o ui_main.py
- Icones de aplicações na internet :
   - https://icon-icons.com
- Usando pyinstaller para gerar um arquivo exe do projeto:
   - pyinstaller.exe --onefile --windowed --icon=icone.ico main.py
- Criar instalador do programa para Windows
   - https://jrsoftware.org
      baixar o innosetup-6.2.0.exe
   - Video de criacao do instalador
         
'''
