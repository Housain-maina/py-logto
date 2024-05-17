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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ApiInteractionBindMfaPostRequestOneOf1Response(BaseModel):
    """
    ApiInteractionBindMfaPostRequestOneOf1Response
    """ # noqa: E501
    client_data_json: StrictStr = Field(alias="clientDataJSON")
    attestation_object: StrictStr = Field(alias="attestationObject")
    authenticator_data: Optional[StrictStr] = Field(default=None, alias="authenticatorData")
    transports: Optional[List[StrictStr]] = None
    public_key_algorithm: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="publicKeyAlgorithm")
    public_key: Optional[StrictStr] = Field(default=None, alias="publicKey")
    __properties: ClassVar[List[str]] = ["clientDataJSON", "attestationObject", "authenticatorData", "transports", "publicKeyAlgorithm", "publicKey"]

    @field_validator('transports')
    def transports_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['usb', 'nfc', 'ble', 'internal', 'cable', 'hybrid', 'smart-card']):
                raise ValueError("each list item must be one of ('usb', 'nfc', 'ble', 'internal', 'cable', 'hybrid', 'smart-card')")
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
        """Create an instance of ApiInteractionBindMfaPostRequestOneOf1Response from a JSON string"""
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
        """Create an instance of ApiInteractionBindMfaPostRequestOneOf1Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clientDataJSON": obj.get("clientDataJSON"),
            "attestationObject": obj.get("attestationObject"),
            "authenticatorData": obj.get("authenticatorData"),
            "transports": obj.get("transports"),
            "publicKeyAlgorithm": obj.get("publicKeyAlgorithm"),
            "publicKey": obj.get("publicKey")
        })
        return _obj

