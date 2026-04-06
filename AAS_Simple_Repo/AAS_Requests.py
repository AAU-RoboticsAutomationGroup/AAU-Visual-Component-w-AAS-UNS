import requests

BASE_URL = "http://localhost:8081"

SUBMODEL_ID_BASE64 = "aHR0cHM6Ly9zbWFydHByb2R1Y3Rpb25sYWIuYWF1LmRrL3N1Ym1vZGVscy9pbnN0YW5jZXMvYWF1RmlsbGluZ0xpbmVBQVMvSGllcmFyY2hpY2FsU3RydWN0dXJlcw"

PATH_LOCATION = f"{BASE_URL}/submodels/{SUBMODEL_ID_BASE64}/submodel-elements/EntryNode.DispensingSystem.Location"
PATH_ENTRY_NODE = f"{BASE_URL}/submodels/{SUBMODEL_ID_BASE64}/submodel-elements/EntryNode"

def get_value(path):
    url = f"{PATH_LOCATION}.{path}/$value"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_list():
    url = f"{PATH_LOCATION}/$value"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def get_entry_node():
    url = f"{PATH_ENTRY_NODE}/$value"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # x = get_value("x")
    # y = get_value("y")
    # yaw = get_value("yaw")
    entry_node = get_entry_node()
    list_value = get_list()

    # print(f"x: {x}")
    # print(f"y: {y}")
    # print(f"yaw: {yaw}")
    print(f"List: {list_value}")

    configurations = {}

    st = {'PlanarTable': {'statements': [{'Location': {'x': '0', 'y': '0', 'yaw': '0'}}, {'SameAs': {'type': 'ModelReference', 'keys': [{'type': 'Submodel', 'value': 'https://smartproductionlab.aau.dk/submodels/instances/planarTableAAS/HierarchicalStructures'}, {'type': 'Entity', 'value': 'EntryNode'}]}}], 'entityType': 'SelfManagedEntity', 'globalAssetId': 'https://smartproductionlab.aau.dk/assets/ZTM1NTAzNzQtMDZkNi00N2Q4LWI1YTktMGNhMmY0MDEyNTk4', 'specificAssetIds': []}}
    
    for station in entry_node.get("statements", []):
        station_name = list(station.keys())[0]
        statements = station[station_name]["statements"]
        location = statements[0].get("Location", {})
        
        print(f"\nStation: {station_name}")
        print(f"Location: {location}")

    #print(f"\nEntry Node: {entry_node}")
