import requests

url = "https://rahulshettyacademy.com"
cookie = {'visit-month': 'February'}

response = requests.get(url, cookies=cookie)

print(response.history)
print(response.status_code)

se = requests.session()
se.cookies.update({'visit-month': 'February'})

res = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'})
print(res.text)

# Attachments
url1 = "https://petstore.swagger.io/v2/pet/984327/uploadImage"
files = {'file': open('C:\\Users\\nir.gurung\\Desktop\\Varonis screenshots\\UEBT-1495 Step 14.png', 'rb')}
r = requests.post(url1, files=files)
print(r.status_code)
print(r.text)
