# Masterproef-Code

## Init

* `python -m venv .venv`  
* `.\.venv\Scripts\activate`  
* `.venv` aangemaakt  
* IBM Quantum account is toegevoegd aan `.venv`. Eerste keer wordt dit gefixt door het script: `handigeScripts/saveIBMQuantumAccount.py`  
* Wordt automatisch opgehaald met: `service = QiskitRuntimeService()`  
* `pip install -r requirements.txt`  

## TetraVex

3x3 raster  
Op elke zijde van een stuk een nummer van 0 tot 9  

### `TetraVex_Generator.py`

Genereert random spelen die oplosbaar zijn voor een gegeven rastergrootte  
Puzzelstukken worden neergeschreven in een `.txt` bestand met op elke lijn een puzzelstuk waarvan de zijdes beschreven staan van noord, oost, zuid, west  

### `TetraVex_Visualiser.py`

Geeft een visuele representatie van een TetraVex `.txt`-bestand
Maakt het gemakkelijker om te controleren of de gegeven oplossing correct is  

## DWave

### API-token
