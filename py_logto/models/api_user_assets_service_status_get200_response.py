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
from py_logto.models.api_user_assets_service_status_get200_response_status import ApiUserAssetsServiceStatusGet200ResponseStatus
from typing import Optional, Set
from typing_extensions import Self

class ApiUserAssetsServiceStatusGet200Response(BaseModel):
    """
    ApiUserAssetsServiceStatusGet200Response
    """ # noqa: E501
    status: ApiUserAssetsServiceStatusGet200ResponseStatus
    allow_upload_mime_types: Optional[List[StrictStr]] = Field(default=None, alias="allowUploadMimeTypes")
    max_upload_file_size: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxUploadFileSize")
    __properties: ClassVar[List[str]] = ["status", "allowUploadMimeTypes", "maxUploadFileSize"]

    @field_validator('allow_upload_mime_types')
    def allow_upload_mime_types_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['image/jpeg', 'image/png', 'image/gif', 'image/vnd.microsoft.icon', 'image/x-icon', 'image/svg+xml', 'image/tiff', 'image/webp', 'image/bmp']):
                raise ValueError("each list item must be one of ('image/jpeg', 'image/png', 'image/gif', 'image/vnd.microsoft.icon', 'image/x-icon', 'image/svg+xml', 'image/tiff', 'image/webp', 'image/bmp')")
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
        """Create an instance of ApiUserAssetsServiceStatusGet200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of status
        if self.status:
            _dict['status'] = self.status.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiUserAssetsServiceStatusGet200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": ApiUserAssetsServiceStatusGet200ResponseStatus.from_dict(obj["status"]) if obj.get("status") is not None else None,
            "allowUploadMimeTypes": obj.get("allowUploadMimeTypes"),
            "maxUploadFileSize": obj.get("maxUploadFileSize")
        })
        return _obj


