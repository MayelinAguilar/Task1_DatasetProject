import psycopg2

conection = psycopg2.connect(
    dbname = 'DNP-ProductoSector',
    user = 'mayelin',
    password = 'contrasena',
    host = 'https://github.com/MayelinAguilar/Task1_DatasetProject/blob/main/DNP-ProductoSector.csv',
    port = 5432
)

# Crear un cursor para ejecutar comandos SQL
cursor = conection.cursor()

# Ejecutar una consulta en la base de datos
query = "DNP-ProductoSector"
cursor.execute(query)

# Obtener los resultados de la consulta
results = cursor.fetchall()

# Imprimir los resultados
for row in results:
    print(row)

# Cerrar la conexión con la base de datos
conection.close()

