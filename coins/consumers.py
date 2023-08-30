import json
import asyncio
import requests
from channels.generic.websocket import AsyncWebsocketConsumer


class CryptoPriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.fetch_crypto_prices()

    async def fetch_crypto_prices(self):
        important_coins = [
            "bitcoin",
            "ethereum",
            "cardano",
            "solana",
            # ارزهای دیگر را به این لیست اضافه کنید
        ]

        while True:
            try:
                response = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={
                    'ids': ','.join(important_coins),
                    'vs_currency': 'usd',
                })
                data = response.json()

                await self.send(text_data=json.dumps(data))
            except Exception as e:
                print(f"An error occurred: {e}")

            await asyncio.sleep(60)