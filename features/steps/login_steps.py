from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(u'que o usuário está na página de login')
def page_login(context):
    title = context.browser.title
    assert "VALIDA APP" in title, "Não está na página de login"

@when(u'informar o login e a senha')
def page_login_submit_user_password(context):
    username = "admin"
    password = "admin"
    context.browser.find_element(By.NAME, "username").send_keys(username)
    context.browser.find_element(By.NAME, "password").send_keys(password)

@then(u'o sistema deve autenticar o usuário')
def authenticate_user_login(context):
    context.browser.find_element(By.XPATH, "//button[contains(@class,'btn btn-primary')]").submit()
    


@then(u'permitir o acesso às funcionalidades do sistema.')
def page_admin(context):
    wait = WebDriverWait(context.browser,10)
    page_admin = wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(.,'Bem vindo ao Desafio')]")))
    assert "Bem vindo ao Desafio" in page_admin.text, "Não está na página do administrador"