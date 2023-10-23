# event-management-DRF

This is an API for an Event Management System built with Django and Django REST Framework. The API allows for the creation, reading, updating, and deletion of users, colleges, students, and events.

## Features:

 - User Management: Register new users, authenticate users, and refresh JWT tokens for ongoing sessions. CRUD operations on user profiles are also supported. 
 - College Management: Perform CRUD operations on college data.
 - Student Management: Manage student data with CRUD operations. Each student is associated with a specific user and college.
 - Event Management: Create, read, update, and delete events. Each event is associated with a specific college.

## Usage
 All endpoints return data in JSON format. Most endpoints require JWT token authentication, which should be included in the Authorization header of the request in the format `Bearer <token>

Refer to the API documentation [here](https://documenter.getpostman.com/view/19992072/2s9YRCVqov)
