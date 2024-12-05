from .options_fund import frequency_options, ghg_reduction_strategies, sfdr_classification, yes_no_asset_scope, yes_no_best_efforts, yes_no_incident_process, yes_no_not_assessed

SCHEMA_FUND = {

    #0.1.1
    #String
    "fund_name": {
        "type": "string",
    },
    
    #0.2.1
    #STRING from yes_no_best_efforts
    "legal_esg_commitment": {
        "type": "string",
        "allowed": yes_no_best_efforts,
    },
    
    #0.2.2
    #STRING from yes_no_asset_scope
    "esg_investment_policy": {
        "type": "string",
        "allowed": yes_no_asset_scope,
    },
    
    #0.2.3
    #STRING from yes_no_asset_scope
    "climate_change_investment_policy": {
        "type": "string",
        "allowed": yes_no_asset_scope,
    },
    
    #0.2.4
    #STRING from yes_no_best_efforts
    "diversity_in_term_sheets_shareholder_agreements": {
        "type": "string",
        "allowed": yes_no_best_efforts,
    },
    
    #0.3.1
    #STRING from yes_no_asset_scope
    "esg_engagement_process": {
        "type": "string",
        "allowed": yes_no_asset_scope,
    },
    
    #0.3.2
    #STRING from yes_no_asset_scope
    "esg_monitoring_processes": {
        "type": "string",
        "allowed": yes_no_asset_scope,
    },
    
    #0.3.3
    #STRING from yes_no_incident_process
    "esg_incident_report_process": {
        "type": "string",
        "allowed": yes_no_incident_process,
    },
    
    #0.3.4
    #STRING from yes_no
    "good_governance_due_diligence": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.3.5
    #STRING from yes_no
    "good_governance_post_investment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #0.3.5.1
    #STRING from yes_no_incident_process
    "good_governance_post_investment_frequency": {
        "type": "string",
        "allowed": frequency_options,
    },
    
    #1.1.1
    #STRING from yes_no_incident_process
    "fund_marketing_under_sfdr": {
        "type": "string",
        "allowed": sfdr_classification,
    },
    
    #1.2.1
    #STRING from yes_no
    "article_8_sustainable_investment_commitment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.2.1.1
    #Float between 0 and 100
    "article_8_sustainable_investment_commitment_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.2.2
    #STRING from yes_no
    "article_8_eu_taxonomy_alignment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.2.2.1
    #Float between 0 and 100
    "article_8_eu_taxonomy_alignment_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.2.3
    #STRING from yes_no
    "article_8_non_eu_taxonomy_environmental_objective": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.2.3.1
    #Float between 0 and 100
    "article_8_non_eu_taxonomy_environmental_objective_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.2.4
    #STRING from yes_no
    "article_8_social_objective_investment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.2.4.1
    #Float between 0 and 100
    "article_8_social_objective_investment_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.2.5
    #STRING from yes_no
    "article_8_considers_significant_negative_impacts": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.2.6
    #STRING from yes_no
    "article_8_ghg_reduction_target": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.2.6.1
    #STRING from ghg_reduction_strategies
    "article_8_ghg_reduction_target_main_strategy": {
        "type": "string",
        "allowed": ghg_reduction_strategies,
    },
    
    #1.2.6.2
    #Float between 0 and 100
    "article_8_ghg_reduction_target_ambition": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.2.6.3
    #Float (positive)
    "article_8_ghg_reduction_target_financed_emissions_baseline":  {"type": "float", 'min': 0},
    
    #1.2.6.4
    #Float between 1900 and 2030
    "article_8_ghg_reduction_target_base_year": {
        "type": "integer",
        "min": 1900,
        "max": 2030,
    },
    
    #1.2.6.5
    #Float between 2000 and 2200
    "article_8_ghg_reduction_target_target_year": {
        "type": "integer",
        "min": 2000,
        "max": 2200,
    },
    
    #1.2.6.6
    #Float (positive)
    "article_8_ghg_reduction_target_financed_emissions_reporting":  {"type": "float", 'min': 0},
    
    #1.2.7
    #STRING from yes_no
    "article_8_uses_index_as_reference_benchmark": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.3.1
    #STRING from yes_no
    "article_9_sustainable_investment_commitment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.3.1.1
    #Float between 0 and 100
    "article_9_sustainable_investment_commitment_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.3.2
    #STRING from yes_no
    "article_9_eu_taxonomy_alignment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.3.2.1
    #Float between 0 and 100
    "article_9_eu_taxonomy_alignment_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.3.3
    #STRING from yes_no
    "article_9_non_eu_taxonomy_environmental_objective": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.3.3.1
    #Float between 0 and 100
    "article_9_non_eu_taxonomy_environmental_objective_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.3.4
    #STRING from yes_no
    "article_9_social_objective_investment": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.3.4.1
    #Float between 0 and 100
    "article_9_social_objective_investment_minimum_share_percentage": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.3.5
    #STRING from yes_no
    "article_9_considers_significant_negative_impacts": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.3.6
    #STRING from yes_no
    "article_9_ghg_reduction_target": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #1.3.6.1
    #STRING from ghg_reduction_strategies
    "article_9_ghg_reduction_target_main_strategy": {
        "type": "string",
        "allowed": ghg_reduction_strategies,
    },
    
    #1.3.6.2
    #Float between 0 and 100
    "article_9_ghg_reduction_target_ambition": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #1.3.6.3
    #Float (positive)
    "article_9_ghg_reduction_target_financed_emissions_baseline":  {"type": "float", 'min': 0},
    
    #1.3.6.4
    #Float between 1900 and 2030
    "article_9_ghg_reduction_target_base_year": {
        "type": "integer",
        "min": 1900,
        "max": 2030,
    },
    
    #1.3.6.5
    #Float between 2000 and 2200
    "article_9_ghg_reduction_target_target_year": {
        "type": "integer",
        "min": 2000,
        "max": 2200,
    },
    
    #1.3.6.6
    #Float (positive)
    "article_9_ghg_reduction_target_financed_emissions_reporting":  {"type": "float", 'min': 0},
    
    #1.3.6.7
    #STRING from ghg_reduction_strategies
    "article_9_ghg_reduction_target_1_5_c_aligned": {
        "type": "string",
        "allowed": yes_no_not_assessed,
    },
    
    #1.3.7
    #STRING from yes_no
    "article_9_uses_index_as_reference_benchmark": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #2.1.1
    #Integer (positive)
    "total_number_of_partners": {"type": "integer", 'min': 0},
    
    #2.1.2
    #Integer (positive)
    "number_of_partners_female": {"type": "integer", 'min': 0},
    
    #2.1.3
    #Integer (positive)
    "number_of_partners_non_binary": {"type": "integer", 'min': 0},
    
    #2.1.4
    #Integer (positive)
    "number_of_partners_non_disclosed": {"type": "integer", 'min': 0},
    
    #2.1.5
    #Integer (positive)
    "number_of_partners_male": {"type": "integer", 'min': 0},
    
    #2.1.6
    #STRING from yes_no
    "gender_diversity_pipeline_tracked": {
        "type": "string",
        "allowed": ["yes", "no"],
    },
    
    #2.1.6.1
    #Float between 0 and 100
    "gender_diversity_pipeline_strategy_fit": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #2.1.6.2
    #Float between 0 and 100
    "gender_diversity_pipeline_dd_undertaken": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
    #2.1.6.3
    #Float between 0 and 100
    "gender_diversity_pipeline_term_sheet_issued": {
        "type": "float",
        "min": 0.0,
        "max": 100.0,
    },
    
}
