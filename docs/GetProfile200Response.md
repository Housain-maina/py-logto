# GetProfile200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**primary_email** | **str** |  | [optional] 
**primary_phone** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**avatar** | **str** |  | [optional] 
**custom_data** | **object** | arbitrary | [optional] 
**identities** | [**Dict[str, GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue]**](GetJwtCustomizer200ResponseOneOfContextSampleUserIdentitiesValue.md) |  | [optional] 
**last_sign_in_at** | **float** |  | [optional] 
**created_at** | **float** |  | [optional] 
**updated_at** | **float** |  | [optional] 
**profile** | [**GetJwtCustomizer200ResponseOneOfContextSampleUserProfile**](GetJwtCustomizer200ResponseOneOfContextSampleUserProfile.md) |  | [optional] 
**application_id** | **str** |  | [optional] 
**is_suspended** | **bool** |  | [optional] 
**has_password** | **bool** |  | [optional] 
**sso_identities** | [**List[GetUser200ResponseSsoIdentitiesInner]**](GetUser200ResponseSsoIdentitiesInner.md) |  | [optional] 

## Example

```python
from py_logto.models.get_profile200_response import GetProfile200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProfile200Response from a JSON string
get_profile200_response_instance = GetProfile200Response.from_json(json)
# print the JSON string representation of the object
print(GetProfile200Response.to_json())

# convert the object into a dict
get_profile200_response_dict = get_profile200_response_instance.to_dict()
# create an instance of GetProfile200Response from a dict
get_profile200_response_from_dict = GetProfile200Response.from_dict(get_profile200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


