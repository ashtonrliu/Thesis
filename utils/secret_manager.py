import os
from dotenv import load_dotenv


class Secret_Manager:
    
    def __init__(self):
        parent_env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
        loaded = load_dotenv(dotenv_path=parent_env_path) # Loads ENV file
        # print(os.getenv("APCA-API-KEY-ID"))
    
