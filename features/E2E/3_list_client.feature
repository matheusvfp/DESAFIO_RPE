Feature: Listar clientes
    
    Scenario: Listagem de Cliente no sistema RPE

    Como um administrador, 
    Eu quero ver a lista de clientes cadastrados 
    Para gerenciar os clientes existentes

    Given que o administrador está na página de listagem de clientes
    When acessar a funcionalidade de listagem
    Then o sistema deve exibir todos os clientes cadastrados com suas respectivas informações
    