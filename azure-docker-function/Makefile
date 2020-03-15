SUBSCRIPTION_ID=29bf4c84-405c-4b40-b3b9-a86d8e854d26
RESOURCE_GROUP_NAME=AzureFunctionsQuickstart-rg
az_container_create:
	az container create \
		--resource-group ${RESOURCE_GROUP_NAME} \
		--name "helloworld" \
		--image cartis0helloworld.azurecr.io/hellow-world:v1

CONTAINER_SERVICE_NAME=cartis0helloworld
REPOSITORY_NAME=hello-world
IMAGE_VERSION=v1
step_1:
	docker pull hello-world
	docker tag hello-world ${CONTAINER_SERVICE_NAME}.azurecr.io/${REPOSITORY_NAME}:${IMAGE_VERSION}
	az acr login --name ${CONTAINER_SERVICE_NAME}
	docker push ${CONTAINER_SERVICE_NAME}.azurecr.io/${REPOSITORY_NAME}:${IMAGE_VERSION}

step_2:
	func init dockerpy --worker-runtime python --docker