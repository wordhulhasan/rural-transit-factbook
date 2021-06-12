from util import preprocess


def init_data():
    # Load data
    data1 = preprocess('data/revenue_vehicle_condition.csv')
    data2 = preprocess('data/revenue_vehicle_replacement_cost.csv')
    data3 = preprocess('data/service.csv')
    dataStatforAgenciesRankedByVRM = preprocess('data/statForAgenciesRankedByVRM.csv')

    return data1, data2, data3, dataStatforAgenciesRankedByVRM
