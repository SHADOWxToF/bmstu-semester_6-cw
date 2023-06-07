from neo4j import GraphDatabase


class Connection:
    def __init__(self, role: str, url: str="bolt://localhost:7687"):
        self.driver = GraphDatabase.driver(url, auth=(role, f"{role}_password"))

    def run(self, query: str):
        session = self.driver.session()
        try:
            result = session.run(query).data()
            session.close()
        except Exception as e:
            session.close()
            raise e
        return result

    def close(self):
        self.driver.close()