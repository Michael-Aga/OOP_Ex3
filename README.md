
# Weighted directed graphs

<img src="https://user-images.githubusercontent.com/62290677/146029438-b362acb8-3da2-4181-893c-aa9820e1ca57.png" alt="drawing" width="650"/>

Create a weighted graph and tests shown below:




## Creators

 - [Goel Didi](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
 - [Michael Agarkov](https://github.com/matiassingers/awesome-readme)




#  Classes: 
## NodeData:
- Node class **:** It holds the values of the Node and Edges from this node to other nodes or other nodes to this node, and key for unique ID and his location.


## DiGraph
###### the class import GraphInterface that represents an interface of a graph.

- #### v_size: Returns the number of vertices in this graph.
- #### e_size: Returns the number of edges in this graph.
- #### get_all_v: return a dictionary of all the nodes in the Graph, each node is represented using a pair (node_id, node_data)
- #### all_in_edges_of_node: return a dictionary of all the nodes connected to (into) node_id , each node is represented using a pair (other_node_id, weight)
- #### all_out_edges_of_node: return a dictionary of all the nodes connected from node_id , each node is represented using a pair (other_node_id, weight)
- #### get_mc: The current version of this graph.
- #### add_edge: Adds an new edge to the graph.
- #### add_node: Adds a new node to the graph.
- #### remove_node: Remove a specific node from the graph.
- #### remove_edge: Remove an specific edge from the graph.

## GraphAlgo
 #### This is the graphClass that all the algorithms would operate in.

We create a graph from the previous class, and on that we will run the algorithm.
- #### get_graph: returns the graph that we preforms the algorithms on.
- #### load_from_json: Loads a graph from a json file.
- #### save_to_json: Saves the graph in JSON format to a file.
- #### shortest_path: finds the shortest path between two nodes that the function receive and returns the distance and a list of the path itself.
- #### TSP: Finds the shortest path that visits all the nodes in the list of our Graph.
- #### centerPoint: Finds the node that has the shortest distance to it's farthest node.
- #### plot_graph: Plots the graph. If the nodes have a position the nodes will be placed there.
  #### Otherwise, they will be placed in a random spot.

## matplotlib
- #### This is a class that receives a graph after the creation of nodes and the edges and the class creates a graphical interface on the screen:
- #### plot_graph - we using this in GraphAlgo class and the function takes the lists of the graph that include the position of the nodes and the eges that connect the nodes and draw it on our screen like that (A3): ![A3](https://user-images.githubusercontent.com/88629415/147497833-c82c2205-0c25-449e-a7ae-293233eeab8d.png)

# Run time

#### A0,A2,A3 Tests

![tsp](https://user-images.githubusercontent.com/88629415/147494496-5abca55a-845d-4300-a37c-04cbc4bfd52f.png)
![center](https://user-images.githubusercontent.com/88629415/147494527-cbfe2242-2cc2-4e1e-9de5-ff4390d548b2.png)
![shortest](https://user-images.githubusercontent.com/88629415/147494566-7b5b79e3-7e8d-4d71-b666-bffd1e16072d.png)
![load](https://user-images.githubusercontent.com/88629415/147494585-cdb71b6d-c545-443d-a455-987f0937826e.png)
![save](https://user-images.githubusercontent.com/88629415/147494600-ffa9ec7f-563e-44f6-98ba-d8a775ce9cf2.png)









# UML

![src_uml](https://user-images.githubusercontent.com/88629415/147495726-8a84f887-f357-4764-a78e-2d1178334fd0.png)


## Run Locally

Clone the project

```bash
  git clone https://github.com/Michael-Aga/OOP_Ex3.git
```

 ### The project can run in 2 ways:
 #### 1) use one of the existing tests in the main or build a graph yourself:
![1](https://user-images.githubusercontent.com/88629415/147498965-cb2ab496-5515-41a3-b1c2-a4b188066616.png)

 #### 2) load json file * and Write down the functions you want to test ** :
![2](https://user-images.githubusercontent.com/88629415/147499001-6c053937-dc3b-4aeb-9aeb-7bd72a667dc0.png)


