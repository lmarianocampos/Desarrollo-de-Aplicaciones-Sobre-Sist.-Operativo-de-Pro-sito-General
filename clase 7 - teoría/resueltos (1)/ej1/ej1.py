import sqlite3
import sys


if len(sys.argv)!=2:
    print("Ingrese nombre archivo como argumento")
    exit(1)

db_file = sys.argv[1]

print("Trabajando con db:"+db_file)

conn = sqlite3.connect(db_file)
c = conn.cursor()

while True:
    sentence = input("Ingrese sentencia:")

    if "exit" in sentence:
        break

    try:
        c.execute(sentence)

        if "SELECT" in sentence:
            #era un select, imprimo resultado
            for r in c:
                print(r)        
        else:
            #hago commit
            conn.commit()
    except Exception as e:
        print(e)


conn.close()
