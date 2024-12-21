import http.client
import re
conn = http.client.HTTPConnection('127.0.0.1',5000)
post=input()
if post=='':
    post=field_name_1='field_name_1=abc@mail.lol&field_name_2=+7 999 999 99 99&field_name_3=+7 999 999 99 99'
post=re.sub(r'\s','%20',post)
conn.request("POST", "get_form?"+post)
response = conn.getresponse()
# print(response.status, response.reason)
print(response.read().decode("utf-8"))
conn.close()