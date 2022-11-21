from dotenv import dotenv_values
import os

path = '.env'
TOKEN = dotenv_values(path).get('token')
PAYMENT_TOKEN = dotenv_values(path).get('payment_token')