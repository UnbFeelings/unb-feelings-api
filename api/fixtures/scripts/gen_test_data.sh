MANAGE_PATH="../../../manage.py"
DUMP_FILE_PATH="../api_test_data.json"

python $MANAGE_PATH dumpdata > $DUMP_FILE_PATH
