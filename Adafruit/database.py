import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LMCJMON\SQLEXPRESS;'
                      'Database=ADADB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
def executeQuery(sql):   
    cursor.execute(sql)
    conn.commit()

def getQuery(sql):
    return cursor.execute(sql)

