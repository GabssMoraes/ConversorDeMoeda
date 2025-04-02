# Conversor de Moedas

## Descrição
Este é um projeto de um conversor de moedas desenvolvido em Django. O sistema permite que os usuários convertam valores entre diferentes moedas em tempo real, utilizando a API ExchangeRate como fonte de dados.

## Tecnologias Utilizadas
- Python
- Django
- HTML, CSS e Bootstrap
- API ExchangeRate
- SQLite (ou outro banco de dados, conforme configuração)

## Funcionalidades
- Conversão de moedas em tempo real
- Interface responsiva
- Seleção de moedas de origem e destino
- Histórico de conversões

## Instalação
1. Clone o repositório:
   ```sh
   git clone https://github.com/seu-usuario/conversor-moedas.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd conversor-moedas
   ```
3. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```
4. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
5. Configure as variáveis de ambiente (chave da API ExchangeRate):
   ```sh
   export EXCHANGE_RATE_API_KEY="sua_chave_aqui"  # Linux/Mac
   set EXCHANGE_RATE_API_KEY="sua_chave_aqui"  # Windows
   ```
6. Execute as migrações do banco de dados:
   ```sh
   python manage.py migrate
   ```
7. Inicie o servidor:
   ```sh
   python manage.py runserver
   ```

## Como Usar
1. Acesse o sistema pelo navegador: `http://127.0.0.1:8000/`
2. Selecione a moeda de origem e destino.
3. Insira o valor desejado e clique em "Converter".
4. O resultado será exibido na tela.

## Contribuição
Se deseja contribuir para este projeto, siga estas etapas:
1. Fork o repositório
2. Crie uma branch para suas modificações: `git checkout -b minha-feature`
3. Faça commit das suas alterações: `git commit -m "Adiciona nova funcionalidade"`
4. Faça push para a branch: `git push origin minha-feature`
5. Abra um Pull Request

## Autor
Desenvolvido por [GabssMoraes](https://github.com/GabssMoraes).

