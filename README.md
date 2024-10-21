# Rule Engine Application

This is a Flask-based Rule Engine application that allows users to create, combine, and evaluate business rules based on user data. It uses MongoDB as the database to store the rules and Abstract Syntax Trees (ASTs). The rule engine processes and evaluates rules dynamically.

## Table of Contents

- [Overview](#overview)
- [Design Choices](#design-choices)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Setup Instructions](#setup-instructions)
  - [Using Virtual Environment](#using-virtual-environment)
  - [Using Docker](#using-docker)
- [Running the Application](#running-the-application)
  - [Running Locally](#running-locally)
  - [Running with Docker](#running-with-docker)

## Overview

This project implements a basic rule engine where you can:
- **Create rules**: Define rules based on conditions like age, salary, department, etc.
- **Combine rules**: Combine multiple rules logically using AND/OR operators.
- **Evaluate rules**: Evaluate user data against defined rules to determine eligibility.

## Design Choices

1. **Flask Framework**: A lightweight and flexible web framework used for building the backend API.
2. **MongoDB**: Used as the database to store rules and AST representations. MongoDB's flexibility in handling JSON-like data structures makes it ideal for this application.
3. **Abstract Syntax Tree (AST)**: Rules are stored in AST format, which allows easy manipulation, combination, and evaluation of conditions.
4. **Tailwind CSS**: Used for UI styling to ensure a clean and responsive interface for interacting with the rule engine.
5. **Docker**: Both the MongoDB database and Flask application can be run using Docker containers to simplify deployment and ensure consistency across environments.




## Dependencies

### Python Dependencies
- Python 3.x
- Flask
- Flask-CORS
- pymongo (MongoDB driver for Python)
- Tailwind CSS (for UI styling)

These dependencies are listed in the `requirements.txt` file.

### Additional Software

- **MongoDB**: Used as the database for storing rules and ASTs.
  - If you’re running MongoDB manually, ensure it’s installed locally or use Docker to run it.
  
- **Docker & Docker Compose**: We provide a `docker-compose.yml` file to set up the application and MongoDB using Docker.

## Setup Instructions

### Using Virtual Environment

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name

2. **Set up the Virtual Environment:**
    ```bash
   python -m venv venv

3.**Activate the Virtual Environment:**

.\venv\Scripts\activate

 ***On macOS/Linux***
 source venv/bin/activate

4. **Set up MongoDB:**

Option 1: Install MongoDB locally (follow the official MongoDB Installation Guide).
Option 2: Use Docker (see Docker instructions below).

   **Using Docker**

Install Docker & Docker Compose:

Follow the official installation instructions for Docker and Docker Compose.
Build and Run Containers: 
Run the following command to build and start both MongoDB and the Flask app:

docker-compose up --build

5. ***Start a MongoDB container***
Set up networking between the Flask app and MongoDB.
Access the Application: Once the containers are up, the Flask application will be available at:

http://localhost:5000

6.***Running the Application***
Running Locally
Start MongoDB: If MongoDB is running locally, start the MongoDB service.

Run the Flask Application:
Once MongoDB is running, you can start the Flask app by running:

python app.py
Access the Application: Open a browser and navigate to:

http://localhost:5000
Running with Docker
Start with Docker Compose:
Run the following command to start both the MongoDB and Flask containers:

```bash 
docker-compose up --build

7.**Access the Application: Open a browser and navigate to**

```bash
http://localhost:5000

