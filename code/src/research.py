import matplotlib.pyplot as plt
from neo4j import GraphDatabase
import time

LOOP = 10

def rs1():
    plt.plot([15, 25, 40, 50, 70, 90, 100, 115, 135], [1, 2, 3.5, 3.5, 5.5, 7, 8, 8.5, 9])
    plt.xlabel('количество узлов')
    plt.ylabel('время (мс)')
    plt.show()

def add_nodes(count: int, driver):
    query = "create (n:test {text: 'qwerty'})"
    session = driver.session()
    for i in range(count):
        session.run(query)
    session.close()


def delete_nodes(driver):
    query = "match (n:test) detach delete n"
    session = driver.session()
    session.run(query)
    session.close()

def rs2():
    driver = GraphDatabase.driver("bolt://localhost:7687", auth=("doctor", f"doctor_password"))
    result_time = []
    x = list(range(15, 501, 5))
    for count in x:
        add_nodes(count, driver)
        query = f"create (n:test {{text: '{count}'}})"
        antiquery = f"match (n:test {{text: '{count}'}}) detach delete n"
        rtime = 0
        for loop in range(LOOP):
            session = driver.session()
            start = time.time()
            session.run(query).data()
            session.close()
            rtime += time.time() - start
            session = driver.session()
            session.run(antiquery).data()
            session.close()
        result_time.append(1000 * rtime / LOOP)
        delete_nodes(driver)
    driver.close()
    plt.plot(x, result_time)
    plt.xlabel('количество узлов')
    plt.ylabel('время (мс)')
    plt.show()
    f = open('rs2.txt', 'w')
    for i in range(len(x)):
        f.write(f'{x[i]} & {result_time[i]:3.1f} \\\\\n \\hline\n')
    f.close()
    print(result_time)

def main():
    # rs1()
    rs2()

import time





if __name__=="__main__":
    main()


if __name__=="__main__":
    main()