# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from py_logto.models.api_interaction_put_request_identifier import ApiInteractionPutRequestIdentifier
from py_logto.models.api_interaction_put_request_profile import ApiInteractionPutRequestProfile
from typing import Optional, Set
from typing_extensions import Self

class ApiInteractionPutRequest(BaseModel):
    """
    ApiInteractionPutRequest
    """ # noqa: E501
    event: StrictStr
    identifier: Optional[ApiInteractionPutRequestIdentifier] = None
    profile: Optional[ApiInteractionPutRequestProfile] = None
    __properties: ClassVar[List[str]] = ["event", "identifier", "profile"]

    @field_validator('event')
    def event_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['SignIn', 'Register', 'ForgotPassword']):
            raise ValueError("must be one of enum values ('SignIn', 'Register', 'ForgotPassword')")
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
        """Create an instance of ApiInteractionPutRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identifier
        if self.identifier:
            _dict['identifier'] = self.identifier.to_dict()
        # override the default output from pydantic by calling `to_dict()` of profile
        if self.profile:
            _dict['profile'] = self.profile.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiInteractionPutRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "event": obj.get("event"),
            "identifier": ApiInteractionPutRequestIdentifier.from_dict(obj["identifier"]) if obj.get("identifier") is not None else None,
            "profile": ApiInteractionPutRequestProfile.from_dict(obj["profile"]) if obj.get("profile") is not None else None
        })
        return _obj

