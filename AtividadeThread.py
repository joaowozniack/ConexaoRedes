import os

def download_url(url):
    print("downloading: " + url + "\n")
    os.system("curl http://localhost/dog/" + url + " --ssl-no-revoke -L -O")
    return url

arquivo = open("dog.txt","r")

listaApk = []

for linha in arquivo:
    linha = linha.replace("\r", "")
    linha = linha.replace("\n", "")
    listaApk.append(linha)

arquivo.close()

for r in listaApk:
    download_url(r)
    print(r)