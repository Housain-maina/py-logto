# UpdateSignInExpRequestUnknownSessionRedirectUrl

The fallback URL to redirect users when the sign-in session does not exist or unknown. Client should initiate a new authentication flow after the redirection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from py_logto.models.update_sign_in_exp_request_unknown_session_redirect_url import UpdateSignInExpRequestUnknownSessionRedirectUrl

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSignInExpRequestUnknownSessionRedirectUrl from a JSON string
update_sign_in_exp_request_unknown_session_redirect_url_instance = UpdateSignInExpRequestUnknownSessionRedirectUrl.from_json(json)
# print the JSON string representation of the object
print(UpdateSignInExpRequestUnknownSessionRedirectUrl.to_json())

# convert the object into a dict
update_sign_in_exp_request_unknown_session_redirect_url_dict = update_sign_in_exp_request_unknown_session_redirect_url_instance.to_dict()
# create an instance of UpdateSignInExpRequestUnknownSessionRedirectUrl from a dict
update_sign_in_exp_request_unknown_session_redirect_url_from_dict = UpdateSignInExpRequestUnknownSessionRedirectUrl.from_dict(update_sign_in_exp_request_unknown_session_redirect_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


