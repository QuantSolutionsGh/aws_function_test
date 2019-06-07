import requests

def lambda_handler(event, context):
  res = requests.get('https://google.com')
  print(res.text)
  return res.text

if __name__ == '__main__':
  lambda_handler(None, None)
