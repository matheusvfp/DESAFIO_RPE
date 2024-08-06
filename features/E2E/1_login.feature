Feature: Login na página 
    
    Scenario: Login no sistema RPE

    Como um administrador do sistema 
    Eu quero acessar o sistema com as credenciais corretas 
    Para garantir que o login seja realizado com sucesso

    Given que o usuário está na página de login
    When informar o login e a senha
    Then o sistema deve autenticar o usuário 
    And permitir o acesso às funcionalidades do sistema.