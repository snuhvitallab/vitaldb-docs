# Introduction

VitalDB APIs use the OAuth2.0 protocol for authentication and authorization.

## Overall Process

Your application must request a code and then extracts an access token from the response. Finally, your application can use the data from VitalDB APIs using the access token.

<img src="images/oauth2/image1.png" width="450" />

# Login Page

Issue a code, which is required to get an access token. Used in “Sign in with VitalDB” service.

<img src="images/oauth2/image2.png" width="450" />

## Endpoint

[**https://vitaldb.net/oauth2/login**](https://vitaldb.net/oauth2/login)

## Method

GET

## Parameters

- Please **urlencode** the parameter if it has any special characters.

| **Field**    | **Type** |
|--------------|----------|
| client_id    | String   |
| redirect_uri | String   |
| state        | String   |

## Return Value

- If successful, it redirected to **redirect_uri?code=xxxxxxxx&state=xxxxxxxx**

| **Field** | **Type** | **Description** |
|----|----|----|
| code | String | A code (random string) which is required to issue an access token. The code will expire in 3 minutes. |
| state | String | Random String used to protect against CSRF (Cross-site Request Forgery). VitalDB server sends back the state parameter. If state parameters are different, CSRF detected. |

## Sample Codes

```
curl -i https://vitaldb.net/oauth2/login?client_id=xxxxxxx&redirect_uri=https://www.path-to-redirect.com/callback
```

# Get Token

Issue an access token which is required to access VitalDB APIs.

## Endpoint

[**https://vitaldb.net/oauth2/token**](https://vitaldb.net/oauth2/token)

## Method

POST

## Parameters

- Please **urlencode** the parameter if it has any special characters.

| **Field**     | **Type** |
|---------------|----------|
| client_id     | String   |
| client_secret | String   |
| code          | String   |

**OR**

| **Field** | **Type** |
|-----------|----------|
| id        | String   |
| pw        | String   |

## Return Value

- Content-type: application/json

| **Field** | **Type** | **Description** |
|----|----|----|
| access_token | String | An access token which is required to access VitalDB APIs |
| token_type | String | Bearer type |
| expires_in | Number | = 3600. The access token expires in an hour. |

## Sample Codes

```
curl -v -d 'code=xxxxxxxxxxxx&client_id=xxxxx&client_secret=xxxxxxxx' https://vitaldb.net/oauth2/token
```

```
curl -v -d 'id=userid&pw=password' https://vitaldb.net/oauth2/token
```
