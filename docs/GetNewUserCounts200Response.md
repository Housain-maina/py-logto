# GetNewUserCounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**today** | [**GetNewUserCounts200ResponseToday**](GetNewUserCounts200ResponseToday.md) |  | 
**last7_days** | [**GetNewUserCounts200ResponseToday**](GetNewUserCounts200ResponseToday.md) |  | 

## Example

```python
from py_logto.models.get_new_user_counts200_response import GetNewUserCounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNewUserCounts200Response from a JSON string
get_new_user_counts200_response_instance = GetNewUserCounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetNewUserCounts200Response.to_json())

# convert the object into a dict
get_new_user_counts200_response_dict = get_new_user_counts200_response_instance.to_dict()
# create an instance of GetNewUserCounts200Response from a dict
get_new_user_counts200_response_from_dict = GetNewUserCounts200Response.from_dict(get_new_user_counts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


