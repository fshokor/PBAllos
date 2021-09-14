import pandas as pd
import numpy as np
import os

def flat_to_list(input_path=None, output_dir=None):
    """
    Read and convert a flat file into a PB sequence alignment array and table
    Args:
        input_path: path to flat input file
        output_dir: path to the output directory
    """

    fileobj = open(input_path)
    lines = []
    for line in fileobj:
        lines.append(line.strip())

    seqlist = []
    for x in lines:
        x = list(x)
        seqlist.append(x)

    seqlist =np.array(seqlist)

    output_path = os.path.join(output_dir, 'seqlist.npy')
    np.save(output_path, seqlist)

    df = pd.DataFrame(seqlist)
    output_path = os.path.join(output_dir, 'pbseq.csv')
    df.to_csv(output_path)



def convert_to_nb(input_path=None, output_dir=None):
    """
    convert letters in PB sequences list to numbers
    create number sequence alignment array and table
    Args:
        input_path: path to input file of sequences list
        output_dir: path to the output directory

    """
    seqlist = np.load(input_path)

    # convert letters to numbers
    nblist = [[ord(i) % 32 for i in x] for x in seqlist]

    # delete first and last 2 positions (Z)
    I = [0, 1, 139, 140]
    for x in nblist:
        for ele in sorted(I, reverse=True):
            del x[ele]

    nblist = np.array(nblist)
    output_path = os.path.join(output_dir, 'nblist.npy')
    np.save(output_path, nblist)

    df2 = pd.DataFrame(nblist)
    output_path = os.path.join(output_dir, 'nbseq.csv')
    df2.to_csv(output_path)


