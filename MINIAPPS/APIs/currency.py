import requests

currencyListURL="https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.json"
currencyList=requests.get(currencyListURL)
userInput=input('Which currency do you want relative to inr?: ')

url="https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/{INR}/{userInput}.json".format(INR="inr",userInput=userInput)

response=requests.get(url)

print (response.json()[userInput])