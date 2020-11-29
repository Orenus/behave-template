#!/bin/bash

python3 -m pip install -r requirements.txt

echo " "
echo " === CALIDAD DE SOFTWARE: DEVOPS / PRUEBAS AUTOMATIZADAS ==="
echo " "

exec behave 