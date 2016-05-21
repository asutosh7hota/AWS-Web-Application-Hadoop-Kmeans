# AWS-Web-Application-Hadoop-Kmeans
AWS Web Service which demonstrates the use of Hadoop, Kmeans and visualization using D3 <br />

<b>This projects mainly consists of  four areas: </b><br />
# 1. Hadoop Mappers and Reducers: 
Using the mappers and reducers which validates the dataset and fetch the required information needed for logical calculations.
In this using the mappers and reducers to find the weather stations which have min rainfall and max rainfall and display them in bar charts and line charts. <br />
# 2. Kmeans:
Using the kmeans python library from sklearn have used Kmeans clustering in order to cluster the earthquakes that had taken place this month (April), and displaying the information on a scatter plot. <br />
# 3. Visualization D3:
Using D3.js library to display bar charts, line charts and scatter plots on the web service.
# 4. Auto Scaling:
A document to showing how to balance the load of the web application using load balancer, auto-scale group and launch configuration.
Based on the configuration was able to ensure that the response returned for testing for 100 concurrent users was <10 secs for display. (Tested using Apache JMeter)

# Issues faced:
1. Hadoop did not work well with flask <br />
2. Kmeans did not work well with flask <br />

# Solutions found:
1. In order to make hadoop work, created another program that would run hadoop seperately by sockets i was able to pass data from flask to backend code to run the application. <br />
2. In order to make Kmeans work, created another program that would run kmeans and generate the clusters needed for the flask application, the data was passed too and foe using sockets <br />

# Technologies used:
1. Flask <br />
2. Kmeans Sk-learn <br />
3. nvd3 python library for generating graphs in d3 <br />
4. hadoop single node cluster setup
5. AWS EC2 instances 
