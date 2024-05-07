from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigSetting(BaseSettings):
    model_config = SettingsConfigDict(env_file=".config.env", env_file_encoding="utf-8")

    HOST: str = Field(default="0.0.0.0")
    JSON_LOGS: bool = Field(default=False)
    LOG_LEVEL: str = Field(default="DEBUG")
    PORT: int = Field(default=8000)
    RELOAD: bool = Field(default=True)
    WORKERS: int = Field(default=1)


class EnvironmentSetting(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # KEY: str = Field(default="")


setting_cfg = ConfigSetting()
setting_env = EnvironmentSetting()
