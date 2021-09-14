
from Utils.data_utils import flat_to_list, convert_to_nb

from Methods.MI import MI_matrix

import os


import argparse, textwrap

parser = argparse.ArgumentParser(description=textwrap.dedent('''\
                                                Read a protein sequence alignment file (flat/fasta), 
                                                convert it into a dataframe : sequences in rows / positions in columns, 
                                                then convert thr dataframe into array with 16 numbers instead the 16 PB.
                                                Te final step is computing mutual information between columns/positions
                                                '''))

parser.add_argument('--input_path', type=str, default=None, help='path to input dataset')
parser.add_argument('--output_dir', type=str, default=None, help='path to output directory')
parser.add_argument('--start_idx', type=int, default=None, help='first row/frame')
parser.add_argument('--end_idx', type=int, default=None, help='last row/frame')
parser.add_argument('--data_size', type=int, default=None, help='number of rows/frames to take')

args = parser.parse_args()


flat_to_list(input_path=args.input_path, output_dir=args.output_dir)

input_path = os.path.join(args.output_dir, 'seqlist.npy')

convert_to_nb(input_path=input_path, output_dir=args.output_dir)

input_path = os.path.join(args.output_dir, 'nblist.npy')

MI_matrix(input_path=input_path, output_dir=args.output_dir, start_idx=args.start_idx, end_idx=args.end_idx, data_size=args.data_size)
