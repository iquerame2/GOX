# Copyright 2021 <Alex DANDURAN--LEMBEZAT>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Handles connections and requests to the neo4j database

The `DatabaseInstance` class contains all information related to the database and how to connect to it.
It also has methods to add or remove some basic components of the basic topology that we provide (hosts, switches, links).

The language used to query neo4j graph databases is Cypher.
"""

from neo4j import GraphDatabase
from pox.core import core

log = core.getLogger()

class DatabaseInstance(object):

    def __init__(self, uri, username, password):
        self.uri = uri
        self.username = username
        self.password = password
        self.driver = None
        self.session = None

        self.connect()
        self.reset()

        log.info("DatabaseInstance launched")
    
    def connect(self):
        """
        Establishes the connection with the neo4j database thanks to the scheme,
        the ip (usually localhost) and the port on which the database is listening
        """
        self.driver = GraphDatabase.driver(self.uri, auth=(self.username, self.password))
        self.session = self.driver.session()

    def remove(self, name):
        """
        docstring
        """
        query = '''CALL apoc.trigger.remove(name)'''
        self.session.run(query)
        
    def removeAll(self):
        """
        docstring
        """
        query = '''CALL apoc.trigger.removeAll()'''
        self.session.run(query)

    def addProperty(self, nameprop):
        query = '''
                CALL apoc.trigger.add('setAllConnectedNodes','UNWIND apoc.trigger.propertiesByKey({assignedNodeProperties},"{surname}") as prop
                WITH prop.node as n
                MATCH(n)-[]-(a)
                SET a.surname = n.surname', {phase:'after'})
                '''.format(surname=nameprop)
        self.session.run(query)
        
    def addLabel(self, oldlabel, newlabel):
        query = ''' 
                CALL apoc.trigger.add('updateLabels',"UNWIND apoc.trigger.nodesByLabel({removedLabels},'{oldlabelname}') AS node
                MATCH (n:"{oldlabelname}")
                REMOVE n:"{oldlabelname}" SET n:"{newlabelname}" SET node:"{newlabelname}", {phase:'before'})
                '''.format(oldlabelname=oldlabel, newlabelname=newlabel)
        self.session.run(query)

    def connectNodeHost(self, mac, list):
        query = '''
                CALL apoc.trigger.add('create-rel-new-node',"UNWIND {createdNodes} AS h
                MATCH (h:Host {{mac: "{host_mac}"}})
                WHERE h:Host AND h.mac IN "{list_mac}"
                CREATE (n)-[link:Connected_to]->(m)", {phase:'before'})
                '''.format(host_mac=mac, list_mac=list)
        self.session.run(query)
        
    def connectNodeSwitch(self, name, list):
        query = '''
                CALL apoc.trigger.add('create-rel-new-node',"UNWIND {createdNodes} AS s
                MATCH (s:Switch {{name: "{switch_name}"}})
                WHERE s:Switch AND s.name IN "{list_name}"
                CREATE (n)-[link:Connected_to]->(m)", {phase:'before'})
                '''.format(switch_name=name, list_name=list)
        self.session.run(query)
        
    def pauseTrigger(self, name):
        query ='''
                CALL apoc.trigger.pause("{trigger_name}")
                '''.format(trigger_name=name)
        self.session.run(query)
        
    def resumePauseTrigger(self, name):
        query ='''
                CALL apoc.trigger.resume("{trigger_name}")
                '''.format(trigger_name=name)
        self.session.run(query)
    
    

   

def launch():
    print("gox_trigger is not meant to be executed alone. You should execute gox which handles the execution of the required scripts.")


