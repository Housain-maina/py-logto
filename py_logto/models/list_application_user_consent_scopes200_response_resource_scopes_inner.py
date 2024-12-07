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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from py_logto.models.list_application_user_consent_scopes200_response_resource_scopes_inner_resource import ListApplicationUserConsentScopes200ResponseResourceScopesInnerResource
from py_logto.models.list_application_user_consent_scopes200_response_resource_scopes_inner_scopes_inner import ListApplicationUserConsentScopes200ResponseResourceScopesInnerScopesInner
from typing import Optional, Set
from typing_extensions import Self

class ListApplicationUserConsentScopes200ResponseResourceScopesInner(BaseModel):
    """
    ListApplicationUserConsentScopes200ResponseResourceScopesInner
    """ # noqa: E501
    resource: ListApplicationUserConsentScopes200ResponseResourceScopesInnerResource
    scopes: List[ListApplicationUserConsentScopes200ResponseResourceScopesInnerScopesInner]
    __properties: ClassVar[List[str]] = ["resource", "scopes"]

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
        """Create an instance of ListApplicationUserConsentScopes200ResponseResourceScopesInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of resource
        if self.resource:
            _dict['resource'] = self.resource.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in scopes (list)
        _items = []
        if self.scopes:
            for _item_scopes in self.scopes:
                if _item_scopes:
                    _items.append(_item_scopes.to_dict())
            _dict['scopes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListApplicationUserConsentScopes200ResponseResourceScopesInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resource": ListApplicationUserConsentScopes200ResponseResourceScopesInnerResource.from_dict(obj["resource"]) if obj.get("resource") is not None else None,
            "scopes": [ListApplicationUserConsentScopes200ResponseResourceScopesInnerScopesInner.from_dict(_item) for _item in obj["scopes"]] if obj.get("scopes") is not None else None
        })
        return _obj


