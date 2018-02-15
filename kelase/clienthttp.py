import http.client

# Buat koneksi TCP ke server
conn = http.client.HTTPSConnection("ub.ac.id")
# Kirim request
conn.request("GET", "/")
# Terima dan baca response
resp = conn.getresponse()
# Baca header
header = resp.getheaders()
# Baca payload
payload = resp.read()

print(payload)