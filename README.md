# Environment Services
## Motivation for this application
Currently, our earth is facing a severe climate and environment crisis.
Though there are organisations available in many localities which can be used for remediating the problems to some extent, people are not aware of them. Hence, there is a need to consolidate these in a single location.
The chief of the application can decide what all regions have to be listed. There will be a head for each region, who can be contacted about the services listed.
The services manager or the chief can add the services(Waste Management/Tree Plantation/Water Conservation) available in various regions.
The website/phone and other contact details of the services will also be available to the public.

## About the application
Environment Services is a **backend application** which lists the environment services (Waste Management, Tree Plantation, Ground Water Recharge, Lake Cleaning etc.) available in various regions.
The backend is designed to work for two types of users: Chief officers and Service Managers. 
The available services in various regions can be viewed by public users.

The Chief Officer of Environment Services can add/modify/delete regions where services are listed.  
The Services Manager cannot modify regions but can add the services available in all the regions.  
Public can view all the regions where Environment Services are available and all the services.

The application is hosted in Heroku: [https://udacity-environment-services.herokuapp.com/services](https://udacity-environment-services.herokuapp.com/services)  
Your JWT can be obtained from the Browser's address bar(as access_token parameter) after clicking [The Auth0 redirect URL](https://fsndanikaruna.us.auth0.com/authorize?audience=envsrv&response_type=token&client_id=nGhgfyP2tBCsMHFGhqr3FvtsawagHfhu&redirect_uri=https://udacity-environment-services.herokuapp.com/regions)  


**Latest JWT for Test**
``` 
CHIEF_OFFICER_JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRXdG5QNHI5X3RPbUR4V3ZhQk9FRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRhbmlrYXJ1bmEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNWE3NjAxNDRiNjlmMDA3MGRiZjU1ZiIsImF1ZCI6ImVudnNydiIsImlhdCI6MTYxNjU0Mjc5NSwiZXhwIjoxNjE2NjI5MTk1LCJhenAiOiJuR2hnZnlQMnRCQ3NNSEZHaHFyM0Z2dHNhd2FnSGZodSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnJlZ2lvbnMiLCJkZWxldGU6c2VydmljZXMiLCJwYXRjaDpyZWdpb25zIiwicGF0Y2g6c2VydmljZXMiLCJwb3N0OnJlZ2lvbnMiLCJwb3N0OnNlcnZpY2VzIl19.Qg8Nbb6R0ya66647Az77l2RyaDVHDTndZi2348d1kKpyozu7fa5KBbfkjciz1eaWA0AoPtWDCkiDlrvAhCzo2d30QRDzDdpIrm6dT-qRibF-CXffGWSaP19Mt7LhboKT0CFGSOhSP82_1MLGap7g_Y9Cg6KgWM5IO8MymBO9-fW9JKbiHytCvyaxj3nTeU3w_qm_RMF8kFz9Ji3CytaUkdAX6Xo3eYVfejbzfWM3Pd8gd_kDejGv83w18Etwu2vOJ1KXs_zzSzdBkqAhIH7pWogGkeyEnCJOTMd4cAnMFNORJ-Y_xVHluN7GYLYzgWarkLWwIsvIgsP0gLGPn1TtXw
SERVICES_MANAGER_JWT=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImRXdG5QNHI5X3RPbUR4V3ZhQk9FRiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRhbmlrYXJ1bmEudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNWE3NjhiY2EzNzNiMDA3MTJmMDRkZCIsImF1ZCI6ImVudnNydiIsImlhdCI6MTYxNjU0MzIzOCwiZXhwIjoxNjE2NjI5NjM4LCJhenAiOiJuR2hnZnlQMnRCQ3NNSEZHaHFyM0Z2dHNhd2FnSGZodSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOnNlcnZpY2VzIiwicGF0Y2g6c2VydmljZXMiLCJwb3N0OnNlcnZpY2VzIl19.OXm3VO7pJ3qNhF2KuS7qfZiCYntsMW2yUPprqh5MpgqEZcBIoukhrmo1AFOWCB8kt3S-WsxrFI5vJzbLM2pgu1wk-9CxGKY_VIYxgWypgGWPOtlaOK1YlSO-h1lyw-QEtX6H5Qs7Ko8qSjlTn7A9c0UJJGfSbMhRjRQAOVhRi4YPrZHQHz1j1RZiJxs0Nnuh1V6DUZY4fMeDD1i32DIAQH5TyxRUyrUJTBbWF5rd8D-ap_otTY7dmh3-U1tuMbIg7V3YaFwz4j_NNVHUOCf-YxKNFnPg-MRmH6Uy9y_Q9pe4YjK9X02d8Pn1XTSB7rBkSKmsoXBKz2UNXrwm3nlSKg
```

## Getting Started
### Python Dependencies
The project requires Python 3.6 or Higher. Using a virtual environment such as venv is recommended.  
```pip install -r requirements.txt```  
This will install all the required packages to your virtual environment to work with the project.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  - A microservices framework to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) - Python ORM Toolkit 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) - handle cross origin requests from frontend server. 

