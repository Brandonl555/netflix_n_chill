import http.client

conn = http.client.HTTPSConnection("unogs-unogs-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "84af296ba0msh408ed6fb47a4768p14e53ajsn9809ff5d951d",
    'x-rapidapi-host': "unogs-unogs-v1.p.rapidapi.com"
    }

conn.request("GET", "/aaapi.cgi?t=images&q=70219642", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
