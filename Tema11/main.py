import  sqlite3


def main():
    crearAlmno(1, "Luis", "Beltran")
    crearAlmno(2, "Luis", "Reinaldo")
    crearAlmno(3, "Carlos", "Beltran")
    crearAlmno(4, "Alberto", "Beltran")
    crearAlmno(5, "Alberto", "Ruiz")
    crearAlmno(6, "Alberto", "RR")
    crearAlmno(7, "Jose", "Beltran")
    crearAlmno(8, "Jose", "Girón")
    mostrarAlmno()

def crearAlmno(id, nombre, apellido):
    conn=sqlite3.connect('alumnos.db')
    cursor= conn.cursor()

    query='''INSERT INTO alumnos(id, nombre, apellido) VALUES(?, ?, ?)'''
    
    cursor.execute(query, (id, nombre, apellido))
 
    conn.commit()

    cursor.close()
    conn.close()

def mostrarAlmno():
    conn=sqlite3.connect('alumnos.db')
    cursor= conn.cursor()

    query="Select * from alumnos"
    rows=cursor.execute(query)
    for row in rows:
        print(row)


    cursor.close()
    conn.close()



if __name__=="__main__":
    main()