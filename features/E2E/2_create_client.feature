Feature: Criar cliente
    
    Scenario: Cadastro de Cliente no sistema RPE

    Como um administrador 
    Eu quero cadastrar um cliente com todos os campos obrigatórios preenchidos 
    Para garantir que o cliente seja adicionado corretamente

    Given que o administrador está na página de cadastro de clientes
    When preencher todos os campos obrigatórios com dados válidos e clicar em salvar
    Then o cliente deve ser cadastrado com sucesso 
    And o administrador deve ver uma mensagem de confirmação.