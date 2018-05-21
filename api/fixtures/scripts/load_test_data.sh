MANAGE_PATH="../../../manage.py"
DUMP_FILE_PATH="../api_initial_data.json"

python $MANAGE_PATH loaddata $DUMP_FILE_PATH
