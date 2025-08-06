# importar requests
import requests

number = input("ingrese un nunmero:")
print("Numero ingresado:", number)

# realizar una peticion get a la api de numbersapi
trivia_fetch = requests.get(f"http://numbersapi.com/{number}?json")

#imprimir el codigo de estado de la respuesta, se espera 200
print("Codigo de estado:", trivia_fetch.status_code)

# convertir el contenido de la respuesta a formato JSON
# y almacenarlo en una variable
trivia = trivia_fetch.json()
print("Información de la trivia", trivia)

# acceder al valor de la clave 'text' en el JSON
print("Mensaje de la trivia:", trivia['text'])

# acceder al valor de la clave 'number' en el JSON
print("Número de la trivia:", trivia['number'])

