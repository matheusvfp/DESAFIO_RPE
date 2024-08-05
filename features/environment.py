from selenium.webdriver import Firefox



def before_all(context):

    
    context.browser = Firefox()
    context.browser.get("http://provaqa.prc.rpe.tech:9080/desafioqa/login")


def after_all(context):
    ...