# AWS Big Data Analytics Architecture
2019-03-21

----------

This document outlines my suggested AWS architecture for a hypothetical big data analytics platform. At a high level my recommended design is an Amazon SageMaker instance for big data model computation and Redshift for a scalable and queryable data store with intermediate S3 storage. I also discuss additional technologies and as well as other intermediate architectures that can be used to validate and refine the ultimate design.

I’ve broken each requirement into its own section containing:

- My initial architecture recommendations
- Alternate technologies I considered
- Open questions I would want to further explore
- Relevant documentation.

At the end of the document I also outline an iterative deployment plan that would allow for continuous evaluation and improvement of the proposed architecture as new resources are added.

This was a really fun research project for me as I got to do a lot of really rewarding research! I’ve wanted to dig more into this topic since I attended AWS Re:Invent last November. I have varying degrees of familiarity with most of the AWS tools I've used in the architecture, I've written code against some of them, but this was my first time laying out an architecture of more than a few AWS resources.

I think there is still a lot of additional research and testing required to validate my architecture proposal but I think this outline accurately reflects my experience and thought processes. I hope my work demonstrates my ability to quickly get up to speed on new technologies as well as my ability to ask critical design questions when laying out a technical solution.

## Self-Service Big Data Feature Extraction
> The data science team wants to perform self-service feature extraction with a pandas-like experience on datasets larger than single machine memory.

Assuming the feature extraction can be parallelized into some type of map-reduce workflow and bearing in mind the a self-service Python data scientist as the end user we could employ a **Jupyter Notebook** running **PySpark** for our analysis (this gives a pandas-like experience) .

The key decision is how to build a architecture around this. For both this and the next requirement I decided to use **Amazon SageMaker**. This gives us a hosted Jupyter notebook with with PySpark integration as well as several other preloaded ML algorithms. SageMaker also manages our instance allocation. For our data storage at this point we can use **Amazon Simple Storage Service (S3)** to store our data objects. ETL can be performed within the same SageMaker notebooks or sequentially in a separate notebook. The code can be version controlled with Amazon **CodeCommit** or **Git** (GitHub, GitLab, Stash).

An additional option I considered was to use **Amazon Elastic Map Reduce (EMR)** as a hosted cluster while running the Jupyter notebooks on SageMaker and connecting these two with **Livy** which allows SageMaker and EMR to communicate over REST. I decided against this because I prefer to start with as few services as possible, and it’s not immediately apparent to me the benefits of this approach just running SageMaker.

**Additional Questions:**

- What are common big data algorithms in application domain?
****- When would as stand-alone EMR instance be preferable to a SageMaker Instance?
- What are the possible data units in this space?
- If we use Spark do we still need to make a HDFS choice for the spark cluster?
- How is SageMaker priced and are there any inflection points as cost scales?

**References:**

- https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html
****- https://aws.amazon.com/blogs/machine-learning/build-amazon-sagemaker-notebooks-backed-by-spark-in-amazon-emr/

## Production Data Models
> The data science teams wants an infrastructure to feed data, and persist the results for each trained model version they publish.

SageMaker allows us to deploy production data models as **Docker** images to **Amazon Elastic Container Service (ECS).**  Since we want to get new predictions as data comes in we can use SageMaker to set up a persistent endpoint using **SageMaker Hosted Services**. We then have a few options to generate the HTTP request to our model endpoint depending on how the the data is coming in. One option would be to use **AWS Lambda Functions** to send the requests. The results can be stored in S3 where they can be accessed as is and/or pushed to other data stores depending on how the results are used.

I also looked at **Apache Airflow** because it’s mentioned in some of the research I did. Airflow is workflow management platform that could be used to build mode complicated model workflows. Airflow integrates with SageMaker as of 2018 so these are not incompatible technologies.

**Questions:**

- What other data pipeline services could be useful here: Glue, StepFunctions?
- Is the feed for the data models the same data used in the next section?
- What are the data model outputs and how are they used?

**References:**

