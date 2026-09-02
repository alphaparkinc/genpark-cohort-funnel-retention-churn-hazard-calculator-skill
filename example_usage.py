from client import CohortFunnelRetentionChurnHazardCalculatorClient

def main():
    client = CohortFunnelRetentionChurnHazardCalculatorClient()
    res = client.compute_cohort_survival_hazard('2026-06', 22000, 16)
    print('Cohort Retention Calculator: ' + res['cohort_analysis_id'] + ' (' + res['cohort_month'] + ')')
    print('D30: ' + str(res['day_30_retention_rate_pct']) + '% | D90: ' + str(res['day_90_retention_rate_pct']) + '% | Median Lifespan: ' + str(res['kaplan_meier_median_lifespan_days']) + ' days')
    print('Peak Churn Inflection: Week ' + str(res['churn_hazard_peak_inflection_week']))
    print('Heatmap URL: ' + res['retention_matrix_heatmap_url'])

if __name__ == '__main__':
    main()
