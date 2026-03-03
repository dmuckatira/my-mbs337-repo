# Homework 7

This homework retrieves GenBank records from NCBI and stores them in a Redis database.

## Docker Compose Setup

Create a docker-compose.yml file in your homework-7 directory with the following contents:

    services:
        redis-db:
            image: redis:8.6.0
            container_name: redis
            ports:
                - "6379:6379"
            volumes:
                - ./redis-data:/data
            user: "1000:1000"
            command: redis-server --appendonly yes --appendfsync everysec

## Starting the Redis Container

First, create the redis-data directory if it doesn't exist: 

    mkdir redis-data

Then start the Redis container with docker compose:

    docker compose up -d

Verify it is running with:

    docker ps

To stop the container when you are done:

    docker compose down

## Script Description

**Shebang Line and Imports**

    #!/usr/bin/env python3
    from Bio import Entrez, SeqIO
    import json
    import redis
    import argparse
    import logging
    import socket
    import sys

### Functions

1. **search_ncbi()**: This function searches the NCBI protein database for records 
matching a search term. It uses Entrez.esearch to query the database and returns a 
list of GI numbers that match the search term.

2. **get_records()**: This function takes the list of GI numbers returned from 
search_ncbi() and retrieves the full GenBank records using Entrez.efetch. It parses 
the records using SeqIO.parse and returns a list of SeqRecord objects.

3. **genbank_output()**: This function takes the list of SeqRecord objects and 
connects to the Redis database. It iterates over each record, stores it in Redis as 
a JSON string, and writes the record's ID, name, description, and sequence to an 
output text file.

4. **main()**: This function runs the whole script by calling each function in order 
and includes a try/except to handle errors and logs an error message if something 
goes wrong.

## How to Run

First activate your virtual environment:

    source myenv/bin/activate

Then run the script:

    python3 get_ncbi_genbank_records.py

## AI Usage

I used Claude to format my ReadME so it is aesthetic.
