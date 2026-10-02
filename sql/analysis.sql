-- 1. Spending comparison by claim type

SELECT
    claim_type,
    ROUND(AVG(avg_spndg_per_ep_hospital), 2) AS avg_hospital_spending,
    ROUND(AVG(avg_spndg_per_ep_national), 2) AS avg_national_spending,
    ROUND(
        AVG(avg_spndg_per_ep_hospital)
        - AVG(avg_spndg_per_ep_national),
        2
    ) AS average_spending_difference
FROM hospital_spending
GROUP BY claim_type
ORDER BY average_spending_difference DESC;


-- 2. Average hospital spending by state

SELECT
    state,
    COUNT(*) AS number_of_records,
    ROUND(AVG(avg_spndg_per_ep_hospital), 2) AS avg_hospital_spending
FROM hospital_spending
GROUP BY state
ORDER BY avg_hospital_spending DESC;


-- 3. Hospitals with the largest hospital-vs-national spending difference

SELECT
    facility_name,
    state,
    claim_type,
    avg_spndg_per_ep_hospital,
    avg_spndg_per_ep_national,
    hospital_vs_national_spending_diff
FROM hospital_spending
ORDER BY hospital_vs_national_spending_diff DESC
LIMIT 10;

-- 4. Compare hospital, state, and national spending

SELECT
    claim_type,
    ROUND(AVG(avg_spndg_per_ep_hospital), 2) AS avg_hospital_spending,
    ROUND(AVG(avg_spndg_per_ep_state), 2) AS avg_state_spending,
    ROUND(AVG(avg_spndg_per_ep_national), 2) AS avg_national_spending
FROM hospital_spending
GROUP BY claim_type
ORDER BY claim_type;

-- 5. Summary statistics for hospital vs national spending difference

SELECT
    COUNT(*) AS total_records,
    ROUND(AVG(hospital_vs_national_spending_diff), 2) AS average_difference,
    MIN(hospital_vs_national_spending_diff) AS minimum_difference,
    MAX(hospital_vs_national_spending_diff) AS maximum_difference
FROM hospital_spending;

-- 6. Records where hospital spending exceeds national spending

SELECT
    facility_name,
    state,
    claim_type,
    avg_spndg_per_ep_hospital,
    avg_spndg_per_ep_national,
    hospital_vs_national_spending_diff
FROM hospital_spending
WHERE hospital_vs_national_spending_diff > 0
ORDER BY hospital_vs_national_spending_diff DESC
LIMIT 20;

