# Thomas Walsh
# BIFX 546: Machine Learning for Bioinformatics
# Hood College - Spring 2026
# March 04, 2026
# Progress Check 01 - Inital EDA

# Dataset: Mouse Glioblastoma Atlas (snRNA-seq)
#   From README.md found on Hugging Face, link below:
#   https://huggingface.co/datasets/longevity-db/mouse-glioblastoma-snRNAseq/tree/main

# Data Citation:
# The original source of the Mouse Glioblastoma data from CELLxGENE:
#   Original Publication: Darmanis, S., Sloan, S. A., et al. (2023). "Transcriptional programs of glioblastoma subclasses are preserved in the tumor microenvironment." Nature Communications, 14(1), 3848. PMID: 37400346 DOI: 10.1038/s41467-023-39434-2
#   Associated GEO Accession (from CELLxGENE): GSE186252


### 01 - Loading the Dataset ###
# may need to install Hugging Face Hub
#   `pip install huggingface_hub`

# Verify installation of Hugging Face Hub
#   `pip show huggingface_hub`
#   `print(huggingface_hub.__version__)`

# May require login using e.g. `huggingface-cli login` to access this dataset
#   `from huggingface_hub import login`
#   `login()`

# This dataset is hosted on the Hugging Face Hub, allowing for easy programmatic download and loading of its component files.
import pandas as pd
from huggingface_hub import hf_hub_download
import os

# Define the Hugging Face repository ID and the local directory for downloads
HF_REPO_ID = "longevity-db/mouse-glioblastoma-snRNAseq"
LOCAL_DATA_DIR = "downloaded_mouse_glioblastoma_data"

os.makedirs(LOCAL_DATA_DIR, exist_ok=True)
print(f"Created local download directory: {LOCAL_DATA_DIR}")

# List of Parquet files to download (matching the 8 files you generated)
parquet_files = [
    "expression.parquet",
    "gene_metadata.parquet",
    "cell_metadata.parquet",
    "pca_embeddings.parquet",
    "pca_explained_variance.parquet",
    "umap_embeddings.parquet",
    "highly_variable_gene_metadata.parquet",
    "gene_statistics.parquet"
]

# Download each file
downloaded_paths = {}
for file_name in parquet_files:
    try:
        path = hf_hub_download(repo_id=HF_REPO_ID, filename=file_name, local_dir=LOCAL_DATA_DIR)
        downloaded_paths[file_name] = path
        print(f"Downloaded {file_name} to: {path}")
    except Exception as e:
        print(f"Warning: Could not download {file_name}. It might not be in the repository or its name differs. Error: {e}")

# Load core Parquet files into Pandas DataFrames
df_expression = pd.read_parquet(downloaded_paths["expression.parquet"])
df_pca_embeddings = pd.read_parquet(downloaded_paths["pca_embeddings.parquet"])
df_umap_embeddings = pd.read_parquet(downloaded_paths["umap_embeddings.parquet"])
df_cell_metadata = pd.read_parquet(downloaded_paths["cell_metadata.parquet"])
df_gene_metadata = pd.read_parquet(downloaded_paths["gene_metadata.parquet"])
df_pca_explained_variance = pd.read_parquet(downloaded_paths["pca_explained_variance.parquet"])
df_hvg_metadata = pd.read_parquet(downloaded_paths["highly_variable_gene_metadata.parquet"])
df_gene_stats = pd.read_parquet(downloaded_paths["gene_statistics.parquet"])

print("\n--- Data Loaded from Hugging Face Hub ---")
print("Expression data shape:", df_expression.shape)
print("PCA embeddings shape:", df_pca_embeddings.shape)
print("UMAP embeddings shape:", df_umap_embeddings.shape)
print("Cell metadata shape:", df_cell_metadata.shape)
print("Gene metadata shape:", df_gene_metadata.shape)
print("PCA explained variance shape:", df_pca_explained_variance.shape)
print("HVG metadata shape:", df_hvg_metadata.shape)
print("Gene statistics shape:", df_gene_stats.shape)

# Example: Prepare data for a classification/prediction model
# IMPORTANT: You need to inspect `df_cell_metadata.columns` to find the actual relevant columns.
print("\nAvailable columns in cell_metadata.parquet (df_cell_metadata.columns):")
print(df_cell_metadata.columns.tolist())


### 02 - Initial cleaning ###

### 03 - Visualizations (2–3) ###

### 04 - Summary statistics ###

### 05 - Short progress note ###
