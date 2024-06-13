from django.views.generic import ListView
import requests


class GetExchangeListView(ListView):
    template_name = 'api/api_awesome/exchange_currency_list.html'
    context_object_name = 'api_awesome'    

    @staticmethod
    def get_exchange_data():
        currency = "USD-BRL,EUR-BRL,BTC-BRL"
        url = f"https://economia.awesomeapi.com.br/json/last/{currency}"
        response = requests.get(url)
        data = response.json()
        print(data)
        return data.values()

    def get_queryset(self):
        return self.get_exchange_data()        

