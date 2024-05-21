Database Tables and Relationships
Tables
transport_types Table:

Purpose: Stores the different types of transport available (e.g., bus, taxi, train).
Columns:
id: An integer that uniquely identifies each transport type (Primary Key).
name: A string that holds the name of the transport type.
routes Table:

Purpose: Stores the routes available for each type of transport.
Columns:
id: An integer that uniquely identifies each route (Primary Key).
transport_type_id: An integer that references the id in the transport_types table (Foreign Key).
name: A string that holds the name of the route.
schedules Table:

Purpose: Stores the departure times for each route.
Columns:
id: An integer that uniquely identifies each schedule entry (Primary Key).
route_id: An integer that references the id in the routes table (Foreign Key).
departure_time: A string or time value that holds the departure time.
payment_methods Table:

Purpose: Stores the different types of payment methods available (e.g., Mpesa, Bank, Cash).
Columns:
id: An integer that uniquely identifies each payment method (Primary Key).
name: A string that holds the name of the payment method.
payments Table:

Purpose: Records each payment made by users.
Columns:
id: An integer that uniquely identifies each payment record (Primary Key).
user_id: An integer that identifies the user making the payment.
payment_method_id: An integer that references the id in the payment_methods table (Foreign Key).
amount: A decimal value that holds the amount paid.
timestamp: A datetime value that records the date and time of the payment (defaulting to the current time).
Relationships
transport_types to routes:

Type: One-to-Many
Explanation: Each transport type can have multiple routes. This relationship is established by the transport_type_id foreign key in the routes table referencing the id in the transport_types table.
routes to schedules:

Type: One-to-Many
Explanation: Each route can have multiple schedules. This relationship is established by the route_id foreign key in the schedules table referencing the id in the routes table.
payment_methods to payments:

Type: One-to-Many
Explanation: Each payment method can be used in multiple payments. This relationship is established by the payment_method_id foreign key in the payments table referencing the id in the payment_methods table.
These tables and relationships form the foundation for a database that can handle transport types, routes, schedules, and payments, enabling a flexible and scalable system for managing transport-related information and user payments.
