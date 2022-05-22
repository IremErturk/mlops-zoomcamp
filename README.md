# mlops-zoomcamp

### Setting up Development Environment with Poetry

Poetry is Python Package Management tool that helps managing package dependencies.

1. Install poetry as described in the [Poetry installation](https://python-poetry.org/docs/#installation) section

2. Install packages based on defined versions in either `pyproject.toml` or `poetry.lock`. If you are interested to know details , please check [Installing Dependencies](https://python-poetry.org/docs/basic-usage/#installing-dependencies) section.
    ```bash 
    poetry install
    ```

3. Activate the poetry environment 
    ```bash 
    source {path_to_venv}/bin/activate
    ```

4. To add new packages to the poetry environment. Check the [official documentation](https://python-poetry.org/docs/cli/#add) if you are unsure of usage
    ```bash
    poetry add <package-name><condition><version>
    ```