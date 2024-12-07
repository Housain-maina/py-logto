# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetAccountCenterSettings200ResponseFields(BaseModel):
    """
    GetAccountCenterSettings200ResponseFields
    """ # noqa: E501
    name: Optional[StrictStr] = None
    avatar: Optional[StrictStr] = None
    profile: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    password: Optional[StrictStr] = None
    username: Optional[StrictStr] = None
    social: Optional[StrictStr] = None
    custom_data: Optional[StrictStr] = Field(default=None, alias="customData")
    __properties: ClassVar[List[str]] = ["name", "avatar", "profile", "email", "phone", "password", "username", "social", "customData"]

    @field_validator('name')
    def name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('avatar')
    def avatar_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('profile')
    def profile_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('email')
    def email_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('phone')
    def phone_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('password')
    def password_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('username')
    def username_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('social')
    def social_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
        return value

    @field_validator('custom_data')
    def custom_data_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Off', 'ReadOnly', 'Edit']):
            raise ValueError("must be one of enum values ('Off', 'ReadOnly', 'Edit')")
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
        """Create an instance of GetAccountCenterSettings200ResponseFields from a JSON string"""
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
        """Create an instance of GetAccountCenterSettings200ResponseFields from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "avatar": obj.get("avatar"),
            "profile": obj.get("profile"),
            "email": obj.get("email"),
            "phone": obj.get("phone"),
            "password": obj.get("password"),
            "username": obj.get("username"),
            "social": obj.get("social"),
            "customData": obj.get("customData")
        })
        return _obj

