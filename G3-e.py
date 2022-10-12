import mysql.connector

conn = mysql.connector.connect(user="root", password="inter", host="127.0.0.1", database="discografia")
cursor = conn.cursor()

# definisco una funzione insert che in questo caso alimenta la tabella autore, con due colonne Nome e titolo canzone
def insert_autore(nome, titolo_canzone):
    sql = "INSERT INTO autore (nome, TitoloCanzone) VALUES (%s, %s)"
    val = (nome, titolo_canzone)
    try:
        cursor.execute(sql, val)
        conn.commit()
    except:
        conn.rollback()

sql = insert_autore("ligabue", "Certe Notti")
print(sql)
print("numero di righe inserite:", cursor.rowcount)


# con questa funzione cancello dalla tabella autore il valore nome
def delete_autore(nome, titolocanzone):
    sql = "DELETE FROM %s WHERE nome = '%s'"
    val = (nome, titolocanzone)
    try:
        cursor.execute(sql, val)
        conn.commit()
    except:
        conn.rollback()

sql = delete_autore("ligabue", "Certe Notti")
print(sql)
print("numero di righe cancellate:", cursor.rowcount)



def query_constructor(select, frm, join1=None, join2=None, where=None, groupby=None, orderby=None):
    stmt = 'select %s from %s ' % (select, frm)
    if join1 is not None:
        stmt = stmt + 'join %s ' % join1
    if join2 is not None:
        stmt = stmt + 'join %s ' % join2
    if where is not None:
        stmt = stmt + 'where %s ' % where
    if groupby is not None:
        stmt = stmt + 'group by %s ' % groupby
    if orderby is not None:
        stmt = stmt + 'order by %s' % orderby
    stmt = stmt + ';'
    return stmt

query_1 = query_constructor("NomeCantante","canzone","esecuzione on canzone.CodiceReg=esecuzione.CodiceReg","autore on esecuzione.TitoloCanzone=autore.TitoloCanzone","nome=NomeCantante and nome like 'D%'", None, None)
print(query_1)
cursor.execute(query_1)
result = cursor.fetchall()
print(result)

query_2 = query_constructor("TitoloAlbum", "disco", "contiene on disco.NroSerie=contiene.NroSerieDisco", "esecuzione on contiene.CodiceReg=esecuzione.CodiceReg", "ESECUZIONE.anno is NULL")
cursor.execute(query_2)
print(query_2)
result = cursor.fetchall()
print(result)

