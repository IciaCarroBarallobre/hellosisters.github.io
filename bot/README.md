# Como crear un bot para Slack 

### Instalación del entorno

Usaremos un entorno virtual: `$ virtualenv  -p python3 venv` para manejar las dependencias del proyecto. 

Se accede a el mediante el comando:  `$ source venv/bin/activate`. 

Una vez dentro instalaremos las dependencias, como por ejemplo,  API de Slack : ` $ pip install slackclient`, esta librería simplifica el uso de Slack's [RTM API](https://translate.googleusercontent.com/translate_c?depth=1&hl=es&rurl=translate.google.com&sl=auto&sp=nmt4&tl=es&u=https://api.slack.com/rtm&usg=ALkJrhiU9_258YSiWjN7_VKqmz6hCLiW_Q) y [Web API](https://translate.googleusercontent.com/translate_c?depth=1&hl=es&rurl=translate.google.com&sl=auto&sp=nmt4&tl=es&u=https://api.slack.com/web&usg=ALkJrhgVw0DrryM9v5fdqjYN5WhxcWOtgg) .

Dejaremos un archivo que indicará las librerías usadas, por que para instalarlos deberemos hacer:

 `$ pip install requirements.txt ` 

### SLACK bot 

##### Configuracion

###### Token

Debemos exportar el token de nuestro bot como una variable de entorno porque lo pedirá la librería para estar autorizados para usar  Slack RTM y API web como usuario de bot: 

```shell
$ export SLACK_BOT_TOKEN = 'token_aqui'
```



###### Certificados

A veces da un error por el certificado. La razón por la que esto falla proviene del paquete websocket y del paquete CA que usa (que no está actualizado). 

Se puede solucionar de la siguiente forma:

```shell
wget https://www.tbs-certificats.com/issuerdata/DigiCertGlobalRootCA.crt --no-check-certificate

export WEBSOCKET_CLIENT_CA_BUNDLE=DigiCertGlobalRootCA.crt
```



##### Ejecutar

```shell
$ python sisbot.py
```

