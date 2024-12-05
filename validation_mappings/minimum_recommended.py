# List of metrics which make up the IE minimum criteria
MINIMUM_METRICS = [
    "company_name",
    "business_identification_number",
    "business_identification_number_system",
    "country_of_domicile",
    "primary_country_of_operations",
    "main_industry_classification",
    "total_ftes_end_of_report_year",
    "total_ftes_end_of_previous_report_year",
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
    "occurrence_of_esg_incidents",
    "number_of_esg_incidents",
    "total_founders_still_employed",
    "number_of_founders_still_employed_female",
    "number_of_founders_still_employed_non_binary",
    "number_of_founders_still_employed_non_disclosed",
    "number_of_founders_still_employed_male",
]

# List of metrics which make up the IE recommended criteria
RECOMMENDED_METRICS = [
    "company_name",
    "business_identification_number",
    "business_identification_number_system",
    "country_of_domicile",
    "primary_country_of_operations",
    "main_industry_classification",
    "total_ftes_end_of_report_year",
    "total_ftes_end_of_previous_report_year",
    "gross_revenue",
    "gross_revenue_inside_eu",
    "gross_revenue_outside_eu",
    "currency",
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
    "occurrence_of_esg_incidents",
    "number_of_esg_incidents",
    "ghg_scope_measured_calculated",
    "total_ghg_emissions",
    "total_scope_1_emissions",
    "total_scope_1_emissions_methodology",
    "total_scope_2_emissions",
    "total_scope_2_emissions_methodology",
    "total_scope_3_emissions",
    "total_scope_3_emissions_methodology",
    "decarbonisation_strategy_set",
    "ghg_reduction_target_set",
    "long_term_net_zero_goal_set",
    "total_energy_consumption",
    "energy_consumption_renewable",
    "circular_economy_principles",
    "number_of_ftes_end_of_report_year_female",
    "number_of_ftes_end_of_report_year_non_binary",
    "number_of_ftes_end_of_report_year_non_disclosed",
    "number_of_ftes_end_of_report_year_male",
    "total_csuite_employees",
    "number_of_csuite_female",
    "number_of_csuite_non_binary",
    "number_of_csuite_non_disclosed",
    "number_of_csuite_male",
    "total_founders_still_employed",
    "number_of_founders_still_employed_female",
    "number_of_founders_still_employed_non_binary",
    "number_of_founders_still_employed_non_disclosed",
    "number_of_founders_still_employed_male",
    "number_of_new_hires_inside_eu_fte",
    "number_of_new_hires_outside_eu_fte",
    "number_of_leavers_inside_eu_fte",
    "number_of_leavers_outside_eu_fte",
    "number_of_new_hires_ma_fte",
    "number_of_leavers_ma_fte",
    "number_of_organic_net_new_hires_fte",
    "number_of_total_net_new_hires_fte",
    "turnover_fte",
    "implements_employee_survey_questionnaires",
    "implemented_whistleblower_procedure",
    "number_of_workrelated_injuries",
    "number_of_workrelated_fatalities",
    "days_lost_due_to_injury",
    "total_number_of_board_members",
    "number_of_board_members_female",
    "number_of_board_members_non_binary",
    "number_of_board_members_non_disclosed",
    "number_of_board_members_male",
    "total_scope_2_emissions_location_based",
    "total_scope_2_emissions_market_based",
    "total_ghg_emissions_location_based",
    "total_ghg_emissions_market_based",
    "active_in_fossil_sector",
    "non_renewable_energy_consumption",
    "total_energy_production",
    "non_renewable_energy_production",
    "renewable_energy_production",
    "high_impact_climate_section_a_agriculture_forestry_fishing",
    "high_impact_climate_section_a_agriculture_forestry_fishing_energy_consumption_gwh",
    "high_impact_climate_section_a_agriculture_forestry_fishing_gross_revenue",
    "high_impact_climate_section_b_mining_quarrying",
    "high_impact_climate_section_b_mining_quarrying_energy_consumption_gwh",
    "high_impact_climate_section_b_mining_quarrying_gross_revenue",
    "high_impact_climate_section_c_manufacturing",
    "high_impact_climate_section_c_manufacturing_energy_consumption_gwh",
    "high_impact_climate_section_c_manufacturing_gross_revenue",
    "high_impact_climate_section_d_electricity_gas_steam_air_conditioning_supply",
    "high_impact_climate_section_d_electricity_gas_steam_air_conditioning_supply_energy_consumption_gwh",
    "high_impact_climate_section_d_electricity_gas_steam_air_conditioning_supply_gross_revenue",
    "high_impact_climate_section_e_water_supply_sewerage_waste_management_remediation_activities",
    "high_impact_climate_section_e_water_supply_sewerage_waste_management_remediation_activities_energy_consumption_gwh",
    "high_impact_climate_section_e_water_supply_sewerage_waste_management_remediation_activities_gross_revenue",
    "high_impact_climate_section_f_construction",
    "high_impact_climate_section_f_construction_energy_consumption_gwh",
    "high_impact_climate_section_f_construction_gross_revenue",
    "high_impact_climate_section_g_wholesale_retail_trade_repair_motor_vehicles_motorcycles",
    "high_impact_climate_section_g_wholesale_retail_trade_repair_motor_vehicles_motorcycles_energy_consumption_gwh",
    "high_impact_climate_section_g_wholesale_retail_trade_repair_motor_vehicles_motorcycles_gross_revenue",
    "high_impact_climate_section_h_transportation_storage",
    "high_impact_climate_section_h_transportation_storage_energy_consumption_gwh",
    "high_impact_climate_section_h_transportation_storage_gross_revenue",
    "high_impact_climate_section_l_real_estate_activities",
    "high_impact_climate_section_l_real_estate_activities_energy_consumption_gwh",
    "high_impact_climate_section_l_real_estate_activities_gross_revenue",
    "violating_ungp_oecd",
    "has_processes_monitor_ungp_oecd",
    "involved_in_controversial_weapons",
]
