# coding: utf-8

"""
    Logto API references

    API references for Logto services.

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetSignInExperienceConfig200ResponseGoogleOneTap(BaseModel):
    """
    GetSignInExperienceConfig200ResponseGoogleOneTap
    """ # noqa: E501
    is_enabled: Optional[StrictBool] = Field(default=None, alias="isEnabled")
    auto_select: Optional[StrictBool] = Field(default=None, alias="autoSelect")
    close_on_tap_outside: Optional[StrictBool] = Field(default=None, alias="closeOnTapOutside")
    itp_support: Optional[StrictBool] = Field(default=None, alias="itpSupport")
    client_id: StrictStr = Field(alias="clientId")
    connector_id: StrictStr = Field(alias="connectorId")
    __properties: ClassVar[List[str]] = ["isEnabled", "autoSelect", "closeOnTapOutside", "itpSupport", "clientId", "connectorId"]

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
        """Create an instance of GetSignInExperienceConfig200ResponseGoogleOneTap from a JSON string"""
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
        """Create an instance of GetSignInExperienceConfig200ResponseGoogleOneTap from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isEnabled": obj.get("isEnabled"),
            "autoSelect": obj.get("autoSelect"),
            "closeOnTapOutside": obj.get("closeOnTapOutside"),
            "itpSupport": obj.get("itpSupport"),
            "clientId": obj.get("clientId"),
            "connectorId": obj.get("connectorId")
        })
        return _obj

