import pickle
import sklearn

# Load the model (old format)
with open('saved_models/diabetes.pkl', 'rb') as f:
    model = pickle.load(f)

# Save it again with the new scikit-learn version
with open('saved_models/diabetes_new.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model successfully converted to diabetes_new.pkl")
