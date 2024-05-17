# ApiAuthnHasuraGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_hasura_user_id** | **str** |  | [optional] 
**x_hasura_role** | **str** |  | [optional] 

## Example

```python
from py_logto.models.api_authn_hasura_get200_response import ApiAuthnHasuraGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiAuthnHasuraGet200Response from a JSON string
api_authn_hasura_get200_response_instance = ApiAuthnHasuraGet200Response.from_json(json)
# print the JSON string representation of the object
print(ApiAuthnHasuraGet200Response.to_json())

# convert the object into a dict
api_authn_hasura_get200_response_dict = api_authn_hasura_get200_response_instance.to_dict()
# create an instance of ApiAuthnHasuraGet200Response from a dict
api_authn_hasura_get200_response_from_dict = ApiAuthnHasuraGet200Response.from_dict(api_authn_hasura_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


