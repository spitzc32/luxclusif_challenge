# luxclusif_challenge

In this repo, we ingest the data from a spark backend since if we take a look at the given data, the estimate is 20k as its shape. So for this solution, it is not optimal to use a memory based dataframe but instead we use a distributed type of dataframe not relying on a single machine due to the volume of the data.

## The challenge
To answer the challenge, here is the planned architecture overview of the data architecture:

As we can see above, the architecture would be a docker image registry being called in daily but in our case, since we don't really have a source data that updates, I did not implement the part of doing the configs and scheduler ingesting the pipeline image daily. it would be a good for cause but we don't really need that for a static data.

Now, for the pipeline, I built a python script that uses Spark to ingest and do a little transformation on our dataset. But as we can see, there is no source for this part since I omitted that part of ingesting the pipeline image daily due to the nature of the data being static. I believe this is something that should be implemented after the decision of who, whom, where and what will be the common ground for the ingested data source to be dumped into and who will be consuming these. But in an overall scenario, we can add these features if we establish the trademarks we need and validate them according to what will be the usecase.

In balancing the feature development and technical debt on working in an artifact scenario, it would be a good for first step to identify the system design and how it serves its purpose orginally to meet the SLAs of whoever uses it. In identifying that scheme, the technical aspect would be to first identify which has critical impact on the performance (which part or which feature) is then from there we can decide on what needs to be prioritized in terms of the impact to either the cost reduction/performance/customer demands. In this way, someone who will be waiting for this feature would have a clear high level overview on what needs to be addressed.

## Setup
Since this is mainly a python script just for ingestion without any scheduler formed, the Docker image in place would be the main trigger for our script on hand. We run this image as a linux container under python3.x image. This way, the versions would align in running this in your local machine.

`docker build --rm -t luxclusif-challenge .`
`docker run -t -i --rm --name luxclusif-cont luxclusif-challenge`

## Expected output
This pipeline mainly serves as a pipeline for validation and format purpose. As such, we show the schema the pipeline generates as an initial run on how we would ingest the data without compromising the analytical ability of whoever will use it in what datasource.

Output: The schema that we wrote under core/schema.py

## DB setup
simply run start.sh to establish a Docker PSQL instance

## Further Steps
Since the scheduler is not setup, due to the dataset being static, we can further implement the solution with a scheduler,
particularly Airflow, if we need to manage this or we can implement the built in tasks of Spark since this is mainly contained as a JobTask.

AS for the source, via localstack, we can implement a script to run an instance of a data warehouse but this needs to be set up in a way where we can do an agreement on how it will be used.

