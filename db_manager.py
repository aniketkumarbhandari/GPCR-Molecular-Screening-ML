import sqlite3
import pandas as pd

def create_database(csv_file='3EML_synthetic_data.csv', db_name='molecular_data.db'):
    """
    Demonstrates backend database integration.
    Reads the docking data and creates a relational SQL database.
    """
    try:
        # 1. Connect to SQLite database (creates it if it doesn't exist)
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()
        
        # 2. Create a clean table for the molecules
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS gpcr_docking (
                Molecule_ID TEXT PRIMARY KEY,
                Binding_Energy REAL,
                Intermolecular_Energy REAL,
                H_Bonds INTEGER,
                VDW_Desolv_Energy REAL
            )
        ''')
        
        # 3. Load data via Pandas and push to SQL
        df = pd.read_csv(csv_file)
        
        # Rename columns to match SQL table cleanly
        df.columns = ['Molecule_ID', 'Binding_Energy', 'Intermolecular_Energy', 'H_Bonds', 'VDW_Desolv_Energy']
        
        # Push data to SQL, replacing the table if it already exists
        df.to_sql('gpcr_docking', conn, if_exists='replace', index=False)
        
        print(f"Successfully loaded {len(df)} records into the SQL database '{db_name}'.")
        
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_database()
