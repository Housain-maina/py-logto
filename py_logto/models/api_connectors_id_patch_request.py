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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from py_logto.models.api_connectors_id_patch_request_metadata import ApiConnectorsIdPatchRequestMetadata
from typing import Optional, Set
from typing_extensions import Self

class ApiConnectorsIdPatchRequest(BaseModel):
    """
    ApiConnectorsIdPatchRequest
    """ # noqa: E501
    config: Optional[Dict[str, Any]] = Field(default=None, description="The connector config object that will be passed to the connector. The config object should be compatible with the connector factory.")
    metadata: Optional[ApiConnectorsIdPatchRequestMetadata] = None
    sync_profile: Optional[StrictBool] = Field(default=None, description="Whether to sync user profile from the identity provider to Logto at each sign-in. If `false`, the user profile will only be synced when the user is created.", alias="syncProfile")
    __properties: ClassVar[List[str]] = ["config", "metadata", "syncProfile"]

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
        """Create an instance of ApiConnectorsIdPatchRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiConnectorsIdPatchRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": obj.get("config"),
            "metadata": ApiConnectorsIdPatchRequestMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "syncProfile": obj.get("syncProfile")
        })
        return _obj


