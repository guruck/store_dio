from datetime import datetime
from decimal import Decimal
from typing import Any

from bson import Decimal128
from pydantic import BaseModel, Field, model_serializer, ConfigDict


class CreateBaseModel(BaseModel):
    model_config = ConfigDict(extra="allow")

    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    @model_serializer
    def serialize_model(self) -> dict[str, Any]:
        self_dict = dict(self)

        for key, value in self_dict.items():
            if isinstance(value, Decimal):
                self_dict[key] = Decimal128(str(value))

        return self_dict
