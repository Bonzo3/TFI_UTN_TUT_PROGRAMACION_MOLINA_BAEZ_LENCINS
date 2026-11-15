# Bitácora de IA

El punto 1 del trabajo práctico lo hice sin IA. Empecé a consultar en el punto 2. Las capturas compartidas se identifican por su contenido. Cuando una consulta incluía un bloque largo de código, indico el recorte y copio textualmente el pedido que lo acompañaba.

## Punto 2 — Magnitudes

### Corrección del redondeo en el límite

**El prompt**

Consulta acompañada por mi función `con_unidad` y la captura de la consigna. Pedido textual:

> Necesito que corrijas para los casos del ultimo parrafo de la consigna, cuando los valores está en el limite por ejempli 999.9999, que no me devuelva 1000Hz sino 1 kHz. Necesito que mantengas mi codigo y que realices la modiciacion para todas las escalas y unidad

Después pregunté:

> Tengo que garegar eso en cada if y elif?

> Bueno agregalo al codigo como te pido

**Qué contestó**

Propuso comprobar el valor justo después de redondearlo. Si llegaba a `1000`, la función debía devolver `1` con el prefijo siguiente. Después devolvió la función completa con los controles desde pico hasta mega. Por ejemplo, en el bloque sin prefijo agregó:

```python
if numero == 1000:
    return f"1 k{unidad}"
```

**Qué cambiaste**

Pedí que se mantuvieran mis ramas por escala y unidad y que la corrección estuviera integrada en el código completo. La versión devuelta también quitó un `print` de depuración y un redondeo cuyo resultado no se usaba.

**Cómo lo verificaste**

En la salida que compartí apareció `1 kHz` para el caso del límite. La IA también propuso comprobar el mismo valor con `V` y `s`. En el chat no quedó una ejecución de todas esas variantes.

### Diferencia entre dos valores cercanos al límite

**El prompt**

> Me esta devolviendo mal

Adjunté la captura donde probaba `con_unidad(0.9999, "Hz")`.

**Qué contestó**

Explicó que `0.9999 * 1000` da `999.9`. Redondeado a tres decimales sigue siendo `999.9`. Con `0.9999999`, el valor expresado en milihertz sí redondea a `1000` y pasa a `1 Hz`.

**Qué cambiaste**

Revisé el valor que estaba usando para probar el límite. La respuesta no propuso otro cambio en la función.

**Cómo lo verificaste**

La captura muestra `999.9 mHz` para `0.9999 Hz`. Quedó sugerida la comparación con `con_unidad(0.9999999, "Hz")`, que debería devolver `1 Hz`.

## Punto 3 — Órdenes y consultas

### Cantidad de argumentos

**El prompt**

> Vamos con el siguiente, este es  mi codigo hasta ahora. Me genera dudas la regla "Una orden no lleva argumento"

Adjunté mi código de `es_consulta` y `validar` y la captura de la consigna. Después pregunté:

> de donde salio esta variable consulta?

> explicame como funciona esta parte

La última captura mostraba el bloque de `split()` y las condiciones que comprueban los argumentos.

**Qué contestó**

Aclaró que una orden lleva un argumento y una consulta lleva cero. Propuso guardar `es_consulta(comando)` en `consulta`, usar `comando.split()` y calcular `len(partes) - 1`, porque la primera parte es el nombre del comando. También explicó que `validar` devuelve un texto si detecta un error y `None` si el comando pasa todas las reglas.

**Qué cambiaste**

Incorporé el conteo de argumentos y la variable `consulta` en mi validador. Mis capturas muestran que seguí usando mis propios textos para algunos errores.

**Cómo lo verificaste**

Probé `:CH1:DISPlay ON?` y `:CH1:DISPlay ON`. Las primeras ejecuciones mostraron los problemas de condición y de nombre de variable que registré debajo. El resultado esperado es un motivo de rechazo para la consulta con argumento y `None` para la orden válida.

### Condición para validar el primer carácter

**El prompt**

> Esta entrando al segundo if no deberia

Adjunté la condición y la salida de la terminal.

