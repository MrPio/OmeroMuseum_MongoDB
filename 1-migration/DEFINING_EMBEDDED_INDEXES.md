# Define indexes on embedded docs' id
Tickets are embedded inside visitors' docs. Events reference them. Thus, tickets must have a ID to be retrievable.

First I've added a `_id` field to ticket embedded docs, with value _ObjectId_. Then, I defined an index on such a field.

## Performance improvements
Before defining the index:
```python
db.visitors.find({"tickets._id": ObjectId("<OID>")}).explain()
```

winning plan = `COLLSCAN`. `docsExamined = 50`. `totalKeysExamined = 0`. **Query scanned whole collection.**

Then,
```python
db.visitors.create_index({ "tickets._id": 1 })
```

winning plan = `IXSCAN` -> `FETCH`. `indexName = tickets._id_1`. `totalKeysExamined = 1`. `totalDocsExamined = 1`. **Query scanned 1 document.**

FETCH appears because Mongo must read the full document after the index gives the matching key.

## Index update

MongoDB maintains indexes automatically on writes.