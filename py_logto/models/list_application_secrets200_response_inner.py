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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class ListApplicationSecrets200ResponseInner(BaseModel):
    """
    ListApplicationSecrets200ResponseInner
    """ # noqa: E501
    tenant_id: Annotated[str, Field(strict=True, max_length=21)] = Field(alias="tenantId")
    application_id: Annotated[str, Field(min_length=1, strict=True, max_length=21)] = Field(alias="applicationId")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=256)]
    value: Annotated[str, Field(min_length=1, strict=True, max_length=64)]
    created_at: Union[StrictFloat, StrictInt] = Field(alias="createdAt")
    expires_at: Optional[Union[StrictFloat, StrictInt]] = Field(alias="expiresAt")
    __properties: ClassVar[List[str]] = ["tenantId", "applicationId", "name", "value", "createdAt", "expiresAt"]

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
        """Create an instance of ListApplicationSecrets200ResponseInner from a JSON string"""
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
        # set to None if expires_at (nullable) is None
        # and model_fields_set contains the field
        if self.expires_at is None and "expires_at" in self.model_fields_set:
            _dict['expiresAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListApplicationSecrets200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "applicationId": obj.get("applicationId"),
            "name": obj.get("name"),
            "value": obj.get("value"),
            "createdAt": obj.get("createdAt"),
            "expiresAt": obj.get("expiresAt")
        })
        return _obj

