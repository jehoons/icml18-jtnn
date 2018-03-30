from rdkit import Chem
import os

from jtnn import MolTree


def create_secret_train():
  if os.path.exists('secret_train.txt'):
    return
  lines = [x.strip().split(',') for x in open('secret_data.csv').readlines()]
  lines = lines[1:]
  lines = [x[0] for x in lines]

  full_train = [x.strip() for x in open('train.txt').readlines()]
  full_train += lines
  with open('secret_train.txt', 'w') as fout:
    for line in full_train:
      fout.write(line + "\n")


def create_secret_vocab():
  if os.path.exists('secret_vocab.txt'):
    return
  cset = set()
  lines = [x.strip().split(',')[0] for x in open('secret_data.csv').readlines()][1:]
  for i, line in enumerate(lines):
    mt = MolTree(line)
    for c in mt.nodes:
      cset.add(c.smiles)
  existing_vocab = [x.strip() for x in open('vocab.txt').readlines()]
  cset.update(existing_vocab)
  with open('secret_vocab.txt', 'w') as fout:
    for line in cset:
      fout.write(line + '\n')


def main():
  create_secret_train()
  create_secret_vocab()


if __name__ == "__main__":
  main()
