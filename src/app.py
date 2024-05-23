from flask import Flask, render_template, request, redirect, url_for, jsonify
from utils.request_handler import execute_requests
from utils.workspace_manager import save_workspace, load_workspace

app = Flask(__name__)

# Global variables
environment_variables = {}
variables = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/variables', methods=['GET', 'POST'])
def manage_variables():
    if request.method == 'POST':
        env_name = request.form.get('env_name')
        var_name = request.form.get('var_name')
        var_value = request.form.get('var_value')
        if env_name:
            environment_variables[env_name] = environment_variables.get(env_name, {})
            if var_name and var_value:
                environment_variables[env_name][var_name] = var_value
    return render_template('variables.html', environment_variables=environment_variables)

@app.route('/save_workspace', methods=['POST'])
def save_workspace_route():
    save_workspace(environment_variables)
    return redirect(url_for('index'))

@app.route('/load_workspace', methods=['POST'])
def load_workspace_route():
    global environment_variables
    environment_variables = load_workspace()
    return redirect(url_for('index'))

@app.route('/execute', methods=['POST'])
def execute():
    requests_list = request.form.get('requests_list')
    extract_var_name = request.form.get('extract_var_name')
    extract_var_regex = request.form.get('extract_var_regex')
    responses = execute_requests(requests_list, variables, extract_var_name, extract_var_regex)
    return jsonify(responses)

if __name__ == '__main__':
    app.run(debug=True)
