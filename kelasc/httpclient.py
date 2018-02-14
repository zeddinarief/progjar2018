import http.client

# Buka koneksi
conn = http.client.HTTPConnection("filkom.ub.ac.id")
# Kirim request
req = conn.request("GET", "/")
# Baca response nya
resp = conn.getresponse()
# Print Header
print("=======================================================")
print("Headernya adalah : ")
print(resp.getheaders())
print("=======================================================")
# Print payload
print("Payloadnya adalah : ")
print(resp.read())
print("=======================================================")