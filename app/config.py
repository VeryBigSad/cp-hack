from typing import Union

from pydantic import BaseModel


class MetaConfigsModel(BaseModel):
    IS_PROD: Union[bool] = True


class PostgresDataBaseConfigsModel(BaseModel):
    POSTGRES_DB_USERNAME: Union[str]
    POSTGRES_DB_PASSWORD: Union[str]
    POSTGRES_DB_HOST: Union[str]
    POSTGRES_DB_PORT: Union[int]
    POSTGRES_DB_NAME: Union[str]


class S3ConfigsModel(BaseModel):
    S3_BUCKET_NAME: Union[str]
    S3_ACCESS_KEY: Union[str]
    S3_SECRET_KEY: Union[str]
    S3_ENDPOINT: Union[str]


class ConfigsValidator(
    PostgresDataBaseConfigsModel,
    MetaConfigsModel,
    S3ConfigsModel,
):
    pass
