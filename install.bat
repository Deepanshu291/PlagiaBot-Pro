@echo Installation Starting....
timeout /t 3 /nobreak

@echo Creating Virtual Environment...
timeout /t 2
python -m venv env

@echo Install Dependencies...
timeout /t 2
call \env\Scripts\activate.bat
pip install -r requirements.txt

@echo Installation Complete!
timeout /t 2

exit
