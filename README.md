# EnvironmentServices
## About the application
Environment Services is an application which lists the environment services available in various areas

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


### API End Points
* Region ( /regions )
  * GET /regions - Lists all regions and its details
  * GET /regions/<region_id> - Gets the details of the specific region and the services available in the region.
  * PUT /regions - Adda a new region and its details
  * PATCH /regions - Updates a region details
  * DELETE - Deletes a region
* Services ( /services )
  * GET /services - Lists all regions and its details
  * GET /services/<service_id> - Gets the details of the specific service.
  * PUT /services - Adds a new service and its details
  * PATCH /services - Updates an existing service details
  * DELETE - Deletes a service

##Setting up Local environment
Point the DATABASE_URL environment variable to the local database
In Linux:
DATABASE_URL=postgres://postgres:postgres@localhost:5432/envsvdb
In Windows:
set DATABASE_URL=postgres://postgres:postgres@localhost:5432/envsrvdb

flask db init
flask db migrate
flask db upgrade

