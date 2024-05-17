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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from py_logto.models.api_configs_jwt_customizer_token_type_path_get200_response_one_of_context_sample_user_roles_inner_scopes_inner_resource import ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
from typing import Optional, Set
from typing_extensions import Self

class ApiRolesIdScopesGet200ResponseInner(BaseModel):
    """
    ApiRolesIdScopesGet200ResponseInner
    """ # noqa: E501
    id: Annotated[str, Field(min_length=1, strict=True, max_length=21)]
    resource_id: Annotated[str, Field(min_length=1, strict=True, max_length=21)] = Field(alias="resourceId")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=256)]
    description: Optional[StrictStr]
    created_at: Union[StrictFloat, StrictInt] = Field(alias="createdAt")
    resource: ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource
    __properties: ClassVar[List[str]] = ["id", "resourceId", "name", "description", "createdAt", "resource"]

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
        """Create an instance of ApiRolesIdScopesGet200ResponseInner from a JSON string"""
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
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiRolesIdScopesGet200ResponseInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "resourceId": obj.get("resourceId"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "createdAt": obj.get("createdAt"),
            "resource": ApiConfigsJwtCustomizerTokenTypePathGet200ResponseOneOfContextSampleUserRolesInnerScopesInnerResource.from_dict(obj["resource"]) if obj.get("resource") is not None else None
        })
        return _obj


