# Api Test with Tavern

This project automates a couple of APIs built with SpringBoot [from this project.](https://github.com/bashiulAlam/spring-boot-api-project.git)
***

## Project Tools Used
- **Programming Language:** Python (Version 3.11)
- **Framework:** Tavern
- **IDE:** PyCharm

## Prerequisites

- You need to have the following installations in your machine:
    - Pip
    - Python
    - Any IDE of your choice that supports Python
- Install *tavern* dependency by running the following command from your terminal:

  >   pip install tavern

- Install *pykwwalify* dependency for schema validation by running the following command from your terminal:
  >   pip install pykwalify

## Project Import
1. Clone the project from GitHub or download the project and unzip it
2. Open your IDE and import the project 

## How to Run

1. To run the API tests and then clearing the data from redis cache you have to follow one of the two ways below:

- You can run the full project from your IDE by following the steps:
    1. Open the python file **main.py** from your *{project_root}*
    2. Run this file
- From your *{project_root}*, run the following command from terminal:

  >   python main.py

2. You can run only the api tests using command prompt or terminal by executing the following command from your *{project_root}*:

  >   tavern-ci test_weather-api.tavern.yaml

## Result Monitoring
1. You can see the results from your IDE or terminal console

## Building Docker Image

- The project repository contains the *Dockerfile* to build a docker image of the project
- To build the docker image run the command from terminal:
    >  docker build -t {image_name} .
- To run the image run the command from terminal:
    >  docker run {image_name}