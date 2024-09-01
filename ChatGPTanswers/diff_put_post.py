'''
difference between put () & post () API
-------------------------------------------------------------------------------------------------------------------
The `PUT` and `POST` methods are two HTTP verbs commonly used in RESTful APIs. Both are used
to send data to a server, but they serve different purposes and have distinct behaviors. Here’s a breakdown
of the differences:

### 1. **Purpose**
   - **`POST`**: Used to create a new resource on the server.
   - **`PUT`**: Used to create or update a resource at a specific location on the server.

### 2. **Idempotence**
   - **`POST`**: Not idempotent. Multiple identical `POST` requests will typically create multiple resources with
   different identifiers. The server processes each `POST` request as a new operation.
   - **`PUT`**: Idempotent. Multiple identical `PUT` requests will result in the same resource being created or updated.
    If you send the same `PUT` request multiple times, the result will be the same as if you sent it once.

### 3. **Resource Location**
   - **`POST`**: The server determines the URI of the new resource. The client sends data to a general endpoint,
   and the server creates the resource and assigns it a unique URI.
   - **`PUT`**: The client specifies the URI of the resource to be created or updated. If the resource does not exist,
   `PUT` will create it at the specified URI; if it does exist, `PUT` will update it.

### 4. **Use Case**
   - **`POST`**:
     - Submitting a form to create a new user account.
     - Uploading a file to a server.
     - Posting a comment to a blog post.
   - **`PUT`**:
     - Updating a user profile at a specific URL.
     - Replacing the content of a file at a specified location.
     - Creating a resource with a client-defined identifier.

### 5. **Request Body**
   - **`POST`**: The request body contains the data to create a new resource. The server handles this data and
   returns a response with the status and possibly the location of the new resource.
   - **`PUT`**: The request body contains the full representation of the resource that is to be created or
   updated at the specified URI.

### 6. **Response Codes**
   - **`POST`**:
     - `201 Created`: Indicates that a new resource has been created.
     - `200 OK` or `204 No Content`: Indicates success, but no new resource was created.
     - `400 Bad Request`: If the request is malformed.
   - **`PUT`**:
     - `201 Created`: Indicates that a resource has been created at the specified URI.
     - `200 OK` or `204 No Content`: Indicates success when updating an existing resource.
     - `404 Not Found`: If the resource to be updated does not exist (in some implementations).
     - `400 Bad Request`: If the request is malformed.

### Examples

#### `POST` Example
```http
POST /users HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Response**:
```http
HTTP/1.1 201 Created
Location: /users/12345
```

#### `PUT` Example
```http
PUT /users/12345 HTTP/1.1
Host: example.com
Content-Type: application/json

{
    "name": "John Doe",
    "email": "john.doe@example.com"
}
```
- **Response**:
```http
HTTP/1.1 200 OK
```

### Summary
- **`POST`** is generally used for creating new resources where the server generates the identifier.
- **`PUT`** is used for creating or updating a resource where the client specifies the identifier or URL.


'''
