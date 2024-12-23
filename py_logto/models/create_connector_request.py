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

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_logto.models.create_connector_request_metadata import CreateConnectorRequestMetadata
from typing import Optional, Set
from typing_extensions import Self

class CreateConnectorRequest(BaseModel):
    """
    CreateConnectorRequest
    """ # noqa: E501
    config: Optional[Dict[str, Any]] = Field(default=None, description="The connector config object that will be passed to the connector. The config object should be compatible with the connector factory.")
    connector_id: Annotated[str, Field(min_length=1, strict=True, max_length=128)] = Field(description="The connector factory ID for creating the connector.", alias="connectorId")
    metadata: Optional[CreateConnectorRequestMetadata] = None
    sync_profile: Optional[StrictBool] = Field(default=None, description="Whether to sync user profile from the identity provider to Logto at each sign-in. If `false`, the user profile will only be synced when the user is created.", alias="syncProfile")
    id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=128)]] = Field(default=None, description="The unique ID for the connector. If not provided, a random ID will be generated.")
    __properties: ClassVar[List[str]] = ["config", "connectorId", "metadata", "syncProfile", "id"]

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
        """Create an instance of CreateConnectorRequest from a JSON string"""
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
        """Create an instance of CreateConnectorRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config": obj.get("config"),
            "connectorId": obj.get("connectorId"),
            "metadata": CreateConnectorRequestMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "syncProfile": obj.get("syncProfile"),
            "id": obj.get("id")
        })
        return _obj


