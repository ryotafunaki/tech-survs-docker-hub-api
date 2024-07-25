# Docker Hub Api Technical Survey Repository

This repository is a technical survey of the Docker Hub API.

## Overview

## Requirements

- Python 3.12 and later

## How to use

### Execution on local machine

1.  Execute the application
    ```bash
    poetry run python main.py -n *namespace* -r *repository* -t *tag*
    ```
    e.g.
    ```bash
    poetry run python main.py -n library -r hello-world -t latest
    ```
