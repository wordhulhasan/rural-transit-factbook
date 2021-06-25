from util import preprocess


def init_data():
    # Load data
    data1 = preprocess('data/revenue_vehicle_condition.csv')
    data2 = preprocess('data/revenue_vehicle_replacement_cost.csv')
    data3 = preprocess('data/service.csv')
	
    dataVehiclesByMode = preprocess('data/Table 21.csv')

    dataStatforAgenciesRankedByVRM = preprocess('data/Table 34.csv')
    datastatForDemandResponseRankedByVRM = preprocess('data/Table 40.csv')
    datastatForFixedRouteRankedByVRM = preprocess('data/Table 37.csv')

    dataStatforAgenciesRankedByVRH = preprocess('data/Table 35.csv')
    datastatForDemandResponseRankedByVRH = preprocess('data/Table 41.csv')
    datastatForFixedRouteRankedByVRH = preprocess('data/Table 38.csv')

    dataStatforAgenciesRankedByRidership = preprocess('data/Table 36.csv')
    datastatForDemandResponseRankedByRidership = preprocess('data/Table 42.csv')
    datastatForFixedRouteRankedByRidership = preprocess('data/Table 39.csv')

    return data1, data2, data3, \
		   dataVehiclesByMode, \
           dataStatforAgenciesRankedByVRM, datastatForDemandResponseRankedByVRM, datastatForFixedRouteRankedByVRM,\
           dataStatforAgenciesRankedByVRH, datastatForDemandResponseRankedByVRH, datastatForFixedRouteRankedByVRH,\
           dataStatforAgenciesRankedByRidership, datastatForDemandResponseRankedByRidership, datastatForFixedRouteRankedByRidership
