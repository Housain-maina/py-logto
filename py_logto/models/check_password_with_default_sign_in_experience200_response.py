# coding: utf-8

"""
    Python SDK for Logto API

    Python SDK for Logto API.  Note: This SDK is for Logto Cloud and OSS. However, if you are using Logto OSS, some features available in the SDK may not work for you. Please refer to the response of `/api/swagger.json` endpoint on your Logto OSS instance for features available to you.

    The version of the OpenAPI document: 1.22.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from py_logto.models.check_password_with_default_sign_in_experience200_response_one_of import CheckPasswordWithDefaultSignInExperience200ResponseOneOf
from py_logto.models.check_password_with_default_sign_in_experience200_response_one_of1 import CheckPasswordWithDefaultSignInExperience200ResponseOneOf1
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CHECKPASSWORDWITHDEFAULTSIGNINEXPERIENCE200RESPONSE_ONE_OF_SCHEMAS = ["CheckPasswordWithDefaultSignInExperience200ResponseOneOf", "CheckPasswordWithDefaultSignInExperience200ResponseOneOf1"]

class CheckPasswordWithDefaultSignInExperience200Response(BaseModel):
    """
    CheckPasswordWithDefaultSignInExperience200Response
    """
    # data type: CheckPasswordWithDefaultSignInExperience200ResponseOneOf
    oneof_schema_1_validator: Optional[CheckPasswordWithDefaultSignInExperience200ResponseOneOf] = None
    # data type: CheckPasswordWithDefaultSignInExperience200ResponseOneOf1
    oneof_schema_2_validator: Optional[CheckPasswordWithDefaultSignInExperience200ResponseOneOf1] = None
    actual_instance: Optional[Union[CheckPasswordWithDefaultSignInExperience200ResponseOneOf, CheckPasswordWithDefaultSignInExperience200ResponseOneOf1]] = None
    one_of_schemas: Set[str] = { "CheckPasswordWithDefaultSignInExperience200ResponseOneOf", "CheckPasswordWithDefaultSignInExperience200ResponseOneOf1" }

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
        instance = CheckPasswordWithDefaultSignInExperience200Response.model_construct()
        error_messages = []
        match = 0
        # validate data type: CheckPasswordWithDefaultSignInExperience200ResponseOneOf
        if not isinstance(v, CheckPasswordWithDefaultSignInExperience200ResponseOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CheckPasswordWithDefaultSignInExperience200ResponseOneOf`")
        else:
            match += 1
        # validate data type: CheckPasswordWithDefaultSignInExperience200ResponseOneOf1
        if not isinstance(v, CheckPasswordWithDefaultSignInExperience200ResponseOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CheckPasswordWithDefaultSignInExperience200ResponseOneOf1`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CheckPasswordWithDefaultSignInExperience200Response with oneOf schemas: CheckPasswordWithDefaultSignInExperience200ResponseOneOf, CheckPasswordWithDefaultSignInExperience200ResponseOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CheckPasswordWithDefaultSignInExperience200Response with oneOf schemas: CheckPasswordWithDefaultSignInExperience200ResponseOneOf, CheckPasswordWithDefaultSignInExperience200ResponseOneOf1. Details: " + ", ".join(error_messages))
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

        # deserialize data into CheckPasswordWithDefaultSignInExperience200ResponseOneOf
        try:
            instance.actual_instance = CheckPasswordWithDefaultSignInExperience200ResponseOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CheckPasswordWithDefaultSignInExperience200ResponseOneOf1
        try:
            instance.actual_instance = CheckPasswordWithDefaultSignInExperience200ResponseOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CheckPasswordWithDefaultSignInExperience200Response with oneOf schemas: CheckPasswordWithDefaultSignInExperience200ResponseOneOf, CheckPasswordWithDefaultSignInExperience200ResponseOneOf1. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CheckPasswordWithDefaultSignInExperience200Response with oneOf schemas: CheckPasswordWithDefaultSignInExperience200ResponseOneOf, CheckPasswordWithDefaultSignInExperience200ResponseOneOf1. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], CheckPasswordWithDefaultSignInExperience200ResponseOneOf, CheckPasswordWithDefaultSignInExperience200ResponseOneOf1]]:
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


