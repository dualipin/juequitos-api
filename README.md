# Proceso de Intalacion del la API de la tabla periodica

- **Paso 1**: tener instalado python

- **Paso 2**: crear un entorno virtual con el comando

```bash
python -m venv .venv
```

- **paso 3**: activar el entorno virtual

```bash
./.venv/Scripts/activate
```

- **paso 4**: instalar las dependencias

```bash
pip install -r ./requirements.txt
```

- **realizar las migraciones**

> si no existen las migraciones, inicializarla

```bash
flask db init
```

> crear las migraciones

```bash
flask db migrate -m "Inicializar la base de datos"
```

```bash
flask db upgrade
```

- **paso 5**: ejecutar la aplicacion API

```bash
python ./run.py
```
