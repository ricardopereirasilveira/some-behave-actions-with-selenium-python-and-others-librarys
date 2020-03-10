from behave import given, when, then, step
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

@given('open the browser with the indicated URL')
def step_impl(context):
    # ABRINDO A SESSÃO, VERIFICANDO ALGUNS PARAMETROS E PEDINDO PRO BROWSER AGUARDAR CASO ESTEJA COM LENTINDÃO NO CARREGAMENTO
    context.url = 'http://www.newtours.demoaut.com/'
    context.titulo = 'Welcome: Mercury Tours'
    context.drive = webdriver.Firefox()
    context.drive.get(context.url)
    assert context.url == context.drive.current_url
    context.drive.implicitly_wait(60)
    assert context.titulo == context.drive.title

@when('insert the true username and password to access the restricted page')
def step_impl(context):
    context.drive.implicitly_wait(60)
    # USUARIO E SENHA
    context.username = ''
    context.password = ''
    # INSERINDO AS INFORMAÇÕES NOS CAMPOS NECESSARIOS E INDO PARA A PRÓXIMA PÁGINA
    context.drive.find_element_by_name('userName').click()
    context.drive.find_element_by_name('userName').send_keys(context.username)
    context.drive.find_element_by_name('password').click()
    context.drive.find_element_by_name('password').send_keys(context.password)
    context.drive.find_element_by_name('login').click()

@when('on the first page after login, select the dates of the round trip flights as requested and click on continue')
def step_impl(context):
    # PEDINDO PARA O BROWSER AGUARDAR CASO O CARREGAMENTO LEVE UM TEMPO
    context.drive.implicitly_wait(60)
    ## SELECIONANDO A IDA
    # SELECIONANDO O LONDON
    select = Select(context.drive.find_element_by_name('fromPort'))
    select.select_by_visible_text('London')
    # SELECIONANDO DECEMBER
    select = Select(context.drive.find_element_by_name('fromMonth'))
    select.select_by_value('12')
    # SELECIONANDO O DIA
    select = Select(context.drive.find_element_by_name('fromDay'))
    select.select_by_index('20')
    ## SELECIONANDO O RETORNO
    # SELECIONANDO O OCTOBER
    select = Select(context.drive.find_element_by_name('toMonth'))
    select.select_by_value('10')
    # SELECIONANDO O DIA
    select = Select(context.drive.find_element_by_name('toDay'))
    select.select_by_index('21')
    # SELECIONANDO A FIRST CLASS
    context.drive.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table/tbody/tr[9]/td[2]/font/font/input[2]').click()
    # SELECIONANDO AIRLINES
    select = Select(context.drive.find_element_by_name('airline'))
    select.select_by_visible_text('Blue Skies Airlines')
    sleep(1)
    # CLICANDO EM CONTINUAR
    context.drive.find_element_by_name('findFlights').click()
    sleep(1)


@when('on the next screen, select the outbound and return flights and click on continue')
def step_impl(context):
    # PEDINDO PARA O BROWSER AGUARDAR CASO O CARREGAMENTO LEVE UM TEMPO
    context.drive.implicitly_wait(60)
    # CONFIRMANDO SE O TITULO DA PÁGINA CORRESPONDE A PÁGINA ATUAL
    assert 'Select a Flight: Mercury Tours' == context.drive.title
    # SELECIONANDO O VOO DE IDA
    context.drive.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[1]/tbody/tr[5]/td[1]/input').click()
    sleep(1)
    # SELECIONANDO O VOO DE VOLTA
    context.drive.find_element_by_xpath('/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td/form/table[2]/tbody/tr[5]/td[1]/input').click()
    sleep(1)
    # CLICANDO EM CONTINUAR
    context.drive.find_element_by_name('reserveFlights').click()
    sleep(1)

@when("on this screen, validate the company's information and insert the required fields and click on secure purchase")
def step_impl(context):
    # CONFERINDO O VOO DE IDA
    context.flightGoing = context.drive.find_element_by_css_selector('body > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(3) > td.data_left > font > b').text
    assert context.flightGoing == 'Blue Skies Airlines 361'
    # CONFERINDO O VOO DE VOLTA
    context.flightReturn = context.drive.find_element_by_css_selector('body > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > form > table > tbody > tr:nth-child(2) > td > table > tbody > tr:nth-child(6) > td.data_left > font > font > font:nth-child(1) > b').text
    assert context.flightReturn == 'Blue Skies Airlines 631'
    # INSERINDO O FIRST NAME
    context.drive.find_element_by_name('passFirst0').send_keys('Teste')
    # INSERINDO O LAST NAME
    context.drive.find_element_by_name('passLast0').send_keys('Nextel')
    # INSERINDO O NUMBER
    context.drive.find_element_by_name('creditnumber').send_keys('118989038904')
    # CLICANDO EM SECURE PURCHASE
    context.drive.find_element_by_name('buyFlights').click()

@when('on this last screen, check if the Flight Confirmation Number has been generated')
def step_impl(context):
    # CONFIRMADO O VOO
    context.flightConfirmation = context.drive.find_element_by_css_selector('body > div > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr:nth-child(1) > td:nth-child(2) > table > tbody > tr:nth-child(5) > td > table > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(1) > b > font > font > b > font:nth-child(1)').text
    context.flightConfirmation.strip()
    assert context.drive.title == 'Flight Confirmation: Mercury Tours'
    assert context.drive.current_url == 'http://newtours.demoaut.com/mercurypurchase2.php'
    assert 'flight confirmation' in context.flightConfirmation.lower()

@then('close the browser and finish the selenium session')
def step_impl(context):
    context.drive.close()
    context.drive.quit()

