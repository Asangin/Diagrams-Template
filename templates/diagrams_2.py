from diagrams import Diagram
from diagrams.c4 import Container, System

graph_attr = {
    "splines": "spline"
}

with Diagram(graph_attr=graph_attr):
    release = System("System", type="")

    env_1 = release >> Container("Env 1", style="rounded,filled")
    env_2 = release >> Container("Env 2", shape="circle")
    env_3 = release >> Container("Env 3")

    em1 = env_1 >> Container("M", fillcolor="red")
    ea1 = env_1 >> Container("A", width="1.3", height="0.5")
    em2 = env_2 >> Container("M", fontcolor="black")
    ea2 = env_2 >> Container("A", fontcolor="yellow")
    em3 = env_3 >> Container("M")
    ea3 = env_3 >> Container("A")

    em1 >> Container("TS 1", description="Some description", shape="oval")
    ea1 >> Container("TS 2",description="Some description", shape="hexagon")
    em2 >> Container("TS 3", description="Some description", shape="rhombus")
    ea2 >> Container("TS 4",description="Some description", shape="square")
    em3 >> Container("TS 5",description="Some description", shape="parallelogram")
    ea3 >> Container("TS 6", description="Some description", shape="pentagon")