**Qué contestó**

Explicó que con `or` la condición siempre entra. Si el primer carácter es `:`, ya se cumple que es distinto de `*`. Propuso:

```python
if comando[0] != ":" and comando[0] != "*":
    return "El comando debe empezar con : o *"
```

**Qué cambiaste**

Cambié el `or` por `and`.

**Cómo lo verificaste**

La ejecución siguiente pasó esa comprobación y llegó a la línea que cuenta los argumentos, donde apareció el `NameError` de la entrada siguiente.

### Variable en singular y plural

**El prompt**

> Lo cambie y ahora me tira este error?

Adjunté la captura del `NameError`.

**Qué contestó**

Señaló que había definido `cantidad_argumento` y después usaba `cantidad_argumentos`. Indicó que debía usar el mismo nombre en ambos lugares.

**Qué cambiaste**

La corrección indicada fue agregar la `s` en la asignación para que el nombre coincidiera con el de la condición.

**Cómo lo verificaste**

La captura identifica la diferencia de nombres. Quedó sugerido volver a ejecutar `validar(":CH1:DISPlay ON?")` y comprobar el mensaje de rechazo.

## Punto 4 — Configurar un canal

### Construcción de la lista

**El prompt**

Adjunté mi función incompleta y la consigna. La pregunta textual fue:

> Consideraba usar if para ir construyendo la lista. Sería practico mi forma de hacerla segun se me solicita?

**Qué contestó**

Propuso validar el canal una vez, devolver `None` si no era `CH1` ni `CH2` y armar las cuatro órdenes en una lista inicialmente vacía con `append()`. Explicó que `[3]` crea una lista con un solo elemento, el número `3`.

**Qué cambiaste**

La adaptación propuesta fue usar `[]`, reemplazar los bloques repetidos por cuatro `append()` y devolver la lista desde la función.

**Cómo lo verificaste**

Quedó propuesta la comparación con las cuatro órdenes de la consigna, en orden, y comprobar cada una con `assert validar(comando) is None`. No quedó una salida de esas pruebas en el chat.

### Importación del validador

**El prompt**

> Ahora necesito importar validar del ejercicio anterior, el problema es que el archivo se llama from *03_comandos*.py hay alguna otra forma de importarlo sin usar "from from *03_comandos*.py import validar"?

**Qué contestó**

Mostró cómo importar un módulo cuyo nombre empieza con un número, usando el nombre como texto y sin la extensión:

```python
from importlib import import_module
validar = import_module("03_comandos").validar
```

**Qué cambiaste**

La solución propuesta permitía conservar el nombre `03_comandos.py`. Usé después el mismo mecanismo de importación en los puntos 6 y 7.

**Cómo lo verificaste**

En el chat se ve que el mismo mecanismo permitió cargar otros módulos numerados del TP. Quedó pendiente confirmar con la salida del punto 4 que las cuatro órdenes pasan `validar`.

## Punto 5 — Cliente del instrumento

### Método de instancia y conexión TCP

**El prompt**

> como definia un metodo dentro de una clase?

> Vamos con el 5. Tengo que conectar con un servidor local en mi equipo. Ahora estoy probando la conexón pero me arrija error en el metodo enviar

Adjunté una captura de mi clase y los dos `TypeError`.

**Qué contestó**

Explicó que Python pasa automáticamente la instancia como primer argumento del método. La firma quedó como `def enviar(self, ip, puerto, orden):`. También corrigió `connect(ip, puerto)` a `connect((ip, puerto))` y propuso `sendall()` para enviar el comando entero.

**Qué cambiaste**

En mi versión posterior se ve un primer parámetro para recibir la instancia (escrito `sefl` en la captura), la tupla `(ip, puerto)` y el uso de `sendall()`.

**Cómo lo verificaste**

Volví a probar la conexión local con `*IDN?`. El siguiente problema fue que el servidor quedaba esperando la terminación del comando.

### Terminación de la orden

**El prompt**

> El servidor no responde

**Qué contestó**

