from flask import Flask, request, jsonify, render_template
from analyticsp import student_analyze

app = Flask(__name__, template_folder='.', static_url_path='', static_folder='.')

@app.route('/')
def home():
    return render_template('p.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if not request.is_json:
        return jsonify({'error': 'Request content-type must be application/json'}), 400

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({'error': 'Invalid JSON body'}), 400

    required_fields = ['cgpa', 'skill', 'projects', 'certifications', 'internships']
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({'error': 'Missing fields', 'missing': missing}), 400

    try:
        cgpa = float(data['cgpa'])
        skill = str(data['skill'])
        projects = int(data['projects'])
        certifications = int(data['certifications'])
        internships = int(data['internships'])
    except (TypeError, ValueError) as exc:
        return jsonify({'error': 'Invalid field type', 'details': str(exc)}), 400

    result = student_analyze(cgpa, skill, projects, certifications, internships)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)