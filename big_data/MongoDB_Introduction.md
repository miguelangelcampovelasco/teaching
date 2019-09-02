# 0. Prerequisites

* Install MongoDB Compass (Community Edition Stable)  from [https://www.mongodb.com/download-center/compass](https://www.mongodb.com/download-center/compass)
* Install Anaconda (Python 3.7 version) from [anaconda download](https://www.anaconda.com/distribution/#download-section) following [anaconda installation](https://docs.anaconda.com/anaconda/install/)
* Install MongoDB python driver `pymongo`,  open Anaconda Prompt for windows or Terminal for MacOS/Linux, exercute `pip install -U pymongo`

# 1. Introduction to MongoDB

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

![1567306477-74b398457ab57bd38be0c517383c73ce](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567306477-74b398457ab57bd38be0c517383c73ce.png)

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

![1567306477-74b398457ab57bd38be0c517383c73ce](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567306477-74b398457ab57bd38be0c517383c73ce.png)

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

# 2. MongoDB  GUI client
[MongoDB Compass](https://docs.mongodb.com/compass/current/) is the GUI for MongoDB. The following tutorial uses MongoDB Compass to  connect to MonogoDB server and  perform mutiple operations.

### MongoDB Connect

1. Install MongoDB Compass (Community Edition Stable)  from [https://www.mongodb.com/download-center/compass](https://www.mongodb.com/download-center/compass)

2. Open MongoDB Compass, log in with your account:
   username: `<NetID>`, password:`<NetID>123`

![2019-09-01_11-14](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_11-14.png)

### MongoDB Create Database

1. At the bottom of left sidebar, click '+' to create a new database.

![2019-09-01_12-00](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_12-00.png)

![2019-09-01_12-00_1](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_12-00_1.png)

2. Permission of your account '<NetID>' is limited to Northwind (read) and bigdata_<NetID>(read and write), so you can not create a new database here.

### MongoDB Create Collection

1. Choose the database `bigdata_<NetID>`.

2. Choose `CREATE COLLECTION`, input `inventory` as Collection Name.

![2019-09-01_15-53](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_15-53.png)

![2019-09-01_15-53_1](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_15-53_1.png)



### MongoDB Insert

1. From the **Collections** tab, click the `test_collection` collection.

   ![2019-09-01_15-56](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_15-56.png)

2. Insert the following [document](https://docs.mongodb.com/manual/core/document/) by entering the `fields` and `values`, then selecting the appropriate types from the dropdowns. Add fields by clicking the last line number, then clicking **Add Field After ….**

```javascript
{ item: "journal", qty: 25, status: "A", 
    size: { h: 14, w: 21, uom: "cm" }, tags: [ "blank", "red" ] }
```

*   For `Object` types, add nested fields by clicking the last field’s number and selecting Add Field After ….
*   For `Array` types, add additional elements to the array by clicking the last element’s line number and selecting Add Array Element After ….

![1567365708-a0ba4b9f70979c77f7bbdd574b7b71c7](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567365708-a0ba4b9f70979c77f7bbdd574b7b71c7.png)

![1567365708-58d28db3cee8a5546fc392c7cdf64a6b](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567365708-58d28db3cee8a5546fc392c7cdf64a6b.png)

![2019-09-01_12-35](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_12-35.png)

### MongoDB Query

We will perform query on `inventory`. Choose **bigdata_<NetID>**  ->  **inventory**

* ##### Match specific equality conditions

pass a [query filter document](https://docs.mongodb.com/manual/core/document/#document-query-filter) to the Filter with the `<field>: <value>` of the desired documents. The following query filter document selects all documents where the `status` equals `"D"` from the `inventory` collection:

Copy the following filter into the Compass query bar and click Find:

```javascript
{ status: "D" }
```

![2019-09-01_16-01](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_16-01.png)

* #### Match embedded documents

Equality matches on the whole embedded document require an _exact_ match of the specified `<value>` document, including the field order. For example, the following query selects all documents where the field `size` equals the document `{ h: 14, w: 21, uom: "cm" }`:

  ```javascript
  { size: { h: 14, w: 21, uom: "cm" } }
  ```

![2019-09-01_16-04](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_16-04.png)

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
{ status: "A", $or: [ { qty: { $lt: 30 } }, {item: { "$regex": "^p" } }] }
```

![2019-09-01_16-33](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_16-33.png)

* #### Query with limit

Click **Options**, set **LIMIT** as 1, click **FIND**

![2019-09-01_16-35](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_16-35.png)

* #### Query with Project

Click **RESET** then **Options**, set **Project** as:

```javas
{ item: 1, qty: 1 }
```

![2019-09-01_16-40](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_16-40.png)

```javasc
{ size: 0, status: 0 }
```

![2019-09-01_16-41](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_16-41.png)



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

![2019-09-01_17-37](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_17-37.png)



### MongoDB Update

##### Update Documents in a Collection

To update a document in Compass, hover over the target document and click the pencil icon:

![1567384785-fa99544a1efb00b1ad4859ec02c11046](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-fa99544a1efb00b1ad4859ec02c11046.png)

After clicking the pencil icon, the document enters edit mode:

![1567384785-7a29355f4ed7125715b91d48b0ae3d8a](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-7a29355f4ed7125715b91d48b0ae3d8a.png)

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
    
    ![1567384785-c80d1be2a4f6243354f137c59453ff9a](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-c80d1be2a4f6243354f137c59453ff9a.png)
    
2.  Use the Compass [query bar](https://docs.mongodb.com/compass/current/query/filter/#query-bar-filter "(in compass vmaster)") to locate the target document.
    
    Copy the following filter document into the query bar and click Find:
    
    ```javascript
    { item: "paper" }
    ```
    
    ![1567384785-bda1915b24a5833c85c84d3eed03a782](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-bda1915b24a5833c85c84d3eed03a782.png)
    
3.  Hover over the `status` field and click the pencil icon which appears on the right side of the document to enter edit mode:
    
    ![1567384785-ccebb99ba25ef37a9cf1ad92a3feb616](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-ccebb99ba25ef37a9cf1ad92a3feb616.png)
    
4.  Change the value of the field to `"P"`.
    
5.  Click the Update button below the field to save your changes.
    
6.  Hover over the `size` field and click the outward-pointing arrows which appear on the right side of the field. This opens a new tab which displays the fields within the `size` object:
    
    ![1567384785-aa6d741a238d892476b536ddaaf4b438](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-aa6d741a238d892476b536ddaaf4b438.png)
    
7.  Using the same process outlined in steps 3-5 for editing the `status` field, change the value of the `size.uom` field to `"cm"`.
    
8.  Click the left-most tab above the table labelled `inventory` to return to the original table view, which displays the top-level document:
    
    ![1567384785-b0d36217b52e2e73bd80891ae3716482](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-b0d36217b52e2e73bd80891ae3716482.png)
    
9.  Hover over the `status` field and click the pencil icon which appears on the right side of the document to re-enter edit mode.
    
10.  Click inside of the `status` field and click the plus button icon which appears in the edit menu.
    Click the Add Field After status button which appears below the plus button:
    
    ![1567384785-23b60016b65d5870e117e7986cd787bb](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-23b60016b65d5870e117e7986cd787bb.png)
    
11.  Add a new field called `lastModified` with a value of today’s date. Set the field type to `Date`:
        ![1567384785-80fb4ac39d05c94d3c104094d29eac76](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567384785-80fb4ac39d05c94d3c104094d29eac76.png)
    
12.  Click the Update button below the field to save your changes.


**note**

Once set `_id` field, you cannot update the value of the `_id` field nor can you replace an existing document with a replacement document that has a different `_id` field value.

### MongoDB Delete

MongoDB Compass provides a simple way to delete a document from a collection. The following example shows how to delete the document with `item` equal to `paper` from the `inventory` collection:

1.  Click the Table button in the top navigation to access the [Table View](https://docs.mongodb.com/compass/current/documents/#documents-table-view "(in compass vmaster)"):
    
    ![1567385579-c54023307ac836d5c6d159ae1e3756cd](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567385579-c54023307ac836d5c6d159ae1e3756cd.png)
    
2.  Use the Compass [query bar](https://docs.mongodb.com/compass/current/query/filter/#query-bar-filter "(in compass vmaster)") to locate the target document.
    
    Copy the following filter document into the query bar and click Find:
    
    ```javascript
    { item: "paper" }
    ```
    
    ![1567385579-8a1b381606f8097ad4be6145ef1863c0](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567385579-8a1b381606f8097ad4be6145ef1863c0.png)
    
     
    
3.  Hover over the document and click the trash icon which appears on the right-hand side:
    
      ![1567385579-e72fb95147f6f1c7265613c09151c3ca](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567385579-e72fb95147f6f1c7265613c09151c3ca.png)
    
    After clicking the delete button, the document is flagged for deletion and Compass asks for confirmation that you want to remove the document:
    
    ![1567385579-1e2c2e450a0fbc7c269fb3885c6e8ab0](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/1567385579-1e2c2e450a0fbc7c269fb3885c6e8ab0.png)
    
4.  Click Delete to confirm. Compass deletes the document from the collection.

### MongoDB Drop Collection

Click database `bigdata_<NetID>` , click the delete button at end of the collection:

![2019-09-01_18-02](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_18-02.png)



### MongoDB Aggregation

[Aggregation](https://docs.mongodb.com/manual/aggregation/) operations process data records and return computed results. Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result.

Choose **bigdata_<NetID>** -> **inventory**, click **Aggregations**:

![2019-09-01_18-42](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_18-42.png)

In the stage box, select `$count`, rename it as `"total_documents"`, which shows total number of documents

![2019-09-01_18-45](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_18-45.png)

In the following example, group all documents by `status`, sum all `qty` for each status

```json
{
  _id: {status:'$status'},
  total_qty: {
    $sum: '$qty'
  }
}
```

![2019-09-01_19-55](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-01_19-55.png)

In the following example, group all documents by status, count total number of documents for each status

```javascript
{
  _id: {status:'$status'},
  total_qty: {
    $sum: 1
  }
}
```

![2019-09-02_10-54](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-02_10-54.png)

You can find more aggregation operators from [https://docs.mongodb.com/manual/reference/operator/aggregation/#aggregation-expression-operators](https://docs.mongodb.com/manual/reference/operator/aggregation/#aggregation-expression-operators)


# 3. MongoDB and Python

The official Python MongoDB driver is called [PyMongo](https://pypi.org/project/pymongo/). We can install it using pip as shown below:

`pip install pymongo`

Please delete collections in `bigdata_<NetID>` and disconnect before we start.

![2019-09-02_11-19](https://github.com/liuhoward/teaching/raw/master/big_data/mongodb/2019-09-02_11-19.png)


```python
from pymongo import MongoClient

# set your NetID as user name
user = "liuhao16" "<NetID>"
password = f"{user}123"
uri = f"mongodb://{user}:{password}@liuhoward.tk:27017"

user_client = MongoClient(uri)
```

### MongoDB Create Database

**Important:** In MongoDB, a database is not created until it gets content!


```python
# we could print existing databases
print(user_client.list_database_names())
```


```python
# three ways to create database

# get_database()
user_db = user_client.get_database(f'bigdata_{user}')

# user_client as dictionary of name->database
#user_db = user_client[f'bigdata_{user}']

# use dot notation, attribute style
#user_db = user_client.bigdata_liuhao16
```


```python
# bigdata_netid is not created yet
print(user_client.list_database_names())
```

### MongoDB Create Collection


```python
user_col = user_db.get_collection("inventory")
```


```python
# bigdata_netid is not created yet
print(user_client.list_database_names())
```

### MongoDB Insert


```python
# insert one document

first_document = {"item": "journal", "qty": 25,"size": {"h": 14, "w": 21, "uom": "cm"},"tags": ["blank", "red"],"status": "A"}

user_col.insert_one(first_document)

```


```python
# bigdata_netid is created
print(user_client.list_database_names())
```


```python
# insert multiple documents
inventory_list = [
    {"item": "canvas", "qty": 100, "size": {"h": 28, "w": 35.5, "uom": "cm"}, "tags": ["plain"], "status": "A"},
    {"item": "mat","qty": 85,"size": {"h": 27.9, "w": 35.5, "uom": "cm"},"status": "A"},
    {"item": "mousepad","qty": 25,"size": {"h": 19, "w": 22.85, "uom": "cm"},"status": "P"},
    {"item": "notebook","qty": 50,"size": {"h": 8.5, "w": 11, "uom": "in"},"tags": ["red", "blank"],"status": "P"},
    {"item": "paper","qty": 100,"size": {"h": 8.5, "w": 11, "uom": "in"},"tags": ["red", "blank", "plain"],"status": "D"},
    {"item": "planner","qty": 75,"size": {"h": 22.85, "w": 30, "uom": "cm"},"tags": ["blank", "red"],"status": "D"},
    {"item": "postcard","qty": 45,"size": {"h": 10, "w": 15.25, "uom": "cm"},"tags": ["blue"],"status": "A"},
    {"item": "sketchbook","qty": 80,"size": {"h": 14, "w": 21, "uom": "cm"},"status": "A"},
    {"item": "sketch pad","qty": 95,"size": {"h": 22.85, "w": 30.5, "uom": "cm"},"status": "A"}
]

ret = user_col.insert_many(inventory_list)

print(ret.inserted_ids)
```

### MongoDB Query


```python
# The find_one() method returns the first occurrence in the selection.
first_document = user_col.find_one()
print(first_document)
```


```python
# The find() method returns all occurrences in the selection.
all_documents = user_col.find()
type(all_documents)
```


```python
for x in all_documents:
    print(x)
```


```python
# query
query = {"status": "D" }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query to match embedded documents
query = { "size": { "h": 14, "w": 21, "uom": "cm" } }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query to match embedded documents
query = { "size.uom": "in" }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query elements in array
query = { "tags": "red" }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query to match array
query = { "tags": ["red", "blank"] }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query with operators
query = { "status": { "$in": [ "A", "D" ] } }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query with operators
query = { "status": "A", "qty": { "$lt": 30 } }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query with operators
query = { "$or": [ { "status": "A" }, { "qty": { "$lt": 30 } } ] }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query with operators, why is there one document found?
query = { "status": "A", "$or": [ { "qty": { "$lt": 30 } }, { "item": "/^p/" } ] }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query with operators
query = { "status": "A", "$or": [ { "qty": { "$lt": 30 } }, {"item": { "$regex": "^p"} } ] }
query_documents = user_col.find(query)
for x in query_documents:
    print(x)
```


```python
# query with limit
query = { "status": "A"}
query_documents = user_col.find(query).limit(2)
for x in query_documents:
    print(x)
```


```python
# query with limit
query = { "status": "A"}
query_documents = user_col.find(filter=query, limit=2)
for x in query_documents:
    print(x)
```


```python
# query with projection
query = { "status": "A"}
query_documents = user_col.find(filter=query, projection={"item": 1, "qty": 1})
for x in query_documents:
    print(x)
```


```python
# query with project
query = { "status": "A"}
query_documents = user_col.find(filter=query, projection={"size": 0, "status": 0})
for x in query_documents:
    print(x)
```

### MongoDB Sort


```python
# query with projection
query_documents = user_col.find().sort("item", 1)
for x in query_documents:
    print(x)
```


```python
# query with projection
query_documents = user_col.find(sort=[("qty", -1), ("status", 1)])
for x in query_documents:
    print(x)
```


```python
# query with projection
query_documents = user_col.find().sort([("qty", -1), ("status", 1)])
for x in query_documents:
    print(x)
```

### MongoDB Update


```python
# The first parameter of the update_one() method is a query object defining which document to update.

query = { "item": "paper"}
query_documents = user_col.find(filter=query)
for x in query_documents:
    print(x)
```


```python
# change status from "D" to "P"
query = { "item": "paper"}
newvalues = { "$set": { "status": "P" } }
user_col.update_one(query, newvalues)

query_documents = user_col.find(filter=query)
for x in query_documents:
    print(x)
```


```python
# add a new field lastModified with current date & time
from datetime import datetime

query = { "item": "paper"}
newvalues = { "$set": { "lastModified": datetime.today()} }
user_col.update_one(query, newvalues)

query_documents = user_col.find(filter=query)
for x in query_documents:
    print(x)
```


```python
# To update all documents that meets the criteria of the query, use the update_many() method.

# add a new field lastModified with current date & time
from datetime import datetime

query = { "status": "A"}
newvalues = { "$set": { "lastModified": datetime.today()} }
user_col.update_many(query, newvalues)

query_documents = user_col.find(filter=query)
for x in query_documents:
    print(x)

```

### MongoDB Delete


```python
# The first parameter of the delete_one() method is a query object defining which document to delete.
query = { "item": "paper"}

user_col.delete_one(query)
# could not find the deleted document
query_documents = user_col.find(filter=query)
for x in query_documents:
    print(x)

```


```python
# To delete more than one document, use the delete_many() method.
query = { "status": "A"}

ret = user_col.delete_many(query)
# could not find the deleted document
query_documents = user_col.find(filter=query)
for x in query_documents:
    print(x)
    
print(ret.deleted_count, " documents deleted.")
```

**note** you can delete all documents by setting query as {}

### MongoDB Aggregation


```python
pipeline = [{"$count": "total_documents"}]
ret = user_db.inventory.aggregate(pipeline)

print(list(ret))
```


```python
# To run an explain plan for this aggregation use the command() method:
user_db.command('aggregate', 'inventory', pipeline=pipeline, explain=True)
```


```python
pipeline = [
     {"$group": {"_id": {"status": "$status"}, "total_qty": {"$sum": "$qty"}}}]
ret = user_db.inventory.aggregate(pipeline)

print(list(ret))
```


```python
# To run an explain plan for this aggregation use the command() method:
user_db.command('aggregate', 'inventory', pipeline=pipeline, explain=True)
```


```python
pipeline = [
     {"$group": {"_id": {"status": "$status"}, "avg_qty": {"$avg": "$qty"}}}]
ret = user_db.inventory.aggregate(pipeline)

print(list(ret))
```


```python
# As python dictionaries don’t maintain order you should use SON or collections.OrderedDict 
# where explicit ordering is required eg “$sort”:
from bson.son import SON

print(user_db.name)

# there two stages in this pipeline: group and sort
pipeline = [
    {"$group": {"_id": {"status": "$status"}, "total_qty": {"$sum": "$qty"}}},
    {"$sort": SON([("total_qty", -1)])}
]
ret = user_db.inventory.aggregate(pipeline)

print(list(ret))

```

### MongoDB Drop Collection


```python
user_col.drop()
```

**important**
remenber to close the connection


```python
user_client.close()
```

More pymongo examples could be found here [**Pymongo examples**](https://api.mongodb.com/python/current/examples/index.html)

# Screenshots for submission
0. Use python code in this tutorial, rebuild collection `inventory`, insert the 10 documents.
1. In MongoDB Compass Community, aggregation:
    group the 10 documents by `status`, and calculate the **average** `qty`. Take a screenshot of the whole screen.
2. Use python code, print database name, group the 10 documents by `status` and calculate the **average** `qty`, sort them by `avg_qty` in ascending order. Take a screenshot including code & output.

**note**: Put these two screenshots in MS word and save it as pdf for submission.

# Reference
[1] [https://www.datacamp.com/community/tutorials/introduction-mongodb-python](https://www.datacamp.com/community/tutorials/introduction-mongodb-python)  
[2] [https://docs.mongodb.com/manual/](https://docs.mongodb.com/manual/)  
[3] [https://www.tutorialspoint.com/mongodb/](https://www.tutorialspoint.com/mongodb/)  
[4] [https://api.mongodb.com/python/current/tutorial.html](https://api.mongodb.com/python/current/tutorial.html)  


```python

```
