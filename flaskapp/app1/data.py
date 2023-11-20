from util import preprocess


def init_data():
    # Load data
    data1 = preprocess('data/revenue_vehicle_condition.csv')
    data2 = preprocess('data/revenue_vehicle_replacement_cost.csv')
    data3 = preprocess('data/service.csv')

    dataRidershipByYear = preprocess('data/Table 13_ridership.csv')
    dataVrmByYear = preprocess('data/Table 13_vrm.csv')
    dataVrhByYear = preprocess('data/Table 13_vrh.csv')

    dataRidershipByRank = preprocess('data/Table 17_ridership_percentile_rank.csv')
    dataVrmByRank = preprocess('data/Table 18_vrm_percentile_rank.csv')
    dataVrhByRank = preprocess('data/Table 19_vrh_percentile_rank.csv')

    dataCapitalFunding = preprocess('data/Table 20_funding_source_capital_yearly.csv')
    dataOperatingFunding = preprocess('data/Table 20_funding_source_operating_yearly.csv')

    dataVehiclesByMode = preprocess('data/Table 21_vehicles_by_mode.csv')
    dataFleetByMode = preprocess('data/Table 23_fleet_size_by_mode.csv')
    dataAdaAccessible = preprocess('data/Table 24_ada_percentage.csv')
    dataVehicleAge = preprocess('data/Table 25_average_vehicle_age.csv')
    dataVehicleLength = preprocess('data/Table 26_average_vehicle_length.csv')
    dataSeatingCapacity = preprocess('data/Table 27_average_seating_capacity.csv')
    dataVehicleOwnerShip = preprocess('data/Table 28_vehicle_ownership.csv')
    dataFundingSource = preprocess('data/Table 29_funding_source.csv')

    dataTripsPerMile = preprocess('data/Table 30A_trips_per_vrm.csv')
    dataTripsPerHour = preprocess('data/Table 30B_trips_per_vrh.csv')
    dataTripsMilesHoursPerVehicle = preprocess('data/Table 31_trips_miles_hours_per_vehicle.csv')
    dataOperatingExpensePerTrip = preprocess('data/Table 32A_operating_expense_per_trip.csv')
    dataOperatingExpensePerVehicleMile = preprocess('data/Table 32B_operating_expense_per_VRM.csv')
    dataOperatingExpensePerVehicleHour = preprocess('data/Table 32C_operating_expense_per_VRH.csv')
    dataFareboxRecoveryRatio = preprocess('data/Table 32D_farebox_recovery_ratio.csv')
    dataPercentileTotal = preprocess('data/Table 33A_PMP_total.csv')
    dataPercentileFixedRoute = preprocess('data/Table 33B_PMP_fixed_route.csv')
    dataPercentileDemandResponse = preprocess('data/Table 33C_PMP_demand_response.csv')

    dataStatforAgenciesRankedByVRM = preprocess('data/Table 34_statistics_for_agencies_ranked_by_vrm.csv')
    dataStatforAgenciesRankedByVRH = preprocess('data/Table 35_statistics_for_agencies_ranked_by_vrh.csv')
    dataStatforAgenciesRankedByRidership = preprocess('data/Table 36_statistics_for_agencies_ranked_by_ridership.csv')

    datastatForFixedRouteRankedByVRM = preprocess('data/Table 37_statistics_for_FRS_ranked_by_VRM.csv')
    datastatForFixedRouteRankedByVRH = preprocess('data/Table 38_statistics_for_FRS_ranked_by_VRH.csv')
    datastatForFixedRouteRankedByRidership = preprocess('data/Table 39_statistics_for_FRS_ranked_by_ridership.csv')

    datastatForDemandResponseRankedByVRM = preprocess('data/Table 40_statistics_for_DRS_ranked_by_VRM.csv')
    datastatForDemandResponseRankedByVRH = preprocess('data/Table 41_statistics_for_DRS_ranked_by_VRH.csv')
    datastatForDemandResponseRankedByRidership = preprocess('data/Table 42_statistics_for_DRS_ranked_by_ridership.csv')

    dataAgenciesByRegion = preprocess('data/Table 43_transit_agencies_by_region.csv')
    dataRidershipByRegion = preprocess('data/Table 44A_operating_statistics_by_region_ridership.csv')
    dataVrmByRegion = preprocess('data/Table 44B_operating_statistics_by_region_VRM.csv')
    dataVrhByRegion = preprocess('data/Table 44C_operating_statistics_by_region_VRH.csv')
    dataVehiclesByRegion = preprocess('data/Table 45_fleet_statistics_by_region.csv')

    dataPerformanceByRegion = preprocess('data/Table 46A_key_performance_measures_by_region.csv')
    dataTripsPerVRMByRegion = preprocess('data/Table 46_trips_per_VRM.csv')
    dataTripsPerVRHByRegion = preprocess('data/Table 46_trips_per_VRH.csv')
    dataOperatingPerTripByRegion = preprocess('data/Table 46_operating_expense_per_trip.csv')
    dataOperatingPerVRMByRegion = preprocess('data/Table 46_operating_expense_per_VRM.csv')
    dataOperatingPerVRHByRegion = preprocess('data/Table 46_operating_expense_per_VRH.csv')
    dataAgencyPerformanceByRegion = preprocess('data/Table 47_median_agency_values.csv')

    dataRidershipByState = preprocess('data/Table 48_state_statistics_by_ridership.csv')
    dataVrmByState = preprocess('data/Table 48_state_statistics_by_VRM.csv')
    dataVrhByState = preprocess('data/Table 48_state_statistics_by_VRH.csv')

    dataRidershipTotalYearlyByState = preprocess('data/Table 49_ridership_by_state_yearly_total.csv')
    dataRidershipFRYearlyByState = preprocess('data/Table 49_ridership_by_state_yearly_fixed_route.csv')
    dataRidershipDRYearlyByState = preprocess('data/Table 49_ridership_by_state_yearly_demand_response.csv')
    dataRidershipOtherYearlyByState = preprocess('data/Table 49_ridership_by_state_yearly_other.csv')

    dataVrmTotalYearlyByState = preprocess('data/Table 50_VRM_by_state_yearly_total.csv')
    dataVrmFrsYearlyByState = preprocess('data/Table 50_VRM_by_state_yearly_fixed_route.csv')
    dataVrmDrsYearlyByState = preprocess('data/Table 50_VRM_by_state_yearly_demand_response.csv')
    dataVrmOtherYearlyByState = preprocess('data/Table 50_VRM_by_state_yearly_other.csv')

    dataFinancialOnOperationsByState = preprocess('data/Table 51_state_financial_statistics_fund_expended_on_operations.csv')
    dataFinancialOnCapitalByState = preprocess('data/Table 51_state_financial_statistics_fund_expended_on_capital.csv')

    dataFleetStatisticsByState = preprocess('data/Table 52_state_fleet_statistics.csv')

    dataPerformanceMeasuresByState = preprocess('data/Table 53_state_performance_measures_averages.csv')

    dataPerformanceMeasuresMedianByState = preprocess('data/Table 54_state_performance_measures_median.csv')

    dataAgencyPercentileRidershipByState = preprocess('data/Table 55_transit_agency_percentile_by_ridership.csv')
    dataAgencyPercentileVrmByState = preprocess('data/Table 55_transit_agency_percentile_by_VRM.csv')
    dataAgencyPercentileVrhByState = preprocess('data/Table 55_transit_agency_percentile_by_VRH.csv')

    dataRidershipYearlyByTribal = preprocess('data/Table 57_tribal_transit_ridership_yearly_in_thousand.csv')
    dataVrmYearlyByTribal = preprocess('data/Table 57_tribal_transit_VRM_yearly_in_thousand.csv')
    dataVrhYearlyByTribal = preprocess('data/Table 57_tribal_transit_VRH_yearly_in_thousand.csv')

    dataVehiclesByTribal = preprocess('data/Table 58_tribal_transit_vehicle_information.csv')
    dataFleetStatisticsByTribal = preprocess('data/Table 58_tribal_transit_fleet_statistics.csv')
    dataTripsPerVehicleByTribal = preprocess('data/Table 58_tribal_transit_trips_per_vehicle.csv')
    dataVRMPerVehicleByTribal = preprocess('data/Table 58_tribal_transit_VRM_per_vehicle.csv')
    dataVRHPerVehicleByTribal = preprocess('data/Table 58_tribal_transit_VRH_per_vehicle.csv')

    dataTripsPerVrmByTribal = preprocess('data/Table 59_tribal_transit_trips_per_VRM.csv')
    dataTripsPerVrhByTribal = preprocess('data/Table 59_tribal_transit_trips_per_VRH.csv')
    dataOperatingExpensePerTripByTribal = preprocess('data/Table 59_tribal_transit_operating_expense_per_trip.csv')
    dataOperatingExpensePerVrmByTribal = preprocess('data/Table 59_tribal_transit_operating_expense_per_VRM.csv')
    dataOperatingExpensePerVrhByTribal = preprocess('data/Table 59_tribal_transit_operating_expense_per_VRH.csv')
    dataFareboxRecoveryRatioByTribal = preprocess('data/Table 59_tribal_transit_farebox_recovery_ratio.csv')

    dataPerformanceMeasureMedianByTribal = preprocess('data/Table 60_tribal_transit_median_agency_values.csv')

    return data1, data2, data3, dataRidershipByYear, dataVrmByYear, dataVrhByYear,\
		   dataRidershipByRank, dataVrmByRank,dataVrhByRank, \
           dataCapitalFunding, dataOperatingFunding,\
           dataVehiclesByMode, dataFleetByMode, dataAdaAccessible, dataVehicleAge, dataVehicleLength, dataSeatingCapacity, \
		   dataVehicleOwnerShip, dataFundingSource, dataTripsPerMile, dataTripsPerHour, dataTripsMilesHoursPerVehicle, \
           dataOperatingExpensePerTrip, dataOperatingExpensePerVehicleMile, dataOperatingExpensePerVehicleHour, dataFareboxRecoveryRatio, \
           dataPercentileTotal, dataPercentileFixedRoute, dataPercentileDemandResponse, \
           dataAgenciesByRegion, dataRidershipByRegion, dataVrmByRegion, dataVrhByRegion, dataVehiclesByRegion, \
           dataPerformanceByRegion, dataTripsPerVRMByRegion,  dataTripsPerVRHByRegion, dataOperatingPerTripByRegion, dataOperatingPerVRMByRegion, \
           dataOperatingPerVRHByRegion, dataAgencyPerformanceByRegion, \
           dataRidershipByState, dataVrmByState, dataVrhByState, \
           dataRidershipTotalYearlyByState, dataRidershipFRYearlyByState, dataRidershipDRYearlyByState, dataRidershipOtherYearlyByState, \
           dataVrmTotalYearlyByState, dataVrmFrsYearlyByState, dataVrmDrsYearlyByState, dataVrmOtherYearlyByState, \
           dataFinancialOnOperationsByState, dataFinancialOnCapitalByState, \
           dataFleetStatisticsByState, \
           dataPerformanceMeasuresByState, \
           dataPerformanceMeasuresMedianByState, \
           dataAgencyPercentileRidershipByState, dataAgencyPercentileVrmByState, dataAgencyPercentileVrhByState, \
           dataRidershipYearlyByTribal, dataVrmYearlyByTribal, dataVrhYearlyByTribal, \
           dataVehiclesByTribal, dataFleetStatisticsByTribal, dataTripsPerVehicleByTribal, dataVRMPerVehicleByTribal, dataVRHPerVehicleByTribal, \
           dataTripsPerVrmByTribal, dataTripsPerVrhByTribal, dataOperatingExpensePerTripByTribal, \
           dataOperatingExpensePerVrmByTribal, dataOperatingExpensePerVrhByTribal, dataFareboxRecoveryRatioByTribal, \
           dataPerformanceMeasureMedianByTribal,\
           dataStatforAgenciesRankedByVRM, datastatForDemandResponseRankedByVRM, datastatForFixedRouteRankedByVRM,\
           dataStatforAgenciesRankedByVRH, datastatForDemandResponseRankedByVRH, datastatForFixedRouteRankedByVRH,\
           dataStatforAgenciesRankedByRidership, datastatForDemandResponseRankedByRidership, datastatForFixedRouteRankedByRidership
