from util import preprocess


def init_data():
    # Load data
    data1 = preprocess('data/revenue_vehicle_condition.csv')
    data2 = preprocess('data/revenue_vehicle_replacement_cost.csv')
    data3 = preprocess('data/service.csv')

    dataRidershipByYear = preprocess('data/Table 13_ridership.csv')
    dataVrmByYear = preprocess('data/Table 13_vrm.csv')
    dataVrhByYear = preprocess('data/Table 13_vrh.csv')

    dataRidershipByRank = preprocess('data/Table 17.csv')
    dataVrmByRank = preprocess('data/Table 18.csv')
    dataVrhByRank = preprocess('data/Table 19.csv')

    dataCapitalFunding = preprocess('data/Table 20Capital.csv')
    dataOperatingFunding = preprocess('data/Table 20Operating.csv')

    dataVehiclesByMode = preprocess('data/Table 21.csv')
    dataFleetByMode = preprocess('data/Table 23.csv')
    dataAdaAccessible = preprocess('data/Table 24.csv')
    dataVehicleAge = preprocess('data/Table 25.csv')
    dataVehicleLength = preprocess('data/Table 26.csv')
    dataSeatingCapacity = preprocess('data/Table 27.csv')
    dataVehicleOwnerShip = preprocess('data/Table 28.csv')
    dataFundingSource = preprocess('data/Table 29.csv')

    dataTripsPerMile = preprocess('data/Table 30A.csv')
    dataTripsPerHour = preprocess('data/Table 30B.csv')
    dataTripsMilesHoursPerVehicle = preprocess('data/Table 31.csv')
    dataOperatingExpensePerTrip = preprocess('data/Table 32A.csv')
    dataOperatingExpensePerVehicleMile = preprocess('data/Table 32B.csv')
    dataOperatingExpensePerVehicleHour = preprocess('data/Table 32C.csv')
    dataFareboxRecoveryRatio = preprocess('data/Table 32D.csv')
    dataPercentileTotal = preprocess('data/Table 33A.csv')
    dataPercentileFixedRoute = preprocess('data/Table 33B.csv')
    dataPercentileDemandResponse = preprocess('data/Table 33C.csv')

    dataAgenciesByRegion = preprocess('data/Table 43.csv')
    dataRidershipByRegion = preprocess('data/Table 44A.csv')
    dataVrmByRegion = preprocess('data/Table 44B.csv')
    dataVrhByRegion = preprocess('data/Table 44C.csv')
    dataVehiclesByRegion = preprocess('data/Table 45.csv')

    dataPerformanceByRegion = preprocess('data/Table 46A.csv')
    dataTripsPerVRMByRegion = preprocess('data/Table 46TripsPerVRM.csv')
    dataTripsPerVRHByRegion = preprocess('data/Table 46TripsPerVRH.csv')
    dataOperatingPerTripByRegion = preprocess('data/Table 46OEPerTrip.csv')
    dataOperatingPerVRMByRegion = preprocess('data/Table 46OEPerVRM.csv')
    dataOperatingPerVRHByRegion = preprocess('data/Table 46OEPerVRH.csv')
    dataAgencyPerformanceByRegion = preprocess('data/Table 47.csv')

    dataRidershipByState = preprocess('data/Table 48Ridership.csv')
    dataVrmByState = preprocess('data/Table 48VRM.csv')
    dataVrhByState = preprocess('data/Table 48VRH.csv')

    dataRidershipTotalYearlyByState = preprocess('data/Table 49Total.csv')
    dataRidershipFRYearlyByState = preprocess('data/Table 49FRS.csv')
    dataRidershipDRYearlyByState = preprocess('data/Table 49DRS.csv')
    dataRidershipOtherYearlyByState = preprocess('data/Table 49Other.csv')

    dataVrmTotalYearlyByState = preprocess('data/Table 50VRM_Total.csv')
    dataVrmFrsYearlyByState = preprocess('data/Table 50VRM_FRS.csv')
    dataVrmDrsYearlyByState = preprocess('data/Table 50VRM_DRS.csv')
    dataVrmOtherYearlyByState = preprocess('data/Table 50VRM_Other.csv')

    dataFinancialOnOperationsByState = preprocess('data/Table 51FS_Operations.csv')
    dataFinancialOnCapitalByState = preprocess('data/Table 51FS_Capital.csv')

    dataFleetStatisticsByState = preprocess('data/Table 52.csv')

    dataPerformanceMeasuresByState = preprocess('data/Table 53.csv')

    dataPerformanceMeasuresMedianByState = preprocess('data/Table 54.csv')

    dataAgencyPercentileRidershipByState = preprocess('data/Table 55Ridership.csv')
    dataAgencyPercentileVrmByState = preprocess('data/Table 55VRM.csv')
    dataAgencyPercentileVrhByState = preprocess('data/Table 55VRH.csv')

    dataRidershipYearlyByTribal = preprocess('data/Table 57Ridership.csv')
    dataVrmYearlyByTribal = preprocess('data/Table 57VRM.csv')
    dataVrhYearlyByTribal = preprocess('data/Table 57VRH.csv')

    dataVehiclesByTribal = preprocess('data/Table 58Vehicles.csv')
    dataFleetStatisticsByTribal = preprocess('data/Table 58Fleet.csv')
    dataTripsPerVehicleByTribal = preprocess('data/Table 58Trips.csv')
    dataVRMPerVehicleByTribal = preprocess('data/Table 58VRM.csv')
    dataVRHPerVehicleByTribal = preprocess('data/Table 58VRH.csv')

    dataTripsPerVrmByTribal = preprocess('data/Table 59Trips_VRM.csv')
    dataTripsPerVrhByTribal = preprocess('data/Table 59Trips_VRH.csv')
    dataOperatingExpensePerTripByTribal = preprocess('data/Table 59OE_Trip.csv')
    dataOperatingExpensePerVrmByTribal = preprocess('data/Table 59OE_VRM.csv')
    dataOperatingExpensePerVrhByTribal = preprocess('data/Table 59OE_VRH.csv')
    dataFareboxRecoveryRatioByTribal = preprocess('data/Table 59Farebox.csv')

    dataPerformanceMeasureMedianByTribal = preprocess('data/Table 60.csv')

    dataStatforAgenciesRankedByVRM = preprocess('data/Table 34.csv')
    datastatForDemandResponseRankedByVRM = preprocess('data/Table 40.csv')
    datastatForFixedRouteRankedByVRM = preprocess('data/Table 37.csv')

    dataStatforAgenciesRankedByVRH = preprocess('data/Table 35.csv')
    datastatForDemandResponseRankedByVRH = preprocess('data/Table 41.csv')
    datastatForFixedRouteRankedByVRH = preprocess('data/Table 38.csv')

    dataStatforAgenciesRankedByRidership = preprocess('data/Table 36.csv')
    datastatForDemandResponseRankedByRidership = preprocess('data/Table 42.csv')
    datastatForFixedRouteRankedByRidership = preprocess('data/Table 39.csv')

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
