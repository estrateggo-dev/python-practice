# Python Practice

Repositorio personal para practicar Python mediante ejercicios organizados por bloques y lecciones.

El objetivo principal es aprender Python escribiendo código real, manteniendo una estructura clara y usando herramientas básicas de desarrollo como `uv`, `ruff`, `black` y Git.

## 1. Objetivos del proyecto

- Practicar Python de forma progresiva.
- Resolver cada ejercicio en un archivo `.py` independiente.
- Mantener el proyecto ordenado por bloques y lecciones.
- Usar un entorno virtual gestionado con `uv`.
- Aplicar formato automático con `black`.
- Revisar el código con `ruff`.
- Mantener historial del aprendizaje con Git.

## 2. Estructura del proyecto

```text
python-practice/
├── exercises/
│   └── bloque_01_fundamentos/
│       └── leccion_01_print_input/
│           └── ejercicio_01_saludo.py
│
├── playground/
│   └── pruebas.py
│
├── .vscode/
│   ├── settings.json
│   └── python-exercises.code-snippets
│
├── .gitignore
├── README.md
├── pyproject.toml
├── uv.lock
└── .python-version
```

## 3. Carpetas principales

### `exercises/`

Contiene los ejercicios organizados por bloques y lecciones.

Regla principal:

```text
1 ejercicio = 1 archivo .py
```

Ejemplo:

```text
exercises/
└── bloque_01_fundamentos/
    └── leccion_01_print_input/
        ├── ejercicio_01_saludo.py
        └── ejercicio_02_datos_usuario.py
```

### `playground/`

Carpeta para pruebas rápidas, experimentos y código temporal.

Sirve para probar ideas sin ensuciar los ejercicios finales de `exercises/`.

Ejemplos de uso:

- probar cómo funciona `input()`;
- hacer pruebas con strings, listas o diccionarios;
- comprobar pequeños fragmentos de código;
- experimentar antes de pasar una solución limpia a `exercises/`.

Ejemplo:

```text
playground/
├── pruebas.py
├── pruebas_strings.py
└── pruebas_listas.py
```

### `.vscode/`

Contiene configuración específica del proyecto para VS Code.

Incluye:

```text
.vscode/settings.json
.vscode/python-exercises.code-snippets
```

El archivo de snippets permite crear rápidamente una plantilla base para cada ejercicio.

## 4. Entorno virtual

El proyecto usa `uv` para gestionar el entorno virtual y las dependencias.

El entorno virtual está en:

```text
.venv/
```

Esta carpeta no se sube a GitHub.

## 5. Archivos de configuración de `uv`

### `pyproject.toml`

El archivo `pyproject.toml` define la configuración principal del proyecto Python.

En este proyecto se usa para declarar:

- el nombre del proyecto;
- la versión;
- la versión mínima de Python;
- las dependencias normales;
- las dependencias de desarrollo.

Ejemplo de dependencia de desarrollo:

```toml
[dependency-groups]
dev = [
    "black",
    "ruff",
]
```

Este archivo responde a la pregunta:

```text
¿Qué necesita el proyecto?
```

### `uv.lock`

El archivo `uv.lock` guarda las versiones exactas de todos los paquetes resueltos por `uv`.

Incluye:

- dependencias directas;
- dependencias indirectas;
- versiones exactas;
- metadatos necesarios para reproducir el entorno.

Ejemplo:

```text
black == 26.5.1
ruff == 0.15.19
click == 8.4.2
```

Este archivo responde a la pregunta:

```text
¿Qué versiones exactas se están usando?
```

### Diferencia rápida

| Archivo        | Función                                   |
|----------------|-------------------------------------------|
| `pyproject.toml` | Declara qué paquetes necesita el proyecto |
| `uv.lock`        | Fija las versiones exactas instaladas     |
| `.venv/`         | Contiene el entorno virtual local         |

`pyproject.toml` y `uv.lock` sí deben subirse a GitHub.

La carpeta `.venv/` no debe subirse, porque se puede reconstruir ejecutando:

```bash
uv sync
```

## 6. Versión de Python

Actualmente el proyecto usa:

```text
Python 3.13.7
```

Se puede comprobar con:

```bash
uv run python --version
```

O, si el entorno virtual está activo:

```bash
python --version
```

## 7. Dependencias instaladas

Dependencias directas de desarrollo:

```text
black
ruff
```

Estas dependencias están declaradas en `pyproject.toml`.

## 8. Dependencias indirectas actuales

Al instalar `black` y `ruff`, también se instalan algunas dependencias necesarias para que funcionen:

```text
black
click
colorama
mypy-extensions
packaging
pathspec
platformdirs
pytokens
ruff
```

Se pueden consultar con:

```bash
uv pip list
```

## 9. Diferencia entre dependencias normales y de desarrollo

Las dependencias normales son necesarias para que el programa funcione.

Ejemplo:

```bash
uv add requests
```

Las dependencias de desarrollo solo se usan mientras se programa, prueba, revisa o formatea el código.

Ejemplo:

```bash
uv add --dev ruff black
```

En este proyecto, `ruff` y `black` son dependencias de desarrollo.

