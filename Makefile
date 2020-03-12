setup:
	# install pyenv
	# https://realpython.com/intro-to-pyenv/
	# https://github.com/pyenv/pyenv
	pyenv install 3.6.0
	pyenv global 3.6.0
	# install nvm
	nvm install 10.15.2
	nvm use 10.15.2
	# install serverless
	npm install -g serverless

# create app
# langauge is defined at app level
# http sub-domain is defined at app level

step_1:
	func init v2functions --worker-runtime python

# cd to the app created (v2functions)
# move to v2functions/ and check Makefile.

# Create supporting Azure resources for your function
# Before you can deploy your function code to Azure, you need to create three resources:

# A resource group, which is a logical container for related resources.
# A Storage account, which maintains state and other information about your projects.
# A function app, which provides the environment for executing your function code. A function app maps to your local function project and lets you group functions as a logical unit for easier management, deployment, and sharing of resources.
step_10:
	az login
	

# Create a resource group 
step_11:
	az group create --name AzureFunctionsQuickstart-rg --location westus

check_available_locations:
	az account list-locations

# create storage unit
step_12:
	az storage account create --name cartisazfuncquickstart --location westus --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS

