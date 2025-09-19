import pandas as pd
def wrangle(file_path):
    #load csv file
    df = pd.read_csv(file_path)
    
    # subset to properties in 'Capital Federal'
    mask_prop = df['place_with_parent_names'].str.contains('Capital Federal') 
    
    # subset to 'apartment' property_type 
    mask_prop_type = df['property_type'] == 'apartment'
    
    # subset to properties with price less than 400_000
    mask_price = df['price_aprox_usd'] < 400_000
    df = df[mask_prop & mask_prop_type & mask_price]
    
    # remove outliers from the size column of apartments in capital federal properties with price less than 400000
    lower, upper = df['surface_covered_in_m2'].quantile([0.1, 0.9])
    mask_size = df['surface_covered_in_m2'].between(lower, upper)
    
    df = df[mask_prop & mask_prop_type & mask_price & mask_size]
    
    return df