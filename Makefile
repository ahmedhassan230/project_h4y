

build_container_local:
	docker build --platform linux/amd64 --tag=MVPmvp:dev .

run_container_local:
	docker run --platform linux/amd64 -e PORT=8088 -p 8085:8088 new:dev

#Allow Docker push
build_production:
	docker build --platform linux/amd64 -t  $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod .

allow_docker_push:
	gcloud auth configure-docker $GCP_REGION-docker.pkg.dev

create_artifacts_repo:
	gcloud artifacts repositories create $ARTIFACTSREPO --repository-format=docker \
	--location =$GCP_REGION --description="repository for storing docker image"
