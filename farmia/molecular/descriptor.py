from rdkit import Chem
from rdkit.Chem import Descriptors

def calculate_descriptors(smiles):
    molecule = Chem.MolFromSmiles(smiles)
    if not molecule:
        raise ValueError('Invalid SMILES string')
    descriptors = {
        'Molecular Weight': Descriptors.MolWt(molecule),
        'LogP': Descriptors.MolLogP(molecule),
        'TPSA': Descriptors.TPSA(molecule),
        'Num Rotatable Bonds': Descriptors.NumRotatableBonds(molecule),
        'Num Aromatic Rings': Descriptors.SysAromaticRings(molecule)
    }
    return descriptors
