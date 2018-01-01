#user.py

from library import Base

# to avoid breaking, write a test and run the test before deploy
# OR
# early warning that the method in parent class doesn't exist
assert hasattr(Base, 'foo'), "method is broken"

class Derived(Base):
    def bar(self):
        return self.foo
        # this will break if there's no foo method in parent class

    def bar2(self):
        return "bar"