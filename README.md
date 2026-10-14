A containerized **Infrastructure Health Monitoring API** built with Python and FastAPI to expose real-time system health and resource utilization metrics.

### API Endpoints
- `GET /` — Returns a welcome message confirming the API is running.
- `GET /health` — Returns the application health status.
- `GET /system` — Reports CPU utilization, memory utilization, and disk usage percentage using `psutil`.
- `GET /docs` — Provides interactive Swagger UI documentation for exploring and testing endpoints.

### Tech Stack
Python • FastAPI • Uvicorn • psutil • Docker • GitHub Actions • AWS EC2 • Terraform

### DevOps Implementation
- Dockerized application for consistent deployment.
- GitHub Actions workflow for dependency installation, import checks, and Docker image builds.
- Deployed the containerized API on AWS EC2.
- Terraform used to provision and manage AWS infrastructure resources.

**Project Goal:** Demonstrate practical skills in API development, containerization, CI automation, cloud deployment, and Infrastructure as Code.
