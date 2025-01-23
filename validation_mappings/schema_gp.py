from .options_gp import OPTIONS_GP
SCHEMA_GP = {

    #String
    "company_name": {
        "type": "string",
    },

    #0.1.1
    #String
    "use_of_international_disclosing_standard": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.1
    #String
    "use_of_international_disclosing_standard_tcfd": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.2
    #String
    "use_of_international_disclosing_standard_gri": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.3
    #String
    "use_of_international_disclosing_standard_sasb": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.4
    #String
    "use_of_international_disclosing_standard_cdsb": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.5
    #String
    "use_of_international_disclosing_standard_ghg_protocol": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.6
    #String
    "use_of_international_disclosing_standard_tnfd": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.7 
    #String
    "use_of_international_disclosing_standard_sbti": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.8 
    #String
    "use_of_international_disclosing_standard_cdp": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.9 
    #String
    "use_of_international_disclosing_standard_wef": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.1.10 
    #String
    "use_of_international_disclosing_standard_other": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2 
    #String
    "participates_in_sustainability_climate_initiatives": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2.1 
    #String
    "participates_in_sustainability_climate_initiatives_pri": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2.2 
    #String
    "participates_in_sustainability_climate_initiatives_nzaoa": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2.3 
    #String
    "participates_in_sustainability_climate_initiatives_nzami": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2.4 
    #String
    "participates_in_sustainability_climate_initiatives_ici": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
     
    #0.1.2.5 
    #String
    "participates_in_sustainability_climate_initiatives_the_investor_agenda": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2.6 
    #String
    "participates_in_sustainability_climate_initiatives_transition_pathway_initiative": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2.7 
    #String
    "participates_in_sustainability_climate_initiatives_iigcc": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.2.8 
    #String
    "participates_in_sustainability_climate_initiatives_other": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.1 
    #String
    "code_of_conduct": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.2 
    #String
    "overall_sustainability_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
     
    #0.1.3.3 
    #String
    "environmental_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.4 
    #String
    "anti_discrimination_and_equal_opportunities_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.5 
    #String
    "diversity_inclusion_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.6 
    #String
    "salary_remuneration_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.7 
    #String
    "health_and_safety_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.8 
    #String
    "human_rights_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
     
    #0.1.3.9 
    #String
    "anti_corruption_bribery_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.10 
    #String
    "data_privacy_security_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.11 
    #String
    "supply_chain_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.1.3.12 
    #String
    "cybersecurity_data_management_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from ems_presence_select
    "ems_implemented": {
        "type": "string",
        "allowed": list(OPTIONS_GP["ems_presence_select"].keys()),
    },

    #String
    "other_ems_certification": {
        "type": "string",
    },
    
    #STRING from ghg_scope_list
    "ghg_scope_measured_calculated": {
        "type": "string",
        "allowed": list(OPTIONS_GP["ghg_scope_list"].keys()),
    },

    #Float (positive)
    "total_ghg_emissions": {"type": "float", 'min': 0},

    #Float (positive)
    "total_scope_1_emissions":  {"type": "float", 'min': 0},

    #STRING from ghg_scope_1_methodology
    "total_scope_1_emissions_methodology": {
        "type": "string",
        "allowed": list(OPTIONS_GP["ghg_scope_1_methodology"].keys()),
    },

    #Float (positive)
    "total_scope_2_emissions":  {"type": "float", 'min': 0},

    #STRING from ghg_scope_2_methodology
    "total_scope_2_emissions_methodology": {
        "type": "string",
        "allowed": list(OPTIONS_GP["ghg_scope_2_methodology"].keys()),
    },

    #Float (positive)
    "total_scope_3_emissions":  {"type": "float", 'min': 0},

    #STRING from ghg_scope_3_methodology
    "total_scope_3_emissions_methodology": {
        "type": "string",
        "allowed": list(OPTIONS_GP["ghg_scope_3_methodology"].keys()),
    },
    
    #Float (positive)
    "carbon_offset_tco2e":  {"type": "float", 'min': 0},
    
    #1.1.8.1 
    #String
    "environmental_impact_international_organisations": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.1.8.2 
    #String
    "environmental_impact_european_commission": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
     
    #1.1.8.3 
    #String
    "environmental_impact_national_promotional_institutions": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.1.8.4 
    #String
    "environmental_impact_other_public_bodies": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.1.8.5 
    #String
    "environmental_impact_private_non_profit": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.1.8.6 
    #String
    "environmental_impact_other_private": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #Float (positive)
    "total_ftes_end_of_report_year":  {"type": "float", 'min': 0},
    
    #Float (positive)
    "number_of_ftes_end_of_report_year_female":  {"type": "float", 'min': 0},
    
    #Float (positive)
    "number_of_ftes_end_of_report_year_non_binary":  {"type": "float", 'min': 0},
    
    #Float (positive)
    "number_of_ftes_end_of_report_year_non_disclosed":  {"type": "float", 'min': 0},
    
    #Float (positive)
    "number_of_ftes_end_of_report_year_male":  {"type": "float", 'min': 0},
    
    #Float (positive)
    "turnover_fte":  {"type": "float", 'min': 0},
    
    #Integer (positive)
    "total_number_of_partners": {"type": "integer", 'min': 0},
    
    #Integer (positive)
    "number_of_partners_female": {"type": "integer", 'min': 0},
    
    #Integer (positive)
    "number_of_partners_non_binary": {"type": "integer", 'min': 0},
    
    #Integer (positive)
    "number_of_partners_non_disclosed": {"type": "integer", 'min': 0},
    
    #Integer (positive)
    "number_of_partners_male": {"type": "integer", 'min': 0},
}

