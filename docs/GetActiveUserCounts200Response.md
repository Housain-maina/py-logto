# GetActiveUserCounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dau_curve** | [**List[GetActiveUserCounts200ResponseDauCurveInner]**](GetActiveUserCounts200ResponseDauCurveInner.md) |  | 
**dau** | [**GetNewUserCounts200ResponseToday**](GetNewUserCounts200ResponseToday.md) |  | 
**wau** | [**GetNewUserCounts200ResponseToday**](GetNewUserCounts200ResponseToday.md) |  | 
**mau** | [**GetNewUserCounts200ResponseToday**](GetNewUserCounts200ResponseToday.md) |  | 

## Example

```python
from py_logto.models.get_active_user_counts200_response import GetActiveUserCounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetActiveUserCounts200Response from a JSON string
get_active_user_counts200_response_instance = GetActiveUserCounts200Response.from_json(json)
# print the JSON string representation of the object
print(GetActiveUserCounts200Response.to_json())

# convert the object into a dict
get_active_user_counts200_response_dict = get_active_user_counts200_response_instance.to_dict()
# create an instance of GetActiveUserCounts200Response from a dict
get_active_user_counts200_response_from_dict = GetActiveUserCounts200Response.from_dict(get_active_user_counts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


