# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "18424928"))
    API_HASH = getenv("API_HASH", "d12e98533ee6d6222e63dac56c504913")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    FSUB = getenv("FSUB", "Ellisa_movies_hub")
    CHID = int(getenv("CHID", "-1001786658222"))
    SUDO = list(map(int, getenv("SUDO", "1017302540").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Ellisa1:Ellisa1@ellisa1.3wsw2lx.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
