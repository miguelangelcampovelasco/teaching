[TOC]

# Prerequisites

* Install MongoDB Compass (Community Edition Stable)  from [https://www.mongodb.com/download-center/compass](https://www.mongodb.com/download-center/compass)
* Install Anaconda (Python 3.7 version) from [anaconda download](https://www.anaconda.com/distribution/#download-section) following [anaconda installation](https://docs.anaconda.com/anaconda/install/)
* Install MongoDB python driver `pymongo`,  open Anaconda Prompt for windows or Terminal for MacOS/Linux, exercute `pip install -U pymongo`


# Introduction to MongoDB

MongoDB is a leading open-source NoSQL database that is written in C++. This tutorial will give the reader a better understanding of MongoDB concepts.

## The SQL vs. NoSQL Difference

SQL databases use Structured Query Language(SQL) in defining and manipulating data. When using SQL, we need a Relational Database Management System(RDBMS) server such as SQL Server, MySQL server or MS Access. Data in RDBMS is stored in database objects called tables. A table is a collection of related data entries, and it consists of columns and rows.

A NoSQL database has a dynamic schema for unstructured data. In NoSQL, data is stored in several ways: it can be column-oriented, document-oriented, graph-based or organized as a key-value store. A NoSQL database has the following advantages:

*   Documents can be created without having to first define their structure
*   Each document can have its own unique structure
*   The syntax can vary from database to database
*   Large volumes of structured, semi-structured, and unstructured data
*   Object-oriented programming that is easy to use and flexible
*   It is horizontally scalable

## NoSQL Database Types

The following are the different types of NoSQL databases:

*   **Document databases** pair each key with a complex data structure known as a _document_. A document is a set of key-value pairs. MongoDB is an example of a document store database. A group of MongoDB documents is known as a collection. This is the equivalent of an RDBMS table.
    
*   **Graph stores** are used to store information about networks of data, for instance, social connections. Graph stores include Neo4J and Giraph.
    
*   **Key-value stores** databases store every single item in the database as a key together with its value. Examples of key-value stores are Riak and Berkeley DB. Some key-value stores, such as Redis, allow each value to have a type, such as an _integer_, which adds functionality.
    
*   **Wide-column** stores such as Cassandra and HBase are optimized for queries over large datasets, and store columns of data together, instead of rows.

## Document Database
MongoDB is a document database designed for ease of development and scaling.  
A record in MongoDB is a document, which is a data structure composed of field and value pairs. MongoDB documents are similar to JSON objects. The values of fields may include other documents, arrays, and arrays of documents.

![1567306477-74b398457ab57bd38be0c517383c73ce](/home/hao/work/teaching/big_data/mongodb/1567306477-74b398457ab57bd38be0c517383c73ce.svg)

The advantages of using documents are:

* Documents (i.e. objects) correspond to native data types in many programming languages.

* Embedded documents and arrays reduce need for expensive joins.

* Dynamic schema supports fluent polymorphism.

### Collection overview
MongoDB stores documents in [collections](https://docs.mongodb.com/manual/core/databases-and-collections/#collections). Collections are analogous to tables in relational databases. A collection exists within a single database. Collections do not enforce a schema. Documents within a collection can have different fields. Typically, all documents in a collection are of similar or related purpose.

### Document overview
A document is a set of key-value pairs. Documents have dynamic schema. Dynamic schema means that documents in the same collection do not need to have the same set of fields or structure, and common fields in a collection's documents may hold different types of data.

### Comparing MongoDB to RDBMS
In order to get a thorough understanding of the terms used in MongoDB, we'll compare them with the equivalent in RDBMS.

| RDBMS | MongoDB |
| --- | --- |
| Database | Database |
| Table | Collection |
| Row | Document |
| Column | Field |
| Primary Key | Primary Key |
| Table Join | Embedded Documents |

###  Key features

#### High Performance

MongoDB provides high performance data persistence. In particular,

*   Support for embedded data models reduces I/O activity on database system.
*   Indexes support faster queries and can include keys from embedded documents and arrays.

#### Rich Query Language

MongoDB supports a rich query language to support [read and write operations (CRUD)](https://docs.mongodb.com/manual/crud/) as well as:

*   [Data Aggregation](https://docs.mongodb.com/manual/core/aggregation-pipeline/)
*   [Text Search](https://docs.mongodb.com/manual/text-search/) and [Geospatial Queries](https://docs.mongodb.com/manual/tutorial/geospatial-tutorial/).

#### High Availability

MongoDB’s replication facility, called [replica set](https://docs.mongodb.com/manual/replication/), provides:

*   _automatic_ failover and
*   data redundancy.

A [replica set](https://docs.mongodb.com/manual/replication/) is a group of MongoDB servers that maintain the same data set, providing redundancy and increasing data availability.

#### Horizontal Scalability

MongoDB provides horizontal scalability as part of its _core_ functionality:

*   [Sharding](https://docs.mongodb.com/manual/sharding/#sharding-introduction) distributes data across a cluster of machines.
*   Starting in 3.4, MongoDB supports creating [zones](https://docs.mongodb.com/manual/core/zone-sharding/#zone-sharding) of data based on the [shard key](https://docs.mongodb.com/manual/reference/glossary/#term-shard-key). In a balanced cluster, MongoDB directs reads and writes covered by a zone only to those shards inside the zone. See the [Zones](https://docs.mongodb.com/manual/core/zone-sharding/#zone-sharding) manual page for more information.

#### Support for Multiple Storage Engines

MongoDB supports [multiple storage engines](https://docs.mongodb.com/manual/core/storage-engines/):

*   [WiredTiger Storage Engine](https://docs.mongodb.com/manual/core/wiredtiger/) (including support for [Encryption at Rest](https://docs.mongodb.com/manual/core/security-encryption-at-rest/))
*   [In-Memory Storage Engine](https://docs.mongodb.com/manual/core/inmemory/)

In addition, MongoDB provides pluggable storage engine API that allows third parties to develop storage engines for MongoDB.

### Documents
MongoDB stores data records as BSON documents. BSON is a binary representation of [JSON](https://docs.mongodb.com/manual/reference/glossary/#term-json) documents, though it contains more data types than JSON. For the BSON spec, see [bsonspec.org](http://bsonspec.org/). See also [BSON Types](https://docs.mongodb.com/manual/reference/bson-types/).

![1567306477-74b398457ab57bd38be0c517383c73ce](/home/hao/work/teaching/big_data/mongodb/1567306477-74b398457ab57bd38be0c517383c73ce.svg)

#### Document Structure

MongoDB documents are composed of field-and-value pairs and have the following structure:

```javascript
{
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}
```

The value of a field can be any of the BSON [data types](https://docs.mongodb.com/manual/reference/bson-types/), including other documents, arrays, and arrays of documents. For example, the following document contains values of varying types:

```javascript
var mydoc = {
               _id: ObjectId("5099803df3f4948bd2f98391"),
               name: { first: "Alan", last: "Turing" },
               birth: new Date('Jun 23, 1912'),
               death: new Date('Jun 07, 1954'),
               contribs: [ "Turing machine", "Turing test", "Turingery" ],
               views : NumberLong(1250000)
            }
```

The above fields have the following data types:

*   `_id` holds an [ObjectId](https://docs.mongodb.com/manual/reference/bson-types/#objectid).
*   `name` holds an _embedded document_ that contains the fields `first` and `last`.
*   `birth` and `death` hold values of the _Date_ type.
*   `contribs` holds an _array of strings_.
*   `views` holds a value of the _NumberLong_ type.

##### Field Names

Field names are strings.

[Documents](#) have the following restrictions on field names:

*   The field name `_id` is reserved for use as a primary key; its value must be unique in the collection, is immutable, and may be of any type other than an array.
*   Field names **cannot** contain the `null` character.
*   Top-level field names **cannot** start with the dollar sign (`$`) character.
    Otherwise, starting in MongoDB 3.6, the server permits storage of field names that contain dots (i.e. `.`) and dollar signs (i.e. `$`).
    **Important**
    Until support is added in the query language, the use of `$` and `.` in field names is not recommended and is not supported by the official MongoDB drivers.

BSON documents may have more than one field with the same name. Most [MongoDB interfaces](https://docs.mongodb.com/ecosystem/drivers), however, represent MongoDB with a structure (e.g. a hash table) that does not support duplicate field names. If you need to manipulate documents that have more than one field with the same name, see the [driver documentation](https://docs.mongodb.com/ecosystem/drivers) for your driver.

Some documents created by internal MongoDB processes may have duplicate fields, but _no_ MongoDB process will _ever_ add duplicate fields to an existing user document.

##### Field Value Limit

For [indexed collections](https://docs.mongodb.com/manual/indexes/), the values for the indexed fields have a [`Maximum Index Key Length`](https://docs.mongodb.com/manual/reference/limits/#Index-Key-Limit "Index Key Limit"). See [`Maximum Index Key Length`](https://docs.mongodb.com/manual/reference/limits/#Index-Key-Limit "Index Key Limit") for details.

#### Dot Notation

MongoDB uses the _dot notation_ to access the elements of an array and to access the fields of an embedded document.

##### Arrays

To specify or access an element of an array by the zero-based index position, concatenate the array name with the dot (`.`) and zero-based index position, and enclose in quotes:

```javascript
"<array>.<index>"
```

For example, given the following field in a document:

```javascript
{
   ...
   contribs: [ "Turing machine", "Turing test", "Turingery" ],
   ...
}
```

To specify the third element in the `contribs` array, use the dot notation `"contribs.2"`.

For examples querying arrays, see:
*   [Query an Array](https://docs.mongodb.com/manual/tutorial/query-arrays/)
*   [Query an Array of Embedded Documents](https://docs.mongodb.com/manual/tutorial/query-array-of-documents/)

See also
*   [`$[]`](https://docs.mongodb.com/manual/reference/operator/update/positional-all/#up._S_[] "$[]") all positional operator for update operations,
*   `$[/<identifier/>]` filtered positional operator for update operations,
*   [`$`](https://docs.mongodb.com/manual/reference/operator/update/positional/#up._S_ "$") positional operator for update operations,
*   [`$`](https://docs.mongodb.com/manual/reference/operator/projection/positional/#proj._S_ "$") projection operator when array index position is unknown
*   [Query an Array](https://docs.mongodb.com/manual/tutorial/query-arrays/#read-operations-arrays) for dot notation examples with arrays.

##### Embedded Documents

To specify or access a field of an embedded document with dot notation, concatenate the embedded document name with the dot (`.`) and the field name, and enclose in quotes:

```javascript

"<embedded document>.<field>"
```

For example, given the following field in a document:

```javascript
{
   ...
   name: { first: "Alan", last: "Turing" },
   contact: { phone: { type: "cell", number: "111-222-3333" } },
   ...
}
```

*   To specify the field named `last` in the `name` field, use the dot notation `"name.last"`.
*   To specify the `number` in the `phone` document in the `contact` field, use the dot notation `"contact.phone.number"`.

For examples querying embedded documents, see:

*   [Query on Embedded/Nested Documents](https://docs.mongodb.com/manual/tutorial/query-embedded-documents/)
*   [Query an Array of Embedded Documents](https://docs.mongodb.com/manual/tutorial/query-array-of-documents/)

#### Document Limitations

Documents have the following attributes:

##### Document Size Limit

The maximum BSON document size is 16 megabytes.

The maximum document size helps ensure that a single document cannot use excessive amount of RAM or, during transmission, excessive amount of bandwidth. To store documents larger than the maximum size, MongoDB provides the GridFS API. See [`mongofiles`](https://docs.mongodb.com/manual/reference/program/mongofiles/#bin.mongofiles "bin.mongofiles") and the documentation for your [driver](https://docs.mongodb.com/ecosystem/drivers) for more information about GridFS.

##### Document Field Order

MongoDB preserves the order of the document fields following write operations _except_ for the following cases:

*   The `_id` field is always the first field in the document.
*   Updates that include [`renaming`](https://docs.mongodb.com/manual/reference/operator/update/rename/#up._S_rename "$rename") of field names may result in the reordering of fields in the document.

##### The `_id` Field

In MongoDB, each document stored in a collection requires a unique [_id](https://docs.mongodb.com/manual/reference/glossary/#term-id) field that acts as a [primary key](https://docs.mongodb.com/manual/reference/glossary/#term-primary-key). If an inserted document omits the `_id` field, the MongoDB driver automatically generates an [ObjectId](https://docs.mongodb.com/manual/reference/bson-types/#objectid) for the `_id` field.

This also applies to documents inserted through update operations with [upsert: true](https://docs.mongodb.com/manual/reference/method/db.collection.update/#upsert-parameter).

The `_id` field has the following behavior and constraints:
*   By default, MongoDB creates a unique index on the `_id` field during the creation of a collection.
*   The `_id` field is always the first field in the documents. If the server receives a document that does not have the `_id` field first, then the server will move the field to the beginning.
*   The `_id` field may contain values of any [BSON data type](https://docs.mongodb.com/manual/reference/bson-types/), other than an array.

### BSON
[BSON](https://docs.mongodb.com/manual/reference/glossary/#term-bson) is a binary serialization format used to store documents and make remote procedure calls in MongoDB. The BSON specification is located at [bsonspec.org](http://bsonspec.org/).

Each BSON type has both integer and string identifiers as listed in the following table:


| Type | Number | Alias | Notes |
| --- | --- | --- | --- |
| Double | 1 | “double” |   |
| String | 2 | “string” |   |
| Object | 3 | “object” |   |
| Array | 4 | “array” |   |
| Binary data | 5 | “binData” |   |
| Undefined | 6 | “undefined” | Deprecated. |
| ObjectId | 7 | “objectId” |   |
| Boolean | 8 | “bool” |   |
| Date | 9 | “date” |   |
| Null | 10 | “null” |   |
| Regular Expression | 11 | “regex” |   |
| DBPointer | 12 | “dbPointer” | Deprecated. |
| JavaScript | 13 | “javascript” |   |
| Symbol | 14 | “symbol” | Deprecated. |
| JavaScript (with scope) | 15 | “javascriptWithScope” |   |
| 32-bit integer | 16 | “int” |   |
| Timestamp | 17 | “timestamp” |   |
| 64-bit integer | 18 | “long” |   |
| Decimal128 | 19 | “decimal” | New in version 3.4. |
| Min key | -1 | “minKey” |   |
| Max key | 127 | “maxKey” |   |

You can use these values with the [`$type`](https://docs.mongodb.com/manual/reference/operator/query/type/#op._S_type "$type") operator to query documents by their BSON type. The [`$type`](https://docs.mongodb.com/manual/reference/operator/aggregation/type/#exp._S_type "$type") aggregation operator returns the type of an [operator expression](https://docs.mongodb.com/manual/meta/aggregation-quick-reference/#agg-quick-ref-operator-expressions) using one of the listed BSON type strings.

To determine a field’s type, see [Check Types in the mongo Shell](https://docs.mongodb.com/manual/core/shell-types/#check-types-in-shell).

If you convert BSON to JSON, see the [Extended JSON](https://docs.mongodb.com/manual/reference/mongodb-extended-json/) reference.



# MongoDB  GUI client
[MongoDB Compass](https://docs.mongodb.com/compass/current/) is the GUI for MongoDB. The following tutorial uses MongoDB Compass to  connect to MonogoDB server and  perform mutiple operations.

### MongoDB Connect

1. Install MongoDB Compass (Community Edition Stable)  from [https://www.mongodb.com/download-center/compass](https://www.mongodb.com/download-center/compass)

2. Open MongoDB Compass, log in with your account:
   username: `<NetID>`, password:`<NetID>123`

![2019-09-01_11-14](/home/hao/work/teaching/big_data/mongodb/2019-09-01_11-14.png)

### MongoDB Create Database

1. At the bottom of left sidebar, click '+' to create a new database.

![2019-09-01_12-00](/home/hao/work/teaching/big_data/mongodb/2019-09-01_12-00.png)

![2019-09-01_12-00_1](/home/hao/work/teaching/big_data/mongodb/2019-09-01_12-00_1.png)

2. Permission of your account '<NetID>' is limited to Northwind (read) and bigdata_<NetID>(read and write), so you can not create a new database here.

### MongoDB Create Collection

1. Choose the database `bigdata_<NetID>`.

2. Choose `CREATE COLLECTION`, input `inventory` as Collection Name.

![2019-09-01_15-53](/home/hao/work/teaching/big_data/mongodb/2019-09-01_15-53.png)

![2019-09-01_15-53_1](/home/hao/work/teaching/big_data/mongodb/2019-09-01_15-53_1.png)



### MongoDB Insert

1. From the **Collections** tab, click the `test_collection` collection.

   ![2019-09-01_15-56](/home/hao/work/teaching/big_data/mongodb/2019-09-01_15-56.png)

2. Insert the following [document](https://docs.mongodb.com/manual/core/document/) by entering the `fields` and `values`, then selecting the appropriate types from the dropdowns. Add fields by clicking the last line number, then clicking **Add Field After ….**

```javascript
{ item: "journal", qty: 25, status: "A", 
    size: { h: 14, w: 21, uom: "cm" }, tags: [ "blank", "red" ] }
```

*   For `Object` types, add nested fields by clicking the last field’s number and selecting Add Field After ….
*   For `Array` types, add additional elements to the array by clicking the last element’s line number and selecting Add Array Element After ….

![1567365708-a0ba4b9f70979c77f7bbdd574b7b71c7](/home/hao/work/teaching/big_data/mongodb/1567365708-a0ba4b9f70979c77f7bbdd574b7b71c7.png)

![1567365708-58d28db3cee8a5546fc392c7cdf64a6b](/home/hao/work/teaching/big_data/mongodb/1567365708-58d28db3cee8a5546fc392c7cdf64a6b.png)

![2019-09-01_12-35](/home/hao/work/teaching/big_data/mongodb/2019-09-01_12-35.png)

### MongoDB Query

We will perform query on `inventory`. Choose **bigdata_<NetID>**  ->  **inventory**

* ##### Match specific equality conditions

pass a [query filter document](https://docs.mongodb.com/manual/core/document/#document-query-filter) to the Filter with the `<field>: <value>` of the desired documents. The following query filter document selects all documents where the `status` equals `"D"` from the `inventory` collection:

Copy the following filter into the Compass query bar and click Find:

```javascript
{ status: "D" }
```

![2019-09-01_16-01](/home/hao/work/teaching/big_data/mongodb/2019-09-01_16-01.png)

* #### Match embedded documents

Equality matches on the whole embedded document require an _exact_ match of the specified `<value>` document, including the field order. For example, the following query selects all documents where the field `size` equals the document `{ h: 14, w: 21, uom: "cm" }`:

  ```javascript
  { size: { h: 14, w: 21, uom: "cm" } }
  ```

![2019-09-01_16-04](/home/hao/work/teaching/big_data/mongodb/2019-09-01_16-04.png)

The following example selects all documents where the field `uom` nested in the `size` field equals the string value `"in"`:

```javascript
{ "size.uom": "in" }
```

The following example queries for all documents where `tags` is an array that contains the string `"red"` as one of its elements:

```javascript
{ tags: "red" }
```

The following example queries for all documents where the field `tags` value is an array with exactly two elements, `"red"` and `"blank"`, in the specified order:

```javascript
{ tags: ["red", "blank"] }
```

*  #### Specify Conditions Using Query Operators

A [query filter document](https://docs.mongodb.com/manual/core/document/#document-query-filter) can use the [query operators](https://docs.mongodb.com/manual/reference/operator/query/#query-selectors) to specify conditions in the following form:

```javascript
{ <field1>: { <operator1>: <value1> }, ... }
```

The following example retrieves all documents from the `inventory` collection where `status` equals either `"A"` or `"D"`:

```javascript
{ status: { $in: [ "A", "D" ] } }
```

The following example retrieves all documents in the `inventory` collection where the `status` equals `"A"` **and** `qty` is less than ([`$lt`](https://docs.mongodb.com/manual/reference/operator/query/lt/#op._S_lt "$lt")) `30`:

```javascript
{ status: "A", qty: { $lt: 30 } }
```

The following example retrieves all documents in the collection where the `status` equals `"A"` **or** `qty` is less than ([`$lt`](https://docs.mongodb.com/manual/reference/operator/query/lt/#op._S_lt "$lt")) `30`:

```javascript
{ $or: [ { status: "A" }, { qty: { $lt: 30 } } ] }
```

In the following example, the compound query document selects all documents in the collection where the `status` equals `"A"` **and** _either_ `qty` is less than ([`$lt`](https://docs.mongodb.com/manual/reference/operator/query/lt/#op._S_lt "$lt")) `30` _or_ `item` starts with the character `p`:

```javascript
{ status: "A", $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ] }
```
```javascript
{ status: "A", $or: [ { qty: { $lt: 30 } }, { "$regex": "^p" } ] }
```

![2019-09-01_16-33](/home/hao/work/teaching/big_data/mongodb/2019-09-01_16-33.png)

* #### Query with limit

Click **Options**, set **LIMIT** as 1, click **FIND**

![2019-09-01_16-35](/home/hao/work/teaching/big_data/mongodb/2019-09-01_16-35.png)

* #### Query with Project

Click **RESET** then **Options**, set **Project** as:

```javas
{ item: 1, qty: 1 }
```

![2019-09-01_16-40](/home/hao/work/teaching/big_data/mongodb/2019-09-01_16-40.png)

```javasc
{ size: 0, status: 0 }
```

![2019-09-01_16-41](/home/hao/work/teaching/big_data/mongodb/2019-09-01_16-41.png)



### MongoDB Sort

Click **RESET** then **Options**, enter the sort document into the **Sort** field.

* To specify ascending order for a field, set the field to `1` in the sort document.
* To specify descending order for a field, set the field and `-1` in the sort documents.

try examples:
```javascript
{ item: -1}
```
```javascript
{ qty: -1, status: 1 }
```

![2019-09-01_17-37](/home/hao/work/teaching/big_data/mongodb/2019-09-01_17-37.png)



### MongoDB Update

##### Update Documents in a Collection

To update a document in Compass, hover over the target document and click the pencil icon:

![1567384785-fa99544a1efb00b1ad4859ec02c11046](/home/hao/work/teaching/big_data/mongodb/1567384785-fa99544a1efb00b1ad4859ec02c11046.png)

After clicking the pencil icon, the document enters edit mode:

![1567384785-7a29355f4ed7125715b91d48b0ae3d8a](/home/hao/work/teaching/big_data/mongodb/1567384785-7a29355f4ed7125715b91d48b0ae3d8a.png)

You can now change the this document by clicking the item you wish to change and modifying the value.

For detailed instructions on updating documents in Compass, refer to the [Compass documentation](https://docs.mongodb.com/compass/current/documents/#compass-modify-documents "(in compass vmaster)") or follow the [example](#write-op-updateone) below.

Once you are satisfied with your changes, click **Update** to save the updated document.

Click **Cancel** to revert any modifications made to the document and exit edit mode.

##### Update a Single Document

The following example demonstrates using MongoDB Compass to modify a single document where `item: paper` in the `inventory` collection:

Modify the target document as follows:

*   Change the `status` field from `D` to `P`.
*   Change the `size.uom` field from `in` to `cm`.
*   Add a new field called `lastModified` whose value will be today’s date.

1.  Click the Table button in the top navigation to access the [Table View](https://docs.mongodb.com/compass/current/documents/#documents-table-view "(in compass vmaster)"):
    
    ![1567384785-c80d1be2a4f6243354f137c59453ff9a](/home/hao/work/teaching/big_data/mongodb/1567384785-c80d1be2a4f6243354f137c59453ff9a.png)
    
2.  Use the Compass [query bar](https://docs.mongodb.com/compass/current/query/filter/#query-bar-filter "(in compass vmaster)") to locate the target document.
    
    Copy the following filter document into the query bar and click Find:
    
    ```javascript
    { item: "paper" }
    ```
    
    ![1567384785-bda1915b24a5833c85c84d3eed03a782](/home/hao/work/teaching/big_data/mongodb/1567384785-bda1915b24a5833c85c84d3eed03a782.png)
    
3.  Hover over the `status` field and click the pencil icon which appears on the right side of the document to enter edit mode:
    
    ![1567384785-ccebb99ba25ef37a9cf1ad92a3feb616](/home/hao/work/teaching/big_data/mongodb/1567384785-ccebb99ba25ef37a9cf1ad92a3feb616.png)
    
4.  Change the value of the field to `"P"`.
    
5.  Click the Update button below the field to save your changes.
    
6.  Hover over the `size` field and click the outward-pointing arrows which appear on the right side of the field. This opens a new tab which displays the fields within the `size` object:
    
    ![1567384785-aa6d741a238d892476b536ddaaf4b438](/home/hao/work/teaching/big_data/mongodb/1567384785-aa6d741a238d892476b536ddaaf4b438.png)
    
7.  Using the same process outlined in steps 3-5 for editing the `status` field, change the value of the `size.uom` field to `"cm"`.
    
8.  Click the left-most tab above the table labelled `inventory` to return to the original table view, which displays the top-level document:
    
    ![1567384785-b0d36217b52e2e73bd80891ae3716482](/home/hao/work/teaching/big_data/mongodb/1567384785-b0d36217b52e2e73bd80891ae3716482.png)
    
9.  Hover over the `status` field and click the pencil icon which appears on the right side of the document to re-enter edit mode.
    
10.  Click inside of the `status` field and click the plus button icon which appears in the edit menu.
    Click the Add Field After status button which appears below the plus button:
    
    ![1567384785-23b60016b65d5870e117e7986cd787bb](/home/hao/work/teaching/big_data/mongodb/1567384785-23b60016b65d5870e117e7986cd787bb.png)
    
11.  Add a new field called `lastModified` with a value of today’s date. Set the field type to `Date`:
        ![1567384785-80fb4ac39d05c94d3c104094d29eac76](/home/hao/work/teaching/big_data/mongodb/1567384785-80fb4ac39d05c94d3c104094d29eac76.png)
    
12.  Click the Update button below the field to save your changes.
    

**note**

Once set `_id` field, you cannot update the value of the `_id` field nor can you replace an existing document with a replacement document that has a different `_id` field value.



### MongoDB Delete

### 

### MongoDB Drop Collection

### MongoDB Aggregation












# MongoDB and Python

### MongoDB Connect

### MongoDB Create Database

### MongoDB Create Collection

### MongoDB Insert

### MongoDB Query

### MongoDB Sort

### MongoDB Delete

### MongoDB Update

### MongoDB Drop Collection

### MongoDB Aggregation



In order to start using MongoDB, we first have to install it. Installation instructions are found at the official [MongoDB documentation](https://docs.mongodb.com/manual/installation/). To run a quick install on Ubuntu run the commands below:

`sudo apt update sudo apt install -y mongodb`

Once this is done we'll check the service and database by running this command on the terminal:

`sudo systemctl status mongodb`

**●** mongodb.service - An object/document-oriented database
   Loaded: loaded (/lib/systemd/system/mongodb.service; enabled; vendor preset:
   Active: **active (running)** since Thu 2018-09-20 13:14:02 EAT; 23h ago
     Docs: man:mongod(1)
 Main PID: 11446 (mongod)
    Tasks: 27 (limit: 4915)
   CGroup: /system.slice/mongodb.service
           └─11446 /usr/bin/mongod --unixSocketPrefix=/run/mongodb --config /etc

Sep 20 13:14:02 derrick systemd\[1\]: Started An object/document-oriented database
lines 1-10/10 (END)

The message above means that all is well and that we are set to start using MongoDB.

Now that we have MongoDB installed we need a way to interact with it in our Python code. The official Python MongoDB driver is called [PyMongo](https://pypi.org/project/pymongo/). We can install it using pip as shown below:

`pip install pymongo`

Its possible for us to interact with MongoDB from the terminal, however for the purposes of this tutorial we'll run all our code in a [Jupyter Notebook](http://jupyter.org/).

### Making a Connection with `MongoClient`

The first thing we need to do is import `pymongo`. The import should run without any errors to signify that we've done our installation well.

```python
import
```

Establishing a connection in MongoDB requires us to create a [MongoClient](http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient) to the running MongoDB instance.

```python
from
import
```

The above code will connect to the default host and port, but we can specify the host and port as shown below:

```python
client = MongoClient("localhost", 27017)
```

MongoDB also has a URI format for doing this.

```python
'mongodb://localhost:27017/'
```

### Creating a Database

To create a database in MongoDB, we use the `MongoClient` instance and specify a database name. MongoDB will create a database if it doesn't exist and connect to it.

```python
'datacampdb'
```

It is important to note that databases and collections are created lazily in MongoDB. This means that the collections and databases are created when the first document is inserted into them.

### Data in MongoDB

Data in MongoDB is represented and stored using [JSON-Style](https://en.wikipedia.org/wiki/JSON) documents. In PyMongo we use dictionaries to represent documents. Let's show an example of a PyMongo document below:

```python
"author"
"Derrick Mwiti"
"about"
"Introduction to MongoDB and Python"
"tags"
"mongodb"
"python"
"pymongo"
```

### Inserting a Document

To insert a document into a collection, we use the `insert_one()` method. As we saw earlier, a collection is similar to a table in RDBMS while a document is similar to a row.

```python
articles = db.articles
result = articles.insert_one(article)
```

When the document is inserted, a special key `_id` is generated and its unique to this document. We can print the document ID as shown below:

```python
"First article key is: {}"
```

```plain
First article key is: 5ba5c05e2e8ca029163417f8
```

The articles collection is created after inserting the first document. We can confirm this using the `list_collection_names` method.

```python
db.list_collection_names()
```

```plain
['articles', 'user']
```

We can insert multiple documents to a collection using the `insert_many()` method as shown below.

```python
"author"
"Emmanuel Kens"
"about"
"Knn and Python"
"tags"
"Knn"
"pymongo"
"author"
"Daniel Kimeli"
"about"
"Web Development and Python"
"tags"
"web"
"design"
"HTML"
"The new article IDs are {}"
```

```plain
The new article IDs are [ObjectId('5ba5c0c52e8ca029163417fa'), ObjectId('5ba5c0c52e8ca029163417fb')]
```

### Retrieving a Single Document with `find_one()`

`find_one()` returns a single document matching the query or none if it doesn't exist. This method returns the first match that it comes across. When we call the method below, we get the first article we inserted into our collection.

```python
print(articles.find_one())
```

```plain
{'_id': ObjectId('5ba5c0b52e8ca029163417f9'), 'author': 'Derrick Mwiti', 'about': 'Introduction to MongoDB and Python', 'tags': ['mongodb', 'python', 'pymongo']}
```

### Finding all Documents in a Collection

MongoDB also allows us to retrieve all documents in a collection using the `find` method.

```python
for
in
```

```plain
{'_id': ObjectId('5ba5c0b52e8ca029163417f9'), 'author': 'Derrick Mwiti', 'about': 'Introduction to MongoDB and Python', 'tags': ['mongodb', 'python', 'pymongo']}
{'_id': ObjectId('5ba5c0c52e8ca029163417fa'), 'author': 'Emmanuel Kens', 'about': 'Knn and Python', 'tags': ['Knn', 'pymongo']}
{'_id': ObjectId('5ba5c0c52e8ca029163417fb'), 'author': 'Daniel Kimeli', 'about': 'Web Development and Python', 'tags': ['web', 'design', 'HTML']}
```

When building web applications, we usually get document IDs from the URL and try to retrieve them from our MongoDB collection. In order to achieve this, we first have to convert the obtained string ID into an `ObjectId`.

```python
from bson.objectid import ObjectId
def get(post_id):
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})
```

### Return Some Fields Only

Sometimes we might not want to return all the fields from our documents. Let's show we'd fetch specific fields. In our case we use 0 to specify that the `_id` should not be fetched and 1 to specify that `author` and `about` should be fetched. MongoDB doesn't allow us to specify zero twice. For example, specify `tags` to 0 below will generate an error. We are not allowed to specify both 0 and 1 values in the same object (unless one of the fields is the `_id` field). When we specify a field with the value 0, all other fields get the value 1.

```python
for article in articles.find({},{ "_id": 0, "author": 1, "about": 1}):
  print(article)
```

```plain
{'author': 'Derrick Mwiti', 'about': 'Introduction to MongoDB and Python'}
{'author': 'Emmanuel Kens', 'about': 'Knn and Python'}
{'author': 'Daniel Kimeli', 'about': 'Web Development and Python'}
```

### Sorting the Results

We can use the `sort()` method to sort the results in ascending or descending order. The default order is ascending. We use 1 to signify ascending and -1 to signify descending.

```python
doc = articles.find().sort("author", -1)

for x in doc:
  print(x)
```

```plain
{'_id': ObjectId('5ba5c0c52e8ca029163417fa'), 'author': 'Emmanuel Kens', 'about': 'Knn and Python', 'tags': ['Knn', 'pymongo']}
{'_id': ObjectId('5ba5c0b52e8ca029163417f9'), 'author': 'Derrick Mwiti', 'about': 'Introduction to MongoDB and Python', 'tags': ['mongodb', 'python', 'pymongo']}
{'_id': ObjectId('5ba5c0c52e8ca029163417fb'), 'author': 'Daniel Kimeli', 'about': 'Web Development and Python', 'tags': ['web', 'design', 'HTML']}
```

### Updating a Document

We update a document using the `update_one()` method. The first parameter taken by this function is a query object defining the document to be updated. If the method finds more than one document, it will only update the first one. Let's update the name of the author in the article written by Derrick.

```python
query = { "author": "Derrick Mwiti" }
new_author = { "$set": { "author": "John David" } }

articles.update_one(query, new_author)

for article in articles.find():
  print(article)
```

```plain
{'_id': ObjectId('5ba5c0b52e8ca029163417f9'), 'author': 'John David', 'about': 'Introduction to MongoDB and Python', 'tags': ['mongodb', 'python', 'pymongo']}
{'_id': ObjectId('5ba5c0c52e8ca029163417fa'), 'author': 'Emmanuel Kens', 'about': 'Knn and Python', 'tags': ['Knn', 'pymongo']}
{'_id': ObjectId('5ba5c0c52e8ca029163417fb'), 'author': 'Daniel Kimeli', 'about': 'Web Development and Python', 'tags': ['web', 'design', 'HTML']}
```

### Limiting the Result

MongoDB enables us to limit the result of our query using the `limit` method. In our query below we'll limit the result to one record.

```python
limited_result = articles.find().limit(1)
for x in limited_result:
    print(x)
```

```plain
{'_id': ObjectId('5ba5c0b52e8ca029163417f9'), 'author': 'John David', 'about': 'Introduction to MongoDB and Python', 'tags': ['mongodb', 'python', 'pymongo']}
```

### MongoDB Delete Document

We use the `delete_one()` method to delete a document in MongoDB. The first parameter for this method is the query object of the document we want to delete. If this method finds more than one document, it deletes only the first one found. Let's delete the article with the id `5ba4cbe42e8ca029163417ce`.

```python
"_id"
"5ba4d00e2e8ca029163417d4"
```

```plain
<pymongo.results.DeleteResult at 0x7f3acae72ec8>
```

### Deleting Many Documents

In order to delete many documents, we use the `delete_many()` method. Passing an empty query object will delete all the documents.

```python
" articles deleted."
```

```plain
3  articles deleted.
```

### Dropping a Collection

In MongoDB, we can delete a collection using the `drop()` method.

```python
articles.drop()
```

We can confirm that the collection has been deleted since when we call the `list_collection_names`, we get an empty list.

```python
db.list_collection_names()
```

```plain
[]
```

It is impossible for us to go through all the MongoDB methods in this tutorial. I would recommend that the reader visits the official documentation of [PyMongo](http://api.mongodb.com/python/current/#about-this-documentation) and [MongoDB](https://docs.mongodb.com/) to learn more.

### MongoDB object document mapper (ODM)

In SQL we have object relational mapper (ORM) mappers that provides an abstraction when working with SQL. MongoDB has something similar know as object document mapper(ODM). [MongoEngine](http://mongoengine.org/) is a library that provides a high-level abstraction on top of PyMongo. Run the command below to install it using pip.

`pip install mongoengine`

There are quite a number of other MongoDB ODMs that we can experiment with and choose the best option for our use. Examples of other MongoDB ODMs include [ming](https://ming.readthedocs.io/en/latest/), [minimongo](https://github.com/slacy/minimongo) and, [mongokit](https://github.com/namlook/mongokit).

After we have imported `mongoengine`, we use the `connect` function and specify the database, port, and the host in order to establish a connection with the MongoDB instance.

```python
from mongoengine import *
connect('datacampdb', host='localhost', port=27017)
```

```plain
MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True, read_preference=Primary())
```

### Defining our Documents

Let's assume that we are developing a social site that will allow users to post messages. This means that we need a users and a comments document. Just as if we were using a relational database with an ORM, we define the fields a user will have and the data types. We create the document by sub-classing the _Document_ class from `mongoengine`. `required=True` means that we have to specify this field when creating a user. Otherwise, an exception will be thrown.

```python
class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=30)
    last_name = StringField(max_length=30)
```

Now let's show how we'd create a posts document and reference the users document. The `ReferenceField` enables us to make reference from one document to another in `mongoengine`.

```python
class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User)
```

### Saving Documents

To save the document to the database, call the `save()` method. If the document does not exist in the database, it will be created. If it does already exist, then changes will be updated atomically.

```python
"connect@derrickmwiti.com"
"Derrick"
"Mwiti"
```

```plain
<User: User object>
```

Accessing the just created is very similar to other ORMs

```python
print(user.id, user.email, user.first_name, user.last_name)
```

```plain
5ba5c3bf2e8ca029163417fc connect@derrickmwiti.com Derrick Mwiti
```

## Conclusion

In this tutorial, we have learned how we can use MongoDB in Python. We've also introduced `mongoengine`, an Object Document Mapper that makes it easier for us to interact with MongoDB in Python. In addition, we covered how to create and manipulate documents using pymongo and mongoengine. You can learn more about [MongoDB](https://docs.mongodb.com/), [pymomgo](http://api.mongodb.com/python/current/) and, [mongoengine](http://docs.mongoengine.org/guide/index.html) by visiting their official documentations.

If you would like to learn more about manipulating data in Python, take DataCamp's [Importing Data in Python (Part 1)](https://www.datacamp.com/courses/importing-data-in-python-part-1) course.
