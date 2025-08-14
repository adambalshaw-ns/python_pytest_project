from src.data_utils import read_csv, get_average_age

def test_read_csv():
    data = read_csv('data/sample.csv')
    assert len(data) == 3
    assert data[0]['name'] == 'Alice'

def test_get_average_age():
    data = read_csv('data/sample.csv')
    avg = get_average_age(data)
    assert avg == (30 + 25 + 35) / 3