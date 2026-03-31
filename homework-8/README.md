# Homework 8

This homework sets up a minimal Plotly Dash dashboard containerized with Docker, and demonstrates staging vs. production deployments, Makefile automation, integration testing with pytest, and CI/CD pipelines with GitHub Actions.

## Project Files

    homework08/
    ├── Dockerfile
    ├── Makefile
    ├── app.py
    ├── docker-compose-staging.yml
    ├── docker-compose.yml
    ├── requirements.txt
    └── test
        └── test_app.py

## Starting and Stopping the Dashboard

All commands should be run from inside the `homework08/` directory.

**Production** (port 8050):

To start:

    make compose

To stop:

    make compose-down

**Staging** (port 8051):

To start:

    make compose-staging

To stop:

    make compose-down-staging

To check what containers are currently running:

    make filter

## Staging vs. Production

**Staging** is a separate deployment running on port 8051 that mirrors the production environment exactly, except for the port number. It is used to test new code changes before they go live. 

**Production** is the live deployment of the dashboard, accessible on port 8050. This is the version that end users interact with and should always be stable and tested before deploying. The general steps are:

1. Deploy and test changes in staging first
2. Verify everything looks correct on port 8051
3. Then deploy to production on port 8050 with confidence

The two environments are defined in separate Docker Compose files:

- `docker-compose.yml` — production
- `docker-compose-staging.yml` — staging

## GitHub Actions Workflows

**1. Integration Tests (`integration-test.yml`)**

This workflow runs automatically every time new code is pushed to the repository. It starts the containers with Docker Compose, installs pytest and requests, runs the integration tests, and then tears the containers down. This ensures that new changes do not break the running dashboard.

To trigger it manually, simply push to GitHub:

    git add .
    git commit -m "your message"
    git push

**2. Publish Container Image (`push-to-registry.yml`)**

This workflow runs automatically every time a new version tag is pushed to the repository. It builds the Docker image and pushes it to the GitHub Container Registry (GHCR), so that tagged versions of the image are always available to pull and deploy.

To trigger it, push a new tag:

    git tag -a 0.1.0 -m "first release"
    git push origin 0.1.0

## AI Usage

Claude was used to help debug Makefile tab/space formatting errors and to help make the README aesthetic.
