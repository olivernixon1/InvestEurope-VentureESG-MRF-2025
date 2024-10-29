SCHEMA = {

    #String
    "company_name": {
        "type": "string",
    },

    #String
    "business_identification_number": {
        "type": "string",
    },

    #String
    "business_identification_number_system": {
        "type": "string",
    },

    #STRING from iso_country_code
    "country_of_domicile": {
        "type": "string",
        "allowed": country_list,
    },

    #STRING from iso_country_code
    "primary_country_of_operations": {
        "type": "string",
        "allowed": country_list,
    },

    #STRING or LIST from iso_country_code
    "other_countries_of_operations": {
        "allowed": country_list,
    },

    #STRING or LIST from nace_divisions
    "sectors_of_operation": {
        "allowed": nace_divisions,
    },

    #Float (positive)
    "revenue": {"type": "float", 'min': 0},
    
    #Float (positive)
    "annual_balance_sheet_assets_total": {"type": "float", 'min': 0},

    #Float (positive)
    "turnover": {"type": "float", 'min': 0},

    #STRING from iso_currency_code
    "currency": {
        "type": "string",
        "allowed": iso_currency_code,
    },

    #Float (positive)
    "total_ftes_end_of_report_year": {"type": "float", 'min': 0},

    #Float (positive)
    "total_ftes_end_of_previous_report_year": {"type": "float", 'min': 0},

    #STRING from yes_no
    "listed": {
        "type": "string",
        "allowed": ["yes", "no"],
    }

    #String
    "listed_ticker": {
        "type": "string",
    },
    
    #STRING from yes_no
    "overall_sustainability_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #STRING from yes_no
    "environmental_policy": {
       "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "anti_discrimination_and_equal_opportunities_policy": {
       "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "health_and_safety_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "human_rights_policy": {
       "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "anti_corruption_bribery_policy": {
       "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "data_privacy_security_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "diversity_inclusion_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "code_of_conduct": {
       "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "written_salary_remuneration_policy": {
       "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "supply_chain_policy": {
       "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "cybersecurity_data_management_policy": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #STRING from yes_no
    "dedicated_sustainability_staff": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #STRING or LIST from management_and_board_position_list
    "sustainability_staff_roles": {
        "allowed": management_and_board_position_list
    },
    
    #STRING from yes_no
    "occurrence_of_esg_incidents": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #Integer (positive)
    "number_of_esg_incidents": {"type": "integer", 'min': 0},

    #STRING from yes_no
    "eu_taxonomy_assessment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #Float between 0 and 100
    "percentage_turnover_eu_taxonomy": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },

    #Float between 0 and 100
    "percentage_capex_eu_taxonomy": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },

    #Float between 0 and 100
    "percentage_opex_eu_taxonomy": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },

    #STRING from yes_no
    "tobacco_activities": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #STRING from yes_no
    "hard_coal_and_lignite_activities": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #STRING from yes_no
    "oil_fuels_activities": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #STRING from yes_no
    "gaseous_fuels_activities": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #STRING from yes_no
    "high_ghg_intensity_electricity_generation": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #STRING from ems_presence_select
    "ems_implemented": {
        "type": "string",
        "allowed": ems_presence_select,
    },

    #String
    "other_ems_certification": {
        "type": "string",
    },

    #STRING from ghg_scope_list
    "ghg_scope_measured_calculated": {
        "type": "string",
        "allowed": ghg_scope_list,
    },

    #Float (positive)
    "total_ghg_emissions": {"type": "float", 'min': 0},

    #Float (positive)
    "total_scope_1_emissions":  {"type": "float", 'min': 0},

    #STRING from ghg_scope_1_methodology
    "total_scope_1_emissions_methodology": {
        "type": "string",
        "allowed": ghg_scope_1_methodology,
    },

    #Float (positive)
    "total_scope_2_emissions":  {"type": "float", 'min': 0},

    #STRING from ghg_scope_2_methodology
    "total_scope_2_emissions_methodology": {
        "type": "string",
        "allowed": ghg_scope_2_methodology,
    },

    #Float (positive)
    "total_scope_3_emissions":  {"type": "float", 'min': 0},

    #STRING from ghg_scope_3_methodology
    "total_scope_3_emissions_methodology": {
        "type": "string",
        "allowed": ghg_scope_3_methodology,
    },

    #Float (positive)
    "scope_3_emissions:scope_cat_3:purchased_goods_and_services": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:capital_goods": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:fuel_and_energy_related_not_in_scopes_1_2": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:upstream_transportation_distribution": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:waste_generated_in_operations": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:business_travel": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:employee_commuting": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:upstream_leased_assets": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:investments": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:downstream_transportation_distribution": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:processing_of_sold_products": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:use_of_sold_products": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:endoflife_treatment_of_sold_products": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:downstream_leased_assets": {"type": "float", 'min': 0},

    #Float (positive)
    "scope_3_emissions:scope_cat_3:franchises": {"type": "float", 'min': 0},

    #STRING from decarbonisation_strategy
    "decarbonisation_strategy_set": {
        "type": "string",
        "allowed": decarbonisation_strategy,
    }

    #STRING from ghg_reduction_target
    "ghg_reduction_target_set": {
        "type": "string",
        "allowed": ghg_reduction_target,
    }

    #STRING from long_term_net_zero_goal
    "long_term_net_zero_goal_set": {
        "type": "string",
        "allowed": long_term_net_zero_goal,
    }

    #Float (positive)
    "total_energy_consumption": {"type": "float", 'min': 0},

    #Float (positive)
    "energy_consumption_renewable": {"type": "float", 'min': 0},
    
    #Float (positive)
    "total_emissions_to_water": {"type": "float", 'min': 0},

    #Float (positive)
    "quantity_hazardous_radioactive_waste_generated": {"type": "float", 'min': 0},

    #STRING from yes_no
    "activities_affecting_biodiversity_areas": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #Float (positive) — note: number of FTEs can be non-integer
    "number_ftes_end_of_period_gender:gender:female": {"type": "float", 'min': 0},
    "number_ftes_end_of_period_gender:gender:male": {"type": "float", 'min': 0},
    "number_ftes_end_of_period_gender:gender:non_binary": {"type": "float", 'min': 0},
    "number_ftes_end_of_period_gender:gender:non_disclosed": {"type": "float", 'min': 0},

    #Integer (positive)
    "number_csuite_employees_fte_gender:gender:female": {"type": "integer", 'min': 0},
    "number_csuite_employees_fte_gender:gender:male": {"type": "integer", 'min': 0},
    "number_csuite_employees_fte_gender:gender:non_binary": {"type": "integer", 'min': 0},
    "number_csuite_employees_fte_gender:gender:non_disclosed": {"type": "integer", 'min': 0},

    #Integer (positive)
    "number_founders_still_employed_by_gender:gender:female": {"type": "integer", 'min': 0},
    "number_founders_still_employed_by_gender:gender:male": {"type": "integer", 'min': 0},
    "number_founders_still_employed_by_gender:gender:non_binary": {"type": "integer", 'min': 0},
    "number_founders_still_employed_by_gender:gender:non_disclosed": {"type": "integer", 'min': 0},

    #STRING from yes_no
    "measurement_of_unadjusted_gender_pay_gap": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #Float between 0 and 100
    "unadjusted_gender_pay_gap": {"type": "float", "min": 0.0, "max": 100.0},

    #Float (positive) — note: number of FTEs can be non-integer
    "number_of_organic_net_new_hires_fte": {"type": "float", 'min': 0},

    #Float (positive) — note: number of FTEs can be non-integer
    "number_of_total_net_new_hires_fte": {"type": "float", 'min': 0},

    #Float (positive) — note: number of FTEs can be non-integer
    "number_of_total_net_new_hires_fte_inside_eu": {"type": "float", 'min': 0},

    #Float (positive) — note: number of FTEs can be non-integer
    "number_of_total_net_new_hires_fte_outside_eu": {"type": "float", 'min': 0},

    #Float (positive) — note: number of FTEs can be non-integer
    "number_of_organic_leavers_fte": {"type": "float", 'min': 0},

    #STRING from yes_no
    "implements_employee_survey_questionnaires": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #Float between 0 and 100
    "percentage_employees_responding_employee_survey": {"type": "float", "min": 0.0, "max": 100.0},

    #STRING from yes_no
    "implemented_whistleblower_procedure": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #Float (positive)
    "average_hours_training_employees_taken_during_reporting_period": {"type": "float", 'min': 0},

    #Integer (positive)
    "number_of_workrelated_injuries": {"type": "integer", 'min': 0},

    #Integer (positive)
    "number_of_workrelated_fatalities": {"type": "integer", 'min': 0},

    #Float (positive)
    "days_lost_due_to_injury": {"type": "float", 'min': 0},

    #STRING from yes_no
    "human_rights_due_diligence_process": {
        "type": "string",
        "allowed": ["yes", "no"],
    },

    #Integer (positive)
    "total_number_of_board_members": {"type": "integer", 'min': 0},
    "board_governance_members:gender:female": {"type": "integer", 'min': 0},
    "board_governance_members:gender:male": {"type": "integer", 'min': 0},
    "board_governance_members:gender:non_binary": {"type": "integer", 'min': 0},
    "board_governance_members:gender:non_disclosed": {"type": "integer", 'min': 0},

    #Integer (positive)
    "number_board_members_underrepresented_groups": {"type": "integer", 'min': 0},

    #Integer (positive)
    "number_independent_board_members": {"type": "integer", 'min': 0},

    #Integer (positive)
    "number_of_data_breaches": {"type": "integer", 'min': 0},
}
