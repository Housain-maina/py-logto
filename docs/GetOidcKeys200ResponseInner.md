# GetOidcKeys200ResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**created_at** | **float** |  | 
**signing_key_algorithm** | **str** |  | [optional] 

## Example

```python
from py_logto.models.get_oidc_keys200_response_inner import GetOidcKeys200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetOidcKeys200ResponseInner from a JSON string
get_oidc_keys200_response_inner_instance = GetOidcKeys200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(GetOidcKeys200ResponseInner.to_json())

# convert the object into a dict
get_oidc_keys200_response_inner_dict = get_oidc_keys200_response_inner_instance.to_dict()
# create an instance of GetOidcKeys200ResponseInner from a dict
get_oidc_keys200_response_inner_from_dict = GetOidcKeys200ResponseInner.from_dict(get_oidc_keys200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