### Setting up Database locally
Postgres 10.0 is the database used for local development. The steps 
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

### Running the application
In Linux:
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
In Windows:
```
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```
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
  Foreign Key of Region Table's Id
- Service Id: Unique Id for the service
- Service Type: The type of service
- Service Name: Name of the Organisation
- Address
- email
- phone
- image
- website

##Authentication and Authorization
Application security is provided through RBAC configurations in Auth0.  
The following are some key parameters in Auth0:   
- API_AUDIENCE=envsrv  
- AUTH0_DOMAIN=fsndanikaruna.us.auth0.com  

Your JWT can be obtained from the Browser's address bar(as access_token parameter) on clicking [this Auth0 redirect URL](https://fsndanikaruna.us.auth0.com/authorize?audience=envsrv&response_type=token&client_id=nGhgfyP2tBCsMHFGhqr3FvtsawagHfhu&redirect_uri=https://udacity-environment-services.herokuapp.com/regions)  

### Roles
The following are the different roles who can use the application
 * **Public** : Can __only view__ the details of the environment services available in all the regions
 * **Services Manager** : Can __view/edit/delete/update__ the details of the __services of all regions__
 * **Chief Officer**: Can __view/edit/delete/update__ the details of the __all regions__.


## API End Points

Most of the API End Points Require JWT Authorization.  

Sample JWT of Chief Officer and Services Manager are available in 'setup_jwt.sh'  
You can use them by executing ```source setup_jwt.sh```   
(or)  
You can override them by setting the following 2 environment variables.  
Your JWT can be obtained from the Browser's address bar(as access_token parameter) after logging in [this Auth0 redirect URL](https://fsndanikaruna.us.auth0.com/authorize?audience=envsrv&response_type=token&client_id=nGhgfyP2tBCsMHFGhqr3FvtsawagHfhu&redirect_uri=https://udacity-environment-services.herokuapp.com/regions)
   ```
   CHIEF_OFFICER_JWT=<INSERT_JWT>
   SERVICES_MANAGER_JWT=<INSERT_JWT>
   ```
**Region**
  * GET `/regions`  
    * Lists all regions and its details
    * Everyone has access 
    ```
    curl -X GET \
    https://udacity-environment-services.herokuapp.com/regions
    ```
    Sample Success Response:  
    ```
    {
        "regions": [
            {
                "city": "Chennai",
                "country": "India",
                "name": "West Mambalam",
                "regionhead": "Anitha",
                "state": "Tamil Nadu"
            },
            {
                "city": "Chennai",
                "country": "India",
                "name": "Vadapalani",
                "regionhead": "Amutha",
                "state": "Tamil Nadu"
            }
        ],
        "success": true
    }
    ```
  * GET `/regions/<region_id>`  
    * List details of a region
    * Everyone has access 
    ```
    curl -X GET \
    https://udacity-environment-services.herokuapp.com/regions/2
    ```  
    Sample Success Response:
    ```
    {
    "region": {
        "city": "Chennai",
        "country": "India",
        "id": 1,
        "name": "West Mambalam",
        "regionhead": "Anitha",
        "state": "Tamil Nadu"
        },
    "success": true
    } 
    ```
  * POST `/regions` 
    * Add a new region and its details
    * Only Chief Officer has access
    * The region name should be UNIQUE
    * Region Name, City, State, Country and RegionHead values are mandatory.  

    Sample Request:

    ```
    curl -X POST \
      https://udacity-environment-services.herokuapp.com/regions \
      -H "Authorization: Bearer $CHIEF_OFFICER_JWT" \
      -H 'Content-Type: application/json' \
      -d '{
        "name": "<INSERT UNIQUE NAME>",
        "city": "Chennai",
        "state": "Tamil Nadu",
        "country": "India",
        "regionhead": "Yamini"
        }'
    ```  
    Sample Response:
    ```
    {"created":8,"success":true}
    ```
  * PATCH `/regions/<region_id>`
    * Updates a region details
    * Only Chief Officer has access
    * Request Body contains at least one of Name, city, state, country or regionhead  
    * At least one of the fields (Name/City/State/Country/RegionHead) should be provided for update
    ```
      curl -X PATCH \
      https://udacity-environment-services.herokuapp.com/regions/<INSERT_REGION_ID> \
      -H "Authorization: Bearer $CHIEF_OFFICER_JWT" \
      -H 'Content-Type: application/json' \
      -d '{
        "name": "Jainagar",
        "city": "Bangalore",
        "state": "Karnataka",
        "country": "India",
        "regionhead": "Lavanya"
        }'
    ```
    Sample Success Response:
    ```
    {"success":true,"updated":7}
    ```
  * DELETE `/regions/<region_id>`
    * Deletes a region
    * Only Chief Officer has access
    ```
        curl \
        -H "Authorization: Bearer $CHIEF_OFFICER_JWT" \
        -X DELETE \
        https://udacity-environment-services.herokuapp.com/regions/<INSERT_REGION_ID>
    ```  
    Sample Success Response:
    ```
       {"deleted":8,"success":true} 
    ```

