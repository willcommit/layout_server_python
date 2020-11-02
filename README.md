## INSTALL, START AND UPDATE

**DEPLOY** 
Only for developers

Windows exe deploy with no console  
pyinstaller --onefile --windowed --name LayoutSaver app.py

Windows exe deploy with console  
pyinstaller --onefile -name LayoutSaver app.py

Generate DB with db_model.py

## INSTALL 
Add deployed .exe file, app_config.json and generated db file to a folder. Zip it and distribute.  
Generate shortcut and add to run shell:startup  

## UPDATE 
Replace only exe file in folder location.  

## API ROUTES

**GET**

Get all layouts  
api/layout

Get layout name by id  
api/layout/{id}

Get all screens by layout id  
api/layout/{id}/screen

Get screen on specific layout  
api/layout/{id}/screen/{id}

Get all decoders by layout id  
api/layout/{id}/decoder

Get decoder on specific layout  
api/layout/{id}/decoder/{id}

Get layout amount
api/layout/amount

**POST**

Create or update layout with a name
api/layout

Create or update screen 
api/layout/{id}/screen/{id}

Create or update decoder 
api/layout/{id}/decoder/{id}

Post layout amount
api/layout/amount

**DELETE**

Delete layout
api/layout/{id}  

Delete screen
api/layout/{id}/screen/{id}  

Delete decoder
api/layout/{id}/decoder/{id}  