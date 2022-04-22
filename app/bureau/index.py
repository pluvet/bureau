from fastapi import FastAPI
from routes.bureau import bureau 

app = FastAPI()
app.include_router(bureau, prefix='/bureau')



# subir el proximo proyecto a un repositorio con docker
# 1. empiece a manejar a un mayor nivel FAstApi inyeccion de dependencias definir headers request body, excepciones saber mas de fastapi
# 2. aprender sobre programacion concurrente (asincrona async await)
# 3. elastic search (por ahora no)
# 4. bases de datos mongodb libreria asincrona (no pymongo)
# 
# app:
# crear un pequeño microservicio, API que va a hacer
# crear un pequeño servicio con un solo endpoint al que le puedo mandar data de un usuario (c.i, nombre, apellido)
# va a agarrar esa info personal y va a consultar un buro de credito (imite la llamada al buro)
# al buro se le manda la cedula para que traiga la info similar a la info personal 
# primera comprobacion que la informacion suministrada de la persona en la request concuerda con la del buro 
# la llamada al buro debe ser asincrona (asyncao concurrencia en python)
# guardo un log en mongo de que paso con esa persona (los datos que nos dio, la del buro y la comprobacio y si fue exitosa)
# la llamada a db debe ser asincrona
# en el response si la info fue correcta o incorrecta 
#
# principal objetivo entender la concurrencia 
#
# simular la llamada al buro, programa para simular servidores http



