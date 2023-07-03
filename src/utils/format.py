import numpy as np
import ast


def tree_mapper(categories: str):
    """
    Maps and strips the productname from the category tree

    :param categories: string of category tree the product has
    """
    return [category.strip() for category in categories.split(">>")][:-1]

def format_arr(arr: list):
    """
    Flatten and map items under category tree to get a list of categories

    :param arr: array of category tree
    """
    items = np.array([tree_mapper(item) for item in arr][:-1])
    flat =items.flatten()
    return flat.tolist()

def key_val_extractor(iterable: dict):
    if "key" in iterable:
        return {iterable["key"]: iterable["value"]}
    return {}

def format_str_to_dict(item: str):
    return ast.literal_eval(item.replace("=>", ":"))

def apply_mapping_attribute(item: str):
    """
    validate and flatten attributes for product specifics

    :param iterable: dictionary of product_specification
    """
    items = format_str_to_dict(item)
    mapping = {}
    if "product_specification" in items.keys():
        #validated_items = ProductSpecs(**item)
        for item in items["product_specification"]:
                mapping.update(key_val_extractor(item))

    return mapping
