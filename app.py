from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# MongoDB Atlas connection URI (replace with your actual URI)
# app.config["MONGO_URI"] = "mongodb+srv://cthis9917:12341234@cluster0.etgu0.mongodb.net/mydatabase?retryWrites=true&w=majority"
app.config["MONGO_URI"] = "mongodb+srv://your_mongo_uri_here"


mongo = PyMongo(app)

# User model structure:
# {
#     "_id": ObjectId,
#     "name": str,
#     "email": str
# }

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400
    new_user = {
        "name": name,
        "email": email
    }
    user_id = mongo.db.users.insert_one(new_user).inserted_id
    return jsonify({"id": str(user_id), "name": name, "email": email}), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    result = []
    for user in users:
        result.append({
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        })
    return jsonify(result)

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return jsonify({
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        })
    return jsonify({"error": "User not found"}), 404

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    updated_data = {}
    if name:
        updated_data["name"] = name
    if email:
        updated_data["email"] = email
    if not updated_data:
        return jsonify({"error": "No data to update"}), 400

    result = mongo.db.users.update_one(
        {"_id": ObjectId(user_id)}, {"$set": updated_data}
    )
    if result.matched_count:
        return jsonify({"msg": "User updated successfully"})
    return jsonify({"error": "User not found"}), 404

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return jsonify({"msg": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
