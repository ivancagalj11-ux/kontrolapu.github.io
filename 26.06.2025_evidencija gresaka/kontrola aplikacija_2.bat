@echo off
echo Pokrecem Python server...

:: 1. Odi u folder gdje je tvoja aplikacija
cd "C:\Users\Public\26.06.2025_evidencija gresaka"

:: 2. Pokreni Python aplikaciju (server) u novom prozoru
:: Komanda 'start' omogucava da se skripta nastavi izvrsavati
start "Moj Python Server" python app.py

echo Cekam 10 sekundi da se server podigne...
:: Ovo daje serveru malo vremena da se pokrene prije otvaranja browsera
timeout /t 12 >nul

echo Otvaram aplikaciju u pregledniku...
:: 3. Otvori adresu u zadanom pregledniku
start http://127.0.0.1:5000

exit