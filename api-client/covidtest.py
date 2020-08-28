from covid.api import CovId19Data

api = CovId19Data(force=False)
res = api.get_stats()
print(res)