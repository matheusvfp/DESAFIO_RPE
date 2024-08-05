Feature: Login na página 
    
    Scenario: Login no sistema RPE

    Como usuário credenciado da RPE
    Eu quero acessar o sistema Backoffice
    Para realizar minhas atividades rotineiras

    Given que o usuário está na página de login
    When informar o login e a senha
    Then o sistema deve autenticar o usuário 
    And permitir o acesso às funcionalidades do sistema.