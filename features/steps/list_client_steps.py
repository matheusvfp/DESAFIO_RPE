from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

@given(u'que o administrador está na página de listagem de clientes')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    actions = ActionChains(context.browser)
    
    qa_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@class='fa fa-lg fa-fw fa-heart']")))
    actions.move_to_element(qa_button).perform()
    
    clientes_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='menu-item-parent'][contains(.,'Clientes')]")))
    actions.move_to_element(clientes_button).perform()
    
    incluir_button = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'menu-item-parent')])[4]")))
    actions.move_to_element(incluir_button).perform()
    
    incluir_button = wait.until(EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'menu-item-parent')])[5]")))
    actions.move_to_element(incluir_button).click().perform()


@when(u'acessar a funcionalidade de listagem')
def step_impl(context):
    
    wait = WebDriverWait(context.browser, 10)
    wait.until(EC.visibility_of_element_located((By.NAME, "j_idt20"))).click()

@then(u'o sistema deve exibir todos os clientes cadastrados com suas respectivas informações')
def step_impl(context):
    wait = WebDriverWait(context.browser, 10)
    table_responsive = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "table-responsive")))
    tbody = table_responsive.find_element(By.TAG_NAME, "tbody")
    
    rows = tbody.find_elements(By.TAG_NAME, "tr")
    assert len(rows) > 0, "Nenhum cliente cadastrado encontrado na tabela."