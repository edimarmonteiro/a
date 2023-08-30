from webdriver_manager.chrome import ChromeDriverManager
#permite criar o navegador
from selenium import webdriver
#me permite encontar coisas no navegador
from selenium.webdriver.common.by import By
#importando modelo de captcha que sera resolvido * (todasa as informações)
from anticaptchaofficial.recaptchav2proxyless import *
#biblioteca de tempo
import time
from chave import chave_api

#acessando o site na web
navegador = webdriver.Chrome()
link = "https://google.com/recaptcha/api2/demo"
navegador.get(link)

#indetificando a chave do captcha com o selenium(Atraves do html)
IdCaptcha = navegador.find_element(By.ID, 'recaptcha-demo').get_attribute('data-sitekey')

resolveCaptcha = recaptchaV2Proxyless()
#mostrar o status do serviço(o andamento)
resolveCaptcha.set_verbose(1)
#configuração da minha conta
resolveCaptcha.set_key(chave_api)
#link do site que ele ira resolver
resolveCaptcha.set_website_url(link)
#a chave do captcha que sera resolvido
resolveCaptcha.set_website_key(IdCaptcha)

#resolvendo o captcha
#solve_and_return_solution() -> resolva o captcha e me retorne en var respostaCapatcha
respostaCapatcha = resolveCaptcha.solve_and_return_solution()

#!=(deu certo) / =0(deu merda)
if respostaCapatcha != 0:
    print(respostaCapatcha)
    #g-recaptcha-response
    #preencher o campo token do captcha
        #execute_script(para realizar um comando JS, que será quem ira interpletar o html)
            #nessa parte eu uso o js(execute_script) em vez de (find_element)como nos outros casos, 
            #pq aqui o elemento selecionado não está visivel para o selenium
    navegador.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{respostaCapatcha}'")
    #enviando a resolução do chaptcha
    navegador.find_element(By.ID, 'recaptcha-demo-submit').click()
else:
    print(resolveCaptcha.err_string)
#time.sleep(500)