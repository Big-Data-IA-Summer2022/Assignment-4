# Assignment-4
Part 1: Automating Benchmarking of datasets.

Summary: In companies, there has been a significant impetus to ensure data quality is understood and methods implemented to ensure the data used for modeling is of the highest quality. With Data-centric approaches (https://spectrum.ieee.org/andrew-ng-data-centric-ai (Links to an external site.) ) becoming adopted as a way of enhancing AI/ML model building techniques, conferences and academic workshops are now adding tracks to foster research in this new area. See the paper and video below for more on the topic

Paper: https://arxiv.org/pdf/2207.10062.pdf (Links to an external site.)

Video: https://slideslive.com/38970646/dataperf-benchmarking-data-for-better-ml?ref=search-presentations-dataprep (Links to an external site.) 

Tasks:

For this assignment, you will focus on the vision debugging challenge codebase (https://github.com/DS3Lab/dataperf-vision-debugging (Links to an external site.) ) we worked on in the class. The goal is to automate the application so that you can trigger a benchmarking task from dataperf using Airflow.

For this, you will have to:

Store data  at a location of your choice so you can reference it when needed
Create an AIRFLOW DAG to run the job.
Create a streamlit application so you can input:
The model
Number of Train, test, Validate
Other parameters (like noise)
Once you get the parameters from streamlit, you will have to create a new task_setup.yml file. See https://medium.com/@luongvinhthao/generate-yaml-file-with-python-and-jinja2-9474f4762b0d (Links to an external site.) for an example on how to use python and ninja to create a yaml file.
Validate the yaml file. Your Airflow DAG shouldn’t run if the Yaml file can’t be parsed!
Deploy the AIRFLOW DAG so that you can trigger the job on the fly from Streamlit.
Once the Airflow job completes, you should be able to come back to the Streamlit appts see the results. (The generated images from the benchmarking app should be viewed on Streamlit)
Create a GitHub and a google code labs doc detailing your design, how to use it with links to the running application.
Additional notes:

You could use Airflow as a managed service (https://aws.amazon.com/managed-workflows-for-apache-airflow/pricing/ (Links to an external site.) )
OR

install your own Airflow on a Ec2 or GCP instance. (See https://towardsdatascience.com/running-airflow-with-docker-on-ec2-ci-cd-with-gitlab-72326d4baeb4  (Links to an external site.)for ideas)

To trigger the DAG, you can either use
A local client
REST API : https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html (Links to an external site.). See https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/trigger_dagrun/index.html (Links to an external site.) too and research the best way to do it. 
You can determine where to store the data. Either S3 or Google storage should work.
Note: Everything needs to be deployed. Don’t use local instances.
 

Part 2: Technology evaluation

As a part of your careers, you will be evaluating multiple technologies. In the prior part, you noted that the benchmarking was done using a package called data scope. Datascope and many other projects are part of the easeml project. See details below:

Video:
https://www.youtube.com/watch?v=YMG3O5wZNBc&feature=emb_logo (Links to an external site.)
 

Paper: https://www.cidrdb.org/cidr2021/papers/cidr2021_paper26.pdf (Links to an external site.) 

Reference: https://github.com/easeml (Links to an external site.) 

Tasks:

Your task is to review the assigned project and do a demo of the working project.  Also summarize:

What the project does?
How to use it?
Possible use cases where this project would be useful?
Strengths of the project
Weakness/ areas of Improvement for the project.
