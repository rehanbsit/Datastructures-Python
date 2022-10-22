import json
import os

storage_mappings = {'json': 'data.json', 'xml': 'data.xml', 'ftp': 'ftp'}


def write_json(data, name):
    with open(name, "w") as f:
        json.dump(data, f)


def push_to_cloud(data):
    pass


def write_xml(data, name):
    pass


function_mapping = {'json': write_json, 'xml': write_xml}


class StorageBucket:

    def __init__(self, format='json', destination='local', name='data.json'):
        self.format = format
        self.destination = destination
        if os.path.exists('data.json'):
            with open('data.json', 'r') as f:
                self.records = json.load(f)
        else:
            self.records = []
        self.error = 'Incorrect format, can not perform operation'
        self.name = name

    def insert(self, record):
        if isinstance(record, dict):
            self.records.append(record)
            write_json(self.records, self.name)
            return True
        else:
            return self.error

    def batch_insert(self, multi_records):
        if isinstance(multi_records, list):
            self.records = self.records + multi_records
            write_json(self.records, self.name)
            return True
        else:
            return self.error

    def retrieve(self, index):
        if index < 0 or index >= len(self.records):
            return 'Not Found. Out of Range'
        print(index, self.records)
        return self.records[index]

    def filter(self, value=None, limit=None, offset=None):
        if value is None and offset is None:
            return self.records[:limit]
        if value is None:
            return self.records[offset:offset + limit]
        return self.records[self.records.index(value)]

    def update(self, index, value):
        if index < 0 or index >= len(self.records):
            print('Not Found. Out of Range')
            return False
        print(index, self.records)
        self.records[index] = value
        write_json(self.records, self.name)
        return True

    def delete(self, index):
        if index < 0 or index >= len(self.records):
            print('Not Found. Out of Range')
            return False
        print("ins", len(self.records))
        self.records.pop(index)
        write_json(self.records, self.name)
        return True
