# Omero Museum MongoDB
Design and implementation of a MongoDB database for the management of the State Omero Museum


## How to load the database
`mongodump` from [*MongoDB Database Tools*](https://www.mongodb.com/docs/database-tools/) was used to dump the database right after MySQL migration. Therefore, you need to load it using `mongorestore`, available in the same collection of tools.

```sh
mongorestore --host localhost:27017 --db omero_museum  "backup/1_after_migration/"
```

Now you're ready to follow the chronological order of the notebooks in this repository.