# app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings configuration class for the application.
    This class uses pydantic's BaseSettings for environment management.
    It defines various configuration settings required for the application.
    """

    # Application Core Settings
    APP_NAME: str = "TrAIvel Mate!"
    APP_VERSION: str = "1.0.0"
    API_PREFIX: str = "/api"

    # Database Connection Settings
    # Replace the default SQLite URL with the specific database URL as needed
    DATABASE_URL: str = "sqlite:///./test.db"

    # Qdrant Server Settings
    # Qdrant is used for vector search, replace with actual server details
    QDRANT_HOST: str = "localhost"
    QDRANT_PORT: int = 6333
    QDRANT_COLLECTION: str = "traivel"

    # External API Keys
    # Keys for various external services like hotels, weather, flights, attractions
    HOTEL_API_KEY: str = ""
    WEATHER_API_KEY: str = "weather API key"
    FLIGHTS_API_KEY: str = ""
    ATTRACTIONS_API_KEY: str = "opentripmap API key"
    RAPIDAPI_KEY: str = "rapid API key"

    # Security Settings
    # OpenAI API key for accessing OpenAI services
    OPENAI_API_KEY: str = "openAI API key"

    class Config:
        """
        Configuration class for environment management.
        Specifies the .env file location and its encoding.
        """
        env_file = ".env"
        env_file_encoding = 'utf-8'

# Create an instance of the Settings class
settings = Settings()
