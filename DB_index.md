## What is index
    * Index is a data sturcture that you build, you assign on top of existing table 
    * 2 type index:
        * B-Tree - PK is deafult INDEX(b-tree) 
        * LSM Tree-
        

## Example
    * "explain analyze 'select * from table_name where id = 2000 (sql query)' "
    * select name from table_name - first time it took more time 2nd time fast, because it "CACHES"
    * CREATE INDEX {name_u_create} ON table_name(field) - take time for b-tree, b-map
    * LIKE - make slow query (Filter, Parallel scan)
    * 

<h2>Joins</h2> 
<br>
* select * from "person" JOIN "post" ON "post".person_id = "person".id;

<br>





