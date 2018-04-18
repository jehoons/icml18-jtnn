from torch.utils.data import Dataset
from .mol_tree import MolTree
import numpy as np
import random


class MoleculeDataset(Dataset):

  def __init__(self, data_file):
    with open(data_file) as f:
      self.data = [line.strip("\r\n ").split()[0] for line in f]

  def __len__(self):
    return len(self.data)

  def __getitem__(self, idx):
    smiles = self.data[idx]
    mol_tree = MolTree(smiles)
    mol_tree.recover()
    mol_tree.assemble()
    return mol_tree


class PropDataset(Dataset):

  def __init__(self, data_file, prop_file):
    self.prop_data = np.loadtxt(prop_file)
    with open(data_file) as f:
      self.data = [line.strip("\r\n ").split()[0] for line in f]

  def __len__(self):
    return len(self.data)

  def __getitem__(self, idx):
    smiles = self.data[idx]
    mol_tree = MolTree(smiles)
    mol_tree.recover()
    mol_tree.assemble()
    return mol_tree, self.prop_data[idx]


class FastMoleculeDataset(Dataset):
  # Same as MoleculeDataset but pickle results so its not so GD slow

  def __init__(self, data_file, shuffle=False):
    with open(data_file) as f:
      self.data = [line.strip("\r\n ").split()[0] for line in f]
    if shuffle:
      random.shuffle(self.data)

  def __len__(self):
    return len(self.data)

  def __getitem__(self, idx):
    smiles = self.data[idx]
    mol_tree = MolTree(smiles)
    mol_tree.recover()
    mol_tree.assemble()
    return mol_tree
