from django.shortcuts import render
import requests

# Create your views here.

def conversor(request):
    if request.method == "POST":
        from_currency = request.POST["from_currency"].upper()
        to_currency = request.POST["to_currency"].upper()
        amount = float(request.POST["amount"])

        url = f"https://open.er-api.com/v6/latest/{from_currency}"

        response = requests.get(url)
        data = response.json()

        if to_currency in data["rates"]:
            exchange_rate = data["rates"][to_currency]
            converted_amount = amount * exchange_rate
            return render(request, 'conversor/conversor.html', {
                'converted_amount' : converted_amount,
                'from_currency' : from_currency,
                'to_currency' : to_currency,
                'amount' : amount,
            })
        else:
            return render(request, 'conversor/conversor.html',{
                'error': 'Error: nao foi possivel encontrar a moeda de destino.'
            })
        
    return render(request, 'conversor/conversor.html')