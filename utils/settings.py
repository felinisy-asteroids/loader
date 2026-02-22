from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_ID: str = "cloud-project-workflow"
    BUCKET_NAME: str = "asteroids-etl"
    TABLE_ID: str = "cloud-project-workflow.etl_workflow.asteroids"


settings = Settings()