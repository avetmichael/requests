import requests
res = requests.request("GET", "https://httpbin.org/robots.txt")
print(res.status_code)
print(res.content)
res1 = requests.request("GET", "https://httpbin.org/get")
print(res1.status_code)
print(res1.content)
res2 = requests.request("GET", "https://httpbin.org/headers")
print(res2.status_code)
print(res2.content)
res3 = requests.request("GET", "https://httpbin.org/user-agent")
print(res3.status_code)
print(res3.content)
res4 = requests.request("GET", "https://httpbin.org/brotli")
print(res4.status_code)
print(res4.content)
################
d = {"name": "Erik"}
res5 = requests.request("POST", "https://httpbin.org/post", data=d)
print(res5.status_code)
res5_json = res5.json
print(res5.json())
res6 = requests.request("POST", "https://httpbin.org/delay/{delay},")
print(res6.status_code)
res6_json = res6.json
print(res6.json())
res7 = requests.request("POST", "https://httpbin.org/anything/{anything}", data=d)
print(res7.status_code)
res7_json = res7.json
print(res7_json())
res8 = requests.request("POST", "https://httpbin.org/anything", data=d)
print(res8.status_code)
res8_json = res8.json
print(res8.json())
res9 = requests.request("POST", "https://httpbin.org/status/{codes}", data=d)
print(res9.status_code)
res9_json = res9.json
print(res9.json())
##################
res10 = requests.request("DELETE", "https://httpbin.org/delete")
print(res10.status_code)
print(res10.content)
res11 = requests.request("DELETE", "https://httpbin.org/anything/wd")
print(res11.status_code)
print(res11.content)
res12 = requests.request("DELETE", "https://httpbin.org/anything")
print(res12.status_code)
print(res12.content)
res13 = requests.request("DELETE", "https://httpbin.org/redirect-to")
print(res13.status_code)
print(res13.content)
res14 = requests.request("DELETE", "https://httpbin.org/delay/23")
print(res14.status_code)
print(res14.content)
#####################
res15 = requests.request("PUT", "https://httpbin.org/put")
print(res15.status_code)
print(res15.content)
res16 = requests.request("PUT", "https://httpbin.org/status/{codes}")
print(res16.status_code)
print(res16.content)
res17 = requests.request("PUT", "https://httpbin.org/delay/31")
print(res17.status_code)
print(res17.content)
res18 = requests.request("PUT", "https://httpbin.org/redirect-to")
print(res18.status_code)
print(res18.content)
res19 = requests.request("PUT", "https://httpbin.org/anything")
print(res19.status_code)
print(res19.content)
