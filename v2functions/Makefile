list_templates:
	func templates list
# create function
step_2:
	func new --language python --template "HttpTrigger" --name HttpTriggerPY

step_3:
	python3.6 -m venv .env

step_4: # needs to run the below command instead of make step_4
	source .env/bin/activate

step_5:
	pip install --upgrade pip
	pip install numpy
	pip install -r requirements.txt

step_6:
	pip freeze > requirements.txt

step_7:
	func extensions install

step_8: # move to previous level; time to test the app.
	cd ..

step_9:
	func host start

# http://localhost:7071/api/HttpTriggerPY?name=name

# time to create a resource for this
# continued at Makefile in parent directory

# create function
APP_NAME=cartishttpfuncquickstart # can be `pwd`[-1]func
STORAGE_NAME=cartisazfuncquickstart # canbe `pwd`[-1]sg
step_13:
	az functionapp create --resource-group AzureFunctionsQuickstart-rg \
		--os-type Linux --consumption-plan-location westus \
		--runtime python --runtime-version 3.6 \
		--functions-version 2 --name ${APP_NAME} --storage-account ${STORAGE_NAME}

step_14:
	# https://github.com/Azure/azure-functions-python-worker/issues/464#issuecomment-533964911
	func azure functionapp publish ${APP_NAME} --build remote
# Functions in test-http-trigger-py:
# HttpTriggerPY - [httpTrigger]
#     Invoke url: https://test-http-trigger-py.azurewebsites.net/api/httptriggerpy?code=6kRreM3Ra5wEKJdY8h2QHj36BaZS6Rk0mObrwZPiExwdzUUJgBhJig==&name=http
# https://cartishttpfuncquickstart.azurewebsites.net/api/httptriggerpy?code=GXK19iEiCOTGrwS0m0GizIXl0GyL0BGWEEPaXNWVjY18rj0t5WNgLg==