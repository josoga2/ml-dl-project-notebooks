from Bio import Entrez

Entrez.email = "josoga2@gmail.com"

def search_pubmed(query, n=10):
    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=n
    )
    record = Entrez.read(handle)
    return record["IdList"]

def fetch_abstracts(ids):
    handle = Entrez.efetch(
        db="pubmed",
        id=",".join(ids),
        rettype="abstract",
        retmode="text"
    )

    return handle.read()
