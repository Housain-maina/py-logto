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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_logto.models.list_applications200_response_inner_custom_client_metadata import ListApplications200ResponseInnerCustomClientMetadata
from py_logto.models.list_applications200_response_inner_oidc_client_metadata import ListApplications200ResponseInnerOidcClientMetadata
from py_logto.models.update_application_request_protected_app_metadata import UpdateApplicationRequestProtectedAppMetadata
from typing import Optional, Set
from typing_extensions import Self

class UpdateApplicationRequest(BaseModel):
    """
    UpdateApplicationRequest
    """ # noqa: E501
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=256)]] = None
    description: Optional[StrictStr] = None
    oidc_client_metadata: Optional[ListApplications200ResponseInnerOidcClientMetadata] = Field(default=None, alias="oidcClientMetadata")
    custom_client_metadata: Optional[ListApplications200ResponseInnerCustomClientMetadata] = Field(default=None, alias="customClientMetadata")
    custom_data: Optional[Dict[str, Any]] = Field(default=None, description="arbitrary", alias="customData")
    protected_app_metadata: Optional[UpdateApplicationRequestProtectedAppMetadata] = Field(default=None, alias="protectedAppMetadata")
    is_admin: Optional[StrictBool] = Field(default=None, description="Whether the application has admin access. User can enable the admin access for Machine-to-Machine apps.", alias="isAdmin")
    __properties: ClassVar[List[str]] = ["name", "description", "oidcClientMetadata", "customClientMetadata", "customData", "protectedAppMetadata", "isAdmin"]

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
        """Create an instance of UpdateApplicationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of oidc_client_metadata
        if self.oidc_client_metadata:
            _dict['oidcClientMetadata'] = self.oidc_client_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of custom_client_metadata
        if self.custom_client_metadata:
            _dict['customClientMetadata'] = self.custom_client_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of protected_app_metadata
        if self.protected_app_metadata:
            _dict['protectedAppMetadata'] = self.protected_app_metadata.to_dict()
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UpdateApplicationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "description": obj.get("description"),
            "oidcClientMetadata": ListApplications200ResponseInnerOidcClientMetadata.from_dict(obj["oidcClientMetadata"]) if obj.get("oidcClientMetadata") is not None else None,
            "customClientMetadata": ListApplications200ResponseInnerCustomClientMetadata.from_dict(obj["customClientMetadata"]) if obj.get("customClientMetadata") is not None else None,
            "customData": obj.get("customData"),
            "protectedAppMetadata": UpdateApplicationRequestProtectedAppMetadata.from_dict(obj["protectedAppMetadata"]) if obj.get("protectedAppMetadata") is not None else None,
            "isAdmin": obj.get("isAdmin")
        })
        return _obj