**Services**
  * GET `/services`
    * Lists all services and its details
    * Everyone has access 
    ```
    curl -X GET \
    https://udacity-environment-services.herokuapp.com/services
    ```
    Sample Success Response:
    ``` 
    {
       "services": 
       [      
          {
             "address": "3 New Tamil Nadu",
             "email": "info@ssrms.com",
             "id": 2,
             "image": null,
             "name": "New Resource Management Services",
             "phone": "5688928349",
             "region_id": 1,
             "type": "Resource Management Service",
             "website": "www.ssrms.com"
          },      
          {
             "address": "3, ABC Street, West Mambalam, Tamil Nadu",
             "email": "info@ssrms.com",
             "id": 3,
             "image": null,
             "name": "Test1 Resource Management Services",
             "phone": "911112223344",
             "region_id": 1,
             "type": "Resource Management Service",
             "website": "www.ssrms.com"
          }
       ],
       "success": true
    }
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
        curl -X POST \
        https://udacity-environment-services.herokuapp.com/services \
        -H "Authorization: Bearer $SERVICES_MANAGER_JWT" \
        -H 'Content-Type: application/json' \
        -d '{
              "name": "Plant Trees",
              "type": "Tree Plantation Service",
              "address": "5, Kodambakkam, Chennai",
              "region_id": 2,
              "email": "info@planttrees.com",
              "phone": "911111111",
              "website": "www.planttrees.com" 
               }'
    ```
    Sample Response:
    ``` 
        {"created":6,"success":true}
    ```
  * PATCH `/services`
    * Updates an existing service details
    * Request body has at least one of name, type, address, region_id, email, phone, website or image  
    * Only Chief Officer and Service Manager has access
    ```
        curl -X PATCH \
        https://udacity-environment-services.herokuapp.com/services/<SERVICE_ID> \
        -H "Authorization: Bearer $SERVICES_MANAGER_JWT" \
        -H 'Content-Type: application/json' \
        -d '{
              "name": "More Trees",
              "type": "Tree Plantation Service",
              "address": "5, Kodambakkam, Chennai",
              "region_id": 2,
              "email": "info@planttrees.com",
              "phone": "222222222",
              "website": "www.planttrees.com" 
               }'
    ```
    Sample Success Response:
    ``` 
        {"success":true,"updated":6}
    ```
  * DELETE `/services/<service_id>`
    * Deletes a service
    * Only Chief Officer and Service Manager has access
    ```
    curl \
       -H "Authorization: Bearer $SERVICES_MANAGER_JWT" \
        -X DELETE \
        https://udacity-environment-services.herokuapp.com/services/<service_id>
    ```
    Sample Success Response:
    ``` 
        {"success":true,"deleted":6}
    ```
## Setting up and Running Unit Tests Locally
1. Create the test database  
```sudo -u postgres createdb test_envsrvdb```
2. Setting TEST_DATABASE_URL Environment Variable  
The test database URL is present in .env file.  
   It can be overridden by changing the environment variable.  
`TEST_DATABASE_URL=postgresql://postgres:postgres@localhost:5432/test_envsrvdb`
3. Sample JWT of Chief Officer and Services Manager are available in setup_jwt.sh  
   You can use them executing ```source setup_jwt.sh```   
   You can override them by setting the following 2 environment variables.
   ```
   CHIEF_OFFICER_JWT=<INSERT_JWT>
   SERVICES_MANAGER_JWT=<INSERT_JWT>
   ```
3. Run the Python Unit Test class
`py test_app.py`

##Deploying the Application on Heroku
[Heroku](https://www.heroku.com/platform) is a cloud platform where developers host applications, databases and other services in several languages.
 Developers use Heroku to deploy, manage, and scale applications. It is easy and flexible to use. It’s almost as straightforward as pushing a repository to Github, plus a few extra commands.
1. Create a Heroku Account
2. Install the [Heroku CLI](https://devcenter.heroku.com/articles/getting-started-with-python#set-up)
3. After Installation of Heroku CLI, run ```heroku login``` from shell or command prompt and login using your credentials
4. From your project's local Git Repository, run ```heroku create udacity-environment-services```
When you create an app, a git remote (called heroku) is also created and associated with your local git repository.
5. Create a Heroku Free Postgres Database using ```heroku addons:create heroku-postgresql:hobby-dev --app udacity-environment-services```
6. Deploy your code using ```git push heroku main ```
7. The environment variables set in Heroku can be listed by: ```heroku config --app udacity-environment-services```
8. The environment variables can be set from UI or from command shell like ```heroku config:set FLASK_APP=app --app udacity-environment-services```
9. [Procfile](Procfile) in this project has code to flask upgrade the database and to start the gunicorn server
10. The Heroku postgres database can be accessed locally using ```heroku pg:psql --app udacity-environment-services```
11. Sometimes, Heroku Postgres Database might have to be re-initialised. You can do this by  
    ```
    heroku pg:reset
    heroku run flask db upgrade --app udacity-environment-services 
    ```
12. The bash terminal of the server in Heroku can be accessed using ```heroku run bash --app udacity-environment-services```
Finally the application can opened in browser using ```heroku open --app udacity-environment-services```
