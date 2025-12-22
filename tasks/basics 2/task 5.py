def dict_update(d1, d2):
    for k, v in d2.items():
        d1[k] = v
    return d1

print(dict_update({"a": 1}, {"b": 2, "a": 3}))
