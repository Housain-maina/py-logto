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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from py_logto.models.get_sign_in_exp200_response_password_policy_character_types import GetSignInExp200ResponsePasswordPolicyCharacterTypes
from py_logto.models.get_sign_in_exp200_response_password_policy_length import GetSignInExp200ResponsePasswordPolicyLength
from py_logto.models.get_sign_in_exp200_response_password_policy_rejects import GetSignInExp200ResponsePasswordPolicyRejects
from typing import Optional, Set
from typing_extensions import Self

class GetSignInExp200ResponsePasswordPolicy(BaseModel):
    """
    Password policies to adjust the password strength requirements.
    """ # noqa: E501
    length: Optional[GetSignInExp200ResponsePasswordPolicyLength] = None
    character_types: Optional[GetSignInExp200ResponsePasswordPolicyCharacterTypes] = Field(default=None, alias="characterTypes")
    rejects: Optional[GetSignInExp200ResponsePasswordPolicyRejects] = None
    __properties: ClassVar[List[str]] = ["length", "characterTypes", "rejects"]

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
        """Create an instance of GetSignInExp200ResponsePasswordPolicy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of length
        if self.length:
            _dict['length'] = self.length.to_dict()
        # override the default output from pydantic by calling `to_dict()` of character_types
        if self.character_types:
            _dict['characterTypes'] = self.character_types.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rejects
        if self.rejects:
            _dict['rejects'] = self.rejects.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetSignInExp200ResponsePasswordPolicy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "length": GetSignInExp200ResponsePasswordPolicyLength.from_dict(obj["length"]) if obj.get("length") is not None else None,
            "characterTypes": GetSignInExp200ResponsePasswordPolicyCharacterTypes.from_dict(obj["characterTypes"]) if obj.get("characterTypes") is not None else None,
            "rejects": GetSignInExp200ResponsePasswordPolicyRejects.from_dict(obj["rejects"]) if obj.get("rejects") is not None else None
        })
        return _obj


