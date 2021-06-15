from util import preprocess


def init_data():
    # Load data
    data1 = preprocess('data/revenue_vehicle_condition.csv')
    data2 = preprocess('data/revenue_vehicle_replacement_cost.csv')
    data3 = preprocess('data/service.csv')

    dataStatforAgenciesRankedByVRM = preprocess('data/statForAgenciesRankedByVRM.csv')
    datastatForDemandResponseRankedByVRM = preprocess('data/statForDemandResponseRankedByVRM.csv')
    datastatForFixedRouteRankedByVRM = preprocess('data/statForFixedRouteRankedByVRM.csv')

    dataStatforAgenciesRankedByVRH = preprocess('data/statForAgenciesRankedByVRH.csv')
    datastatForDemandResponseRankedByVRH = preprocess('data/statForDemandResponseByVRH.csv')
    datastatForFixedRouteRankedByVRH = preprocess('data/statForFixedRouteRankedByVRH.csv')

    dataStatforAgenciesRankedByRidership = preprocess('data/statForAgenciesRankedByRidership.csv')
    datastatForDemandResponseRankedByRidership = preprocess('data/statForDemandResponseRankedByRidership.csv')
    datastatForFixedRouteRankedByRidership = preprocess('data/statForFixedRouteRankedByRidership.csv')

    return data1, data2, data3, \
           dataStatforAgenciesRankedByVRM, datastatForDemandResponseRankedByVRM, datastatForFixedRouteRankedByVRM,\
           dataStatforAgenciesRankedByVRH, datastatForDemandResponseRankedByVRH, datastatForFixedRouteRankedByVRH,\
           dataStatforAgenciesRankedByRidership, datastatForDemandResponseRankedByRidership, datastatForFixedRouteRankedByRidership
