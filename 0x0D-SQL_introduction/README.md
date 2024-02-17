In this project, we initiated our work with relational databases, focusing on introductory SQL tasks involving data definitions and manipulation. This included practicing subqueries and utilizing functions.

Tasks:
0. Listing Databases

0-list_databases.sql: MySQL script to list all databases.
1. Creating a Database

1-create_database.sql: MySQL script to create the hbtn_0c_0 database.
2. Deleting a Database

2-remove_databases.sql: MySQL script to delete the hbtn_0c_0 database.
3. Listing Tables

3-list_tables.sql: MySQL script to list all tables.
4. Creating the First Table

4-first_table.sql: MySQL script to create a table named first_table.
Description:
id: INT
name: VARCHAR(256)
5. Displaying Full Table Description

5-full_table.sql: MySQL script to print the full description of the first_table.
6. Listing All Entries in the Table

6-list_values.sql: MySQL script to list all rows of the first_table.
7. Adding the First Entry

7-insert_value.sql: MySQL script to insert a new row into the first_table.
Description:
id = 89
name = Best School
8. Counting Entries with ID 89

8-count_89.sql: MySQL script to display the number of records with id = 89 in the first_table.
9. Creating and Populating a New Table

9-full_creation.sql: MySQL script to create and fill a table named second_table.
Description:
id: INT
name: VARCHAR(256)
score: INT
Records:
id = 1, name = "John", score = 10
id = 2, name = "Alex", score = 3
id = 3, name = "Bob", score = 14
id = 4, name = "George", score = 8
10. Listing Records Sorted by Best Score

10-top_score.sql: MySQL script to list the score and name of all records from second_table in descending order of score.
11. Selecting Records with Scores >= 10

11-best_score.sql: MySQL script to list the score and name of records with a score >= 10 in second_table in descending order of score.
12. Updating Bob's Score

12-no_cheating.sql: MySQL script to update Bob's score to 10 in second_table.
13. Removing Records with Scores <= 5

13-change_class.sql: MySQL script to remove all records with a score <= 5 in second_table.
14. Calculating Average Score

14-average.sql: MySQL script to compute the average score of all records in second_table.
15. Counting Records by Score

15-groups.sql: MySQL script to list the score and the number of records with the same score in second_table, ordered by descending count.
16. Listing Records with Names and Scores

16-no_link.sql: MySQL script to list the score and name of all records in second_table, ordered by descending score.
Excludes rows without a name value.
17. Converting to UTF8

100-move_to_utf8.sql: MySQL script to convert the hbtn_0c_0 database to UTF8.
18. Average Temperatures by City

101-avg_temperatures.sql: MySQL script to display the average temperature (Fahrenheit) by city in descending order.
19. Top Cities by Temperature

102-top_city.sql: MySQL script to display the three cities with the highest average temperature from July to August in descending order.
20. Maximum Temperatures by State

103-max_state.sql: MySQL script to display the maximum temperature of each state, ordered by state name.
Dump File:
Queries 101-103 extracted from the database temperatures.sql.
