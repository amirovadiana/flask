from pydantic import BaseModel, field_validator, ValidationError
from errors import HttpError


class BaseAdvertRequest(BaseModel):
    title: str
    description: str
    author: str

    @field_validator('title')
    @classmethod
    def secure_title(cls, value: str):
        if len(value) > 150:
            raise ValueError('Title is too long')
        return value
    
    @field_validator('description')
    @classmethod
    def secure_description(cls, value: str):
        if len(value) > 500:
            raise ValueError('Description is too long')
        return value


class CreateAdvertRequest(BaseAdvertRequest):
    pass


class UpdateAdvertRequest(BaseAdvertRequest):
    title: str | None = None
    description: str | None = None
    author: str | None = None


def validate(
        schema: type[CreateAdvertRequest | UpdateAdvertRequest],
        json_data: dict
) -> dict:
    try:
        schema_instance = schema(**json_data)
        return schema_instance.model_dump(exclude_unset=True)
    except ValidationError as error:
        errors = error.errors()
        for error in errors:
            error.pop('ctx', None)
        raise HttpError(400, errors)
