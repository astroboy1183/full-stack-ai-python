import arrow
from collections import namedtuple

brewing_time = arrow.utcnow()
brewing_time.to("Europe/London")

chaiProfile = namedtuple("ChaiProfile", ["size", "cardamom"])
profile = chaiProfile(size="Large", cardamom="crushed")
print(f"Chai profile: {profile}")

