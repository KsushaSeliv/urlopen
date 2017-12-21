import task
def test():
    assert task.i_d(16179475).get('response[0]') == 'Ольга'
    assert task.i_d(390427847).get('response[0]') == 'Зинаида'
