#!/bin/bash

FROM=$1
PASSWORD=$2
TOMAIL=$3


sed -i 's/u.u.u.u/'$FROM'/g' mailsender.py
sed -i 's/p.p.p.p/'$PASSWORD'/g' mailsender.py
sed -i "s/t.t.t.t/$TOMAIL/g" mailsender.py
chmod +x mailsender.py
/usr/bin/python mailsender.py

