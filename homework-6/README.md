# Homework 6

This homework containerized 4 bioinformatics scripts.


## Exercise Descriptions

### 1. Build the Docker Image
docker build -t username/dockername:1.0 .

### 2. Obtain Input Data 
FASTA: A multi-sequence FASTA file named immune_proteins.fasta. Download with:
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/immune_proteins.fasta.gz
gunzip immune_proteins.fasta.gz

FASTQ: A FASTQ file named sample1_rawReads.fastq.
wget https://github.com/TACC/mbs-337-sp26/raw/refs/heads/main/docs/unit03/sample-data/sample1_rawReads.fastq.gz
gunzip sample1_rawReads.fastq.gz

mmCIF: The hemoglobin structure 4HHB. Download with:
wget https://files.rcsb.org/download/4HHB.cif.gz
gunzip 4HHB.cif.gz

### 3. Run the Container 
docker run --rm -v "$PWD:/data" -u "$(id -u):$(id -g)" username/dockername:1.0 (script_name) (arugments)

### 4. Script Usage

**fasta_stats.py**

Calculates statistics for a FASTA file.

docker run --rm -v "$PWD:/data" -u "$(id -u):$(id -g)" username/dockername:1.0 fasta_stats.py -i /data/immune_proteins.fasta -o /data/immune_proteins_stats.txt -l INFO

**fasta_filter.py**

Filters FASTA sequences by length.

docker run --rm -v "$PWD:/data" -u "$(id -u):$(id -g)" username/dockername:1.0 fasta_filter.py -i /data/immune_proteins.fasta -o /data/long_only.fasta -m 300 -l INFO

**fastq_filter.py**

Filters FASTQ reads by quality and length.

docker run --rm -v "$PWD:/data" -u "$(id -u):$(id -g)" username/dockername:1.0 fastq_filter.py -i /data/sample1_rawReads.fastq -o /data/sample1_cleanReads.fastq -e fastq-sanger -m 30 -l INFO

**mmcif_summary.py**

Summarizes chain and residue information from an mmCIF file.

docker run --rm -v "$PWD:/data" -u "$(id -u):$(id -g)" username/dockername:1.0 mmcif_summary.py -i /data/4HHB.cif -o /data/4HHB_summary.json -l INFO


### 5. Output Files
5. Output Files
After running all scripts, the following files will be created in your working directory:

immune_proteins_stats.txt
long_only.fasta
sample1_cleanReads.fastq
4HHB_summary.json
