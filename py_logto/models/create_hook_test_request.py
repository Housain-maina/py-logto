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
from py_logto.models.create_hook_test_request_config import CreateHookTestRequestConfig
from typing import Optional, Set
from typing_extensions import Self

class CreateHookTestRequest(BaseModel):
    """
    CreateHookTestRequest
    """ # noqa: E501
    events: List[StrictStr] = Field(description="An array of hook events for testing.")
    config: CreateHookTestRequestConfig
    event: Optional[Any] = Field(default=None, description="Use `events` instead.")
    __properties: ClassVar[List[str]] = ["events", "config", "event"]

    @field_validator('events')
    def events_validate_enum(cls, value):
        """Validates the enum"""
        for i in value:
            if i not in set(['PostRegister', 'PostSignIn', 'PostResetPassword', 'User.Created', 'User.Deleted', 'User.Data.Updated', 'User.SuspensionStatus.Updated', 'Role.Created', 'Role.Deleted', 'Role.Data.Updated', 'Role.Scopes.Updated', 'Scope.Created', 'Scope.Deleted', 'Scope.Data.Updated', 'Organization.Created', 'Organization.Deleted', 'Organization.Data.Updated', 'Organization.Membership.Updated', 'OrganizationRole.Created', 'OrganizationRole.Deleted', 'OrganizationRole.Data.Updated', 'OrganizationRole.Scopes.Updated', 'OrganizationScope.Created', 'OrganizationScope.Deleted', 'OrganizationScope.Data.Updated']):
                raise ValueError("each list item must be one of ('PostRegister', 'PostSignIn', 'PostResetPassword', 'User.Created', 'User.Deleted', 'User.Data.Updated', 'User.SuspensionStatus.Updated', 'Role.Created', 'Role.Deleted', 'Role.Data.Updated', 'Role.Scopes.Updated', 'Scope.Created', 'Scope.Deleted', 'Scope.Data.Updated', 'Organization.Created', 'Organization.Deleted', 'Organization.Data.Updated', 'Organization.Membership.Updated', 'OrganizationRole.Created', 'OrganizationRole.Deleted', 'OrganizationRole.Data.Updated', 'OrganizationRole.Scopes.Updated', 'OrganizationScope.Created', 'OrganizationScope.Deleted', 'OrganizationScope.Data.Updated')")
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
        """Create an instance of CreateHookTestRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of config
        if self.config:
            _dict['config'] = self.config.to_dict()
        # set to None if event (nullable) is None
        # and model_fields_set contains the field
        if self.event is None and "event" in self.model_fields_set:
            _dict['event'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateHookTestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "events": obj.get("events"),
            "config": CreateHookTestRequestConfig.from_dict(obj["config"]) if obj.get("config") is not None else None,
            "event": obj.get("event")
        })
        return _obj

