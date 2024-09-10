# Difference between URI and URL with simple examples use HTTP methods python Rest Api
'''
The terms **URI (Uniform Resource Identifier)** and **URL (Uniform Resource Locator)** are often used interchangeably,
 but they have distinct meanings. Here's a breakdown of their differences, followed by simple examples using HTTP
 methods in Python REST API:

### URI vs. URL:

1. **URI (Uniform Resource Identifier)**:
   - A URI is a broader term that identifies a resource, which could be a webpage, a document, or any entity on the web.
   - It can include both URLs (which specify how to locate the resource) and URNs (Uniform Resource Names, which
   specify a name for the resource without telling where to find it).

2. **URL (Uniform Resource Locator)**:
   - A URL is a type of URI that provides both the location and the means to access the resource.
   - It includes a scheme (such as `http` or `https`), the domain (such as `www.example.com`),
   and often a path that points to a specific resource (like `/users/123`).

### Example:
- **URI**: It could be just an identifier for a resource like `/users/123`.
- **URL**: It provides the full address of the resource, including the protocol,
domain, and path, like `https://api.example.com/users/123`.

All URLs are URIs, but not all URIs are URLs.

---

### Simple Example Using HTTP Methods in Python REST API

Let’s assume we have a REST API that manages user data with the following endpoints:

- **Base URL**: `https://api.example.com`

1. **GET** Request (Retrieve a user)
   - **URI**: `/users/123` (Identifies the resource, but doesn’t tell how to access it)
   - **URL**: `https://api.example.com/users/123` (Tells how to access the resource)

```python
import requests

# URL: Full path to locate the resource using GET method
url = "https://api.example.com/users/123"
response = requests.get(url)

if response.status_code == 200:
    print("User data:", response.json())
else:
    print("Failed to retrieve user data")
```

2. **POST** Request (Create a new user)
   - **URI**: `/users` (Just identifies the collection of users)
   - **URL**: `https://api.example.com/users` (Where to send the request and the method used)

```python
url = "https://api.example.com/users"
data = {
    "name": "John Doe",
    "email": "john@example.com"
}
response = requests.post(url, json=data)

if response.status_code == 201:
    print("User created:", response.json())
else:
    print("Failed to create user")
```

3. **PUT** Request (Update an existing user)
   - **URI**: `/users/123` (Identifies the specific user resource)
   - **URL**: `https://api.example.com/users/123` (Where to send the request and the method used)

```python
url = "https://api.example.com/users/123"
data = {
    "name": "John Smith",
    "email": "johnsmith@example.com"
}
response = requests.put(url, json=data)

if response.status_code == 200:
    print("User updated:", response.json())
else:
    print("Failed to update user")
```

4. **DELETE** Request (Delete a user)
   - **URI**: `/users/123` (Identifies the resource to be deleted)
   - **URL**: `https://api.example.com/users/123` (Specifies the location and method)

```python
url = "https://api.example.com/users/123"
response = requests.delete(url)

if response.status_code == 204:
    print("User deleted successfully")
else:
    print("Failed to delete user")
```

---

### Key Takeaways:
- **URI**: Identifies a resource. It could be a part of a URL but doesn't specify how to access the resource.
  - Example: `/users/123`
- **URL**: Provides the complete address, including the protocol, domain, and path to access the resource.
  - Example: `https://api.example.com/users/123`

In Python REST API testing, we typically use URLs to make requests because
URLs tell us **where** to find the resource and **how** to access it (e.g., via `GET`, `POST`, `PUT`, `DELETE` methods).


'''
