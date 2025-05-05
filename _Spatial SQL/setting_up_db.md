---
format: 
  html:
    toc: true
    page-layout: full
execute:
  echo: true
---


# Setting up a Spatial Database with Your Local Machine

In this tutorial, we will set up a spatial database using the PostGIS extension for PostgreSQL. We will use the `psql` command-line tool to create a new database, enable the PostGIS extension, and load spatial data into the database.

## Step 1: Install PostgreSQL and PostGIS

First, you need to install PostgreSQL and PostGIS on your system. You can download the installer for your operating system from the official websites:

- PostgreSQL: [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
- PostGIS: [https://postgis.net/install/](https://postgis.net/install/)

- Code for installing PostgreSQL and PostGIS on Ubuntu:
```bash
brew update
brew install postgresql postgresql-contrib postgis
```

`brew` is used to install, update, and manage packages on macOS.


## Step 2: Create a New Database

With PostgreSQL and PostGIS installed, you can now create a new database. Open Terminal and execute the following command:


```bash
createdb spatial_db

```
This command creates a new database named `spatial_db`. Feel free to replace `spatial_db` with any name you prefer.


## Step 3: Enable PostGIS Extension

To enable the PostGIS extension in your newly created database, execute the following command in Terminal:


```bash
psql -d spatial_db -c "CREATE EXTENSION postgis;"
```

This enables the PostGIS extension within the `spatial_db` database.


## Step 4: Load Spatial Data

To load spatial data into your database, use the `shp2pgsql` tool for importing shapefiles into a PostGIS-enabled database.

For instance, to import a shapefile named 'countries.shp' into the 'spatial_db' database, run the following command:

```bash

shp2pgsql -I -s 4326 countries.shp public.countries | psql -d spatial_db

```

This imports the 'countries.shp' shapefile into the 'spatial_db' database under the 'public.countries' table.


## Step 5: Verify the Database Setup

You can verify that the database setup is successful by connecting to the database using the `psql` command-line tool. Run the following command in the terminal:

```bash
psql -d spatial_db
```

This command connects to the 'spatial_db' database. You can run SQL queries to verify that the PostGIS extension is enabled and the spatial data is loaded correctly.

That's it! You have successfully set up a spatial database using the PostGIS extension for PostgreSQL. You can now use the database to perform spatial queries and analysis.

### Conventions to know about

- Port: A port is a communication endpoint used to identify specific processes or network services on a computer. PostgreSQL's default port is 5432. To connect to a database on a different port, you'd use the command:

    ```bash
    psql -h localhost -p 5433 -U postgres -d spatial_db
    ```

- User: The default user for PostgreSQL is `postgres`. You can specify a different user using the `-U` flag:

    ```bash
    psql -U myuser -d spatial_db
    ```

- Host: The default host for PostgreSQL is `localhost`. If your database is hosted on a different server, you can specify the host using the `-h` flag:

    ```bash
    psql -h myhost -d spatial_db
    ```
