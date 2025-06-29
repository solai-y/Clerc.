from flask import Flask, request, jsonify
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()

print("Supabase URL:")
print(os.environ.get("SUPABASE_URL"))
supabase_url = os.environ.get("SUPABASE_URL")
supabase_key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(supabase_url, supabase_key)

app = Flask(__name__)

@app.route('/e2e', methods=['GET'])
def e2e_test():
    # Here you would implement your end-to-end test logic
    return jsonify({'message': 'Categories service is reachable'}), 200

@app.route('/categories', methods=['GET'])
def get_categories():
    response = supabase.table('categories').select("*").execute()
    return jsonify(response.data), 200

@app.route('/categories/<int:category_id>', methods=['GET'])
def get_category(category_id):
    response = supabase.table('categories').select("*").eq("id", category_id).execute()
    if response.data:
        return jsonify(response.data[0]), 200
    return jsonify({'error': 'Category not found'}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
