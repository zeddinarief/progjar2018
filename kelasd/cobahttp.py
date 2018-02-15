import http.client

# Buat koneksi ke server
conn = http.client.HTTPConnection("filkom.ub.ac.id")

# Kirim request
conn.request("GET", "/")
# Baca response
resp = conn.getresponse()

# Baca header 
header = resp.getheaders()
# Baca body
body = resp.read()

# Cetak header dan body
#print(header)
print(body)