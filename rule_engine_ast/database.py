from pymongo import MongoClient  # type: ignore
from config import MONGODB_CONFIG
from ast_node import Node
from bson.objectid import ObjectId  # type: ignore


client = MongoClient(MONGODB_CONFIG["host"], MONGODB_CONFIG["port"])
db = client[MONGODB_CONFIG["db_name"]]
rules_collection = db[MONGODB_CONFIG["collection_name_rules"]]
ast_collection = db[MONGODB_CONFIG["collection_name_ast"]]

def save_rule_to_db(rule_string, rule_ast):
    try:
        
        rule = {
            "rule_string": rule_string
        }
        rule_id = rules_collection.insert_one(rule).inserted_id

        
        ast_doc = _ast_to_dict(rule_ast)
        ast_doc["rule_id"] = rule_id
        ast_collection.insert_one(ast_doc)

        return str(rule_id)
    except Exception as e:
        print(f"Error saving rule to database: {e}")
        return None

def _ast_to_dict(node):
    node_dict = {
        "type": node.type,
        "value": node.value,
    }
    if node.left:
        node_dict["left"] = _ast_to_dict(node.left)
    if node.right:
        node_dict["right"] = _ast_to_dict(node.right)
    return node_dict

def get_rule_ast(rule_id):
    try:
        
        ast_doc = ast_collection.find_one({"rule_id": ObjectId(rule_id)})
        if ast_doc:
            return _dict_to_ast(ast_doc)
        else:
            return None
    except Exception as e:
        print(f"Error fetching rule AST: {e}")
        return None

def _dict_to_ast(ast_dict):
    node = Node(node_type=ast_dict["type"], value=ast_dict["value"])
    if "left" in ast_dict:
        node.left = _dict_to_ast(ast_dict["left"])
    if "right" in ast_dict:
        node.right = _dict_to_ast(ast_dict["right"])
    return node