Propuso agregar `\n` a la orden antes de codificarla y enviarla. También propuso un tiempo de espera de cinco segundos para diagnosticar una falta de respuesta.

**Qué cambiaste**

Agregué el salto de línea a la orden. En mi captura posterior aparece tanto en `enviar()` como en `preguntar()`.

**Cómo lo verificaste**

Confirmé en el chat: «Si faltaba el \n». Las ejecuciones posteriores del barrido ya mostraron respuestas del servidor.

## Punto 6 — Barrido

### Uso del objeto y conversión de la respuesta

**El prompt**

> No estoy entendiendo bien que hay que hacer en este punto. No se si tengo que trabajar con el objeto desde este bloque.

Después de adjuntar la consigna del punto 6, mostré mi código inicial. El pedido que acompañaba ese código fue:

> este es micodigo por ahora, no se bien como debería continuar

También pregunté:

> Sigo sin comprender bien como trabajan juntos el punto 5 y 6

> Entonces barrer debería ser llamda desde el punto 5?

> Ok, entonces tambien desde el punto 6 debo llamar a la funcion para convertir los valores

**Qué contestó**

Explicó que `barrer(instrumento, canales)` recibe un objeto creado afuera. Recorre los canales y las tres magnitudes, arma cada consulta con el signo `?`, llama a `instrumento.preguntar(...)` y guarda un diccionario con el texto recibido y el resultado de `a_numero()`. Mostró también cómo importar el módulo sin escribir `.py`.

**Qué cambiaste**

Armé los comandos usando el canal y la magnitud de cada vuelta. Conservé la firma de mi cliente, que recibe IP, puerto y comando, y guardé tanto el texto crudo como el número convertido.

**Cómo lo verificaste**

Ejecuté el barrido para `CH1` y `CH2`. La primera salida mostró seis diccionarios, pero todos tenían `None` en el texto y el valor. La corrección y la siguiente salida quedaron registradas abajo.

### Respuesta perdida entre los puntos 5 y 6

**El prompt**

> No hay algo que no esta bien: Mira la salida del 6

> aca esta el 5 que hice yo

Adjunté la salida con los seis valores en `None` y una captura del cliente.

**Qué contestó**

Detectó que `preguntar()` devolvía `parsear_idn(respuesta)` para todas las consultas. Indicó devolver `respuesta` directamente y llamar a `parsear_idn()` donde se prueba específicamente `*IDN?`.

**Qué cambiaste**

En mi versión posterior de `05_cliente.py`, `preguntar()` termina con `return respuesta`.

**Cómo lo verificaste**

Volví a ejecutar el barrido. La captura siguiente mostró las seis mediciones con texto crudo y números. Por ejemplo, para la frecuencia de CH2 se veía un valor convertido de `2488.912` Hz.

### Unidades base y prefijos

**El prompt**

> OK, parece que funicono mas o menos, al parecer la lista con las mediciones no cambia las magnitudes bien

> Perdon, las unidades. Donde vez kHz o mV?

**Qué contestó**

Explicó que la salida de mi captura muestra `Hz` y `V`, que son las unidades base de los números del barrido. `kHz` y `mV` eran ejemplos de lo que se vería al aplicar `con_unidad()` para mostrar el resultado.

**Qué cambiaste**

La respuesta propuso aplicar `con_unidad()` al imprimir y conservar la unidad base en el diccionario del barrido. No quedó registrado si incorporé ese formato de impresión.

**Cómo lo verificaste**

Comparé la unidad de la salida con el número guardado. La captura muestra `2488.912` con `Hz`. El ejemplo de formato sugerido fue `con_unidad(2488.912, "Hz")`, cuyo resultado esperado es `2.489 kHz`.

## Punto 7 — Verificación

### Cálculo y comparación del RMS

**El prompt**

> Sigamos con el 7.

Adjunté la consigna. Después pedí:

> Explicame el codigo paso a paso

**Qué contestó**

Propuso calcular el RMS teórico de una senoide con `vpp / (2 * sqrt(2))`, calcular el error relativo con `abs(medido - teorico) / abs(teorico)` y compararlo con `0.02`. En `verificar_canal()` buscó `PKPK` y `CYCRms` para el canal pedido y usó sus valores del barrido.

