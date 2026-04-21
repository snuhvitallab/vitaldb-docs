# Manual de Usuario de VitalRecorder (Spanish)

VitalRecorder es una aplicacion de registro de signos vitales en tiempo real para Windows, Raspberry Pi y Ubuntu. Captura datos de mas de 80 dispositivos medicos y los almacena en formato de archivo `.vital`.

---

## Tabla de Contenidos

1. [Instalacion](#instalacion)
2. [Inicio Rapido](#inicio-rapido)
3. [Interfaz de Usuario](#interfaz-de-usuario)
4. [Agregar Dispositivos](#agregar-dispositivos)
5. [Tipos de Conexion](#tipos-de-conexion)
6. [Filtrado de Puertos](#filtrado-de-puertos)
7. [Grabacion](#grabacion)
8. [Carga al Servidor](#carga-al-servidor)
9. [Archivo de Configuracion (vr.conf)](#archivo-de-configuracion-vrconf)
10. [Opciones de Linea de Comandos](#opciones-de-linea-de-comandos)
11. [Dispositivos Compatibles](#dispositivos-compatibles)
12. [Solucion de Problemas](#solucion-de-problemas)

---

## Instalacion

### Windows

Descargue e instale desde Microsoft Store:
- Store URL: https://apps.microsoft.com/detail/9MVBQL8R0TFL

O descargue el instalador MSI o el paquete MSIX desde la pagina de versiones.

### Raspberry Pi / Ubuntu

Descargue el binario especifico de la plataforma (`pivr64` o `ubuntu64`) desde la pagina de versiones y ejecutelo directamente.

---

## Inicio Rapido

1. Inicie VitalRecorder.
2. Haga clic en el boton **Agregar Dispositivo** para agregar un dispositivo medico.
3. Seleccione el tipo de dispositivo (por ejemplo, `Medtronic : BIS`, `Philips : Intellivue`).
4. Elija el puerto de conexion (COM port, direccion IP o numero de puerto).
5. Haga clic en **Aceptar**. VitalRecorder comenzara a comunicarse con el dispositivo.
6. Haga clic en **Grabar** para iniciar la grabacion de datos.

---

## Interfaz de Usuario

VitalRecorder utiliza una interfaz basada en pestanas. Cada pestana representa una "sala" o "cama" y puede tener multiples dispositivos conectados.

- **Pistas (Tracks)**: Cada dispositivo genera una o mas pistas (por ejemplo, HR, SpO2, BIS). Las pistas se muestran como formas de onda o valores numericos.
- **Eventos**: Puede agregar marcadores de eventos durante la grabacion.
- **Monitor**: Un panel de monitor configurable muestra los parametros seleccionados en texto grande.

### Nombre de Cama

A cada pestana se le puede asignar un **nombre de cama**. Este se utiliza para:
- Identificar la sala al cargar datos al servidor.
- Separar datos de multiples camas provenientes de dispositivos de gateway HL7.

---

## Agregar Dispositivos

Vaya a **Agregar Dispositivo** y seleccione entre los grupos de dispositivos:

| Grupo | Ejemplos |
|-------|----------|
| Dispositivos VitalDB | SNUADC, SNUADCM, BUTTON, VitalBOLUS |
| Convertidor analogico-digital | DataQ DI-149, DI-155, DI-245, DI-1100, DI-1120 |
| Monitor de paciente | Philips Intellivue, GE Solar/Dash/Bx50, Nihon Kohden, Mindray HL7, MEKICS |
| Monitor multifuncion | Masimo Radical-7/Root, Sentec SDM |
| Maquina de anestesia | Draeger Primus/Zeus/Fabius, GE Datex-Ohmeda Aisys/Avance |
| Ventilador mecanico | Maquet SERVO-i/s/U, Hamilton MR1/C2/C6/T1 |
| Bomba de infusion de farmacos | Fresenius Agilia/Primea/PCBM, BBraun SpaceCom/HL7, Daiwha, Pion |
| Monitor cerebral | Medtronic BIS/VISTA/INVOS, Fresenius Conox, OBELAB NirsitON |
| Monitor neuromuscular | TwitchView, TOFScan, TOFcuff |
| Calentador de fluidos | Belmont FMS 2000 |
| Monitor de gasto cardiaco | Edwards Hemosphere/Vigilance/EV1000/Vigileo, Getinge PulsioFlex |
| Monitor fetal | GE Corometrics 250cx |

---

## Tipos de Conexion

### RS-232 (Serial / COM Port)

La mayoria de los dispositivos utilizan comunicacion serial RS-232 a traves de un COM port fisico o un adaptador USB-to-Serial.

- Seleccione el numero de COM port (por ejemplo, `COM3`).
- La velocidad de transmision y otros parametros seriales se configuran automaticamente segun el tipo de dispositivo.
- Instale el controlador USB-to-Serial antes de conectar.

### TCP (Red)

Para dispositivos conectados por red. VitalRecorder puede actuar como **cliente** o **servidor** TCP.

- **Modo cliente**: Introduzca la direccion IP y el puerto del dispositivo como `IP:PORT` (por ejemplo, `192.168.1.100:9001`).
- **Modo servidor**: Introduzca solo el numero de puerto (por ejemplo, `2575`). VitalRecorder escucha y espera que el dispositivo se conecte.

Los dispositivos HL7 (Mindray HL7, Nihon Kohden HL7GW, BBraun HL7) generalmente usan el modo servidor con encapsulamiento MLLP.

### UDP (Red)

Algunos dispositivos transmiten datos por UDP.

- Introduzca el numero de puerto para escuchar.

### BLE (Bluetooth Low Energy)

Para sensores inalambricos como Movesense.

- Requiere Windows 10 o superior con un adaptador Bluetooth 4.0.
- El dispositivo debe estar en modo de emparejamiento.

---

## Filtrado de Puertos

Al conectar dispositivos TCP/UDP, puede agregar filtros a la cadena de puerto para aceptar selectivamente conexiones o mensajes. Solo funciona con comunicaciones basadas en tramas con delimitadores (como HL7).

### Formato

```
PORT#KEYWORD@IP_ADDRESS
```

Todas las partes excepto PORT son opcionales.

### Filtro de Palabra Clave (`#`)

Filtra los mensajes entrantes buscando una cadena de palabra clave dentro del contenido del mensaje. Los mensajes que no contienen la palabra clave se descartan silenciosamente.

```
2575#BED-001
```

Esto escucha en el puerto 2575 y solo procesa mensajes que contienen `BED-001`. Esto es util cuando un unico gateway HL7 (por ejemplo, DoseLink, Mindray Gateway) envia datos de multiples camas a traves de una sola conexion.

#### Multiples Palabras Clave

- **Condicion AND**: Separe las palabras clave con un espacio para procesar solo los mensajes que contienen todas las palabras clave.
  ```
  2575#BED-001 Propofol
  ```
- **Condicion OR**: Use `#` multiples veces para procesar mensajes que contienen cualquiera de las palabras clave.
  ```
  2575#BED-001#BED-002
  ```

### Filtro de IP (`@`)

Filtra las conexiones TCP entrantes por la direccion IP de origen. Las conexiones desde otras direcciones IP se rechazan en la etapa de aceptacion TCP. El filtro de IP solo funciona en modo servidor TCP y UDP.

```
2575@192.168.100.22
```

Esto escucha en el puerto 2575 y solo acepta conexiones desde `192.168.100.22`.

#### Coincidencia por Sufijo

Se admite la coincidencia por sufijo separado por puntos (`.`). No es necesario introducir la direccion IP completa; basta con especificar la parte final.

```
2575@.100.22
```

Esta configuracion permite conexiones desde todas las IPs con el formato `xxx.xxx.100.22`.

### Combinacion

```
2575#BED-001@192.168.100.22
```

Esto escucha en el puerto 2575, solo acepta conexiones desde `192.168.100.22` y solo procesa mensajes que contienen `BED-001`.

### Casos de Uso

- **BBraun DoseLink**: Cuando el Endpoint Filtering de DoseLink esta habilitado, use `#` para filtrar por numero de serie de la bomba o identificador de cama.
- **Mindray HL7 Gateway**: Multiples camas que comparten un unico puerto de gateway pueden separarse usando la palabra clave del nombre de cama.
- **Multiples servidores DoseLink**: Use `@` para distinguir que servidor DoseLink debe conectarse a que pestana de VitalRecorder.

### Enrutamiento Multicama para Pasarelas HL7

Cuando una unica pasarela HL7 (Mindray eGateway, BBraun DoseLink, Nihon Kohden HL7GW) envia datos de varias camas por una sola conexion TCP, VitalRecorder enruta automaticamente cada trama a la pestana correcta:

1. **Solo una pestana vincula** el puerto TCP (la pestana *primaria*); las demas pestanas que usan el mismo puerto y tipo de dispositivo pasan automaticamente a ser suscriptoras pasivas. Esto elimina la carrera de Windows `SO_REUSEADDR` que antes obligaba a hacer clic en "Add device" tras cada reinicio.

2. **Enrutamiento por nombre de cama (recomendado, tiene prioridad sobre el filtro por palabra clave)** — establezca el Nombre de Cama de cada pestana igual a **cualquier** identificador que envia la pasarela; no hace falta configurar ningun filtro de puerto:
   - **Mindray**: ID de cama de `PV1-3` (p. ej. `SU-1`, `BED-001`)
   - **Nihon Kohden**: campo JSON `deviceId` o prefijo MFER de 12 bytes
   - **BBraun**: **cualquier** token no vacio separado por `~` del OBX `MDC_ATTR_LOCATION` (p. ej. `Forskning`, `Bord4`, `Anilab`, `Operasjon`)

   Si varias pestanas pudieran coincidir con la misma trama (p. ej. existen tanto `Forskning` como `Bord4` y la LOCATION de la trama es `Forskning~Operasjon~Bord4~Anilab~~~~~Bord4`), **gana el token mas especifico**. Los tokens se comprueban en orden inverso, de modo que `Bord4` (el nombre corto al final de LOCATION) prevalece sobre `Forskning` (la etiqueta departamental al inicio). Cada trama se entrega a una sola pestana.

3. **Enrutamiento por palabra clave (alternativa)** — cuando el Nombre de Cama no puede coincidir directamente con el identificador de la pasarela, use la sintaxis `puerto#palabra_clave` descrita arriba. Solo se aplica si no hay coincidencia por nombre de cama.

4. **Creacion automatica de pestana** — si ninguna pestana coincide y la trama trae un identificador de cama, se crea una pestana nueva con el **token mas especifico** (el ultimo no vacio). Esto evita la perdida de paquetes durante la configuracion inicial.

5. **Recuperacion automatica tras reinicio** — al reiniciar VitalRecorder, todas las pestanas restablecen la relacion primario/suscriptor en unos 15 segundos sin intervencion manual.

En BBraun DoseLink una trama HL7 representa un rack (una cama); las multiples bombas del rack se envian como bloques VMD dentro de la trama y se registran en pistas separadas (PUMP1 ... PUMP16) de la misma pestana.

#### Modo de pantalla minima BBraun (1.18.29+)

Para reducir el desorden visual cuando hay varias bombas activas simultaneamente, anada `minimal=1` a la seccion del dispositivo BBraun en `vr.conf`. Solo se registran las tres pistas esenciales por bomba — `PUMP{N}_DRUG` (nombre del farmaco), `PUMP{N}_RATE` (velocidad de infusion, mL/h) y `PUMP{N}_VOL` (volumen infundido, mL); el resto de los campos (presion, concentracion, velocidad de dosis, jeringa, bolo, tiempo de infusion, peso del paciente, drug library, care area, etc.) se omiten de la visualizacion y del archivo grabado. Las pestanas de cama creadas automaticamente heredan esta configuracion de la pestana primaria.

```ini
[DEV/BBraun HL7]
type=BBraun : HL7
port=5000
minimal=1
```

Tanto BBraun HL7 (DoseLink) como BBraun SpaceCom (RS-232) soportan esta opcion.

> **Aviso 1.18.23 para Windows no ingles** — las versiones anteriores sufrian un problema del C runtime de Windows: en idiomas con `,` como separador decimal (noruego, aleman, frances, etc.) las velocidades de infusion menores que 1.0 mL/h se registraban como 0. Desde 1.18.23 el parseo numerico siempre usa `.` como separador decimal, independientemente de la configuracion regional de Windows. El limite de bombas BBraun por dispositivo se amplio de 8 a 16.

### Reenvio de Tramas

Cuando se recibe un mensaje que no coincide con el filtro de palabras clave, VitalRecorder lo reenvia automaticamente a otros dispositivos en otras pestanas que estan escuchando en el mismo puerto. Si no hay ninguna pestana coincidente y el mensaje contiene un identificador de cama (por ejemplo, un segmento PV1 de HL7), se crea automaticamente una nueva pestana con ese nombre de cama.

---

## Grabacion

### Grabacion Automatica

Por defecto, VitalRecorder inicia la grabacion automaticamente al ejecutarse (configuracion `RECORD_WHEN_START`).

### Formato de Archivo

Las grabaciones se guardan como archivos `.vital`, un formato binario comprimido con organizacion basada en pistas.

### Directorio de Guardado

Configure el directorio de guardado en la Configuracion. El valor predeterminado es la carpeta Documentos del usuario.

### Plantilla de Nombre de Archivo

El nombre de archivo se genera a partir de una plantilla. Valor predeterminado: `%r_%y%m%d_%h%i%s`

| Codigo | Significado |
|--------|-------------|
| `%r` | Nombre de sala/cama |
| `%y` | Ano (4 digitos) |
| `%m` | Mes (2 digitos) |
| `%d` | Dia (2 digitos) |
| `%h` | Hora (2 digitos) |
| `%i` | Minuto (2 digitos) |
| `%s` | Segundo (2 digitos) |

---

## Carga al Servidor

VitalRecorder puede cargar datos en tiempo real a una instancia de VitalServer a traves de WebSocket.

### Configuracion

| Configuracion | Descripcion |
|---------------|-------------|
| `SERVER_IP` | Direccion IP o nombre de host de VitalServer |
| `SEND_WEB` | Habilitar/deshabilitar la carga al servidor (`1` o `0`) |
| `CLOUD_UPLOAD` | Habilitar/deshabilitar la carga a la nube (`1` o `0`) |
| `VRCODE` | Identificador unico de esta instancia de VitalRecorder |

### Que se Carga

- **Version, SO, arquitectura** de la instancia de VitalRecorder.
- **Configuracion** y **lista de tipos de dispositivos compatibles** (se envian una sola vez en la primera carga exitosa despues del arranque).
- **Datos de sala**: nombre de cama, lista de dispositivos, valores de pistas y formas de onda de cada pestana.

Los datos se comprimen con zlib antes de la carga.

### Modo HL7

Cuando la configuracion `HL7` esta habilitada, VitalRecorder envia los datos de sala en formato HL7 en lugar de JSON.

---

## Archivo de Configuracion (vr.conf)

VitalRecorder almacena todas las configuraciones en un unico archivo de configuracion llamado `vr.conf`. Este archivo utiliza un formato similar a INI y puede editarse manualmente para implementaciones sin interfaz grafica o aprovisionamiento por lotes.

### Ubicacion del Archivo

| Plataforma | Ruta |
|------------|------|
| Windows | `%APPDATA%\VitalRecorder\vr.conf` |
| Linux | `./vr.conf` > `~/vr.conf` > `/boot/vr.conf` (se buscan en orden) |

- Codificacion: UTF-8
- Use `--conf <ruta>` para especificar un archivo de configuracion alternativo.

### Estructura del Archivo

```ini
# Configuracion global (antes de cualquier seccion)
KEY=VALUE

# Definicion de cama (pestana)
[BED/nombre_cama]

# Dispositivo bajo esta cama
[DEV/nombre_dispositivo]
type=TipoDispositivo
port=EspecPuerto

# Filtro bajo esta cama
[FILT/nombre_modulo_filtro]
```

**Reglas:**
- Un par `KEY=VALUE` por linea.
- Los encabezados de seccion comienzan con `[`.
- Las lineas en blanco se ignoran.
- Las secciones `[DEV/...]` y `[FILT/...]` pertenecen al `[BED/...]` anterior.
- Un unico `[BED/...]` puede contener multiples dispositivos y filtros.

### Configuracion Global

#### General

| Clave | Valor Predeterminado | Descripcion |
|-------|----------------------|-------------|
| `SAVEDIR` | (predeterminado del sistema) | Directorio de guardado de archivos de grabacion |
| `VRCODE` | (generado automaticamente) | Codigo de identificacion unico de VitalRecorder |
| `FILENAME_TEMPLATE` | `%r_%y%m%d_%h%i%s` | Plantilla de nombre de archivo de grabacion |

#### Grabacion

| Clave | Valor Predeterminado | Descripcion |
|-------|----------------------|-------------|
| `RECORD_WHEN_START` | 1 | Grabar automaticamente al iniciar (0: desactivado, 1: activado) |
| `CUT_FILE` | 1 | Dividir archivo en los limites de paciente (0: desactivado, 1: activado) |
| `CUT_HOURLY` | 0 | Dividir archivo cada hora (0: desactivado, 1: activado) |
| `CUT_BY` | (ninguno) | Senal de activacion para la division de archivo (por ejemplo, `spo2`, `hr`, `any`) |
| `PT_WAITING_TIME` | 5 | Tiempo de espera del paciente en minutos |

#### Servidor

| Clave | Valor Predeterminado | Descripcion |
|-------|----------------------|-------------|
| `SERVER_IP` | (ninguno) | Direccion del servidor VitalDB (IP:port) |
| `UPLOAD_SERVER_IP` | (ninguno) | Direccion del servidor de carga de archivos |
| `MONITOR_SERVER_IP` | (ninguno) | Direccion del servidor de monitoreo web |
| `SEND_WEB` | 1 | Enviar datos al servidor web (0: desactivado, 1: activado) |
| `CLOUD_UPLOAD` | 0 | Habilitar carga a la nube (0: desactivado, 1: activado) |

#### Ventana

| Clave | Valor Predeterminado | Descripcion |
|-------|----------------------|-------------|
| `START_MAXIMIZED` | 1 | Iniciar maximizado |
| `START_MINIMIZED` | 0 | Iniciar minimizado |
| `OPTION_MIN_TO_TRAY` | 0 | Minimizar a la bandeja del sistema |
| `OPTION_ALWAYS_ON_TOP` | 0 | Siempre visible encima |
| `PLAY_SOUND` | 1 | Reproducir sonidos de alarma |

#### Preajustes de Eventos

Se pueden definir hasta 30 etiquetas de preajustes de eventos con `EVT_TEXT_0` a `EVT_TEXT_29`.

```ini
EVT_TEXT_0=Induction
EVT_TEXT_1=Intubation
EVT_TEXT_2=Incision
```

### Seccion de Cama

Define una cama (pestana). Se pueden definir multiples camas en un unico archivo de configuracion.

```ini
[BED/OR1]
```

- El nombre de cama sigue a `BED/` (por ejemplo, `OR1`, `ICU_BED3`).
- Si se omite, el nombre de cama se genera automaticamente a partir de VRCODE o el nombre de host del PC.

### Seccion de Dispositivo

Los dispositivos se agregan bajo una seccion `[BED/...]`.

```ini
[DEV/nombre_dispositivo]
type=TipoDispositivo
port=EspecPuerto
```

| Clave | Obligatorio | Descripcion |
|-------|-------------|-------------|
| `type` | Si | Tipo de dispositivo (por ejemplo, `BIS`, `Intellivue`, `Solar8000`) |
| `port` | Si | Puerto de conexion (ver Formatos de Puerto a continuacion) |
| `company` | No | Fabricante (por ejemplo, `Nihon Kohden`) |
| `readonly` | No | Modo solo lectura (0: desactivado, 1: activado) |

#### Formatos de Puerto

| Formato | Ejemplo | Descripcion |
|---------|---------|-------------|
| COM port | `COM1`, `COM3` | Puerto serial de Windows |
| TCP/IP | `192.168.1.100:4343` | Dispositivo de red (IP:port) |
| Numero de puerto | `4343` | Modo servidor TCP en localhost |
| RPi serial | `F1`-`F4` | Puertos AMA de Raspberry Pi |
| RPi USB | `LU`, `LU1`-`LU4` | USB superior izquierdo |
| RPi USB | `RU`, `RU1`-`RU4` | USB superior derecho |

#### Filtrado de Puertos en la Configuracion

El valor del puerto admite filtros de palabra clave e IP (misma sintaxis descrita en [Filtrado de Puertos](#filtrado-de-puertos)):

```
port=PORT#keyword1 keyword2#keyword3@IP_SUFFIX
```

#### Configuracion de Dispositivos ADC

Para dispositivos ADC (Convertidor Analogico-Digital), estan disponibles configuraciones adicionales por canal:

| Clave | Descripcion |
|-------|-------------|
| `srate` | Frecuencia de muestreo en Hz |
| `parname1`, `parname2`, ... | Nombre del parametro para cada canal |
| `gain1`, `gain2`, ... | Ganancia de conversion de voltaje a unidad fisica para cada canal |

```ini
[DEV/SNUADC]
type=SNUADC
port=COM3
srate=500
parname1=ECG
gain1=1.0
parname2=ART
gain2=100.0
```

### Seccion de Filtro

Agrega un filtro de procesamiento de senales en tiempo real. Las definiciones de filtros se cargan desde el servidor de filtros.

```ini
[FILT/nombre_modulo_filtro]
```

- El nombre del modulo debe coincidir con el `modname` de un filtro registrado en el servidor.
- No se necesitan configuraciones adicionales (los parametros del filtro son proporcionados por el servidor).

### Ejemplos de Configuracion

#### Monitor de Paciente Unico

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1
```

#### Multiples Dispositivos

```ini
SAVEDIR=D:\VitalData
VRCODE=OR1_PC

[BED/OR1]

[DEV/Intellivue]
type=Intellivue
port=192.168.1.100:4343

[DEV/BIS]
type=BIS
port=COM3

[DEV/Primus]
type=Primus
port=COM4
```

#### Multiples Camas

```ini
SAVEDIR=D:\VitalData

[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[BED/OR2]

[DEV/Philips]
type=Intellivue
port=192.168.1.101:4343
```

#### Depuracion / Prueba

```ini
SAVEDIR=C:\Users\lucid\Desktop

[BED/test]

[DEV/NK EGA]
type=EGA
company=Nihon Kohden
port=9001
```

#### Con Filtro

```ini
[BED/OR1]

[DEV/Solar8000]
type=Solar8000
port=COM1

[FILT/pleth_spi]
```

---

## Opciones de Linea de Comandos

```
vital.exe [opciones] [nombre_archivo]
```

| Opcion | Descripcion |
|--------|-------------|
| `--version`, `-v` | Mostrar numero de version |
| `--devtypes`, `-d` | Listar todos los tipos de dispositivos compatibles |
| `--console`, `-c` | Ejecutar en modo consola (sin GUI) |
| `--debug [conf]` | Ejecutar en modo depuracion (incluye modo consola, archivo de configuracion opcional) |
| `--conf <ruta>` | Especificar la ruta del archivo de configuracion |
| `--upgrade`, `-u` | Actualizar a la ultima version |
| `-u1.18.0` | Actualizar a una version especifica |
| `--help`, `-h` | Mostrar ayuda |
| `nombre_archivo.vital` | Abrir un archivo `.vital` para reproduccion |

### Modo Consola

El modo consola (`--console` o `-c`) ejecuta VitalRecorder sin la GUI. Esto es util para implementaciones sin interfaz grafica en Raspberry Pi o servidores Ubuntu. Los dispositivos se cargan desde la configuracion guardada.

### Modo Depuracion

El modo depuracion (`--debug`) incluye el modo consola y muestra registros detallados en la salida estandar, incluyendo apertura/cierre de dispositivos, reenvio de tramas, etc. En modo depuracion no se generan archivos `.vital` reales.

```bash
# Ejecutar en modo depuracion con la configuracion predeterminada
vital.exe --debug

# Ejecutar en modo depuracion con un archivo de configuracion especifico
vital.exe --debug test_mindray.conf
```

---

## Dispositivos Compatibles

Para la lista completa de dispositivos compatibles con detalles de conexion y parametros, consulte [Supported Devices](../VitalRecorder/Supported_Devices.md).

### Referencia Rapida: Dispositivos Comunes

| Dispositivo | Conexion | Configuracion de Puerto |
|-------------|----------|------------------------|
| Philips Intellivue | RS-232 | COM port, 115200 baud |
| GE Solar 8000 | RS-232 | COM port, 9600 baud |
| Nihon Kohden (Serial) | RS-232 | COM port, 9600 baud |
| Nihon Kohden (HL7GW) | TCP Server | Port 9001 |
| Nihon Kohden (EGA) | UDP | Port number |
| Mindray (HL7) | TCP Server | Port 10000 |
| Draeger (Medibus) | RS-232 | COM port, 9600 baud (8N2) |
| GE Datex-Ohmeda | RS-232 | COM port, 19200 baud (7E1) |
| Medtronic BIS | RS-232 | COM port, 57600 baud |
| BBraun SpaceCom | RS-232 | COM port, 9600 baud |
| BBraun HL7 (DoseLink) | TCP Server | Port 2575 |
| Masimo Radical-7 | RS-232 | COM port, 9600 baud |
| Edwards Hemosphere | RS-232 | COM port, 9600 baud |
| Hamilton ventilator | RS-232 | COM port, 38400 baud |

---

## Solucion de Problemas

### El Dispositivo No Se Conecta

1. **RS-232**: Verifique que se ha seleccionado el COM port correcto. Compruebe el numero de puerto en el Administrador de Dispositivos. Asegurese de que el controlador USB-to-Serial esta instalado.
2. **Modo servidor TCP**: Compruebe que el firewall permite conexiones entrantes en el puerto especificado.
3. **Modo cliente TCP**: Verifique que la direccion IP del dispositivo es accesible (prueba con `ping`).

### No Se Muestran Datos

- Algunos dispositivos requieren una configuracion especifica en el lado del dispositivo (por ejemplo, habilitar la salida RS-232 en el menu de servicio de Draeger, activar la salida MIB en Philips Intellivue).
- Compruebe que la velocidad de transmision y los parametros seriales coinciden con la configuracion del dispositivo.
- Use el modo `--debug` para verificar la comunicacion.

### Multiples Dispositivos en el Mismo Puerto

Para dispositivos HL7 que comparten un unico puerto de gateway, use la funcion de [Filtrado de Puertos](#filtrado-de-puertos) con la palabra clave `#` para separar las camas.

### BBraun HL7 Multi-Bomba

BBraun DoseLink envia datos de multiples bombas a traves de una unica conexion TCP. VitalRecorder identifica automaticamente cada bomba usando el numero de serie en OBX-18 (Equipment Instance Identifier) y las asigna de PUMP1 a PUMP8.

Si las bombas no se separan correctamente:
- Use el modo `--debug` para verificar los registros.
- Compruebe los valores de OBX-18 en los mensajes HL7 sin procesar.
- Cuando utilice DoseLink Endpoint Filtering, use el filtro de palabra clave `#` si es necesario.

### La Carga al Servidor No Funciona

- Verifique que `SERVER_IP` esta configurado correctamente.
- Compruebe que `SEND_WEB` esta establecido en `1`.
- Asegurese de la conectividad de red con el servidor.
- La configuracion y la lista de tipos de dispositivos se envian en la primera carga exitosa despues del arranque. Si VitalRecorder se inicia sin dispositivos activos, la carga inicial puede retrasarse hasta que un dispositivo se conecte.