- https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-deploy-model.html
- https://aws.amazon.com/about-aws/whats-new/2018/11/amazon-sagemaker-is-now-integrated-with-apache-airflow/

## Scalable and Queryable Infrastructure
> The CTO wants a linearly scalable data storage and SQL query infrastructure that fits with a cloud-native (AWS) infrastructure and (cost-aside) can maintains SLAs regardless of number of partners or size of the data.

I think these requirements point towards **Amazon Redshift** which as a hosted database cluster designed for these applications. You can query your stored data in a SQL like manned and  **Redshift Spectrum** allows you to extent your queries into your “data lake” by enabling direct querying of S3 contents. Otherwise you can use **AWS Glue** to directly stream data into redshift.

I also considered **Amazon Relational Database Service (RDS)** using a standard engine like PostgresSQL (Redshift is based on Postgres) but the question seems to be implying more extreme requirements. However RDS could serve as an intermediate data solution if for example it is significantly easier/faster/cheaper to spin up an RDS instance while still evaluating the benefits of the architecture or the business value of the pipeline as a whole. Data could then be moved over using **Amazon Database Migration Service (DMS)**. This would also allow us to establish more standard cost and performance benchmarks in order to better evaluate Redshift.

Along the same lines of prototyping Redshift with an RDS instance until we can validate our architecture and our project value, we can use **Amazon Athena** to validate the value of using Redshift Spectrum. Athena is a serverless interactive query service that allows you write SQL queries against S3 buckets; however at $5 per terrabyte scanned this would be too expensive for anything other than rare queries or a proof of concept.

**Additional Questions:**

- What are the SLAs for Redshift?
- How is Redshift different from Postgres
- What connects should we use to get data into Redshift from different services?

**References:**

- https://aws.amazon.com/redshift/
- https://aws.amazon.com/dms/
- https://docs.aws.amazon.com/redshift/latest/dg/proof-of-concept-playbook.html

## Data Query Infrastructure
> The data visualization product team wants the data query infrastructure to deliver consistent low single-digit (seconds) response time for aggregate queries regardless of data volume.

The same architecture can be initially be used here as in previous CTO question. The type of performance in the question requires a complete understanding of what questions the end user wants to answer and may want to answer in the future. This mutual understanding is critical to designing a useful data model with the number of attributes and appropriate indexes.

Depending on the questions the visualization team wants to ask multiple data stores might be necessary to provide the right combination of columnar-data, key-value stores, and time-series data. Depending on the configuration these data stores can use native integrations to broadcast data incoming to one another or be connected by pipeline applications such as Lambda workers or Glue.

## Additional Use Case
> As Engineering lead for the Analytics platform I want, well … analytics on how my system is performing and what it’s up to.

In order to monitor statistics like resources allocation and data volume in this system I would want some type of analytics dashboard. I am most familiar with **Grafana** which can have a variety of data sources and integrations specifically **Amazon CloudWatch**. Additionally, I’ve heard very good things about **DataDogs** on AWS for system analytics. In either case I would be concerned with make sure I can track metrics like bucket sizes, instance disk, memory, and CPU utilization, PySpark jobs being ran and their duration, deployments of model version to production, etc.

**Resources:**

- https://aws.amazon.com/marketplace/pp/B01LYD359R
- http://docs.grafana.org/features/datasources/cloudwatch/

## Deployment, Development, Etc.

Following the "infrastructure as code" trend in cloud DevOps either **Amazon CloudFormation** or **Hashicorp Terraform** could be used to create a deployment template. This could be used to create staging and production infrastructures. We could then iteratively test architecture changes as we tune existing services, replace services, or add new functionality without effecting production. This iterative testing and development in two environments is a key part of how I would go about validating my architecture.

Most AWS services offer native connections to other services, where this is not an option something like a lambda function can be used calling the **boto** library or requests for messaging over HTTP. For testing the **moto**, **responses**, **localstack** Python libraries could be used.

Lastly, a key part of any major engineering task for me is always talking to others get get feedback and ideas. In this case this would past and present colleagues who have designed these types of architectures, and potentially even AWS solutions architects.

