# uv package manager



```bash

$ mkdir DIR & cd DIR
$ uv init
$ mkdir project_name & cd project_name

# add package 
$ uv add 

# call file
$ python3 project_name/file.py

# 
$ uv tree

# create .venv
$ uv sync


# refresh dep-s
# Устанавливает все пакеты, которые перечислены в uv.lock в соответствии с зафиксированными версиями
$ uv sync --upgrade

# обновление всех установленных в проекте пакетов
$ uv sync -U


# delete dep-s
$ uv remove PACKGAGE-NAME

# dev lib add 
$ uv add --dev pytest


# Вот теперь зависимости из dev-dependencies устанавливаться не будут
uv sync --no-dev

```

## uv.lock

Фиксирует версии транзитивных зависимостей, так как обновление большого числа зависимых друг от друга библиотек может привести к неработоспособности всего проекта

##  Обновление зависимостей

Устанавливает все пакеты, которые перечислены в uv.lock в соответствии с зафиксированными версиями

```bash
$ uv sync --upgrade

# обновление всех установленных в проекте пакетов
$ uv sync -U

```

```bash
# execute script:
$ uv run python3 script.py

```

### Install specific version of python

```bash

# создает проект с указанной версией
uv init --python=3.13

# устанавливает проект с указанной версией
uv sync --python=3.13

# создает лишь окружение с указанной версией
uv venv  --python=3.13

# запускает команду с указанной версией
uv run --python=3.13 <команда>


```

## Установка не python инструментов 


```bash

$ uv tool install pydf


$ uv tool uninstall 

$ uv tool run <утилита>
# or
$ uvx <утилита>

```

Если библиотека импортируется в коде, то тогда 

```
$ uv add package
```


Если утилита только запускается (например, линтер), то достаточно ее использовать как tool: 
```bash
$ uv tool unstall utulity-name
$ uv tool run utility-name
```


 


