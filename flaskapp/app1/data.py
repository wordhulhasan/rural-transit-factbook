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

    dataVehiclesByMode = preprocess('data/Table 21.csv')
    dataFleetByMode = preprocess('data/Table 23.csv')
    dataAdaAccessible = preprocess('data/Table 24.csv')
    dataVehicleAge = preprocess('data/Table 25.csv')
    dataVehicleLength = preprocess('data/Table 26.csv')
    dataSeatingCapacity = preprocess('data/Table 27.csv')
    dataVehicleOwnerShip = preprocess('data/Table 28.csv')
    dataFundingSource = preprocess('data/Table 29.csv')

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
		   dataRidershipByRank, dataVrmByRank,dataVrhByRank,\
           dataVehiclesByMode, dataFleetByMode, dataAdaAccessible, dataVehicleAge, dataVehicleLength, dataSeatingCapacity, \
		   dataVehicleOwnerShip, dataFundingSource, \
           dataStatforAgenciesRankedByVRM, datastatForDemandResponseRankedByVRM, datastatForFixedRouteRankedByVRM,\
           dataStatforAgenciesRankedByVRH, datastatForDemandResponseRankedByVRH, datastatForFixedRouteRankedByVRH,\
           dataStatforAgenciesRankedByRidership, datastatForDemandResponseRankedByRidership, datastatForFixedRouteRankedByRidership
