# Comprehensive Technical Document for HBnB Project 

 

## 1. Introduction 

**Purpose of the Document**: 
This document serves as a detailed blueprint for the HBnB project, a simplified version of Airbnb.
It provides a comprehensive overview of the system's architecture, design, and interactions through diagrams and explanatory notes.
The document will guide the implementation phases and serve as a reference for developers, ensuring consistency and clarity throughout the project. 

**Scope of the Project** 

The HBnB project aims to create a web application that allows users to: 

* Register and authenticate themselves.
* Create and manage property listings.
* Submit reviews for properties.
* Search and view a list of available properties. 

This document focuses on the high-level architecture, business logic layer, and API interaction flows,
providing a clear understanding of the system's design and functionality. 

 

## 2. High-Level Architecture 

**High-Level Package Diagram**: 
 

 ![Paquage Diagram](./jpg/High-Level_Paquage_Diagram.jpg)
 
**Explanatory Notes**: 

- **Layered Architecture**: The system is divided into layers to promote separation of concerns, making the application modular, scalable, and easier to maintain. 
- **Facade Pattern**: The facade layer acts as an intermediary between the presentation layer and the business logic layer, simplifying complex interactions and ensuring loose coupling. 
- **Persistence Layer**: This layer interacts with the database to store and retrieve data, ensuring data integrity and consistency. 

 

## 3. Business Logic Layer 

**Detailed Class Diagram**:

[Click here to see diagram](./jpg/Class_diagram.drawio)

**Explanatory Notes**:

 <ins>**Entities and Relationships**</ins>: 

* User: Represents a user of the system, with attributes like name, email, and password. 
* Place: Represents a property listing, with attributes like title, description, price, and location. 
* Review: Represents a review submitted by a user for a place, with attributes like rating, comment, and date. 

<ins>**Design Decisions**</ins>: 

* The User class is central to the system, as it interacts with both Place and Review. 
* The Place class aggregates Review objects, ensuring that reviews are tied to specific properties. 
* The use of encapsulation ensures that each class manages its own data and behavior, promoting modularity and reusability. 

 

## 4. API Interaction Flow 

**Sequence Diagrams**: 

<ins>**User Registration**</ins>: 

![Diagram user](./jpg/Sequence_Diagram_User.jpg)

* The user submits registration details (e.g., name, email, password) through the presentation layer. 
* The facade layer validates the input and passes it to the business logic layer. 
* The business logic layer creates a new User object and saves it to the database via the persistence layer. 

<ins>**Place Creation**</ins>: 

![Diagram place](./jpg/Sequence_Diagram_Place.jpg)

* The user submits property details (e.g., title, description, price) through the presentation layer.
* The facade layer validates the input and forwards it to the business logic layer.
* The business logic layer creates a new Place object, associates it with the logged-in user, and saves it to the database. 

<ins>**Review Submission**</ins>: 

![Diagram review](./jpg/Sequence_Diagram_Review.jpg)

* The user submits a review (e.g., rating, comment) for a specific property.
* The facade layer validates the input and passes it to the business logic layer.
* The business logic layer creates a new Review object, associates it with the corresponding Place and User, and saves it to the database. 

<ins>**Fetching a List of Places**</ins>: 

![Diagram fetch](./jpg/Sequence_Diagram_Fetch.jpg)

* The user requests a list of available properties.
* The facade layer forwards the request to the business logic layer.
* The business logic layer retrieves the list of Place objects from the database and returns it to the presentation layer for display. 

 

***Conclusion*** 

This document provides a comprehensive overview of the HBnB project's architecture, business logic, and API interactions.
By following this blueprint, developers can ensure a consistent and efficient implementation process.
The diagrams and explanatory notes serve as a reference for understanding the system's design and functionality,
ensuring that all components work together seamlessly. 

 
