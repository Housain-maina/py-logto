# GetHasuraAuth200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_hasura_user_id** | **str** |  | [optional] 
**x_hasura_role** | **str** |  | [optional] 

## Example

```python
from py_logto.models.get_hasura_auth200_response import GetHasuraAuth200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetHasuraAuth200Response from a JSON string
get_hasura_auth200_response_instance = GetHasuraAuth200Response.from_json(json)
# print the JSON string representation of the object
print(GetHasuraAuth200Response.to_json())

# convert the object into a dict
get_hasura_auth200_response_dict = get_hasura_auth200_response_instance.to_dict()
# create an instance of GetHasuraAuth200Response from a dict
get_hasura_auth200_response_from_dict = GetHasuraAuth200Response.from_dict(get_hasura_auth200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


