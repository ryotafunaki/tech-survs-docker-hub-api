# Docker Hub API Technical Survey Repository

This repository is a technical survey of the Docker Hub API.

## Overview

## Requirements

- Python 3.12 and later

## How to use

### Execution on local machine

1.  Start the Dev Container
1.  Install dependencies
    ```bash
    poetry install
    ```
1.  Execute the application
    ```bash
    poetry run python main.py -n <namespace> -r <repository> -t <tag>
    ```
    e.g.
    ```bash
    poetry run python main.py -n library -r hello-world -t latest
    ```

## Maintenance

### How to update dependencies

1.  Update dependencies
    ```bash
    poetry update
    ```
1.  Update the latest API specification
    ```bash
    kiota download apisguru::docker.com:hub -o openapi.json
    kiota update -o ./api/client
    rm openapi.json
    ```
