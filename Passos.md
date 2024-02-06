
# Introdução

## Servidor

Foi utilizado o docker compose de exemplo do HAPI FIR.
Continuou sendo utilzado o postgress pois é a db que eu tenho mais familiaridade das apresentadas.

Com essa solução, já está configurado a parte de java e de carregamento pelo marv.

rodando o docker-compose.yaml na pasta raiz irá subir o servidor sem nenhum problema.

## Script

Foi utilizado um script python junto com a biblioteca Pandas pois é a que eu mais tenho familiaridade para utilização, e como verifiquei que a empresa utiliza IA, é a linguagem mais em comum com os outros desenvolvedores.

Ela lerá o arquivo patient.csv e irá carregar o Resource através de um payload json de paciente a paciente.
