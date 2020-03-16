# https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-function-linux-custom-image?tabs=portal%2Cbash&pivots=programming-language-python
# nomenclature xxxxxx00yyyxxxxxxxxx
# xxxxxx -> product string lower case
# 00 -> stage id
# 	eg: 00 - prod; 01 - staging; 02 - dev; 03 - testing; 04+ - custom
# yyy -> location; eg wus -> west us
PRODUCT=${PRODUCT_ENV}
RESOURCE_GROUP_NAME=AzureFunctionsQuickstart-rg
CONTAINER_SERVICE_NAME=${PRODUCT}0helloworld
REPOSITORY_NAME=dockerpysample
# if you want to use per deployment(staging|dev|production) tags, specify below.
IMAGE_VERSION=latest
ACR_DOCKER_IMAGE=${CONTAINER_SERVICE_NAME}.azurecr.io/${REPOSITORY_NAME}:${IMAGE_VERSION}
CONTAINER_USERNAME=${CONTAINER_SERVICE_NAME}

# creates a container service (which can hold many repositories/images)
step_1:
	az acr create \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--name  ${CONTAINER_SERVICE_NAME} \
		--subscription ${SUBSCRIPTION_ID} \
		--sku Basic \
		--admin-enabled true
		# --image ${ACR_DOCKER_IMAGE} \
		# --registry-login-server ${CONTAINER_SERVICE_NAME}.azurecr.io \
		# --registry-username ${CONTAINER_USERNAME} \
		# --registry-password ${CONTAINER_PASSWORD} \

step_2:
	az acr login --name ${CONTAINER_SERVICE_NAME}

step_2_1:
	docker build --tag ${ACR_DOCKER_IMAGE} .

# create a new image in container service.
step_3:
	docker build --tag ${ACR_DOCKER_IMAGE} .
	docker push ${ACR_DOCKER_IMAGE}

step_4:
	docker run -p 8082:80 -it ${ACR_DOCKER_IMAGE}


LOCATION=westeurope
RESOURCE_GROUP_NAME=AzureFunctionsWestEU-rg
step_4_1:
	az group create --name ${RESOURCE_GROUP_NAME} --location ${LOCATION}

STORAGE_NAME=${PRODUCT}03weudockerpystora
step_5: # create storage
	az storage account create \
		--name ${STORAGE_NAME} \
		--location ${LOCATION} \
		--resource-group ${RESOURCE_GROUP_NAME} --sku Standard_LRS

# FUNC_PLAN_NAME=dockerpyfunc
# LOCATION=westus
step_6: # create function plan
	az functionapp plan create \
		--name ${FUNC_PLAN_NAME} \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--location ${LOCATION} \
		--number-of-workers 1 --sku EP1 --is-linux

FUNC_NAME=${PRODUCT}03wusdockerpyfunc
FUNC_PLAN_NAME=WestUSLinuxDynamicPlan
step_7:
	az functionapp create \
		--name ${FUNC_NAME} \
		--storage-account ${STORAGE_NAME} \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--plan ${FUNC_PLAN_NAME} \
		--deployment-container-image-name ${ACR_DOCKER_IMAGE}

step_8:
	STORAGE_CONNECTION_STRING=$(az storage account show-connection-string \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--name ${STORAGE_NAME} --query connectionString --output tsv)

step_9:
	az functionapp config appsettings set \
		--name ${FUNC_NAME} \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--settings AzureWebJobsStorage=${STORAGE_CONNECTION_STRING}

step_10:
	az functionapp deployment container config \
		--enable-cd --query CI_CD_URL --output tsv \
		--name ${FUNC_NAME} --resource-group ${RESOURCE_GROUP_NAME}