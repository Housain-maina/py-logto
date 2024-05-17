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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_logto.models.api_sso_connectors_get200_response_inner_branding import ApiSsoConnectorsGet200ResponseInnerBranding
from typing import Optional, Set
from typing_extensions import Self

class ApiSsoConnectorsIdPatchRequest(BaseModel):
    """
    ApiSsoConnectorsIdPatchRequest
    """ # noqa: E501
    config: Optional[Dict[str, Any]] = Field(default=None, description="arbitrary")
    domains: Optional[List[StrictStr]] = None
    branding: Optional[ApiSsoConnectorsGet200ResponseInnerBranding] = None
    sync_profile: Optional[StrictBool] = Field(default=None, alias="syncProfile")
    connector_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=128)]] = Field(default=None, alias="connectorName")
    __properties: ClassVar[List[str]] = ["config", "domains", "branding", "syncProfile", "connectorName"]

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
        """Create an instance of ApiSsoConnectorsIdPatchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of branding
        if self.branding:
            _dict['branding'] = self.branding.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiSsoConnectorsIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": obj.get("config"),
            "domains": obj.get("domains"),
            "branding": ApiSsoConnectorsGet200ResponseInnerBranding.from_dict(obj["branding"]) if obj.get("branding") is not None else None,
            "syncProfile": obj.get("syncProfile"),
            "connectorName": obj.get("connectorName")
        })
        return _obj


