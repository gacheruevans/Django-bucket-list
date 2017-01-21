[![Build Status](https://travis-ci.org/andela-gacheruevans/cp3-django-bucketlist.svg?branch=implement-tests)](https://travis-ci.org/andela-gacheruevans/cp3-django-bucketlist)
[![Coverage Status](https://coveralls.io/repos/github/andela-gacheruevans/cp3-django-bucketlist/badge.svg?branch=implement-tests)](https://coveralls.io/github/andela-gacheruevans/cp3-django-bucketlist?branch=develop)
# cp3-django-bucketlist

This application helps you log and catalog all the stuff you want to accomplish before you expire.

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

##Installation