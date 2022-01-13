## FARM-STACK-TEMPLATE 🧑‍🌾

**Features**

- FastAPI 
- React with Tailwind css
- MongoDB for db needs
- Nginx reverse proxy for deployment
- Docker-compose for local development


## Quick Start

Install cookiecutter on your system

```bash 
pip install cookiecutter
```
Then from the directory on which you want your project run 

```bash
cookiecutter gh:prabum3/farm-stack-template
```
Cookiecutter would prompt you for the following inputs:
  - project_slug: name for your project (required)
  - container_registry: container-registry where you would like to push your container images (optional default:docker.io)
 
 ## Local Development
 
 You can get started with your project locally by running the command
 
 ```bash
   docker compose -f docker-compose-local.yml up --build -d  
 ```
 
 This sets up the website at port:5000
 
## Reference 

https://github.com/Buuntu/fastapi-react
