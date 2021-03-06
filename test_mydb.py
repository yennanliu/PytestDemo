"""
Not good to test with below code/style

1. code repetition
2. duplicated DB connection 

Way to fix 
1. setup - teardown (classic way)
2. fixtures 
"""
import pytest
from mydb import MyDB

def test_employ_query1():
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    id = cur.execute("select id from employee where name=jim")
    assert id == 123
    cur.close()
    conn.close()

def test_employ_query2():
    db = MyDB()
    conn = db.connect("server")
    cur = conn.cursor()
    id = cur.execute("select id from employee where name=tom")
    assert id == 789
    cur.close()
    conn.close()


if __name__ == '__main__':
    pytest.main([__file__])
