from http.client import responses

from exa_py import Exa

exa = Exa('b5f6fac1-9341-43b5-9428-ea34e169b6a3')

query = input('Enter search query: ')

responses = exa.search(query)

print(responses)