**Qué cambiaste**

Usé el resultado del punto 6 como entrada y llamé a `verificar_canal` para los dos canales. En mi captura se ve la función `coincide()` con la tolerancia del 2 %.

**Cómo lo verificaste**

Ejecuté varias veces con el servidor. La prueba con un caso fuera de tolerancia se registra debajo.

### Desde dónde llamar al barrido

**El prompt**

> Ahora la duda es desde donde debería ser llamada barrido?

> Así importe yo barrido, esta bien?

```python
from math import isfinite, sqrt
import importlib

barrido = importlib.import_module("06_barrido")
```

> No logro conseguir que llame al objeto instrumento. Creo que está bien importado

La última consulta incluía las capturas de los intentos y sus errores.

**Qué contestó**

Indicó que el bloque de prueba del punto 7 podía crear `instrumento1 = cliente.Instrumento()`, llamar una sola vez a `barrido.barrer(instrumento1, ["CH1", "CH2"])` y pasar las filas a ambas verificaciones. Explicó que los paréntesis crean la instancia y que el objeto de prueba del punto 5 solo se crea cuando se ejecuta ese archivo directamente.

**Qué cambiaste**

Creé la instancia en el punto 7 y pasé esa instancia al barrido. La captura de la ejecución posterior muestra la llamada con `instrumento1`.

**Cómo lo verificaste**

El punto 7 imprimió dos diccionarios, uno por canal, con Vpp, RMS medido, RMS teórico y el resultado de la comparación.

### Salidas que siempre daban True

**El prompt**

> Despues de varias pruebas noto que siemre arroja TRUE. hay algun error en mi funcion?

> Analisa estas salidas. Me parece raro que siempre salga True

Adjunté las capturas de `coincide()` y las corridas.

**Qué contestó**

Calculó el error relativo de las mediciones visibles. Por ejemplo, en una corrida de CH1 comparó `0.7105606` con aproximadamente `0.7039732`, lo que da un error de `0.94 %`. Propuso armar filas con `PKPK = 2.0` y `CYCRms = 1.0` para comprobar el caso que debe devolver `False`.

**Qué cambiaste**

La revisión de las salidas mantuvo la fórmula y la tolerancia. La prueba sugerida cambia los datos de entrada a un caso fuera del margen.

**Cómo lo verificaste**

Las corridas compartidas fueron compatibles con el `True` que mostró la función. Para las filas de la señal cuadrada, el RMS teórico es aproximadamente `0.7071 V` y el error relativo es aproximadamente `41.4 %`. Quedó sugerido ejecutar `assert verificar_canal(filas_prueba, "CH1")["coincide"] is False`. No compartí el resultado de esa prueba.

## Punto 8 — Registro de la sesión

### El par de resultados por línea

**El prompt**

> vamos al 8. No entiendo a que se refiere en que devuelva medicion y motivo

> Podría definir a medicion como un diccionario y a motivo como una lista

```python
medicion = {}
   motivo = []
```

Después compartí mi función inicial, que abría el archivo y recorría sus líneas, y pregunté:

> Por que dice que siempre alguno de los dos e None?

**Qué contestó**

Explicó que `analizar_linea(linea)` devuelve dos posiciones. Una línea válida devuelve `(medicion, None)`, una rechazada devuelve `(None, motivo)` con un texto, y una ignorada devuelve `(None, None)`. Mostró cómo llamar a la función desde `leer_log(ruta)` y recibir los dos resultados con `medicion, motivo = analizar_linea(linea)`.

**Qué cambiaste**

En mi avance ya leía el archivo y filtraba los comentarios. La adaptación propuesta fue pasar el recorrido a `leer_log()`, analizar una línea por llamada y usar la lista para acumular rechazos con su número de línea.

**Cómo lo verificaste**

Probé la lectura del archivo y mostré mi código de avance. Quedó pendiente comprobar la tupla para una línea válida, una rechazada y una ignorada, además de verificar las agrupaciones del archivo completo.
