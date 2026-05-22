import requests

PEPTIDEATLAS_URL = "https://peptideatlas.org/api/promast/v1/map"
UNIPROT_URL = "https://rest.uniprot.org/uniprotkb"


def search_peptideatlas(peptide):
    params = {
        "proteome": "Hs",
        "peptide": peptide,
        "output": "json"
    }

    response = requests.get(PEPTIDEATLAS_URL, params=params)
    response.raise_for_status()
    return response.json()


def extract_accession(protein_name):
    """
    Example:
    CONTAM_sp|P01012|OVAL_CHICK
    returns:
    P01012
    """
    parts = protein_name.split("|")

    if len(parts) >= 3:
        return parts[1]

    return None


def get_uniprot_info(accession):
    url = f"{UNIPROT_URL}/{accession}.json"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    return response.json()


def print_uniprot_info(data):
    protein_description = data.get("proteinDescription", {})
    recommended_name = protein_description.get("recommendedName", {})
    full_name = recommended_name.get("fullName", {})

    description = full_name.get("value", "No description found")

    genes = data.get("genes", [])
    gene_symbol = "No gene symbol found"

    if genes:
        gene_name = genes[0].get("geneName", {})
        gene_symbol = gene_name.get("value", gene_symbol)

    sequence_data = data.get("sequence", {})
    sequence = sequence_data.get("value", "")
    length = sequence_data.get("length", "Unknown")

    print("Gene Symbol:", gene_symbol)
    print("Description:", description)
    print("Primary sequence length:", length)

    if sequence:
        print("Primary sequence:")
        print(sequence)

def get_pubmed_papers(accession):
    search_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"

    params = {
        "db": "pubmed",
        "term": accession,
        "retmode": "json",
        "retmax": 5
    }

    response = requests.get(search_url, params=params)
    response.raise_for_status()

    data = response.json()
    pmids = data["esearchresult"]["idlist"]

    return pmids


def print_pubmed_links(pmids):
    if not pmids:
        print("No PubMed papers found.")
        return

    print("Linked PubMed papers:")
    for pmid in pmids:
        print(f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/")

def main():
    peptide = input("Enter peptide sequence: ").strip().upper()

    data = search_peptideatlas(peptide)

    print("\nResults:\n")

    if data["status"] != "OK" or not data["mappings"]:
        print("No mappings found.")
        return

    for hit in data["mappings"]:
        protein = hit["protein"]
        location = int(hit["location"])
        peptide_seq = hit["peptide"]
        end_location = location + len(peptide_seq) - 1

        print("Protein:", protein)
        print("Peptide:", peptide_seq)
        print(f"Location: {location}-{end_location}")

        accession = extract_accession(protein)

        if accession:
            print("Accession:", accession)

            uniprot_data = get_uniprot_info(accession)

            if uniprot_data:
                print_uniprot_info(uniprot_data)
            else:
                print("No UniProt information found.")
            pmids = get_pubmed_papers(accession)
            print_pubmed_links(pmids)
        else:
            print("Could not extract accession.")

        print("-" * 50)


if __name__ == "__main__":
    main()
