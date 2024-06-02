

build_container_local_m1:
	docker build --platform linux/amd64 --tag=MVP$IMAGE:dev .

run_container_local_m1:
	docker run -p 8080:8000 --platform linux/amd64 $IMAGE:dev

#Allow Docker push
build_production_m1:
	docker build --platform linux/amd64 -t  $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod .

allow_docker_push:
	gcloud auth configure-docker $GCP_REGION-docker.pkg.dev

create_artifacts_repo:
	gcloud artifacts repositories create $ARTIFACTSREPO --repository-format=docker --location=$GCP_REGION --description="repository for storing docker image"

push_image_production:
	docker push $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod

run_production_image_locally:
	docker run --platform linux/amd64 -e PORT=8000 -p 8000:8000 --env-file .env $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod

deploy_to_cloud_run:
	gcloud run deploy --image $GCP_REGION-docker.pkg.dev/$GCP_PROJECT/$ARTIFACTSREPO/$IMAGE:prod --memory $MEMORY --region $GCP_REGION

delete_prod_deployment:
	gcloud run services list
	gcloud run services delete $IMAGE
