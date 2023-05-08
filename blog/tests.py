from django.test import TestCase

# Create your tests here.
import requests

url = 'http://localhost:8000/contact/'
headers = {
    'Content-Type': 'application/json'
}
data = {
    'subject': 'Test message',
    'email': 'test@example.com',
    'message': 'This is a test message'
}
try:

    response = requests.post(url)
# print(response.values())
except Exception as e:
    print(e)

if response.status_code == 200:
    print('Email sent successfully')
else:
    print(response.text[0:5000])
    print('Failed to send email')