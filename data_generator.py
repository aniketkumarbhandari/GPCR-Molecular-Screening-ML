import pandas as pd
import numpy as np

def generate_synthetic_docking_data(num_samples=1000, output_file='3EML_synthetic_data.csv'):
    """
    Simulates AutoDock Vina output for PDB 3EML.
    Generates statistically correlated physicochemical features to stress-test the ML pipeline.
    """
    np.random.seed(42)
    
    # 1. Generate core features based on typical GPCR docking ranges
    # H-bonds typically range from 0 to 5
    h_bonds = np.random.randint(0, 6, num_samples)
    
    # VDW energy is usually negative, correlated loosely with size
    vdw_energy = np.random.normal(-5.0, 1.5, num_samples)
    
    # Intermolecular energy combines VDW and electrostatics
    intermolecular = vdw_energy + np.random.normal(-2.0, 1.0, num_samples) - (h_bonds * 0.5)
    
    # 2. Calculate Binding Energy (Target Variable)
    # Stronger (more negative) binding energy correlates with lower intermolecular energy and more H-bonds
    binding_energy = intermolecular + np.random.normal(0, 0.5, num_samples)
    
    # 3. Construct the DataFrame
    data = {
        'Molecule_ID': [f'Mol_{i:04d}' for i in range(1, num_samples + 1)],
        'Binding_Energy_kcal_mol': np.round(binding_energy, 2),
        'Intermolecular_Energy': np.round(intermolecular, 2),
        'H_Bonds': h_bonds,
        'VDW_Desolv_Energy': np.round(vdw_energy, 2)
    }
    
    df = pd.DataFrame(data)
    df.to_csv(output_file, index=False)
    print(f"Successfully generated {num_samples} synthetic docking records in {output_file}")

if __name__ == "__main__":
    generate_synthetic_docking_data()
