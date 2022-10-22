import pytest
import os
from data_storage import StorageBucket


class TestDataStorage:

    def test_insert(self):
        bucket = StorageBucket(name='test.json')
        value = {'a': 65, 'b': 66}
        assert bucket.insert(value) is True
        value = [1, 2, 3]
        assert bucket.insert(value) == 'Incorrect format, can not perform operation'
        os.remove('test.json')

    def test_batch_insert(self):
        bucket = StorageBucket(name='test.json')
        values = [{'a': 65, 'b': 66}, {'c': 67, 'd': 68}, {'e': 69, 'f': 70}]
        assert bucket.batch_insert(values) is True
        value = {'a': 65, 'b': 66}
        assert bucket.batch_insert(value) == 'Incorrect format, can not perform operation'
        os.remove('test.json')

    def test_retrieve(self):
        bucket = StorageBucket(name='test.json')
        assert bucket.retrieve(10) == 'Not Found. Out of Range'
        value = {'a': 65, 'b': 66}
        bucket.insert(value)
        assert bucket.retrieve(0) == value
        os.remove('test.json')

    def test_filter(self):
        bucket = StorageBucket(name='test.json')
        values = [{'a': 65, 'b': 66}, {'c': 67, 'd': 68}, {'e': 69, 'f': 70}]
        bucket.batch_insert(values)
        assert bucket.filter({'e': 69, 'f': 70}) == {'e': 69, 'f': 70}
        assert len(bucket.filter(limit=2)) == 2
        assert len(bucket.filter(limit=1, offset=1)) == 1
        os.remove('test.json')

    def test_update(self):
        bucket = StorageBucket(name='test.json')
        value = {'a': 65, 'b': 66}
        bucket.insert(value)
        value = {'a': 65, 'b': 67}
        assert bucket.update(0, value) is True
        assert bucket.update(10, value) is False
        os.remove('test.json')

    def test_delete(self):
        bucket = StorageBucket(name='test.json')
        value = {'a': 65, 'b': 66}
        bucket.insert(value)
        assert bucket.delete(0) is True
        assert bucket.delete(10) is False
        os.remove('test.json')
