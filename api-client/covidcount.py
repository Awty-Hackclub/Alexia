from covid.api import CovId19Data

api = CovId19Data(force=False)
res = api.get_stats()
res = api.filter_by_country("US")
print(res)