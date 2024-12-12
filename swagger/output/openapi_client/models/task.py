# coding: utf-8

"""
    Task Management API

    API cho việc quản lý các nhiệm vụ trong ngày

    The version of the OpenAPI document: 1.0.0
    Contact: anhtoan07112002@gmail.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Task(BaseModel):
    """
    Task
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID của nhiệm vụ")
    tittle: StrictStr = Field(description="Tiêu đề của nhiệm vụ")
    description: StrictStr = Field(description="Mô tả chi tiết của nhiệm vụ")
    status: StrictStr = Field(description="Trạng thái của nhiệm vụ (PENDING, IN_PROGRESS, COMPLETED, OVERDUE)")
    start_time: datetime = Field(description="Thời gian bắt đầu nhiệm vụ")
    end_time: datetime = Field(description="Thời gian kết thúc nhiệm vụ")
    __properties: ClassVar[List[str]] = ["id", "tittle", "description", "status", "start_time", "end_time"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['PENDING', 'IN_PROGRESS', 'COMPLETED', 'OVERDUE']):
            raise ValueError("must be one of enum values ('PENDING', 'IN_PROGRESS', 'COMPLETED', 'OVERDUE')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Task from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Task from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "tittle": obj.get("tittle"),
            "description": obj.get("description"),
            "status": obj.get("status"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time")
        })
        return _obj

