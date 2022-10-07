# Airflow directory
Apache Airflow (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.
When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.
Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.
# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

- Clone this repo
- Install the prerequisites
- Run the service
- Check http://localhost:8080
- Done! 🎉
# Prerequisites
- Install Docker
- Install Docker Compose
# Following the Airflow release from Python Package Index
- Usage
             Run the web service with docker
             docker-compose up -d

            # Build the image
            #docker-compose up -d --build

# Check http://localhost:8080/

- docker-compose logs - Displays log output
- docker-compose ps - List containers
- docker-compose down - Stop containers
# Connect to database
If you want to use Ad hoc query, make sure you've configured connections: Go to Admin -> Connections and Edit "postgres_default" set this values:

- Host : postgres
- Schema : airflow
- Login : airflow
- Password : airflow
# Credits
- Apache Airflow
- docker-airflow
