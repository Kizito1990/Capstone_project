# 1. DRF Movie Review API 

## 1.1 Project Overview
The DRF Movie Review API is an application programming interface (API) built using Django and Django REST Framework (DRF) that allows users to manage and interact with movie reviews. It is designed to handle tasks like user authentication, managing reviews for movies, and providing endpoints to perform CRUD (Create, Read, Update, Delete) operations on reviews. This API serves as a backend system for applications that require movie review functionality.

## 1.2 Objectives
- Implement the ability to Create, Read, Update, and Delete (CRUD) reviews.
- Implement CRUD operations for users.
- Efficient Database designs using ORM
- Use Django Rest Framework (DRF) to design and expose the API endpoints.
- Ensure secure access through token-based authentication.
- Provide endpoints for searching and filtering data.
- Implement efficient error handling and data validation ith relevant HTTP status codes 
- Deploy the API in a live environment.

## 1.3 Use Case:
This API is ideal for:
- Movie review websites or apps.
- Platforms where users can share and browse reviews for films.
- Backend services for movie-related applications requiring user-generated content.



# 2.0 Key Features of the DRF Movie Review API:

### 2.1 Review Management (CRUD):
**Users can create, read, update, and delete reviews**.
- Each review has the following:

- **Movie Title:** The title of the movie being reviewed.
- **Review Content:** The text describing the user's opinion.
- **Rating:** A numerical score (e.g., out of 5 stars).
- **User ID:** The identifier for the user who submitted the review.
- **Timestamps:** Created and updated dates for reviews.

### 2.2 User Management (CRUD):

- **Custom user model with unique usernames, emails, and passwords**.
- **Users can register, log in, and manage their accounts**.
- **Authentication ensures that only registered users can submit or modify reviews**.

### 2.3 Movie Review Retrieval:
- **Users can view reviews for a specific movie by searching or filtering by the movie's title**.
- **Pagination ensures efficient handling of large datasets**.
- **Review Search and Filtering**:
- **Search by movie title or rating**.
- **Filter reviews to display only those with specific ratings (e.g., 4-star or 5-star reviews)**.

### 2.4 Authentication and Authorization:
- **Uses JWT (JSON Web Token) for secure authentication**.
- **Ensures only authenticated users can create or modify their reviews**.
- **Enforces permissions to prevent users from editing or deleting reviews by others**.

### 2.5 Database Management:
- **Django ORM (Object-Relational Mapping) manages the database**.
- **Models for users and reviews ensure a robust relational data structure**.

# 3.0 PROJECT MODEL
This project has three models
- User Model
- Review Model
- Like model


# API ENDPOINTS

- 1.0 Retrieve or create a new user.
    - /api/users/
    - GET, POST

- 2.0 Retrieve, update, or delete a user.
    - /api/users/<id>/
    - GET, PUT, DELETE

- 3.0 Retrieve or create a new review.
    - /api/reviews/
    - GET, POST

- 4.0 Retrieve, update, or delete a review.
    - /api/reviews/<id>/
    - GET, PUT, DELETE

- 5 Retrieve likes for a review.
    - /api/reviews/<id>/likes/
    - GET

- 6 Retrieve or create a new like.
    - /api/likes/
    - GET, POST

- 7 Retrieve or delete a like.
    - /api/likes/<id>/
    - GET, DELETE



# Technology Stack
- **Python**
- **Django**
- **Backend Framework: Django and Django Rest Framework (DRF)**.
- **Database: MYSQL for both development and  production**.
- **Json Web Token(JWT): JWT was used to generate Authentication token**
- **Postman: Postman was used for user authentication using Token(JWT)**


# Django Movie Review API Documentation

## Overview
The Movie Review API allows users to manage their accounts, write and view reviews for movies, and like reviews. The API is secured with JWT authentication.

---

## Endpoints

### Authentication
#### 1. **Register User**
- **Path:** `/api/auth/register/`
- **Method:** `POST`
- **Description:** Register a new user.
- **Request Parameters:**
  ```json
  {
    "username": "string",
    "email": "string",
    "password": "string"
  }
  ```
- **Response:**
  - **201 Created**
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
    ```
  - **400 Bad Request**
    ```json
    {
      "error": "string"
    }
    ```

#### 2. **Login User**
- **Path:** `/api/auth/login/`
- **Method:** `POST`
- **Description:** Authenticate a user and issue a JWT token.
- **Request Parameters:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "access": "string",
      "refresh": "string"
    }
    ```
  - **401 Unauthorized**
    ```json
    {
      "error": "string"
    }
    ```

#### 3. **Refresh Token**
- **Path:** `/api/auth/token/refresh/`
- **Method:** `POST`
- **Description:** Refresh the JWT access token.
- **Request Parameters:**
  ```json
  {
    "refresh": "string"
  }
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "access": "string"
    }
    ```

---

### User
#### 1. **Retrieve User Profile**
- **Path:** `/api/users/profile/`
- **Method:** `GET`
- **Description:** Get details of the authenticated user.
- **Headers:**
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "id": "integer",
      "username": "string",
      "email": "string"
    }
    ```

---

### Reviews
#### 1. **Create a Review**
- **Path:** `/api/reviews/`
- **Method:** `POST`
- **Description:** Add a review for a movie.
- **Headers:**
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```
- **Request Parameters:**
  ```json
  {
    "movie_title": "string",
    "content": "string",
    "rating": "integer"  // between 1 and 5
  }
  ```
- **Response:**
  - **201 Created**
    ```json
    {
      "id": "integer",
      "movie_title": "string",
      "content": "string",
      "rating": "integer",
      "user": {
        "id": "integer",
        "username": "string"
      },
      "likes": "integer"
    }
    ```

#### 2. **Retrieve Reviews**
- **Path:** `/api/reviews/`
- **Method:** `GET`
- **Description:** Retrieve all reviews.
- **Response:**
  - **200 OK**
    ```json
    [
      {
        "id": "integer",
        "movie_title": "string",
        "content": "string",
        "rating": "integer",
        "user": {
          "id": "integer",
          "username": "string"
        },
        "likes": "integer"
      }
    ]
    ```

#### 3. **Retrieve a Single Review**
- **Path:** `/api/reviews/<id>/`
- **Method:** `GET`
- **Description:** Get a specific review by ID.
- **Response:**
  - **200 OK**
    ```json
    {
      "id": "integer",
      "movie_title": "string",
      "content": "string",
      "rating": "integer",
      "user": {
        "id": "integer",
        "username": "string"
      },
      "likes": "integer"
    }
    ```

---

### Likes
#### 1. **Like a Review**
- **Path:** `/api/reviews/<id>/like/`
- **Method:** `POST`
- **Description:** Like a review.
- **Headers:**
  ```
  Authorization: Bearer <JWT_TOKEN>
  ```
- **Response:**
  - **200 OK**
    ```json
    {
      "message": "Review liked successfully",
      "likes": "integer"
    }
    ```

---

## Notes
- All endpoints that modify data require JWT authentication.
- Error handling should follow standard HTTP response codes (e.g., `400 Bad Request`, `404 Not Found`, `500 Internal Server Error`).





