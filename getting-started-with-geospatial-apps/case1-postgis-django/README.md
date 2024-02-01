# GeoDjango

The following is a template of a simple GeoDjango App. GeoDjango is Django with geospatial capabilities using PostGIS and GDAL.

## Components

- PostGIS
- Django
- GDAL

## Setup

1. Run the application.
   ```
   docker compose up
   ```
2. Open your browser and go to `http://localhost:7500/admin/`
3. Enter the following credentials:
   ```
   username: admin@sample.com
   password: adminpassword012
   ```
4. Login to the `geodjango` container.
   ```
   docker exec -it geodjango bash
   python manage.py load_geo
   ```
5. Get the authorization token by going to `admin > Tokens`. Copy the token.
6. Run the following in your terminal that is logged into the container.
   ```
   curl -X GET -H "Authorization: Token <token>" http://localhost:8000/geo/
   ```

## Activity

- Add a new feature using the Django Admin
- Analyse the structure of the app
- Play around with CRUD endpoint with Django Rest Framework
