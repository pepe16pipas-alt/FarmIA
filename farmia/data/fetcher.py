import requests

class MolecularDataFetcher:
    def __init__(self, pubchem_base_url='https://pubchem.ncbi.nlm.nih.gov/rest/pug', chembl_base_url='https://www.ebi.ac.uk/chembl/api/data/'):
        self.pubchem_base_url = pubchem_base_url
        self.chembl_base_url = chembl_base_url

    def fetch_pubchem_data(self, cid):
        response = requests.get(f"{self.pubchem_base_url}/compound/cid/{cid}/JSON")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def fetch_chembl_data(self, chembl_id):
        response = requests.get(f"{self.chembl_base_url}/molecule/{chembl_id}/")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

# Example usage:
# if __name__ == '__main__':
#     fetcher = MolecularDataFetcher()
#     pubchem_data = fetcher.fetch_pubchem_data(2244)
#     chembl_data = fetcher.fetch_chembl_data('CHEMBL25')
#     print(pubchem_data)
#     print(chembl_data)