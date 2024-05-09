# Capstone Internet Hotspot Management with POS | ML API

### Instalasi
      
      python -m venv venv
      # linux
      source venv/bin/activate
      # cmd
      .\venv\Scripts\activate.bat
      # powershell
      .\venv\Scripts\Activate.ps1
      pip install -r requirements.txt


### Generate Model
      python model.py


### Run API
      uvicorn main:app --host 0.0.0.0 --reload
