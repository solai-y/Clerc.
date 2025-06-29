from flask import Flask, request, jsonify
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

app = Flask(__name__)

# Dummy in-memory storage for demonstration
companies = []

@app.route('/companies', methods=['GET'])
def get_companies():
    return jsonify(companies)

@app.route('/companies', methods=['POST'])
def add_company():
    data = request.json
    companies.append(data)
    return jsonify(data), 201

@app.route('/companies/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    data = request.json
    for company in companies:
        if company['company_id'] == company_id:
            company.update(data)
            return jsonify(company)
    return jsonify({'error': 'Company not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)