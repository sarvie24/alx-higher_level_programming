Tests :heavy_check_mark:
tests: This directory contains SQL and Python scripts used for setting up test tables related to all project files. These scripts were provided by ALX.
Tasks :page_with_curl:
0. Retrieve all states

0-select_states.py: This Python script employs MySQLdb to retrieve and list all states stored in the hbtn_0e_0_usa database.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>.
The results are sorted in ascending order based on the states.id column.
1. Filter states

1-filter_states.py: This Python script utilizes MySQLdb to filter and list states whose names start with the letter N from the hbtn_0e_0_usa database.
Usage: ./1-filter_states.py <mysql username> <mysql password> <database name>.
The results are sorted in ascending order based on the states.id column.
2. Filter states by user input

2-my_filter_states.py: This Python script employs MySQLdb to display all states matching a provided name from the states table within the hbtn_0e_0_usa database.
Usage: ./2-my_filter_states.py <mysql username> <mysql password> <database name> <state name searched>.
The results are sorted in ascending order based on the states.id column, utilizing string formatting for constructing the SQL query.
3. Protection against SQL Injection

3-my_safe_filter_states.py: This Python script uses MySQLdb to securely display all states matching a provided name from the states table within the hbtn_0e_0_usa database, protecting against SQL injection attacks.
Usage: ./3-my_safe_filter_states.py <mysql username> <mysql password> <database name> <state name searched>.
The results are sorted in ascending order based on the states.id column.
4. Cities by states

4-cities_by_state.py: This Python script utilizes MySQLdb to list all cities stored in the hbtn_0e_4_usa database.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>.
The results are sorted in ascending order based on the cities.id column.
5. All cities by state

5-filter_cities.py: This Python script employs MySQLdb to list all cities of a specified state from the hbtn_0e_4_usa database.
Usage: ./5-filter_cities.py <mysql username> <mysql password> <database name>.
The results are sorted in ascending order based on the cities.id column.
6. First state model

model_state.py: This Python module defines a class named State, which inherits from SQLAlchemy Base and represents the states table in the MySQL database.
7. Retrieving all states via SQLAlchemy

7-model_state_fetch_all.py: This Python script uses SQLAlchemy to retrieve and list all State objects stored in the hbtn_0e_6_usa database.
Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password> <database name>.
The results are sorted in ascending order based on the states.id column.
8. Retrieving the first state via SQLAlchemy

8-model_state_fetch_first.py: This Python script utilizes SQLAlchemy to print the details of the first State object stored in the hbtn_0e_6_usa database, ordered by states.id.
Usage: ./8-model_state_fetch_first.py <mysql username> <mysql password> <database name>.
If the states table is empty, it prints Nothing.
9. States containing the letter 'a'

9-model_state_filter_a.py: This Python script uses SQLAlchemy to list all State objects containing the letter 'a' from the hbtn_0e_6_usa database.
Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>.
The results are sorted in ascending order based on the states.id column.
10. Retrieve a state

10-model_state_my_get.py: This Python script employs SQLAlchemy to print the id of the State object whose name matches the provided argument in the hbtn_0e_6_usa database.
Usage: ./10-model_state_my_get.py <mysql username> <mysql password> <database name> <state searched name>.
It displays the id of the matched State, and if no match is found, it prints Not found.
11. Add a new state

11-model_state_insert.py: This Python script utilizes SQLAlchemy to add the State object "Louisiana" to the hbtn_0e_6_usa database.
Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>.
It prints the id of the newly created State.
12. Update a state

12-model_state_update_id_2.py: This Python script employs SQLAlchemy to change the name of the State object with id = 2 in the hbtn_0e_6_usa database to "New Mexico".
Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>.
13. Delete states

13-model_state_delete_a.py: This Python script uses SQLAlchemy to delete all State objects with names containing the letter 'a' from the hbtn_0e_6_usa database.
Usage: ./13-model_state_delete_a.py <mysql username> <mysql password> <database name>.
14. Cities in state

model_city.py: This Python module defines a class named City, which inherits from SQLAlchemy Base and represents the cities table in the MySQL database. It includes a class attribute `