## 10. Comandos básicos del proyecto

### Ver versión de Python

```bash
uv run python --version
```

### Ver el ejecutable de Python usado

```bash
uv run python -c "import sys; print(sys.executable)"
```

Debe apuntar a algo similar a:

```text
D:\python-practice\.venv\Scripts\python.exe
```

### Ver paquetes instalados

```bash
uv pip list
```

### Ver árbol de dependencias

```bash
uv tree
```

### Ver paquetes desactualizados

```bash
uv tree --outdated
```

O de forma más resumida:

```bash
uv tree --outdated --depth=1
```

### Ejecutar Ruff

Revisar todo el proyecto:

```bash
uv run ruff check .
```

Revisar un archivo concreto:

```bash
uv run ruff check exercises/bloque_01_fundamentos/leccion_01_print_input/ejercicio_01_saludo.py
```

### Ejecutar Black

Formatear todo el proyecto:

```bash
uv run black .
```

Formatear un archivo concreto:

```bash
uv run black exercises/bloque_01_fundamentos/leccion_01_print_input/ejercicio_01_saludo.py
```

### Ejecutar un ejercicio

Ejemplo:

```bash
uv run python exercises/bloque_01_fundamentos/leccion_01_print_input/ejercicio_01_saludo.py
```

Si el entorno virtual está activo, también se puede ejecutar así:

```bash
python exercises/bloque_01_fundamentos/leccion_01_print_input/ejercicio_01_saludo.py
```

## 11. Activar el entorno virtual manualmente

No es obligatorio si se usa `uv run`.

En Git Bash:

```bash
source .venv/Scripts/activate
```

En PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Cuando el entorno esté activo, la terminal mostrará algo parecido a:

```text
(python-practice)
```

## 12. Actualizar dependencias

### Ver primero qué paquetes están desactualizados

```bash
uv tree --outdated --depth=1
```

### Actualizar todas las dependencias

```bash
uv lock --upgrade
uv sync
```

### Actualizar una dependencia concreta

Ejemplo con `ruff`:

```bash
uv add --dev ruff --upgrade-package ruff
```

Ejemplo con `black`:

```bash
uv add --dev black --upgrade-package black
```

## 13. Snippets de ejercicios

El proyecto incluye snippets locales en:

```text
.vscode/python-exercises.code-snippets
```

Estos snippets solo están disponibles dentro de este proyecto.

### Snippet largo

Escribir en un archivo `.py`:

```text
ejercicio
```

Después pulsar `Tab` o seleccionar la sugerencia.

Genera una plantilla como esta:

```python
"""
Ejercicio XX - Título del ejercicio

Enunciado:
Describe aquí el enunciado del ejercicio.

Conceptos practicados:
- Concepto 1
- Concepto 2
- Concepto 3

Notas:
Añade aquí notas, errores detectados o aclaraciones.
"""

# Solución
```

### Snippet corto

Escribir:

```text
ejcorto
```

Genera una versión más simple para ejercicios pequeños.

## 14. Convención para ejercicios

Cada archivo debe seguir esta estructura general:

```python
"""
Ejercicio XX - Título del ejercicio

Enunciado:
...

Conceptos practicados:
- ...
- ...
- ...

Notas:
...
"""

# Solución
```

Ejemplo:

```python
"""
Ejercicio 01 - Saludo personalizado

Enunciado:
Pide al usuario su nombre y muestra un saludo personalizado.

Conceptos practicados:
- print()
- input()
- variables
- f-strings

Notas:
input() siempre devuelve texto.
"""

# Solución

nombre = input("Introduce tu nombre: ")
print(f"Hola, {nombre}")
```

## 15. Flujo de trabajo recomendado

1. Crear un archivo `.py` por ejercicio.
2. Insertar la plantilla con el snippet `ejercicio` o `ejcorto`.
3. Escribir el enunciado.
4. Resolver el ejercicio.
5. Ejecutar el archivo.
6. Revisar con `ruff`.
7. Formatear con `black`.
8. Hacer commit con Git.

## 16. Comandos de Git habituales

Ver estado del repo:

```bash
git status
```

Añadir cambios:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Añade ejercicios de print e input"
```

Ver historial:

```bash
git log --oneline
```

## 17. Archivos que no se suben al repo

El archivo `.gitignore` excluye:

```text
.venv/
__pycache__/
*.pyc
.pytest_cache/
.ruff_cache/
.mypy_cache/
.env
.env.*
```

El archivo `uv.lock` sí debe subirse al repo.

## 18. Estado actual del proyecto

- Proyecto inicializado con `uv`.
- Entorno virtual creado en `.venv/`.
- Python funcionando desde el entorno virtual.
- Ruff instalado como dependencia de desarrollo.
- Black instalado como dependencia de desarrollo.
- Snippets locales configurados para ejercicios.
- Configuración local de VS Code preparada.

## 19. Próximos pasos

- Crear el primer ejercicio en `exercises/bloque_01_fundamentos/leccion_01_print_input/`.
- Probar el snippet `ejercicio`.
- Ejecutar el archivo con `uv run python`.
- Revisar con `ruff`.
- Formatear con `black`.
- Hacer el primer commit.