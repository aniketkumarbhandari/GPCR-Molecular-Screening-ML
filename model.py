from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from data_parser import load_and_clean_data

def run_virtual_screening():
    """
    Trains an ML model to predict GPCR docking success based on AutoDock parameters.
    Demonstrates supervised learning applied to computational chemistry.
    """
    # 1. Load the processed PDB 3EML data
    X, y = load_and_clean_data('3EML_docking_results.csv')
    
    if X is None:
        return
        
    # 2. Split data into training and testing sets (80/20 split)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Initialize and train the ML model
    print("Training Random Forest Classifier on GPCR parameters...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluate the model's predictive power
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

if __name__ == "__main__":
    # Execute the pipeline when the script is run directly
    run_virtual_screening()
