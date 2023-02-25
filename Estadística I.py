#!/usr/bin/env python
# coding: utf-8

# ### Clase 01: Introducción a Python

# In[5]:


#Comentarios
"""
Comenarios
multi
linea
"""
#Operaciones básicas
5+8
9-7
x=5; x  #{formas de imprimir
x     
print(x)     #}
y=12; y
print(x,y)
print('La suma es', x+y)
x**2
x**(1/2)
x>y        #{Comparación
x==y
x!=y       #}


# In[7]:


texto1 = "Uno"
texto2 = "uno"
texto1<texto2    #Porque las mayúsculas tienen más peso que las minúsculas


# Paqueterías a utilizar: 
# -Numpy (matrices y vectores), cálculos numéricos
# -Pandas (Filtrar, leer archivos, manejo de estructura de datos, csv, sql)
# -Matplolib (Histogramas, gráficos de linea, barra, estadística descriptiva)
# -Seaborn

# In[16]:


v1 = [1,2,3,4,5]; print(v1)   #Listas con corchetes
v2 = [6,7,8,9,10]; print(v2)
v1+v2     #concatena

import numpy as np    #Llamas y nombras a la paquetería
v3 = np.array([1,2,3,4,5]); print(v3)     #array hace que trabaje con vectores, no con listas
v4 = np.array([6,7,8,9,10]); print(v4)
print(v3 + v4)                 #{Gracias a array, las operaciones entre vectores se pueden hacer entrada a entrada
print(v3*v4)                   #} 

len(v3)             #len me da la longitud de la lista


# In[31]:


M1 = np.array([[1,2],[3,4]]); print(M1)      #Construcción de matriz
M2 = np.array([[5,6],[7,8]]); print(M2)
M1 + M2
MP = np.dot(M1,M2); MP       #Producto matricial 
MI = np.identity(5); MI       #Matriz identidad de 5 renglones
MT = np.transpose(MP); MT     #Me da la matriz transpuesta
type(MP)                     #Me da el tipo de dato
MP.shape                    #Me da el tamaño de la matriz
MP.dtype               #Me da el tipo de dato de la matriz
M3 = np.array([["a","b"],["c","d"]]); M3      #Matriz con letras
M3 = np.array([["a",1],["c","d"]]); M3      #No puedo trabajar números con letras, requerimos un data frame;


# In[38]:


import pandas as pd 
import numpy as np
datos = {
    "Nombre": ["Viay", "Luz", "Dana", "Axel"],
    "Edad": [np.nan,21,21,22],                   #np.nan nos da el valor nulo
    "Carrera": ["Act","Act","Act","Act"]
}

df = pd.DataFrame(datos); df   #Me genera un data frame (Tabla con los valores de la lista)
df.info()                      #Me da información de mi data frame


# ### Clase 02: Uso de csv, filtros, medidas de tendencia central y dispersión

# In[40]:


import pandas as pd 
import numpy as np
datos = [["Viay", np.nan, "Act"],
         ["Luz", 21, "Act"], 
         ["Dana", 21, "Act"],
         ["Axel", 22, "Act"]]
columnas = ["Nombre", "Edad", "Carrera"]
filas = ["P1","P2","P3","P4"]                                  #{Cambiamos la columna que empezaba desde 0 a 3 por una columna
df = pd.DataFrame(datos,columns= columnas, index= filas); df   #<- que va desde P1 hasta P4}


# In[47]:


bejaia = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vT01D6JDV7LYXfqqpa3DUrXjw1vEftZkYe4jANgO936Mh16fePpOx38LuiOiX-H70D82zrKqi8CL3Ao/pub?gid=1108899917&single=true&output=csv")    #Lee los datos del csv
#bejaia.head(10)      #Me muestra las primeras diez filas de los datos
#bejaia.info()
bejaia.shape
bejaia.columns    #Me da las columnas de los datos


# In[53]:


# Partición del df

Incendio = bejaia[bejaia['Classes']==1]; Incendio    #Filtro de los días que hubo incendio
In30 = bejaia[bejaia['Temperature']>30]; In30         #Filtro de los días que hubo temperatura mayor a 30 grados

# & es para intersección,    | es para la unión
NoIncendio = bejaia[bejaia['Classes']==0]; NoIncendio   #Filtro de los días que NO hubo incendio
Incendio.describe()                          #Me da una descripción del data frame de Incendio


# In[54]:


Incendio.head(5)


# In[62]:


# Medidas de tendencia central
a = Incendio.iloc[:,3:7]        #La primera entrada me dará todos los renglones, la segunda las columnas del 3 al 7
a.head()
a.mean()                   #Medidas de tendencia central
a.median()                 #Me da la mediana de cada variable
a['Temperature'].value_counts()    #Cuenta cuántas veces se repitió la misma temperatura
a['Temperature'].mode()            #Me da la moda


# In[71]:


# Medidas de dispersión
m1 = a.min()        #Me da el mínimo
m2 = a.max()       #Me da el máximo
R = m2 - m1; R    #Me da el rango
print(a.var())            #Me da la varianza
print(a.std())           #Me da la desviación estándar

# Cuantiles, deciles, percentiles
np.quantile(a['Temperature'],[0,0.25,0.5,0.75,1])     #Me d alos valores que ocupan los cuartiles


# ### Clase 03: Tablas de frecuencia, agregar variables, intervalos, gráficos

# In[74]:


# Medidas de forma
a.skew()        #Coeficiente de asimetría
a.kurt()        #Curtosis


# In[80]:


#Tablas de frecuencia (conteo)
Incendio['month'].value_counts()
Incendio.groupby('month')['Temperature'].value_counts()     #{Me agrupa los meses con los datos de temperatura registrados 
                                                            #y las veces en que se repitieron} 
    
Incendio.groupby('month')['Temperature'].mean()             #{Hizo una agrupación por meses de la variable temperatura y
                                                            #sacó el promedio}
    
Incendio.groupby('month')['Temperature'].agg([np.min, np.max, np.mean, np.median])     #{Me genera una tabla resumen al agregar
                                                                                       #las funciones de numpy}


# In[85]:


#Tabla de frecuencia (intervalos)
Incendio['Intervalos']= pd.cut(Incendio['Temperature'], bins= 8)   #{Agrego una nueva variable a mi data frame (Intervalos),
                                                                   #donde 8 indica el número de divisiones que se hicieron
                                                                   #sobre la variable temperatura}
b = Incendio.groupby('Intervalos').agg(frequency= ('Temperature', 'count')); b


# In[93]:


#Gráficos: Histograma, boxplot, densidades, gráficos de barra, gráficos de pastel, gráficas de linea, polígono de frecuencias

#list(range(10))     #Me da los valores del 0 al 10
#list(range(1,10))    #Me da los valores del 1 al 10

import seaborn as sns
sns.relplot(x=list(range(len(bejaia))), hue= "Classes",y= "Temperature", data=bejaia)

