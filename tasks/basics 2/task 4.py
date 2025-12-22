def rvrt_dict(d):
    return {v: k for k, v in d.items()}

print(rvrt_dict({"a": 1, "b": 2, "c": 3}))
