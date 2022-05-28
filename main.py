import csv
import sqlite3

with open("currencies22.csv", mode = 'r', encoding='utf-8') as r_file:

    file_reader = csv.reader(r_file, delimiter = ";")
    count = 0
    for row in file_reader:
        if count == 0:
            print(f' Name           Price        Marcet Cap')
            print(f' {"     ".join(row)}')
        else:
            print(f' {row[0]}       {row[1]}       {row[2]} ')
        count += 1

    print (" ")

print("Index massive")
print(" ")

con = sqlite3.Connection('cryptoDataBase1.db')
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS CTable (Name, Price, Marcet_Cap);")

moreCrypto = [('Bitcoin','$39,042.91', '$740,185,900,096'),
              ('Ethereum','$2,629.03', '$314,699,571,974'),
              ('Tether','$1.00', '$79,727,654,799'),
              ('BNB','$375.66', '$61,923,153,319'),
              ('USD Coin','$1.00', '$52,874,805,350'),
              ('XRP','$0.7222', '$34,571,861,293'),
              ('Terra','$83.70', '$30,924,825,975'),
              ('Cardano','$0.8485', '$28,572,471,711'),
              ('Solana','$88.44', '$27,996,936,059'),
              ('Avalanche','$76.12', '$20,206,218,196'),
              ('Binance USD','$0.9996', '$17,945,162,902'),
              ('Polkadot','$16.74', '$16,527,777,456'),
              ('Dogecoin','$0.1229', '$16,305,497,774'),
              ('TerraUSD','$1.00', '$13,551,925,953'),
              ('Shiba Inu','$0.00002401', '$13,184,282,172'),
              ('Polygon','$1.48', '$11,259,979,784'),
              ('Wrapped Bitcoin','$39,020.00', '$10,401,835,175'),
              ('Cronos','$0.4018', '$10,149,874,833'),
              ('Dai','$0.9999', '$9,732,171,809'),
              ('Cosmos','$30.20', '$8,642,212,818'),
              ('Litecoin','$101.93', '$7,111,312,915'),
              ('NEAR Protocol','$10.62', '$6,842,198,633'),
              ('Chainlink','$13.86', '$6,457,496,696'),
              ('Uniswap','$8.92', '$6,128,650,374'),
              ('TRON','$0.05834', '$5,928,496,012')]

cur.executemany("INSERT INTO CTable VALUES (?, ?, ?)", moreCrypto)
cur.execute("SELECT * FROM CTable")

records = cur.fetchmany(26)
count = 0
for row in records:
    print(count, row[0])
    count += 1

search = input ("Write crypto index for 0 to 24: ")
def searchcrypto(search):
    if int(search) <= 24:
        print(records[int(search)])
    else:
        print("Index out of range")


searchcrypto(search)

con.commit()
con.close()
