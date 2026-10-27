# Flask CI/CD Pipeline with GitHub Actions & Docker

## Overview

This project demonstrates an automated CI/CD pipeline for a Python Flask application using GitHub Actions and Docker. The pipeline runs automated tests, builds a Docker image, and publishes the image to Docker Hub when changes are pushed to the `main` branch.

## Architecture

Developer → GitHub Repository → GitHub Actions → Automated Tests → Docker Build → Docker Hub → Docker Container

## Technologies Used

- **Python & Flask** — REST API application
- **Pytest** — Automated application testing
- **Docker** — Application containerization
- **Docker Compose** — Local container management
- **Git & GitHub** — Version control and source code hosting
- **GitHub Actions** — CI/CD automation
- **Docker Hub** — Docker image registry

## Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | Returns application status and version |
| `/health` | Health check endpoint |

## CI/CD Workflow

1. A developer pushes code to the `main` branch.
2. GitHub Actions checks out the source code.
3. Python dependencies are installed.
4. Pytest runs the automated tests.
5. If tests pass, Docker builds the application image.
6. GitHub Actions authenticates securely with Docker Hub using repository secrets.
7. The image is published with `latest` and commit-SHA tags.

## Run Locally

### Prerequisites

- Docker and Docker Compose

### Start the application

```bash
git clone https://github.com/shivamnegii01/flask-cicd-project.git
cd flask-cicd-project
docker compose up --build -d
```

Open `http://localhost:5000/` or test the health endpoint:

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
```

Stop the application:

```bash
docker compose down
```

## Run the Published Docker Image

Pull and run the image from Docker Hub:

```bash
docker pull shivamnegi07/flask-cicd-project:latest
docker run -d --name flask-cicd-app -p 5000:5000 shivamnegi07/flask-cicd-project:latest
```

Test the application:

```bash
curl http://localhost:5000/
curl http://localhost:5000/health
```

Clean up:

```bash
docker stop flask-cicd-app
docker rm flask-cicd-app
```

## Configuration

Configure the following GitHub repository secrets for Docker Hub publishing:

- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`

Never commit access tokens or other credentials to the repository.

## Project Links

- **GitHub:** https://github.com/shivamnegii01/flask-cicd-project
- **GitHub Actions:** https://github.com/shivamnegii01/flask-cicd-project/actions
- **Docker Hub:** https://hub.docker.com/r/shivamnegi07/flask-cicd-project

## Learning Outcomes

- Built an automated CI/CD pipeline.
- Implemented automated testing before Docker image publishing.
- Containerized a Flask application.
- Configured secure GitHub Actions secrets.
- Published and tested a Docker image from Docker Hub.

