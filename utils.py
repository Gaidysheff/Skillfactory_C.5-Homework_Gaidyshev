import requests
import json
from config import keys


class ConvertionException(Exception):
	pass


class CurrencyConverter:
	@staticmethod
	def convert(quote: str, base: str, amount: str):
		if quote == base:
			raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}')

		try:
			quote_ticker = keys[quote]
		except KeyError:
			raise ConvertionException(f'Не удалось обработать валюту {quote}')

		try:
			base_ticker = keys[base]
		except KeyError:
			raise ConvertionException(f'He удалось обработать валюту {base}')

		try:
			amount = float(amount.replace(',', '.'))
		except ValueError:
			raise ConvertionException(f'He удалось обработать количество {amount}')

		r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
		total = json.loads(r.content)[keys[base]] * amount
		total_base = float('{:.2f}'.format(total))

		return total_base

