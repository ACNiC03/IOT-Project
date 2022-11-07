import psycopg2
import SQLScript as SQL
con = psycopg2.connect(
    host='ahmetnicanci.ddns.net',       # De host waarop je database runt
    database='iot',    # Database naam
    user='admin',        # Als wat voor gebruiker je connect, standaard  postgres als je niets veranderd
    password='Studentje1'     # Wachtwoord die je opgaf bij installatie
    # port=5432 runt standaard op deze port en is alleen nodig als je de port handmatig veranderd
)
cur = con.cursor()

db = SQL.Database("ahmetnicanci.ddns.net", "iot", "admin", "Studentje1")


test = db.select("RFIDid" , "Employee")
print(test)

ids = db.select("rfid.rfidid", "RFID")
print(ids)