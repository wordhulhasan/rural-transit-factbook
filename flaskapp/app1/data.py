from util import preprocess


def init_data():
    # Load data
    data1 = preprocess('data/revenue_vehicle_condition.csv')
    data2 = preprocess('data/revenue_vehicle_replacement_cost.csv')
    data3 = preprocess('data/service.csv')

    dataStatforAgenciesRankedByVRM = preprocess('data/Table 34.xlsx')
    datastatForDemandResponseRankedByVRM = preprocess('data/Table 40.xlsx')
    datastatForFixedRouteRankedByVRM = preprocess('data/Table 37.xlsx')

    dataStatforAgenciesRankedByVRH = preprocess('data/Table 35.xlsx')
    datastatForDemandResponseRankedByVRH = preprocess('data/Table 41.xlsx')
    datastatForFixedRouteRankedByVRH = preprocess('data/Table 38.xlsx')

    dataStatforAgenciesRankedByRidership = preprocess('data/Table 36.xlsx')
    datastatForDemandResponseRankedByRidership = preprocess('data/Table 42.xlsx')
    datastatForFixedRouteRankedByRidership = preprocess('data/Table 39.xlsx')

    return data1, data2, data3, \
           dataStatforAgenciesRankedByVRM, datastatForDemandResponseRankedByVRM, datastatForFixedRouteRankedByVRM,\
           dataStatforAgenciesRankedByVRH, datastatForDemandResponseRankedByVRH, datastatForFixedRouteRankedByVRH,\
           dataStatforAgenciesRankedByRidership, datastatForDemandResponseRankedByRidership, datastatForFixedRouteRankedByRidership
