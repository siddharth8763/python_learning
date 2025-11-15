# with open("demo.txt","w") as file:
#     file.write("This is for context manager demo")


# context manager using class

class FileManger:
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        print("Enter")
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("exception handled")
        # print("exc:",exc_type,exc_value)
        print("Exit")
        return True

with FileManger("demo2.txt") as f:
    print("Inside with block")
    f.write("This is demo for context manager using class")
    f.jjjjjj()
print("continuing")

# context manager using function

from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    print("Enter function")
    f = open(filename, 'w')
    try:
        yield f
    except Exception as e:
        print("Exception handled in function:", e)
    finally:
        f.close()
        print("Exit function")

with open_managed_file("demo3.txt") as f:
    print("Inside with block of function")
    f.write("This is demo for context manager using function")
    f.kkkkk()