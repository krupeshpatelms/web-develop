from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for notes
notes = []

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Notes API"})

# Route for GET (fetching) and POST (creating) notes
@app.route('/notes', methods=['GET', 'POST'])
def notes_handler():
    global notes

    if request.method == 'GET':
        return jsonify(notes)  # Return all notes

    elif request.method == 'POST':
        data = request.json
        if not data or "text" not in data:
            return jsonify({"error": "Invalid request. 'text' field required."}), 400

        new_note = {"id": len(notes) + 1, "text": data["text"]}
        notes.append(new_note)
        return jsonify(new_note), 201

# Route for updating a note
@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.json
    for note in notes:
        if note["id"] == note_id:
            note["text"] = data.get("text", note["text"])
            return jsonify(note)
    return jsonify({"error": "Note not found"}), 404

# Route for deleting a note
@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note["id"] != note_id]
    return jsonify({"message": "Note deleted"}), 204

# Debugging helper to check incoming requests
@app.before_request
def log_request():
    print(f"Request Method: {request.method}, Request URL: {request.url}")

if __name__ == '__main__':
    app.run(debug=True)
