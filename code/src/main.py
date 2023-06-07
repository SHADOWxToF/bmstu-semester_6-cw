from neo4j import GraphDatabase
from fastapi import FastAPI
from connection import Connection

app = FastAPI()


# CREATE

@app.post("/post/noun")
def post_noun(role: str="doctor", noun: str="enim", path: str="images/enim.png"):
    con = Connection(role)
    try:
        result = con.run(f"merge (n:noun {{text: '{noun}', image: '{path}'}}) return n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'noun' : nodes[0]}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}
        

@app.post("/post/obAction")
def post_obAction(role: str="doctor", obAction: str="eu", path: str="images/eu.png"):
    con = Connection(role)
    try:
        result = con.run(f"merge (n:obAction {{text: '{obAction}', image: '{path}'}}) return n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'obAction' : nodes[0]}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}


@app.post("/post/subAction")
def post_subAction(role: str="doctor", subAction: str="lectus", path: str="images/lectus.png"):
    con = Connection(role)
    try:
        result = con.run(f"merge (n:subAction {{text: '{subAction}', image: '{path}'}}) return n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'subAction' : nodes[0]}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}


@app.post("/post/adjective")
def post_adjective(role: str="doctor", adjective: str="rhoncus", path: str="images/rhoncus.png"):
    con = Connection(role)
    try:
        result = con.run(f"merge (n:adjective {{text: '{adjective}', image: '{path}'}}) return n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'adjective' : nodes[0]}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}


@app.post("/post/owner")
def post_owner(role: str="doctor", owner: str="Lorem ipsum", date: str="2005-02-15", desease: str="Lorem ipsum dolor sit amet"):
    con = Connection(role)
    try:
        result = con.run(f"merge (n:owner {{name: '{owner}', date: datetime('{date}'), desease: '{desease}'}}) return n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'owner' : nodes[0]}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/noun2adjective")
def post_noun2adjective(role: str="doctor", noun: str="enim", adjective: str="rhoncus"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:noun {{text: '{noun}'}}), (m:adjective {{text: '{adjective}'}}) merge (n)-[:have]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/noun2subAction")
def post_noun2subAction(role: str="doctor", noun: str="enim", subAction: str="lectus"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:noun {{text: '{noun}'}}), (m:subAction {{text: '{subAction}'}}) merge (n)-[:is_done]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/noun2obAction")
def post_noun2obAction(role: str="doctor", noun: str="enim", obAction: str="eu"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:noun {{text: '{noun}'}}), (m:obAction {{text: '{obAction}'}}) merge (n)-[:doing]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/subAction2adjective")
def post_subAction2adjective(role: str="doctor", subAction: str="lectus", adjective: str="magna"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:subAction {{text: '{subAction}'}}), (m:adjective {{text: '{adjective}'}}) merge (n)-[:have]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/obAction2adjective")
def post_obAction2adjective(role: str="doctor", obAction: str="eu", adjective: str="tincidunt"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:obAction {{text: '{obAction}'}}), (m:adjective {{text: '{adjective}'}}) merge (n)-[:have]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/owner2noun")
def post_owner2noun(role: str="doctor", owner: str="Lorem ipsum", noun: str="enim", path: str="images/enim.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}}), (m:noun {{text: '{noun}', image: '{path}'}}) merge (n)-[:own]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/owner2obAction")
def post_owner2obAction(role: str="doctor", owner: str="Lorem ipsum", obAction: str="eu", path: str="images/eu.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}}), (m:obAction {{text: '{obAction}', image: '{path}'}}) merge (n)-[:own]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/owner2subAction")
def post_owner2subAction(role: str="doctor", owner: str="Lorem ipsum", subAction: str="lectus", path: str="images/lectus.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}}), (m:subAction {{text: '{subAction}', image: '{path}'}}) merge (n)-[:own]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.post("/post/owner2adjective")
def post_owner2adjective(role: str="doctor", owner: str="Lorem ipsum", adjective: str="tincidunt", path: str="images/tincidunt.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}}), (m:adjective {{text: '{adjective}', image: '{path}'}}) merge (n)-[:own]->(m) return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}


# READ

@app.get("/get/all")
def get_allNodes(role: str="doctor"):
    con = Connection(role)
    try:
        result = con.run("match (n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.get("/get/allByOwner")
def get_allNodesByOwner(role: str="doctor", owner: str="Lorem ipsum"):
    con = Connection(role)
    try:
        result = con.run(f"match (n) where (:owner {{name: '{owner}'}})-->(n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}


@app.get("/get/all_nouns")
def get_all_nouns(role: str="doctor", owner: str="Lorem ipsum"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:noun) where (:owner {{name: '{owner}'}})-->(n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.get("/get/subActionsByNoun")
def get_subActions(role: str="doctor", owner: str="Lorem ipsum", noun: str="lorem"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:subAction) where (:owner {{name: '{owner}'}})-->(n) and (:noun {{text: '{noun}'}})-->(n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.get("/get/obActionsByNoun")
def get_obActions(role: str="doctor", owner: str="Lorem ipsum", noun: str="lorem"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:obAction) where (:owner {{name: '{owner}'}})-->(n) and (:noun {{text: '{noun}'}})-->(n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.get("/get/adjectiveByNoun")
def get_adjectiveByNoun(role: str="doctor", owner: str="Lorem ipsum", noun: str="lorem"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:adjective) where (:owner {{name: '{owner}'}})-->(n) and (:noun {{text: '{noun}'}})-->(n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.get("/get/adjectiveByObAction")
def get_adjectiveByObAction(role: str="doctor", owner: str="Lorem ipsum", obAction: str="lorem"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:adjective) where (:owner {{name: '{owner}'}})-->(n) and (:obAction {{text: '{obAction}'}})-->(n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.get("/get/adjectiveBySubAction")
def get_adjectiveBySubAction(role: str="doctor", owner: str="Lorem ipsum", subAction: str="lorem"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:adjective) where (:owner {{name: '{owner}'}})-->(n) and (:subAction {{text: '{subAction}'}})-->(n) RETURN n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'results' : len(nodes), 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}


# UPDATE

@app.patch("/patch/noun")
def patch_noun(role: str="doctor", owner: str="Lorem ipsum", noun: str="enim", path: str="images/enim.png", new_path: str="images/enim.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}})-->(m:noun {{text: '{noun}', image: '{path}'}}) set m.image='{new_path}' return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.patch("/patch/obAction")
def patch_obAction(role: str="doctor", owner: str="Lorem ipsum", obAction: str="eu", path: str="images/eu.png", new_path: str="images/eu.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}})-->(m:obAction {{text: '{obAction}', image: '{path}'}}) set m.image='{new_path}' return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.patch("/patch/subAction")
def patch_subAction(role: str="doctor", owner: str="Lorem ipsum", subAction: str="lectus", path: str="images/lectus.png", new_path: str="images/lectus.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}})-->(m:subAction {{text: '{subAction}', image: '{path}'}}) set m.image='{new_path}' return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.patch("/patch/adjective")
def patch_adjective(role: str="doctor", owner: str="Lorem ipsum", adjective: str="rhoncus", path: str="images/rhoncus.png", new_path: str="images/rhoncus.png"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}'}})-->(m:adjective {{text: '{adjective}', image: '{path}'}}) set m.image='{new_path}' return n, m")
        con.close()
        nodes = []
        for record in result:
            nodes += list(record.values())
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.patch("/patch/owner")
def patch_owner(role: str="doctor", owner: str="Lorem ipsum", date: str="2005-02-15", desease: str="Lorem ipsum dolor sit amet", new_desease: str="Lorem ipsum dolor sit amet"):
    con = Connection(role)
    try:
        result = con.run(f"match (n:owner {{name: '{owner}', date: datetime('{date}'), desease: '{desease}'}}) set n.desease='{new_desease}' return n")
        con.close()
        nodes = [record['n'] for record in result]
        return {'status' : 'success', 'nodes' : nodes}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}


# DELETE

@app.delete("/delete/noun")
def delete_noun(role: str="doctor", noun: str="existingNoun", path: str="existingPath"):
    con = Connection(role)
    try:
        con.run(f"match (n:noun {{text: '{noun}', image: '{path}'}}) detach delete n")
        con.close()
        return {'status' : 'success'}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.delete("/delete/obAction")
def delete_obAction(role: str="doctor", obAction: str="existingObAction", path: str="existingPath"):
    con = Connection(role)
    try:
        con.run(f"match (n:obAction {{text: '{obAction}', image: '{path}'}}) detach delete n")
        con.close()
        return {'status' : 'success'}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.delete("/delete/subAction")
def delete_subAction(role: str="doctor", subAction: str="existingSubAction", path: str="existingPath"):
    con = Connection(role)
    try:
        con.run(f"match (n:subAction {{text: '{subAction}', image: '{path}'}}) detach delete n")
        con.close()
        return {'status' : 'success'}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.delete("/delete/adjective")
def delete_adjective(role: str="doctor", adjective: str="existingAdjective", path: str="existingPath"):
    con = Connection(role)
    try:
        con.run(f"match (n:adjective {{text: '{adjective}', image: '{path}'}}) detach delete n")
        con.close()
        return {'status' : 'success'}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}

@app.delete("/delete/owner")
def delete_noun(role: str="doctor", owner: str="existingOwner", date: str="2000-01-01", desease: str="existingDesease"):
    con = Connection(role)
    try:
        con.run(f"match (n:owner {{name: '{owner}', date: datetime('{date}'), desease: '{desease}'}}) detach delete n")
        con.close()
        return {'status' : 'success'}
    except Exception as e:
        con.close()
        return {'status' : 'failure', 'message' : e.message}