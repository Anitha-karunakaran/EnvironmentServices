# Environment Services
## About the application
Environment Services is an application which lists the environment services available in various regions.


The Chief Officer of Environment Services can add/modify/delete regions.  
The Services Manager cannot modify regions but can add the services available in all the regions.  
Public can view all the regions where Environment Services are available and all the services.

The application is hosted in Heroku: [https://udacity-environment-services.herokuapp.com/services](https://udacity-environment-services.herokuapp.com/services)

Your JWT can be obtained from the [The Auth0 redirect URL](https://fsndanikaruna.us.auth0.com/authorize?audience=envsrv&response_type=token&client_id=nGhgfyP2tBCsMHFGhqr3FvtsawagHfhu&redirect_uri=https://udacity-environment-services.herokuapp.com/regions)  

Latest JWT for Test
``` 
CHIEF_OFFICER_JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRXdG5QNHI5X3RPbUR4V3ZhQk9FRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRhbmlrYXJ1bmEudXMuYXV0aDAuY29tLyIsInN1YiI6Imdvb2dsZS1vYXV0aDJ8MTEyNjMxMDczNjE5NTMxOTE0ODUxIiwiYXVkIjoiZW52c3J2IiwiaWF0IjoxNjE2MzQ3NjU0LCJleHAiOjE2MTY0MzQwNTQsImF6cCI6Im5HaGdmeVAydEJDc01IRkdocXIzRnZ0c2F3YWdIZmh1Iiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6cmVnaW9ucyIsImRlbGV0ZTpzZXJ2aWNlcyIsInBhdGNoOnJlZ2lvbnMiLCJwYXRjaDpzZXJ2aWNlcyIsInBvc3Q6cmVnaW9ucyIsInBvc3Q6c2VydmljZXMiXX0.tqV-a4oQLiw-Ryk924mKPIY-yrlqv4xDOOpfdToMPH5ws8xrA8M-0wlJDO7VEh5HscqEJFLeuoBFRLBp_sR0FSf7x8x_XK9sAQCNKnx0PolUCfukIais0cvQXvdkijrLucSjyVzjQv6oLI5bJkKHXkFT4B6i-JN-wmHXQy_uJp3Kc2exw8YM8XNJBLZeC_7_qkyiXl_Ckb0EkPHjWSFlE96NF-VqxS9Lzllrl5CUNnoOM7WQf4kKVD18SzLp4x56iDiy7ASW7D9p-4EMiriCWZ-7s9bQXx6iIZc9CcamiL3PVxknsm7wm_euZOnsCi4yNNEAfeiEOgixhRFI9P2uzg
SERVICES_MANAGER_JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRXdG5QNHI5X3RPbUR4V3ZhQk9FRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRhbmlrYXJ1bmEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTNmOTZhMGY5MmJiMDA2OWMwN2I0YyIsImF1ZCI6ImVudnNydiIsImlhdCI6MTYxNjM0NzcwMCwiZXhwIjoxNjE2NDM0MTAwLCJhenAiOiJuR2hnZnlQMnRCQ3NNSEZHaHFyM0Z2dHNhd2FnSGZodSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnNlcnZpY2VzIiwicGF0Y2g6c2VydmljZXMiLCJwb3N0OnNlcnZpY2VzIl19.Y4f82qnUNO8TuNGZ28VlDMLrsiRzKH_UHUUr6LsA2oqFLucqFdtodpccP3ay5NhITASW_3IwVGVOKRuqz6jBS4C1ALO6zPI7S0bQW0XhGSxmLz6hfTbD4kdpSWcM1RbTgZQ40m34UPGpeN_JM_MyjN2WRGlo26c_HbCDySkaSGelatOz4-IsyRzNCwEAdl-u0y6ngLDkvewy_JfNaI9CJ464gTR6BgKC2eQVdWmM-VF0c2_fzfSUXlChkKFwsL0iaOGOMj662IpXvTvrRTHuKposUiXfdaXwlupl4Eg12QzBl5NEbENVp3P8lle6-Rt2_ZXPcAZTASVGBE1hFBu0_Q
```

## Technical Specification

### Roles
 * **Public** : Can view the details of the environment services available in all the regions
 * **Services Manager** : Can view/edit/delete/update the details of the __services of all regions__
 * **Chief Officer**: Can view/edit/delete/update the details of the __all regions__.

### Database Models
**REGION**
- Id: Unique Id for a local region where the environment services are listed
- Name: Name of the local region
- City
- State
- Country
- RegionHead

**SERVICE**
- Region Id: Id of the region in which the service is available
- Service Id: Unique Id for the service
- Service Type: The type of service
- Service Name: Name of the Organisation
- Address
- email
- phone
- image
- website


## API End Points
**Region**
  * GET `/regions`  
    * Lists all regions and its details
    * Everyone has access 
    ```
    curl -X GET \
    https://udacity-environment-services.herokuapp.com/regions
    ```
  * GET `/regions/<region_id>`  
    * List details of a region
    * Everyone has access 
    ```
    curl -X GET \
    https://udacity-environment-services.herokuapp.com/regions/2
    ```  
  * POST `/regions` 
    * Add a new region and its details
    * Only Chief Officer has access
    * The region name should be UNIQUE
    ```
    curl \
    -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>'\
    -H 'Content-Type: application/json' \
    -d '{
    "name": "<INSERT UNIQUE REGION>",
    "city": "Chennai",
    "state": "Tamil Nadu",
    "country": "India",
    "regionhead": "Anitha"
    }'\
    -X POST \
    https://udacity-environment-services.herokuapp.com/regions
    ```  
  * PATCH `/regions/<region_id>`
    * Updates a region details
    * Only Chief Officer has access
    ```
    curl \
    -H "Authorization: Bearer <INSERT_YOUR_TOKEN>"\
    -H 'Content-Type: application/json' \
    -d '{
    "regionhead": "Anitha Karunakaran"
    }'\
    -X PATCH \
    https://udacity-environment-services.herokuapp.com/regions/2

    ```
  * DELETE `/regions/<region_id>`
    * Deletes a region
    * Only Chief Officer has access
    ```
    curl \
    -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>'\
    -X DELETE \
    https://udacity-environment-services.herokuapp.com/regions/2
    ```

**Services**
  * GET `/services`
    * Lists all services and its details
    * Everyone has access 
    ```
    curl -X GET \
    https://udacity-environment-services.herokuapp.com/services
    ```
  * GET `/services/<service_id>`
    * Gets the details of the specific service.
    * Everyone has access 
    ```
    curl -X GET \
    https://udacity-environment-services.herokuapp.com/services/2
    ```  
  * POST `/services`
    * Adds a new service and its details
    * Only Chief Officer and Service Manager has access
    ```
    curl \
    -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>'\
    -H 'Content-Type: application/json' \
    -d '{
      "name": "Save Trees",
      "type": "Tree Plantation Service",
      "address": "5, Kodambakkam, Chennai",
      "region_id": 2,
      "email": "info@savetrees.com",
      "phone": "911111111",
      "website": "www.savetrees.com" 
      }'\
    -X POST \
    https://udacity-environment-services.herokuapp.com/services
    ```
  * PATCH `/services`
    * Updates an existing service details
    * Only Chief Officer and Service Manager has access
    ```
    curl -X PATCH \
    https://udacity-environment-services.herokuapp.com/services/<service_id>\
    -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>\
    -H 'Content-Type: application/json' \
    -d '{
    "name": "Rain Harvesting"
    }'
  * DELETE `/services/<service_id>`
    * Deletes a service
    * Only Chief Officer and Service Manager has access
    ```
    curl \
    -H 'Authorization: Bearer <INSERT_YOUR_TOKEN>'\
    -X DELETE \
    https://udacity-environment-services.herokuapp.com/services/<service_id>
    ```

##Setting up Local environment
### Python Dependencies
The project requires Python 3.6
Using a virtual environment such as venv is recommended.  
```pip install -r requirements.txt```  
### Setting up Database
1. Create the Database  
```sudo -u postgres createdb envsrvdb```  
2. Point the DATABASE_URL environment variable to the local database
```DATABASE_URL=postgres://postgres:postgres@localhost:5432/envsvdb```  
3. Run flask migrate commands
```
flask db init  
flask db migrate  
flask db upgrade  
```
### Run the application
```
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=True
flask run
```
## Setting up and Running Unit Tests
1. Create the test database  
```sudo -u postgres createdb test_envsrvdb```
2. Setting TEST_DATABASE_URL Environment Variable  
The test database URL is present in .env file.  
   It can be overridden by changing the environment variable.  
`TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/test_envsrvdb`
3. Sample JWT of Chief Officer and Services Manager are available in setup_test_jwt.sh
   You can override them by setting the following 2 environment variables.
   ```
   CHIEF_OFFICER_JWT=<INSERT_JWT>
   SERVICES_MANAGER_JWT=<INSERT_JWT>
   ```
3. Run the Python Unit Test class
`py test_app.py`

