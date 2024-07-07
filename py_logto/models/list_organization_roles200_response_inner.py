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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from py_logto.models.list_application_organizations200_response_inner_organization_roles_inner import ListApplicationOrganizations200ResponseInnerOrganizationRolesInner
from py_logto.models.list_organization_roles200_response_inner_resource_scopes_inner import ListOrganizationRoles200ResponseInnerResourceScopesInner
from typing import Optional, Set
from typing_extensions import Self

class ListOrganizationRoles200ResponseInner(BaseModel):
    """
    ListOrganizationRoles200ResponseInner
    """ # noqa: E501
    tenant_id: Annotated[str, Field(strict=True, max_length=21)] = Field(alias="tenantId")
    id: Annotated[str, Field(min_length=1, strict=True, max_length=21)]
    name: Annotated[str, Field(min_length=1, strict=True, max_length=128)]
    description: Optional[Annotated[str, Field(strict=True, max_length=256)]]
    type: StrictStr
    scopes: List[ListApplicationOrganizations200ResponseInnerOrganizationRolesInner]
    resource_scopes: List[ListOrganizationRoles200ResponseInnerResourceScopesInner] = Field(alias="resourceScopes")
    __properties: ClassVar[List[str]] = ["tenantId", "id", "name", "description", "type", "scopes", "resourceScopes"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['User', 'MachineToMachine']):
            raise ValueError("must be one of enum values ('User', 'MachineToMachine')")
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
        """Create an instance of ListOrganizationRoles200ResponseInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in scopes (list)
        _items = []
        if self.scopes:
            for _item in self.scopes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scopes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in resource_scopes (list)
        _items = []
        if self.resource_scopes:
            for _item in self.resource_scopes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['resourceScopes'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ListOrganizationRoles200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenantId": obj.get("tenantId"),
            "id": obj.get("id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "type": obj.get("type"),
            "scopes": [ListApplicationOrganizations200ResponseInnerOrganizationRolesInner.from_dict(_item) for _item in obj["scopes"]] if obj.get("scopes") is not None else None,
            "resourceScopes": [ListOrganizationRoles200ResponseInnerResourceScopesInner.from_dict(_item) for _item in obj["resourceScopes"]] if obj.get("resourceScopes") is not None else None
        })
        return _obj


