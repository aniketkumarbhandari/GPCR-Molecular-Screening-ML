# GPCR Molecular Screening ML Pipeline

## Overview
This project is a computational workflow designed to evaluate molecular interactions at specific G-Protein Coupled Receptor (GPCR) docking sites. It bridges structural chemistry with Machine Learning by processing PDB structural data and predicting binding probabilities.

## Tech Stack
* **Language:** Python 3
* **Machine Learning:** Scikit-learn (Random Forest Classifier)
* **Data Processing:** Pandas, NumPy
* **Scientific Tools:** AutoDockTools, ChimeraX (Data source generation)

## Engineering Approach: Synthetic Data Generation
Running large-scale AutoDock simulations requires significant HPC time. To rapidly develop and test the Machine Learning pipeline, I engineered a Python-based synthetic data generator (`data_generator.py`). This script uses `NumPy` to simulate statistically correlated thermodynamic parameters (VDW, Intermolecular Energy, H-Bonds) that mirror real 3EML binding profiles, allowing the Random Forest model to be tested at scale.

## Project Structure
* `data_parser.py`: Cleans and formats raw physicochemical parameters.
* `model.py`: Trains a Random Forest model on the processed molecular features.

*(Note: Project is currently in active development for pre-incubation phase)*
