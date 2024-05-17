# coding: utf-8

"""
    Logto API references

    API references for Logto services. To learn more about how to interact with Logto APIs, see [Interact with Management API](https://docs.logto.io/docs/recipes/interact-with-management-api/).

    The version of the OpenAPI document: Cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from py_logto.models.api_users_user_id_mfa_verifications_post200_response_one_of import ApiUsersUserIdMfaVerificationsPost200ResponseOneOf
from py_logto.models.api_users_user_id_mfa_verifications_post200_response_one_of1 import ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

APIUSERSUSERIDMFAVERIFICATIONSPOST200RESPONSE_ONE_OF_SCHEMAS = ["ApiUsersUserIdMfaVerificationsPost200ResponseOneOf", "ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1"]

class ApiUsersUserIdMfaVerificationsPost200Response(BaseModel):
    """
    ApiUsersUserIdMfaVerificationsPost200Response
    """
    # data type: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf
    oneof_schema_1_validator: Optional[ApiUsersUserIdMfaVerificationsPost200ResponseOneOf] = None
    # data type: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1
    oneof_schema_2_validator: Optional[ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1] = None
    actual_instance: Optional[Union[ApiUsersUserIdMfaVerificationsPost200ResponseOneOf, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1]] = None
    one_of_schemas: Set[str] = { "ApiUsersUserIdMfaVerificationsPost200ResponseOneOf", "ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = ApiUsersUserIdMfaVerificationsPost200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf
        if not isinstance(v, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiUsersUserIdMfaVerificationsPost200ResponseOneOf`")
        else:
            match += 1
        # validate data type: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1
        if not isinstance(v, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in ApiUsersUserIdMfaVerificationsPost200Response with oneOf schemas: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in ApiUsersUserIdMfaVerificationsPost200Response with oneOf schemas: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ApiUsersUserIdMfaVerificationsPost200ResponseOneOf
        try:
            instance.actual_instance = ApiUsersUserIdMfaVerificationsPost200ResponseOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1
        try:
            instance.actual_instance = ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ApiUsersUserIdMfaVerificationsPost200Response with oneOf schemas: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ApiUsersUserIdMfaVerificationsPost200Response with oneOf schemas: ApiUsersUserIdMfaVerificationsPost200ResponseOneOf, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ApiUsersUserIdMfaVerificationsPost200ResponseOneOf, ApiUsersUserIdMfaVerificationsPost200ResponseOneOf1]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


