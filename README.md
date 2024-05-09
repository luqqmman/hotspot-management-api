# Capstone Internet Hotspot Management with POS | ML API

### Instalasi di linux
      
      python -m venv venv
      source venv/bin/activate
      pip install -r requirements.txt
      

### Instalasi di windows

      python -m venv venv
      source venv/bin/Activate.ps1
      pip install -r requirements.txt


### Generate Model
      python model.py

### Run API
      uvicorn main:app --host 0.0.0.0 --reload
