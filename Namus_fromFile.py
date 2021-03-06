# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:28:01 2015

@author: jenniferstark
"""

import pandas as pd
from bs4 import BeautifulSoup

# begin list where all data from each case ('individual' dictionary) will be appended
namus = []

# code to loop though potential case numbers, see if .html file exists on local machine
# if does exist, is it longer than 500 lines (shorter means it is a 'place holder' file that 
# contains no case data) then open it call 'get_namus_fromFile()' 
def namus_fromFile(cases):
    for case in cases:
        try:
            with open(("../../Namus_data/html_files2/" + 'case_' + str(case) + '.html'), 'rU') as f:
                lines = len(f.readlines())
                if lines > 500:
                    with open(("../../Namus_data/html_files2/" + 'case_' + str(case) + '.html'), 'rU') as f:
                        html = f.read()
                        print(case)
                        namus.append(get_namus_fromFile(html))
        except:
            continue

# code to scrape through the .html file on local machine and extract data into a separate dictionary for 
# each case. Each dictionary then gets appended to 'namus' list
def get_namus_fromFile(html):
    b = BeautifulSoup(html)
    
    individual={}
    
    individual['case_rating'] = b.find(name='dt', attrs={'class':'rating'}).find(name='span').text.strip() 
    individual['case_status'] = b.find(name='label', attrs={'for':'case_status'}).find_next('td').text.strip() 
    individual['case_number'] = b.find(name='label', attrs={'for':'case_case_number'}).find_next('td').text.strip() 
    individual['date_found'] = b.find(name='label', attrs={'for':'case_date_found_2i'}).find_next('td').text.strip()  #make datetime
   
    individual['est_age'] = b.find(name='label', attrs={'for':'case_estimated_age'}).find_next('td').text.strip()  #string?
    individual['min_age']= b.find(name='label', attrs={'for':'case_minimum_age'}).find_next('td').text.strip()  #string!?
    individual['max_age'] = b.find(name='label', attrs={'for':'case_maximum_age'}).find_next('td').text.strip()  #String?!
    individual['race'] = b.find(name='label', attrs={'for':'case_race'}).find_next('td').text.strip() 
    individual['ethnicity'] = b.find(name='label', attrs={'for':'case_ethnicity'}).find_next('td').text.strip()  #if empty, replace w NA
    individual['sex'] = b.find(name='label', attrs={'for':'case_sex'}).find_next('td').text.strip() 
    individual['weight'] = b.find(name='label', attrs={'for':'case_weight'}).find_next('td').text.strip() 
    individual['height'] = b.find(name='label', attrs={'for':'case_height'}).find_next('td').text.strip()
    
    individual['all_parts_recovered'] = int(b.find(name='input', id='case_body_inventory_all_parts_recovered').find_next('input')['value'])
    individual['head_not_recovered'] = int(b.find(name='input', id='case_body_inventory_head_not_recovered').find_next('input')['value'])
    individual['torso_not_recovered'] = int(b.find(name='input', id='case_body_inventory_torso_not_recovered').find_next('input')['value'])
    individual['n-limbs_not_recovered'] = int(b.find(name='input', id='case_body_inventory_limbs_not_recovered').find_next('input')['value'])
    individual['n-hands_not_recovered'] = int(b.find(name='input', id='case_body_inventory_hands_not_recovered').find_next('input')['value'])
    individual['recognizable_face'] = b.find(name='label', attrs={'for':'case_body_condition'}).find_next('td').text.strip() 
    
    individual['min_year_of_death'] = b.find(name='label', attrs={'for':'case_minimum_year_of_death'}).find_next('td').text.strip() # needs improvement
    individual['postmortem_interval'] = b.find(name='label', attrs={'for':'case_postmortem_interval'}).find_next('td').text.strip()
    
    individual['address_1'] = b.find(name='label', attrs={'for':'case_address_found_1'}).find_next('td').text.strip()
    individual['address_2'] = b.find(name='label', attrs={'for':'case_address_found_2'}).find_next('td').text.strip()
    individual['city'] = b.find(name='label', attrs={'for':'case_city_found'}).find_next('td').text.strip()
    individual['state'] = b.find(name='label', attrs={'for':'case_state_found_id'}).find_next('td').text.strip()
    individual['zip'] = b.find(name='label', attrs={'for':'case_zip_found'}).find_next('td').text.strip()
    individual['county'] = b.find(name='label', attrs={'for':'case_county_found_id'}).find_next('td').text.strip()
    
    individual['circumstances'] = b.find(name='div', id="case_circumstances").text.strip()
    
    individual['hair_color'] = b.find(name='label', attrs={'for':'case_hair_color'}).find_next('td').text.strip()
    individual['head_hair'] = b.find(name='div', id='case_head_hair').text.strip() 
    individual['body_hair'] = b.find(name='div', id='case_body_hair').text.strip() 
    individual['facial_hair'] = b.find(name='div', id='case_facial_hair').text.strip() 
    individual['left_eye_color'] = b.find(name='label', attrs = {'for':'case_eye_color_left'}).find_next('td').text.strip() 
    individual['right_eye_color'] = b.find(name='label', attrs = {'for':'case_eye_color_right'}).find_next('td').text.strip() 
    individual['eye_description'] = b.find(name='div', id='case_eye_description').text.strip() 
    
    individual['amputations'] = int(b.find(name='input', id='case_amputations').find_next('input')['value'])
    if individual['amputations'] == 1:
        individual['amputations_description'] = b.find(name='div', id='case_amputations_details').text.strip() 
    else:
        individual['amputations_description'] = 'NA'
        
    individual['deformities'] = int(b.find(name='input', id='case_deformities').find_next('input')['value'])
    if individual['deformities'] == 1:
        individual['deformities_description'] = b.find(name='div', id='case_deformities_details').text.strip() 
    else:
        individual['deformities_description'] = 'NA'
        
    individual['scars_and_marks'] = int(b.find(name='input', id='case_scars_and_marks').find_next('input')['value'])
    if individual['scars_and_marks'] == 1:
        individual['scars_and_marks_description'] = b.find(name='div', id='case_scars_and_marks_details').text.strip() 
    else:
        individual['scars_and_marks_description'] = 'NA'
        
    individual['tattoos'] = int(b.find(name='input', id='case_tattoos').find_next('input')['value'])
    if individual['tattoos'] == 1:
        individual['tattoos_description'] = b.find(name='div', id='case_tattoos_details').text.strip() 
    else:
        individual['tattoos_description'] = 'NA'
    
    individual['piercings'] = int(b.find(name='input', id='case_piercings').find_next('input')['value'])
    if individual['piercings'] == 1:
        individual['piercings_description'] = b.find(name='div', id='case_piercings_details').text.strip() 
    else:
        individual['piercings_description'] = 'NA'
        
    individual['artificial_parts_aids'] = int(b.find(name='input', id='case_artificial_body_parts_and_aids').find_next('input')['value'])
    if individual['artificial_parts_aids'] == 1:
        individual['artificial_parts_aids_description'] = b.find(name='div', id='case_artificial_body_parts_and_aids_details').text.strip() 
    else:
        individual['artificial_parts_aids_description'] = 'NA'
        
    individual['finger_toe_nails'] = int(b.find(name='input', id='case_finger_and_toe_nails').find_next('input')['value'])
    if individual['finger_toe_nails'] == 1:
        individual['finger_toe_nails_description'] = b.find(name='div', id='case_finger_and_toe_nails_details').text.strip() 
    else:
        individual['finger_toe_nails_description'] = 'NA'
        
    individual['other_distinctive_features'] = int(b.find(name='input', id='case_physical_other').find_next('input')['value'])
    if individual['other_distinctive_features'] == 1:
        individual['other_distinctive_features_description'] = b.find(name='div', id='case_physical_other_details').text.strip() 
    else:
        individual['other_distinctive_features_description'] = 'NA'
        
    individual['medical_implants'] = int(b.find(name='input', id='case_medical_implants').find_next('input')['value'])
    if individual['medical_implants'] == 1:
        individual['medical_implants_description'] = b.find(name='div', id='case_medical_implants_details').text.strip() 
    else:
        individual['medical_implants_description'] = 'NA'
        
    individual['foreign_objects'] = int(b.find(name='input', id='case_foreign_objects').find_next('input')['value'])
    if individual['foreign_objects'] == 1:
        individual['foreign_objects_description'] = b.find(name='div', id='case_foreign_objects_details').text.strip() 
    else:
        individual['foreign_objects_description'] = 'NA'
        
    individual['skeletal_findings'] = int(b.find(name='input', id='case_skeletal_findings').find_next('input')['value'])
    if individual['skeletal_findings'] == 1:
        individual['skeletal_findings_description'] = b.find(name='div', id='case_skeletal_findings_details').text.strip() 
    else:
        individual['skeletal_findings_description'] = 'NA'
       
    individual['organ_absent'] = int(b.find(name='input', id='case_organ_absent').find_next('input')['value'])
    if individual['organ_absent'] == 1:
        individual['organ_absent_description'] = b.find(name='div', id='case_organ_absent_details').text.strip() 
    else:
        individual['organ_absent_description'] = 'NA'
        
    individual['prior_surgery'] = int(b.find(name='input', id='case_prior_surgery').find_next('input')['value'])
    if individual['prior_surgery'] == 1:
        individual['prior_surgery_description'] = b.find(name='div', id='case_prior_surgery_details').text.strip() 
    else:
        individual['prior_surgery_description'] = 'NA'
        
    individual['other_medical_information'] = int(b.find(name='input', id='case_medical_other').find_next('input')['value'])
    if individual['other_medical_information'] == 1:
        individual['other_medical_information_description'] = b.find(name='div', id='case_medical_other_details').text.strip() 
    else:
        individual['other_medical_information_description'] = 'NA'
    
    individual['fingerprints'] = b.find(name='div', id='fingerprints').find_next('td', attrs={'class':'view_field'}).text.strip()
   
    individual['clothing_on_body'] = b.find('div', id='case_clothing_on_body').text.strip() 
    individual['clothing_with_body'] = b.find('div', id='case_clothing_with_body').text.strip() 
    individual['footwear'] = b.find('div', id='case_footwear').text.strip() 
    individual['jewelry'] = b.find('div', id='case_jewelry').text.strip() 
    individual['eyewear'] = b.find('div', id='case_eyewear').text.strip() 
    individual['other_items_with_body'] = b.find('div', id='case_other_items_with_body').text.strip() 
    
    individual['dental'] = b.find(name='div', id='dental').find_next('td', attrs={'class':'view_field'}).text.strip()
    
    individual['dna'] = b.find(name='div', id='dna').find_next('td', attrs={'class':'view_field'}).text.strip()
    
    individual['images'] = len(b.find('div', id='image_box').find_all('img'))

    return individual
    
    
namus_fromFile(range(0,16000))

# Convert the list of dictionaries to a pandas dataframe
namusdf = pd.DataFrame(namus)

# save dataframe as both pickled file and as a csv
namusdf.to_csv('namus_html2.csv')
namusdf.to_pickle('namus_html2.pkl')