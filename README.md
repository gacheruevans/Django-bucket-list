[![CircleCI](https://dl.circleci.com/status-badge/img/gh/gacheruevans/Django-bucket-list/tree/develop.svg?style=shield)](https://dl.circleci.com/status-badge/redirect/gh/gacheruevans/Django-bucket-list/tree/develop)

# Django and React App - Bucket List

This application helps you log and catalog all the things you ever wanted to accomplish that are huge milestones before you expire.

## Task Description

In this exercise I was required to create a Django + PostgreSQL based implementation of BucketList App that I had created in Checkpoint 2 (cp2-bucketlist).

###Specification for the API is shown below.

| Endpoint                 				               		   | Functionality 						 | Public Access| 
| -------------------------------------------------------------|-------------------------------------|---------------
| `POST /auth/login`         				                   |  Logs a user in                     |  TRUE        |
| `POST /auth/register`      				                   |  Register a user                    |	FALSE	    |
| `POST /bucketlists`       				                   |  Create a new bucket list	         |  FALSE       |
| `GET /bucketlists`						                   |  List all the created bucket lists	 |  FALSE       |
| `GET /bucketlists/<bucketlists_id>`		                   |  Get single bucket list             |  FALSE       |                     
| `PUT /bucketlists/<bucketlists_id> `                         |  Update this bucket list            |  FALSE       |                       
| `DELETE /bucketlists/<bucketlists_id>`				       |  Delete this single bucket list     |  FALSE       |                              
| `POST /bucketlists/<bucketlists_id>/items`                   |  Create a new item in bucket list   |  FALSE       |                                
| `PUT /bucketlists/<bucketlists_id>/items/<item_id>`          |  Update a bucket list item          |  FALSE       |                         
| `DELETE /bucketlists/<bucketlists_id>/items/<item_id>`       |  Delete an item in a bucket list    |  FALSE       |

##Options

| Endpoint                 				               		   | Functionality 						 	  |    
| -------------------------------------------------------------|:----------------------------------------:|
| `SEARCH /bucketlists?q=abc`         				           | Enter a search parameter                 |
| `LIMIT /bucketlists?limit=2`      				           | Number of items per page(default is 20)  |


| Method                 				               		   | Description 						 	  |    
| -------------------------------------------------------------|:----------------------------------------:|
| GET         				           						   | Retrieves a resource(s)                 |
| POST      				                                   | Creates a new resource                  |
| PUT         				                                   | Updates an existing resource            |
| DELETE      				                                   | Deletes an existing resource            |
| SEARCH                                                       | Searches for an existing resource       |

## Installation and Running Project Instructioons.

1. Clone this repository: git@github.com:gacheruevans/Django-bucket-list.git

    * via SSH
        git@github.com:gacheruevans/Django-bucket-list.git 

2. Navigate into your project directory 

        cd Django-bucket-list 
    
3. Install virtualenv using 
   
        pip install --user virtualenv 
        or sudo apt get python-virtualenv if on ubuntu linux machine, then create virtual environment by running command
    
4. Install dependencies with 
        pipenv install --dev

        Run python manage.py migrate to create database tables, then run python manage.py createsuperuser to add admin credentials if needed.

5. To run project 
        Run python manage.py runserver on terminal or use IDE's debugger if using Pycharm.