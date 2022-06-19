# WIP

This page is still work in progress, and the instructions for installing and using GOX will improve in the following week,
thank you

# GOX

GOX is a suite of POX components that allow the development of SDN applications that rely on a Neo4j Graph Database-based network topology.

GOX was developed as part of 3-months intership in the ENSIIE engineering school in Evry, France.

## GOX core components

GOX is composed of 3 main core components :

1. **gox**: It is the main component which is tasked with properly starting GOX by launching every secondary components which are essentials 
2. **gox_db**: It is GOX's Neo4j database management component. It handles connections and requests heading to the Neo4j database
3. **gox_network**: It is the script that handles network events and other network functions that GOX requires. It uses *gox_db* script so as to communicate with the database

## GOX's dependencies

The functioning of GOX also depends on the 2 following POX components : 

1. **openflow.discovery**: For registering the connectivity between switches
2. **host_tracker**: For gathering information on the hosts on the network

# Installation

## Requirements

* GOX depends on Python 3 and was developed using Python 3.9.

* GOX depends on POX to function. So make sur you have POX's latest version. All the necessary information on how to install and use POX can be found in [POX's documentation](https://noxrepo.github.io/pox-doc/html/)

* To work, GOX needs to be able to connect to a [Neo4j](https://neo4j.com/) database. You can use [Neo4j Server](https://neo4j.com/docs/browser-manual/current/deployment-modes/neo4j-server/) or [Neo4j Desktop](https://neo4j.com/docs/browser-manual/current/deployment-modes/neo4j-desktop/) to create a graph database. 


## Installing GOX

Once you have installed POX and have your Neo4j database up and running, simply copy the python scripts *gox.py*, *gox_db.py* and *gox_network.py* (located in the *gox/* folder) to POX's *ext/* directory.

# Usage

GOX can be started like any other POX component. Only the main core component of GOX called "gox" should be started. Indeed, this component will also launch *gox_db*, *gox_network*, *openflow.discovery* and *host_tracker*

## Quickstart:

```bash
./pox.py gox --uri="bolt://localhost:7687"
```

## Arguments

To be able to connect properly to the Neo4j database, you have to specify a few arguments:

* **uri**: address of the Neo4j database. In the previous example, "bolt" is the protocol method used to connect to Neo4j, and it can differ for you. The port may change as well.
* **username**: username for the Neo4j database. By default, GOX will consider the username to be "neo4j", like Neo4j's default user.
* **password**: password associated to the username of the Neo4j database. By default, it is "password". You should change it!

## Summary

```bash
./pox.py gox --uri="<protocol>://<ip/hostname>:<port>" --username="<username>" --password="<password>"
```

# GOX applications

## GOX's L2 forwarding application

GOX is shipped with a Proof-of-Concept level 2 forwarding application which calculates the shortest path between two hosts on network. You should take a look at it if you want to develop new graph-based SDN applications using GOX.

To use it, simply copy the associated Python script from GOX's repository in the *app/* folder to POX's *ext/* directory and execute it this way:

```bash
./pox.py gox <arguments> gox_l2_forwarding
```

## Developing GOX applications

GOX allows you to develop SDN applications using a powerful graph database. The network topology is stored within this database, and applications can communicate with it for implementing new logic on the network.

GOX provides methods within the *gox_db* component for interacting with the database for very simple tasks. However, it will not be sufficient for more complexe mechanisms, so you should take a look at how to query the Neo4j database using Cypher. 

Executing GOX applications is the same as executing POX applications, so you should take a look at [POX's documentation](https://noxrepo.github.io/pox-doc/html/). 

# Acknowledgments 

I would like to thank Fetia BANNOUR and Stefania DUMBRAVA with whom I worked to create GOX.

I am also grateful to the ENSIIE engineering school in Evry, France, and all its staff for giving me the opportunity to understand SDN, graph databases and to develop GOX.

# Contact

If you have any questions on GOX, how to use it, how to develop GOX applications or if you want to improve GOX, you can send me an e-mail at [alex@danduran.fr](mailto:alex@danduran.fr)
