## Working with docker images:

### Creating docker image:
`docker build -t flask_demo .`

### Listing docker images
`docker images`

### Inspect docker image:
`docker inspect image-name:tag`

### Tagging docker images
`docker tag source-image:source-tag new-image:tag`

### Remove docker image
`docker rmi image_name:tag`

### Pruning docker images
To remove all unused images and free up disk space:

`docker image prune`



## Managing Docker containers

### Run the container:

`docker run [OPTIONS] image-name:tag`

-d (detached mode): Run container in the background.

-p (publish): Map container ports to host ports.

--name: Assign a name to the container.

-e (environment variable): Set environment variables.

-v (volume): Mount host directories or volumes.

### Start the container

`docker start container-id`

### Stop a Running Container:

`docker stop container-id`

### Kill a container
To forcefully stop a running container:

`docker kill container-id`

### Listing Containers

`docker ps`

List All Containers (including stopped ones):

`docker ps -a`

### Inspecting Containers

`docker inspect container-id`

### Viewing container logs

`docker logs container-id`

You can also follow the logs in real-time:

`docker logs -f container-id`

### Removing Containers

`docker rm container-id`

### Executing Commands in a Running Container

`docker exec -it container-id command`


## bind mount





##############################################################################################
Kubernetes
##############################################################################################

### Pod

**Create the Pod**:

`kubectl apply -f pod.yaml`

**Check the pod status**

`kubectl get pods`

**Get wide output**

`kubectl get pods -o wide`

**Get pod log**

`kubectl logs pod_name`

**Port Forwad to expose the application publically**

`kubectl port-forward pod_name local_port:container_port`


**Delete the pod**

`kubectl delete pod pod_name`

## Services

**Create the servive**

`kubectl apply -f service.yaml`

**Get all services**

`kubectl get services`

### Deployments

**Create deployment**

`kubectl apply -f deployment.yaml`

**Get deployments**

`kubectl get deployments`


### Access the Application:

* Identify the NodePort from the output of the kubectl **get service service_name** command. 

* Use the IP of a Node in your cluster to access your application. If running Kubernetes locally (e.g., Minikube or Docker Desktop), you can use localhost.

## Self Healing

1. Delete a Pod:
kubectl delete pod <pod-name>


## Scaling

1. Scale Up:

`kubectl scale deployment deployment_name --replicas=5`

2. Scale Down:

`kubectl scale deployment deployment_name --replicas=2`


## Rolling Updates

1. Modify the image, for this example just create a new tag of the image and update the image with new tag in deployment

`docker tag source_image:latest new_image:latest`

**Apply the changes**

`kubectl apply -f deployment.yaml`

This command will initiate a rolling update.