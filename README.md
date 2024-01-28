# Тестовое задание


# Задание 1

При запуске скрипта из dentalia.py получаем на выходе dentalia.json такого формата

```json
{
    "name": "Encuentro Oceanía",
    "address": "Av. del Peñón 355, Moctezuma 2da Secc, Venustiano Carranza, 15530 Ciudad de México, CDMX",
    "location": "https://www.google.com.mx/maps/place/dentalia+Encuentro+Oceania/@19.4391319,-99.1032383,15z/data=!4m15!1m8!3m7!1s0x85d1fcbfbeb136d9:0xb5ea259848fbedb8!2sdentalia+Encuentro+Oceania!8m2!3d19.4391319!4d-99.0944836!10e5!16s%2Fg%2F1tqg0p8q!3m5!1s0x85d1fcbfbeb136d9:0xb5ea259848fbedb8!8m2!3d19.4391319!4d-99.0944836!16s%2Fg%2F1tqg0p8q?entry=ttu",
    "phone": [
      "(55) 5766-9999",
      "(55) 1164-9418"
    ],
    "working_hours": [
      "Jue a Mar 11am a 8pm",
      "Mie 11am a  5pm"
    ]
  },
```

При запуске dentalia_location.py происходит извлечение данных для поля *location*.

```json
{
    "name": "Encuentro Oceanía",
    "address": "Av. del Peñón 355, Moctezuma 2da Secc, Venustiano Carranza, 15530 Ciudad de México, CDMX",
    "location": [
      "19.4391319",
      "-99.0944836"
    ],
    "phone": [
      "(55) 5766-9999",
      "(55) 1164-9418"
    ],
    "working_hours": [
      "Jue a Mar 11am a 8pm",
      "Mie 11am a  5pm"
    ]
  },
```

# Задание 2

Запускаем файл yapdomik.py и получаем yapdomik.json.

```json
{
    "name": "Японский Домик",
    "address": "Омск, ул. Бульвар Архитекторов, 14/3",
    "location": [
      "54.98987397187852",
      "73.30583935581973"
    ],
    "phones": [
      "+7(962)058-70-97"
    ],
    "working_hours": [
      "Пн - Вс 10:50 — 23:10"
    ]
  },
```

# Задание 3

При запуске santaelena.py получаем santaelena.py.

```json
{
    "name": "Centro Comercial Mayorca Etapa 1",
    "address": "Medellín, Calle 51 Sur # 48 – 57 Local 324",
    "location": "https://www.google.com/maps/d/edit?mid=1PjEJHvVyruJdbvV9JxP1czJJfVtWjko&usp=sharing",
    "phone": "3256600 ext 4906",
    "working_hours": [
      "Lunes a sábado: 9:00 a.m. – 8:00 p.m.",
      "Domingos: 11:30 a.m. – 7:30 p.m"
    ]
  },
```

Извлечь геоданные таким же способом "в лоб", как и для dentalia не получилось. 
Но насчёт этого есть идея:
- 1) Перейти по ссылке и попасть на кастомную карту.
![Alt text](images/image.png)
- 2) Далее, найти и кликнуть на нужное заведение. Например Punto De Venta Mayorca 1![Alt text](images/image-1.png)
- 3) Карта зумиться на нужный нам объект ![Alt text](images/image-2.png)
- 4) И в url поле браузера отображается нажные нам геоданные (в правой части скриншота после "*ll=*") ![Alt text](images/image-3.png)
- 5) Отсаётся их извлечь url-адрес из url поля браузера. Затем с помощью регулярки его достать и обрезать.