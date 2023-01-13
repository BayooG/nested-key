# nested-key

access nested dict values like it's 2023

example:
```
from nkey import ND
d = {
    "level_1": {
        "key": "hello",
        "level_2": {
            "key": "world",
            "other_key" : "catch ya"
        }
    }
}
value_1 = ND.nkey(d, "level_1.key")
value_2 = ND.nkey(d, "level_1-level_2-key", sep= "-")
print(value_1, value_2)
```
output:
```
hello world
```