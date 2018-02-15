ibukota = {
    "Indonesia" : {
        "ibukota" : "Jakarta",
        "mata uang" : "Rupiah",
        "provinsi" : {
            "Jawa Timur" : {
                "ibukota" : "Surabaya",
                "kota" : ["Malang", "Kediri"]
            }
        }
    },
    "Filipina" : "Manila",
    "India" : "New Delhi",
    "Jepang" : "Tokyo"
}

#print(ibukota["Indonesia"]["provinsi"]["Jawa Timur"]["kota"])

import json
print(json.dumps(ibukota))