GP_COMPOUND_ID_UNITS = {
    "total_ghg_emissions": "tCO2e",
    "total_scope_1_emissions": "tCO2e",
    "total_scope_2_emissions": "tCO2e",
    "total_scope_3_emissions": "tCO2e",
    "carbon_offset_tco2e": "tCO2e",
    "total_ftes_end_of_report_year": "FTEs",
    "number_of_ftes_end_of_report_year_female": "FTEs",
    "number_of_ftes_end_of_report_year_non_binary": "FTEs",
    "number_of_ftes_end_of_report_year_non_disclosed": "FTEs",
    "number_of_ftes_end_of_report_year_male": "FTEs",
    "total_number_of_partners": "people",
    "number_of_partners_female": "people",
    "number_of_partners_non_binary": "people",
    "number_of_partners_non_disclosed": "people",
    "number_of_partners_male": "people",
    "turnover_fte": "FTEs"
}

ALL_GP_METRICS = [
    "company_name",
    "use_of_international_disclosing_standard",
    "use_of_international_disclosing_standard_tcfd",
    "use_of_international_disclosing_standard_gri",
    "use_of_international_disclosing_standard_sasb",
    "use_of_international_disclosing_standard_cdsb",
    "use_of_international_disclosing_standard_ghg_protocol",
    "use_of_international_disclosing_standard_tnfd",
    "use_of_international_disclosing_standard_sbti",
    "use_of_international_disclosing_standard_cdp",
    "use_of_international_disclosing_standard_wef",
    "use_of_international_disclosing_standard_other",
    "participates_in_sustainability_climate_initiatives",
    "participates_in_sustainability_climate_initiatives_pri",
    "participates_in_sustainability_climate_initiatives_nzaoa",
    "participates_in_sustainability_climate_initiatives_nzami",
    "participates_in_sustainability_climate_initiatives_ici",
    "participates_in_sustainability_climate_initiatives_the_investor_agenda",
    "participates_in_sustainability_climate_initiatives_transition_pathway_initiative",
    "participates_in_sustainability_climate_initiatives_iigcc",
    "participates_in_sustainability_climate_initiatives_other",
    "code_of_conduct",
    "overall_sustainability_policy",
    "environmental_policy",
    "anti_discrimination_and_equal_opportunities_policy",
    "diversity_inclusion_policy",
    "salary_remuneration_policy",
    "health_and_safety_policy",
    "human_rights_policy",
    "anti_corruption_bribery_policy",
    "data_privacy_security_policy",
    "supply_chain_policy",
    "cybersecurity_data_management_policy",
    "ems_implemented",
    "other_ems_certification",
    "ghg_scope_measured_calculated",
    "total_ghg_emissions",
    "total_scope_1_emissions",
    "total_scope_1_emissions_methodology",
    "total_scope_2_emissions",
    "total_scope_2_emissions_methodology",
    "total_scope_3_emissions",
    "total_scope_3_emissions_methodology",
    "carbon_offset_tco2e",
    "environmental_impact_international_organisations",
    "environmental_impact_european_commission",
    "environmental_impact_national_promotional_institutions",
    "environmental_impact_other_public_bodies",
    "environmental_impact_private_non_profit",
    "environmental_impact_other_private",
    "total_ftes_end_of_report_year",
    "number_of_ftes_end_of_report_year_female",
    "number_of_ftes_end_of_report_year_non_binary",
    "number_of_ftes_end_of_report_year_non_disclosed",
    "number_of_ftes_end_of_report_year_male",
    "total_number_of_partners",
    "number_of_partners_female",
    "number_of_partners_non_binary",
    "number_of_partners_non_disclosed",
    "number_of_partners_male",
    "turnover_fte"
]


REQUIRED_GP_METRICS = [
    "company_name",
    "use_of_international_disclosing_standard",
    "participates_in_sustainability_climate_initiatives",
    "code_of_conduct",
    "overall_sustainability_policy",
    "environmental_policy",
    "anti_discrimination_and_equal_opportunities_policy",
    "diversity_inclusion_policy",
    "salary_remuneration_policy",
    "health_and_safety_policy",
    "human_rights_policy",
    "anti_corruption_bribery_policy",
    "data_privacy_security_policy",
    "supply_chain_policy",
    "cybersecurity_data_management_policy",
    "ems_implemented",
    "ghg_scope_measured_calculated",
    "total_ghg_emissions",
    "total_scope_1_emissions",
    "total_scope_1_emissions_methodology",
    "total_scope_2_emissions",
    "total_scope_2_emissions_methodology",
    "total_scope_3_emissions",
    "total_scope_3_emissions_methodology",
    "carbon_offset_tco2e",
    "environmental_impact_international_organisations",
    "environmental_impact_european_commission",
    "environmental_impact_national_promotional_institutions",
    "environmental_impact_other_public_bodies",
    "environmental_impact_private_non_profit",
    "environmental_impact_other_private",
    "total_ftes_end_of_report_year",
    "number_of_ftes_end_of_report_year_female",
    "number_of_ftes_end_of_report_year_non_binary",
    "number_of_ftes_end_of_report_year_non_disclosed",
    "number_of_ftes_end_of_report_year_male",
    "total_number_of_partners",
    "number_of_partners_female",
    "number_of_partners_non_binary",
    "number_of_partners_non_disclosed",
    "number_of_partners_male",
    "turnover_fte"
]