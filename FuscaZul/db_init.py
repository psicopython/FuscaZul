import os

os.system(
    'rm -r migrations app/database.db'
)

os.system(
    'flask db init && flask db migrate && flask db upgrade'
    )
