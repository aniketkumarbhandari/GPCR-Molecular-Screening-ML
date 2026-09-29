import pandas as pd

def load_and_clean_data(filepath):
    """
    Loads docking parameters extracted from AutoDockTools for PDB 3EML.
    Cleans the dataset by handling missing values and defining binding classes.
    """
    try:
        print(f"Loading structural data from {filepath}...")
        df = pd.read_csv(filepath)
        
        # Drop any failed docking runs missing energy calculations
        df = df.dropna(subset=['Binding_Energy_kcal_mol'])
        
        # Extract core physicochemical features mapped from ChimeraX/AutoDock
        features = ['Binding_Energy_kcal_mol', 'Intermolecular_Energy', 'H_Bonds', 'VDW_Desolv_Energy']
        X = df[features]
        
        # Define target variable: 1 (Strong Binder, Energy < -7.0) or 0 (Weak Binder)
        # This is the 'Feature Engineering' mentioned on the resume
        y = (df['Binding_Energy_kcal_mol'] < -7.0).astype(int)
        
        return X, y
        
    except FileNotFoundError:
        print("Dataset not found. Please ensure the AutoDock output CSV is in the root directory.")
        return None, None
