from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from faker import Faker


@given(u'que o administrador está na página de cadastro de clientes')
def step_impl(context):
    
    wait = WebDriverWait(context.browser, 10)
    actions = ActionChains(context.browser)
    
    qa_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-lg fa-fw fa-heart']")))
    actions.move_to_element(qa_button).perform()
    
    clientes_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='menu-item-parent'][contains(.,'Clientes')]")))
    actions.move_to_element(clientes_button).perform()
    
    incluir_button = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'menu-item-parent')])[4]")))
    actions.move_to_element(incluir_button).click().perform()
    
        
@when(u'preencher todos os campos obrigatórios com dados válidos e clicar em salvar')
def step_impl(context):
    
    wait = WebDriverWait(context.browser, 10)
    fake = Faker('pt_BR')
    
    nome = fake.name()
    cpf = fake.cpf()
    saldo = fake.random_number(digits=5)
    
    wait.until(EC.visibility_of_element_located((By.NAME, "nome"))).send_keys(nome)
    wait.until(EC.visibility_of_element_located((By.NAME, "cpf"))).send_keys(cpf)
    wait.until(EC.visibility_of_element_located((By.NAME, "saldoCliente"))).send_keys(saldo)
    

@then(u'o cliente deve ser cadastrado com sucesso')
def step_impl(context):
    
    context.browser.find_element(By.ID, "botaoSalvar").submit()

@then(u'o administrador deve ver uma mensagem de confirmação.')
def step_impl(context):
    
    wait = WebDriverWait(context.browser, 10)

    success = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="alertMessage"]/strong')))
    assert ("Cliente salvo com sucesso" in success.text), "Erro no cadastro do cliente"