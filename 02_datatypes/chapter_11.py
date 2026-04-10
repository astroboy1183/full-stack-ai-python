import arrow
from collections import namedtuple

brewing_time = arrow.utcnow()
brewing_time.to("Europe/London")

# A namedtuple is a subclass of the built-in tuple data type that allows you to create tuple-like objects with named fields. It provides a way to define a simple class with immutable properties, making it easier to access and work with the data stored in the tuple.
chaiProfile = namedtuple("ChaiProfile", ["size", "cardamom"])
profile = chaiProfile(size="Large", cardamom="crushed")
print(f"Chai profile: {profile}")





