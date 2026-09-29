import unittest
import os
import pandas as pd
from data_generator import generate_synthetic_docking_data

class TestMLPipeline(unittest.TestCase):
    """
    Automated test suite to ensure pipeline reliability and data integrity.
    """
    
    def setUp(self):
        # Define a test file name so we don't overwrite the main data
        self.test_file = 'test_docking_data.csv'
        
    def test_data_generation(self):
        # Run the generator with just 50 rows to test it
        generate_synthetic_docking_data(num_samples=50, output_file=self.test_file)
        
        # Assert the file was actually created
        self.assertTrue(os.path.exists(self.test_file))
        
        # Read the file and assert it has exactly 50 rows
        df = pd.read_csv(self.test_file)
        self.assertEqual(len(df), 50)
        
        # Assert all required columns are present
        expected_columns = ['Molecule_ID', 'Binding_Energy_kcal_mol', 'Intermolecular_Energy', 'H_Bonds', 'VDW_Desolv_Energy']
        for col in expected_columns:
            self.assertIn(col, df.columns)
            
    def tearDown(self):
        # Clean up the test file after tests run
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

if __name__ == '__main__':
    unittest.main()
