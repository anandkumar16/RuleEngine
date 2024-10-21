from flask import Flask, request, jsonify, render_template # type: ignore
from rule_engine import create_rule, evaluate_rule, combine_rules
from database import save_rule_to_db, get_rule_ast

app = Flask(__name__)
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    try:
        data = request.json
        rule_string = data['rule']
        
        
        rule_ast = create_rule(rule_string)
        
       
        rule_id = save_rule_to_db(rule_string, rule_ast)
        
        return jsonify({
            "rule_id": str(rule_id), 
            "message": "Rule created successfully"
        }), 201
    except KeyError:
        return jsonify({"error": "Missing 'rule' in request body"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    try:
        data = request.json
        rule_id = data['rule_id']
        user_data = data.get('user_data', {})
        
       
        rule_ast = get_rule_ast(rule_id)
        
        if not rule_ast:
            return jsonify({"error": "Rule not found"}), 404
        
        result = evaluate_rule(rule_ast, user_data)
        
        return jsonify({
            "result": result,
            "rule_id": rule_id,
            "user_data": user_data
        }), 200
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    try:
        data = request.json
        rule_ids = data['rule_ids']
        
        rules = []
        for rule_id in rule_ids:
            rule_ast = get_rule_ast(rule_id)
            if rule_ast:
                rules.append(rule_ast)
            else:
                return jsonify({"error": f"Rule {rule_id} not found"}), 404
        
        
        combined_ast = combine_rules(rules)
        
        
        combined_rule_id = save_rule_to_db("Combined Rule", combined_ast)
        
        return jsonify({
            "combined_rule_id": str(combined_rule_id),
            "message": "Rules combined successfully"
        }), 201
    except KeyError:
        return jsonify({"error": "Missing 'rule_ids' in request body"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)