class NoneElementException(Exception):

    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return "None element can not be pushed"


class EmptyStackException(Exception):

    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return "Stack is Empty. Can not perform operation"
