import requests
import json

# url = "https://galen.vetrf.ru/list/pagedList"

# payload = json.dumps(
#     {
#         "pageDetails": {"itemsPerPage": 2331, "pageNumber": "1"},
#         "productType": "pharm",
#         "entryType": "registry",
#         "sortOrders": [{"field": "ph_startValidityDate", "asc": False}],
#         "extendedQuery": {},
#     }
# )
# headers = {"Content-Type": "application/json"}

# response = requests.request("POST", url, headers=headers, data=payload)

# response_data = response.json()


# for item in response_data["itemList"]:
#     farm_group = item["product"].get("pharmGroup")
#     if not farm_group:
#         continue
#     if farm_group["name"] in pharm_groups:
#         continue
#     else:
#         pharm_groups.append(farm_group["name"])
# print(len(pharm_groups))
