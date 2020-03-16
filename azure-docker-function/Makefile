SUBSCRIPTION_ID=29bf4c84-405c-4b40-b3b9-a86d8e854d26
RESOURCE_GROUP_NAME=AzureFunctionsQuickstart-rg
az_container_create:
	az container create \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--name "helloworld" \
		--image cartis0helloworld.azurecr.io/hellow-world:v1

CONTAINER_SERVICE_NAME=cartis0helloworld
REPOSITORY_NAME=hellow-world
IMAGE_VERSION=v1
step_1:
	docker pull hello-world
	docker tag hello-world ${CONTAINER_SERVICE_NAME}.azurecr.io/${REPOSITORY_NAME}:${IMAGE_VERSION}
	az acr login --name ${CONTAINER_SERVICE_NAME}
	docker push ${CONTAINER_SERVICE_NAME}.azurecr.io/${REPOSITORY_NAME}:${IMAGE_VERSION}

step_2:
	func init dockerpy --worker-runtime python --docker

# https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image
# Create App Service plan
# https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image#create-app-service-plan
DOCKER_APP_SERVICE_PLAN=cartisDockerAppServicePl
step_3:
	az appservice plan create --name ${DOCKER_APP_SERVICE_PLAN} --resource-group ${RESOURCE_GROUP_NAME} --sku F1 --is-linux

# No credential was provided to access Azure Container Registry. Trying to look up...
# Retrieving credentials failed with an exception:'Failed to retrieve container registry credentials.
# Please either provide the credentials or run 'az acr update -n cartis0helloworld --admin-enabled true' to enable admin first.'
step_3_1:
	az acr update -n ${CONTAINER_SERVICE_NAME} --admin-enabled true

# Create web app
# https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image#create-web-app
WEB_APP=cartiswebapp
step_4:
	az webapp create --resource-group ${RESOURCE_GROUP_NAME} \
		--plan ${DOCKER_APP_SERVICE_PLAN} \
		--name ${WEB_APP} \
		--deployment-container-image-name ${CONTAINER_SERVICE_NAME}.azurecr.io/${REPOSITORY_NAME}:${IMAGE_VERSION}

step_4_1:
	az acr credential show --name ${CONTAINER_SERVICE_NAME}

CONTAINER_USERNAME=${CONTAINER_SERVICE_NAME}
# CONTAINER_PASSWORD=${CONTAINER_PASSWORD} reads from environment
# Configure registry credentials in web app
# https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image#configure-registry-credentials-in-web-app
step_5:
	az webapp config container set --name ${WEB_APP} \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--docker-custom-image-name ${CONTAINER_SERVICE_NAME}.azurecr.io/${REPOSITORY_NAME}:${IMAGE_VERSION} \
		--docker-registry-server-url https://${CONTAINER_SERVICE_NAME}.azurecr.io \
		--docker-registry-server-user ${CONTAINER_USERNAME} \
		--docker-registry-server-password ${CONTAINER_PASSWORD}

step_6:
	az acr repository list -n ${CONTAINER_SERVICE_NAME}

# Configure environment variables
# https://docs.microsoft.com/en-us/azure/app-service/containers/tutorial-custom-docker-image#configure-environment-variables
step_7:
	az webapp config appsettings set --resource-group ${RESOURCE_GROUP_NAME} \
		--name ${WEB_APP} --settings WEBSITES_PORT=8000