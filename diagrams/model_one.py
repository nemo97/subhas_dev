# diagram.py
from diagrams import Diagram,Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.database import ElasticacheForRedis
from diagrams.aws.compute import LambdaFunction as Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import Route53,DirectConnect
from diagrams.onprem.network import Apache
from diagrams.aws.security import Cognito
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

from diagrams.aws.network import ELB
graph_attr = {
    "splines": "spline",
}

with (Diagram("model_one",outformat="png", show=False,graph_attr=graph_attr,direction="LR")) as diag:

    customer = Person(
        name="US Internet User", description="User in the US"
    )


    with SystemBoundary("Tomcat") as us:
        # dns = Route53("dns")
        # lb  =  ELB("lb")
        # db  =  RDS("GatesDB")
        # gems_db  =  RDS("GemsDB")
        # vcsc_db  =  RDS("VcscDB")
        #serverlessNode = Lambda("User NodeJS")
        #serverlessApi = Lambda("API NodeJS")
        #auth = Cognito("oAuth 2 Service")


        with Cluster("APP.WAR") as app_war:
             workerBackend = [("worker1"), EC2("worker2")]


        #>>  >> Cluster("Spring Backend") EC2("")  >> RDS("userdb")
        # customer >> dns >> lb >>  serverlessApi >> workerBackend
        # serverlessApi >> auth 
        # workerBackend >> auth
        # workerBackend >> db
        # workerBackend >> gems_db
        # workerBackend >> vcsc_db        
        # workerBackend >> ElasticacheForRedis("Redis Cache")
        #>> workerBackend >> db

 
