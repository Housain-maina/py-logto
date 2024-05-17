# ApiInteractionConsentPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_ids** | **List[str]** |  | [optional] 

## Example

```python
from py_logto.models.api_interaction_consent_post_request import ApiInteractionConsentPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiInteractionConsentPostRequest from a JSON string
api_interaction_consent_post_request_instance = ApiInteractionConsentPostRequest.from_json(json)
# print the JSON string representation of the object
print(ApiInteractionConsentPostRequest.to_json())

# convert the object into a dict
api_interaction_consent_post_request_dict = api_interaction_consent_post_request_instance.to_dict()
# create an instance of ApiInteractionConsentPostRequest from a dict
api_interaction_consent_post_request_from_dict = ApiInteractionConsentPostRequest.from_dict(api_interaction_consent_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


