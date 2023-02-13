# step 0 - import sqlite 3
import sqlite3

# step 1 - Connect to the database
# triple-check the spelling opf your database filename
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2
cursor = connection.cursor()

# step 3
query = 'SELECT character_id, name FROM charactercreator_character;'

# step 4 - Execute the query on the cursor and fetch the results
# "pulling the results" from the cursor
results = cursor.execute(query).fetchall()

if __name__ == '__main__':
    print(results[:5])