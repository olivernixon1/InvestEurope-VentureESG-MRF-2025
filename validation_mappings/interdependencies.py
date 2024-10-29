# Interdependencies
board_governance_members_keys = [
    "board_governance_members:gender:male",
    "board_governance_members:gender:non_binary",
    "board_governance_members:gender:female",
    "board_governance_members:gender:non_disclosed",
]

energy_consumption_renewable_nonrenewable_keys = [
    "energy_consumption_renewable",
    "total_energy_consumption",
]


energy_production_renewable_nonrenewable_keys = [
    "energy_production_non_renewable",
    "energy_production_renewable",
]

number_csuite_employees_fte_gender_keys = [
    "number_csuite_employees_fte_gender:gender:non_binary",
    "number_csuite_employees_fte_gender:gender:male",
    "number_csuite_employees_fte_gender:gender:female",
    "number_csuite_employees_fte_gender:gender:non_disclosed",
]

number_founders_still_employed_by_gender_keys = [
    "number_founders_still_employed_by_gender:gender:non_binary",
    "number_founders_still_employed_by_gender:gender:male",
    "number_founders_still_employed_by_gender:gender:female",
    "number_founders_still_employed_by_gender:gender:non_disclosed",
]

number_ftes_end_of_period_gender_keys = [
    "number_ftes_end_of_period_gender:gender:male",
    "number_ftes_end_of_period_gender:gender:non_binary",
    "number_ftes_end_of_period_gender:gender:female",
     "number_ftes_end_of_period_gender:gender:non_disclosed",
]

organizational_policies_in_place_esg_related_policies_keys = [
    "overall_sustainability_policy",
    "environmental_policy",
    "anti_discrimination_and_equal_opportunities_policy",
    "health_and_safety_policy",
    "human_rights_policy",
    "anti_corruption_bribery_policy",
    "data_privacy_security_policy",
    "diversity_inclusion_policy",
    "code_of_conduct",
    "written_salary_remuneration_policy",
    "supply_chain_policy",
    "cybersecurity_data_management_policyt"
]

# Master Array of Interdependencies
INTERDEPENDENCIES = [
    board_governance_members_keys,
    energy_consumption_renewable_nonrenewable_keys,
    energy_production_renewable_nonrenewable_keys,
    number_csuite_employees_fte_gender_keys,
    number_founders_still_employed_by_gender_keys,
    number_ftes_end_of_period_gender_keys,
    organizational_policies_in_place_esg_related_policies_keys,
]
