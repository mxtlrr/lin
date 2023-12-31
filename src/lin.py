import sqlite3
con = sqlite3.connect("lin.db")
cur = con.cursor()

LIQUIDS = 0
SOLIDS  = 1
HWGLASS = 2

class LinDB:
    def __init__() -> None:
        pass

    def MakeTables() -> None:
        try:
            cur.execute("CREATE TABLE Liquids(Name VARCHAR, Formula VARCHAR, Volume FLOAT);")
            cur.execute("CREATE TABLE Solids(Name VARCHAR, Formula VARCHAR, Volume FLOAT);")
            cur.execute("CREATE TABLE GlassHardware(Name VARCHAR, Count INT);")
        except sqlite3.OperationalError as e:
            print("[NONFATAL] sqlite3:", e)

    def WriteTableReagent(table: int, name: str, formula: str, quant: float) -> None:
        cur.execute(f"SELECT * FROM {table} WHERE Name='{name}'")
        result = cur.fetchone()
            
        if result: # exists, update.
            cur.execute(f"UPDATE {table} SET Name = '{name}', Formula = '{formula}', Volume = {quant}")
            con.commit()
            return
        else:
            cur.execute(f"INSERT INTO {table} VALUES ('{name}', '{formula}', {quant});")
            con.commit() # make sure our changes our committed into
                            # the DB
 
    def WriteTableGlassware(name: str, count: int):
        cur.execute(f"SELECT * FROM Glasshardware WHERE Name='{name}'")
        result = cur.fetchone()
            
        if result: # exists, update.
            cur.execute(f"UPDATE GlassHardware SET Name = '{name}', Formula = '{formula}', Volume = {quant}")
            con.commit()
            return
        else:
            cur.execute(f"INSERT INTO GlassHardware VALUES ('{name}', {count}")
            con.commit()

    def GetValue(table: int, name: str) -> tuple:
        if table == 0:   return cur.execute(f"SELECT * FROM Liquids WHERE Name='{name}'").fetchone()
        elif table == 1: return cur.execute(f"SELECT * FROM Solids WHERE Name='{name}'").fetchone()
        elif table == 2: return cur.execute(f"SELECT * FROM GlassHardware WHERE Name='{name}'").fetchone()

    def GetAll(table: int) -> tuple:
        if table == 0: return cur.execute(f"SELECT * FROM Liquids").fetchall()
        if table == 1: return cur.execute(f"SELECT * FROM Solids").fetchall()
        if table == 2: return cur.execute(f"SELECT * FROM GlassHardware").fetchall()

def main():
    LinDB.WriteTableReagent('Liquids', "Acetonitrile", "CH3CN", 450.47)
    for rows in LinDB.GetAll(LIQUIDS):
        print(rows)


if __name__ == "__main__":
    LinDB.MakeTables()
    main()
