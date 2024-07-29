# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "26039668")

API_HASH = os.environ.get("API_HASH", "7379fbfb3d101a5075e37d64cbcebc0a")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7131153106:AAGQ_SywBdU2JEpy68mJp-sf3Ek1eD4niEA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Arvindeditorbot") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "ArvindN/A")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://Arvind:fr7r8fkfjfu@cluster0.w3lstd2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2079478016').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
