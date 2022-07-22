from .secrets import get_secrets

class Config:
    db_name: str
    host: str
    port: str
    user: str
    password: str
    
    def __init__(self):
        config_info = get_secrets()
        self.db_name = config_info.get('DB_NAME')
        self.host = config_info.get('DB_HOST')
        self.port = config_info.get('DB_PORT')
        self.user = config_info.get('DB_USER')
        self.password = config_info.get('DB_PASSWORD'),
        
    def get_uri(self) -> str:
        return f'postgresql://{self.user}@{self.host}:{self.port}/{self.db_name}'
