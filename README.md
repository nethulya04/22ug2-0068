**Nethulya Sooriarachchi | 22UG2-0068**
______________________________________________________________________________________________________________________________________
🐳**Dockerized To-Do List Application**
A simple, multi-container web application that allows users to manage a to-do list. This project uses Python/Flask for the web front-end and MongoDB for the database, with the entire environment managed by Docker and Docker Compose.

🚀 Deployment Requirements
To deploy and run this application, you will need the following software installed on your system:

Docker Engine: The core runtime for building and running containers.

Docker Compose: The tool for defining and running multi-container Docker applications.

📝 Application Description
The application provides a straightforward web interface that enables users to perform the following actions:

View all current tasks on the to-do list.

Add a new task to the list through an input form.

Delete an existing task from the list.

The application is designed with data persistence in mind; all to-do items are stored in a MongoDB database, ensuring that user data is preserved even if the application containers are stopped or restarted.

🏛️ Application Architecture
Container List
The application is composed of two distinct services, each running in its own container:

todo-app (Custom Docker Image)

Role: This service acts as the web front-end. It is built from a custom Dockerfile using a Python base image. It runs a Gunicorn server to serve the Flask application, which renders the user interface and handles all user interactions and business logic. It communicates with the mongo-db service to persist and retrieve data.

mongo-db (Image from Docker Hub: mongo:latest)

Role: This service is the application's database backend. It uses the official mongo image from Docker Hub. Its sole responsibility is to store, manage, and provide access to the to-do list data.

Network and Volume Details
Virtual Network: todo-network

A custom bridge network is defined to provide an isolated environment where the application's containers can communicate. The todo-app service connects to the database by referencing its service name, mongo-db, over this network.

Named Volume: mongo-data

This named volume is used to persist the data stored by the mongo-db service. It is mounted to the standard MongoDB data directory (/data/db) inside the mongo-db container. This setup ensures that the to-do list data is safely stored on the host machine and survives container restarts, stops, and removals.

Container Configuration
The application's services are configured within the docker-compose.yaml file:

The todo-app service is configured with an environment variable, MONGO_HOST=mongo-db, which instructs the Flask application on how to locate the database service on the virtual network.

The todo-app service is set to restart: on-failure to enhance its resilience.

Port 8000 on the host machine is mapped to port 8000 inside the todo-app container, allowing users to access the web interface.

🛠️ Instructions & Workflow
A set of executable shell scripts is provided to simplify the management of the application's lifecycle.

1. Prepare Application Resources
This script creates the Docker network and volume required by the application.

./prepare-app.sh

2. Run the Application
This script builds the custom web application image and starts both the todo-app and mongo-db containers in the background.

./start-app.sh

3. Access the Application
Once the application is running, open a web browser and navigate to:
http://localhost:8000

4. Pause the Application
This script stops the running containers without deleting any data or resources.

./stop-app.sh

5. Delete all Application Resources
This script performs a full cleanup by stopping and removing the containers, deleting the network and data volume, and removing the custom-built Docker image.

Warning: This is a destructive action and will permanently erase all to-do list data.

./remove-app.sh

Example Workflow
Below is a typical command-line session for using the scripts to manage the application:

# Create application resources
$ ./prepare-app.sh
Preparing app resources...

# Run the application
$ ./start-app.sh
Running app ...
The app is available at http://localhost:8000

# Open a web browser and interact with the application

# Pause the application
$ ./stop-app.sh
Stopping app ...

# Delete all application resources
$ ./remove-app.sh
Removed app.

