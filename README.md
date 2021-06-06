# Overview
Setup of a continous delivery and intrgration pipeline using Azure piplines and git actions
to deploy a simple machine learning app using Flask web framwork ysed to predict housing prices in Boston. 
The template can be extended to any pre-trained machine learning model, such as those for image recognition and data labeling. 


## Project Plan
* Trello board
https://trello.com/b/4mjiLmgV/udacity-devops
* Prject plan 
https://docs.google.com/spreadsheets/d/1tYQuDqm2EebUbymdccGSOAIrnwG3jesx0YNzeNc6ZWs/edit?usp=sharing

## Instructions
An Azure Account ( https://portal.azure.com/)
A GitHub Account ( http://github.com/)
A CircleCi Account (https://circleci.com/ )
An Azure DevOps Account (https://dev.azure.com/)

<TODO:  
* Architectural Diagram (Shows how key parts of the system work)>

<TODO:  Instructions for running the Python project.  How could a user with no context run this project without asking you for any help.  Include screenshots with explicit steps to create that work. Be sure to at least include the following screenshots:

* Project running on Azure App Service

* Project cloned into Azure Cloud Shell

* Passing tests that are displayed after running the `make all` command from the `Makefile`

* Output of a test run

* Successful deploy of the project in Azure Pipelines.  [Note the official documentation should be referred to and double checked as you setup CI/CD](https://docs.microsoft.com/en-us/azure/devops/pipelines/ecosystems/python-webapp?view=azure-devops).

* Running Azure App Service from Azure Pipelines automatic deployment

* Successful prediction from deployed flask app in Azure Cloud Shell.  [Use this file as a template for the deployed prediction](https://github.com/udacity/nd082-Azure-Cloud-DevOps-Starter-Code/blob/master/C2-AgileDevelopmentwithAzure/project/starter_files/flask-sklearn/make_predict_azure_app.sh).
The output should look similar to this:

```bash
udacity@Azure:~$ ./make_predict_azure_app.sh
Port: 443
{"prediction":[20.35373177134412]}
```

* Output of streamed log files from deployed application

> 

## Enhancements

<TODO: A short description of how to improve the project in the future>

## Demo 

<TODO: Add link Screencast on YouTube>



[![Python application tests with github actions](https://github.com/maur1/azure-devops/actions/workflows/main.yml/badge.svg)](https://github.com/maur1/azure-devops/actions/workflows/main.yml)