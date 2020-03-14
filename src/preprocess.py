import numpy as np
import pandas as pd
import argparse

def clean(school_path='data/hsls_school_v1_0.csv', student_path='data/hsls_student_v1_0.csv'):
    '''
	This method preprocesses the data for both schools
	and students and returns dataframe objects corresponding to each of these factors.
	Returns a list of the following:
	Dataframe object containing school variables.
	Dataframe object containing student variables.
	'''

    assert isinstance(school_path, str) and isinstance(student_path, str), "path variables must be of type str"



    print("Read data...")
    sc = pd.read_csv(school_path)
    st = pd.read_csv(student_path)

    print("Clean data...")
    # remove -5 values, private data
    sc = sc.replace(-5, np.nan)
    st = st.replace(-5, np.nan)
    sc = sc.dropna(axis=1)
    st = st.dropna(axis=1)

    # Remove invalid data
    sc = sc.replace([-9, -8, -7], np.nan)
    st = st.replace([-9, -8, -7], np.nan)
    # Replace NA with minimum value in that column
    sc = sc.fillna(sc.min(axis=0))
    st = st.fillna(st.min(axis=0))
    print('Finish Cleaning')

    return [sc, st]


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('school_file', type=str, default='data/hsls_school_v1_0.csv',
                        help='Path to file containing the school data')
    parser.add_argument('student_file', type=str, default='data/hsls_school_v1_0.csv',
                        help='Path to file containing the student data')
    args = parser.parse_args()

    [sc, st] = clean(args.school_file, args.student_file)
    print("School Dataframe sample")
    print(sc.head())
    print("Student Dataframe sample")
    print(st.head())


