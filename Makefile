deps:
	pip install -r requirements.txt

create-jenkins-jobs:
	nestor create-job "Brew Coffee" jenkins-data/job_config_success_1.xml
	nestor create-job "Feed The Cat" jenkins-data/job_config_success_2.xml
	nestor create-job "Dim Light" jenkins-data/job_config_success_3.xml
	nestor create-job "Wash Dishes" jenkins-data/job_config_failure_1.xml
	nestor create-job "Vacuum Living Room" jenkins-data/job_config_failure_2.xml
	nestor create-job "Call Lady Gaga" jenkins-data/job_config_failure_3.xml

delete-jenkins-jobs:
	nestor delete-job "Brew Coffee"
	nestor delete-job "Feed The Cat"
	nestor delete-job "Dim Light"
	nestor delete-job "Wash Dishes"
	nestor delete-job "Vacuum Living Room"
	nestor delete-job "Call Lady Gaga"

deploy-lambda-webhooks:
	cd lambda-webhooks && chalice deploy

delete-lambda-webhooks:
	cd lambda-webhooks && chalice delete

.PHONY: deps create-jenkins-jobs delete-jenkins-jobs deploy-lambda-webhooks delete-lambda-webhooks
