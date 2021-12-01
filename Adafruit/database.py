import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-LMCJMON\SQLEXPRESS;'
                      'Database=ADADB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor = conn.cursor()
def executeQuery(sql):   # thực hiện insert, update
    cursor.execute(sql)
    conn.commit()

def getQuery(sql):      # thực hiện slect
    return cursor.execute(sql)

