# cloudbeds.app.s3demo
Cloudbeds - App - S3Demo

## Overview

cloudbeds.app.s3demo is an application designed to run as a container on Kubernetes which features functionality to connect to AWS S3 Bucket and outputs all of its contents in json format over http.

## Getting started

### Install the helm-s3 plugin for Amazon S3.

To install the helm-s3 plugin on your client machine, run the following command:
`helm plugin install https://github.com/hypnoglow/helm-s3.git`

### Initialize an S3 bucket as a Helm repository

Create a unique S3 bucket. In the bucket, create a folder called stable/myapp. The example in this pattern uses s3://my-helm-charts/stable/myapp as the target chart repository.
To initialize the target folder as a Helm repository, use the following command:
`helm s3 init s3://cloudbeds-helmrepo/stable/cloudbeds.app.s3demo`
The command creates an `index.yaml` file in the target to track all the chart information that is stored at that location.

### Verify the newly created Helm repository.

To verify that the index.yaml file was created, run the following command:
`aws s3 ls s3://cloudbeds-helmrepo/stable/cloudbeds.app.s3demo`

### Add the Amazon S3 repository to Helm on the client machine.

To add the target repository alias to the Helm client machine, use the following command:
`helm repo add stable-cloudbeds.app.s3demo s3://cloudbeds-helmrepo/stable/cloudbeds.app.s3demo/`

### Package and publish charts in the Amazon S3 Helm repository

To package the chart that you created, use the following command:
`helm package cloudbeds.app.s3demo-chart --debug`
As an example, this pattern uses the `cloudbeds.app.s3demo-chart` chart. The command packages all the contents of the cloudbeds.app.s3demo-chart chart folder into an archive file, which is named using the version number that is mentioned in the `Chart.yaml` file. If you want to create a new chart, you can use the command `helm create myapp-new-chart` and run `helm lint` for any potential issues with the chart.

To upload the local package to the Helm repository in Amazon S3, run the following command:
`helm s3 push cloudbeds.app.s3demo-chart-0.1.0.tgz stable-cloudbeds.app.s3demo`

### Refreash repository configurations

To update the repo local cache and get the latest release list, run the following command:
`helm repo update`

To verify to push process works and list all new and previous versions of a particular application chart, use the following command:
`helm search repo stable-cloudbeds.app.s3demo --versions`

### Deploying the application via Helm

To deploy the latest version of the chart, you can use the command below while passing the environment variable values for `AWS_BUCKET_NAME` which is the AWS S3 Bucket name the application will connect to along with the `AWS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` which are the AWS account Authentication information used by the application to connect to your AWS account to access the S3 bucket contents:
`helm install s3demo stable-cloudbeds.app.s3demo/cloudbeds.app.s3demo-chart --namespace cloudbeds-ns --set "AWS_BUCKET_NAME=cloudbeds-helmrepo" --set "AWS_KEY_ID=yourAwsKeyId" --set "AWS_SECRET_ACCESS_KEY=yourAwsSecretAccessKey"`

## Building and Running the Docker Image

### Building the Docker Image

To start the docker build process, make sure you are located within the Dockerfile directory and run the build command:
`docker build --tag carlcauchi/cloudbeds.app.s3demo .`

Once completed, TAG the docker image with the version number, such as `1.0.0` along with the `latest` tag as per below example:
`docker tag carlcauchi/cloudbeds.app.s3demo:latest carlcauchi/cloudbeds.app.s3demo:0.0.1`

### Pushing the Docker Image to a Public Registry

Push the Docker image to a Container Registry, the example below shows how to push the image to a public docker registry:
`docker push carlcauchi/cloudbeds.app.s3demo`
You can view the repository here: `https://hub.docker.com/repository/docker/carlcauchi/cloudbeds.app.s3demo`

### Running and Testing the application within a docker environment

An example below show you how to run the docker image as a docker containers locally for troubleshooting purpose:
`docker run --rm -it --env "AWS_BUCKET_NAME=cloudbeds-helmrepo" --env "AWS_KEY_ID=yourAwsKeyId" --env "AWS_SECRET_ACCESS_KEY=yourAwsSecretAccessKey" --env "AWS_REGION_NAME=eu-west-1" --env "DEBUG_MODE=True" --publish 5000:80 --name cloudbeds.app.s3demo-container carlcauchi/cloudbeds.app.s3demo`