MANAGE_PATH="../../../manage.py"
DUMP_FILE_PATH="../api_initial_data.json"
POPULATE_MODELS_PATH="load_api_fixtures_data.py"

python $MANAGE_PATH shell < $POPULATE_MODELS_PATH
python $MANAGE_PATH dumpdata > $DUMP_FILE_PATH
