import psycopg2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Establish DB:
DBNAME = "opportunity_youth"

def create_kc_df():
    """
    Function to recreate the king county puma codes df
    """

    # Create a connection to db
    conn = psycopg2.connect(dbname=DBNAME)

    # create df of just WA entries
    puma_names_2010_wa = pd.read_sql("SELECT * FROM puma_names_2010 WHERE state_name = 'Washington';", conn)

    # subset just the king county entries
    king_county = puma_names_2010_wa[puma_names_2010_wa['puma_name'].str.match('^King County*')== True]
    
    conn.close()
    
    return king_county

def create_skc_df():
    """
    Function to recreate the skc puma codes df
    """
    # get puma codes and create skc_df
    skc_puma_codes = ['11613', '11614', '11615', '11612']
    
    # create skc df from king county df:
    skc_pumas = create_kc_df()[create_kc_df()['puma'].isin(skc_puma_codes)]
    
    return skc_pumas


def skc_df():
    """
    Function to create skc pums data set
    """
    # Create a connection to db
    conn = psycopg2.connect(dbname=DBNAME)
    
    skc_puma_codes = ['11613', '11614', '11615', '11612']
    
    QUERY = """
    SELECT serialno AS id, agep AS age, sex, pwgtp AS person_weight, puma, sch AS school_enrollment, schl AS education_attained, 
            esr AS employment_status, nwav AS avail_for_work, nwlk AS look_for_work, nwab AS absent_from_work, nwla AS layoff
    FROM pums_2017
    WHERE agep BETWEEN 16 AND 24"""

    relevant_ages_pums = pd.read_sql(QUERY, conn)
    skc_df = relevant_ages_pums[relevant_ages_pums['puma'].isin(skc_puma_codes)]    
    
    conn.close()
    
    return skc_df


def add_cols_skc(df):
    """
    Adds the 'is_oy' and 'age_group' cols to skc df
    """
    # Function to categorise ages:
    def get_age_group(age):
        if age in range(16, 19):
            return 'Ages 16-18'
        elif age in range(19, 22):
            return 'Ages 19-21'
        else:
            return 'Ages 22-24'
     
    # Assign values to 'age_group'
    df['age_group'] = df['age'].map(get_age_group)
    
    # Create oy employment/school variables:
    oy_employment_status = ['3', '6']
    oy_school_enrollment = ['1']
    
    # Assign values to 'is_oy'
    df['is_oy'] = (df['employment_status'].isin(oy_employment_status)) & (df['school_enrollment'].isin(oy_school_enrollment))
    
    return df