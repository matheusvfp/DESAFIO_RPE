# Desafio Técnico RPE

## Descrição

O objetivo deste desafio foi explorar a página de cadastro de clientes, abrangendo a criação de um plano de teste detalhado, elaboração de casos de teste e relatórios de bugs. A etapa final envolveu a automação de cenários de teste selecionados para garantir a eficiência e a confiabilidade do processo.



## Implementações Realizadas

Para este desafio, foram desenvolvidos os seguintes casos de teste automatizados utilizando Behave e Python com a linguagem Gherkin:

1. **Login**: Testa o fluxo de autenticação com as credenciais fornecidas.
2. **Listagem de Clientes**: Verifica se a lista de clientes é exibida corretamente.
3. **Cadastro de Cliente**: Automatiza o processo de cadastro de um novo cliente.

### Estrutura do Projeto

- **features/E2E**: Contém os arquivos de características e definições dos testes.
  - **login.feature**: Cenários e casos de teste para o fluxo de login.
  - **list_client.feature**: Cenários e casos de teste para a listagem de clientes.
  - **create_client.feature**: Cenários e casos de teste para o cadastro de clientes.
- **steps/**: Implementação dos passos dos testes.
  - **login_steps.py**: Implementa os passos para os cenários de login.
  - **list_client_steps.py**: Implementa os passos para os cenários de listagem de clientes.
  - **create_client_steps.py**: Implementa os passos para os cenários de cadastro de clientes.
- **requirements.txt**: Lista de dependências do projeto.

## Plano de Testes

Você pode acessar o plano de testes através do seguinte link: [Plano de Testes](https://docs.google.com/spreadsheets/d/1oTWI4TCd6i3vF5UZr5QgOht-1GLzsosT5w3cY0KPPtA/edit?usp=sharing)


# Executando o projeto
Abaixo, um passo-a-passo de como executar os testes localmente.

## Pré-requisitos 📋
- [Python 3.x](https://www.python.org/downloads/) (Eu utilizei a versão `3.11.2` enquanto desenvolvia esse projeto).
- WebDriver do seu navegador (veja mais abaixo).

## WebDrivers
Para executar os testes você precisa instalar a versão do webdriver para o seu navegador.
- [ChromeDriver](https://chromedriver.chromium.org/downloads) for Google Chrome
- [Geckodriver](https://github.com/mozilla/geckodriver/releases/latest) for Firefox.
  
ChromeDriver e geckodriver devem estar presentes no [system path](https://en.wikipedia.org/wiki/PATH_(variable)).

## Virtual Environment 🌲
É recomendado a utilização de um ambiente virtual para a instalação de dependencias. <br>
Dentro da pasta do backoffice-jogajunto execute `python -m venv venv` para criar um ambiente virtual:
```bash
python -m venv venv
```

### Ative o ambiente virtual:

- Windows

```bash
venv\Scripts\activate
```
- Linux/MacOs
  
```bash
venv/bin/activate
```

## Instalação 🏗️
Instale todos os requisitos:
```bash
pip install -r requirements.txt
```

## Configs ⚙️
As configurações como **navegador** e **endpoints** da aplicação podem ser configuradas dentro do arquivo `behave.ini`

Os navegadores suportados são, ambos também no modo `headless`:
- Firefox
- Chrome

Lembrando que é necessário o `webdriver` do navegador escolhido, como citado nos **Pré-requisitos**

##  Rodadando os testes ✔️
Para executar os testes, basta utilizar o comando `behave`

```bash
behave
```

## Apoie o projeto 🙌

Se você quiser apoiar o projeto, deixe uma ⭐.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.

## Apoie o Projeto 🙌
Se você quiser apoiar o projeto, deixe uma ⭐.

______

Made with ❤️ by [Matheus Vinícius](https://www.linkedin.com/in/matheusviniciusfp/).