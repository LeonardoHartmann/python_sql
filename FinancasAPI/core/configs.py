from pydantic import BaseSettings

class Settings(BaseSettings):
    # Configuracoes basicas da API
    API_V1_STR: str = '/api/v1'
    DB_HOST: str = '127.0.0.1'
    DB_USER: str = 'root'
    DB_PASS: str = 'password'
    DB_NAME: str = 'pgi_financasapp'


settings = Settings()
