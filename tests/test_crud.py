import crud

def setup_function():
    crud.data.clear()

def test_create_and_read():
    crud.create("item1")
    assert "item1" in crud.read()

def test_update():
    crud.create("item2")
    assert crud.update(0, "nuevo")
    assert crud.read()[0] == "nuevo"

def test_delete():
    crud.create("item3")
    assert crud.delete(0)