from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2
from diagrams.aws.analytics import EMR
from diagrams.aws.database import DynamodbTable
from diagrams.c4 import Person, Container, Relationship
from diagrams.generic.os import Windows
from diagrams.generic.virtualization import Virtualbox
from diagrams.ibm.user import Browser

graph_attr = {
    "splines": "spline",
}

with Diagram(graph_attr=graph_attr):
    user = Person(
        name="User", description="A user"
    )

    qa = Person(name="Manual QA")

    with Cluster("App"):
        dapp = Container(
            name="Desktop application",
            description="Desktop application description",
        )
        [dapp, EMR("DB local")]

    with Cluster("Test desktop app"):
        tdapp = Container(
            name="Test Application",
            technology="C#",
            description="Emulating for real application",
        )
        [tdapp, DynamodbTable("xml configuration")]

    tdapp_tests = Virtualbox("Desktop tests")
    e2e_tdapp_tests = Virtualbox("e2e da tests")
    web_tests = Virtualbox("WEB tests")
    api_tests = Virtualbox("API tests")
    cluster_tests = Virtualbox("Cluster tests")

    with Cluster("Company Project"):
        admin_ui = Browser("Web Admin UI")

        with Cluster("Windows service"):
            tpa = Windows("Third party app")
            happ = Windows("Helper app")

        with Cluster("Saas cloud"):
            api_gateway = EC2("API gateway")
            cluster_internal_services = EC2("internal \nservices")
        admin_ui >> Relationship("HTTP requests") >> api_gateway
        api_gateway >> Relationship("GRPC calls") >> cluster_internal_services
        tpa >> Relationship("Remote calls") >> happ
        happ >> Relationship("HTTP requests") >> api_gateway

    user >> dapp >> Relationship(".NET") >> tpa
    e2e_tdapp_tests >> Relationship("HTTP requests") >> tdapp
    qa >> tdapp >> Relationship(".NET") >> tpa
    qa >> Relationship("QA with access") >> dapp
    tdapp_tests >> Relationship("Remote calls") >> happ
    web_tests >> Relationship("UI interaction") >> admin_ui
    api_tests >> Relationship("HTTP requests") >> api_gateway
    cluster_tests >> Relationship("GRPC calls") >> cluster_internal_services
