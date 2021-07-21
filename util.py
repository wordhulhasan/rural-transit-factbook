from pandas import read_csv, concat, DataFrame
from collections import defaultdict, OrderedDict
from janitor import clean_names


# utility functions
def preprocess(path):
    """
    converts a .csv file and cleans its columns
    path: str
        path to the file
    """
    dataframe = read_csv(path)
    dataframe = clean_names(dataframe)
    return dataframe


def revenue_vehicles(dataframe, state='All', agency=None):
    """
    computes revenue vehicles by state
    dataframe: pandas dataframe
    state: str
    """

    if state == 'All':
        df = dataframe[['vehicle_type', 'active_fleet_vehicles']]. \
            groupby(['vehicle_type']).sum().reset_index()
    else:
        if agency == ' All ':
            df = dataframe[['state', 'vehicle_type', 'active_fleet_vehicles']]. \
                groupby(['state', 'vehicle_type']).sum().reset_index()
            df = df.query("state == @state").reset_index()

        else:
            df = dataframe[['state', 'agency_name', 'vehicle_type', 'active_fleet_vehicles']]. \
                groupby(['state', 'agency_name', 'vehicle_type']).sum().reset_index()
            df = df.query("state == @state and agency_name==@agency").reset_index(drop=True)

    return df

def revenue_vehicles_tribe(dataframe, state='All', agency=None):
    tribe = "Tribe"
    dataframe = dataframe.query("reporting_module == @tribe").reset_index()
    if state == 'All':
        df = dataframe[['vehicle_type', 'active_fleet_vehicles']]. \
            groupby(['vehicle_type']).sum().reset_index()
    else:
        if agency == ' All ':
            df = dataframe[['state', 'vehicle_type', 'active_fleet_vehicles']]. \
                groupby(['state', 'vehicle_type']).sum().reset_index()
            df = df.query("state == @state").reset_index()

        else:
            df = dataframe[['state', 'agency_name', 'vehicle_type', 'active_fleet_vehicles']]. \
                groupby(['state', 'agency_name', 'vehicle_type']).sum().reset_index()
            df = df.query("state == @state and agency_name==@agency").reset_index(drop=True)

    return df


def vehicle_revenue_miles(dataframe, state='All', agency=None):
    odf = dataframe[['state', 'agency', 'mode', 'vehicle_revenue_miles', 'ntd_reporter_type']]
    index_names = odf[(odf['ntd_reporter_type'] == "Full Reporter")].index
    odf.drop(index_names, inplace=True)
    if state == 'All':
        df = odf[['mode', 'vehicle_revenue_miles']]. \
            groupby(['mode']).sum().reset_index()
    else:
        if agency == ' All ':
            df = odf[['state', 'mode', 'vehicle_revenue_miles']]. \
                groupby(['state', 'mode']).sum().reset_index()
            df = df.query("state == @state").reset_index()
        else:
            df = odf[['state', 'agency', 'mode', 'vehicle_revenue_miles']]. \
                groupby(['state', 'agency', 'mode']).sum().reset_index()
            df = df.query("state == @state and agency==@agency").reset_index(drop=True)

    return df


def vehicle_revenue_hours(dataframe, state='All', agency=None):
    odf = dataframe[['state', 'agency', 'mode', 'vehicle_revenue_hours', 'ntd_reporter_type']]
    index_names = odf[(odf['ntd_reporter_type'] == "Full Reporter")].index
    odf.drop(index_names, inplace=True)
    if state == 'All':
        df = odf[['mode', 'vehicle_revenue_hours']]. \
            groupby(['mode']).sum().reset_index()
    else:
        if agency == ' All ':
            df = odf[['state', 'mode', 'vehicle_revenue_hours']]. \
                groupby(['state', 'mode']).sum().reset_index()
            df = df.query("state == @state").reset_index()
        else:
            df = odf[['state', 'agency', 'mode', 'vehicle_revenue_hours']]. \
                groupby(['state', 'agency', 'mode']).sum().reset_index()
            df = df.query("state == @state and agency==@agency").reset_index(drop=True)
    return df


def unlinked_passenger_trips(dataframe, state='All', agency=None):
    odf = dataframe[['state', 'agency', 'mode', 'unlinked_passenger_trips', 'ntd_reporter_type']]
    index_names = odf[(odf['ntd_reporter_type'] == "Full Reporter")].index
    odf.drop(index_names, inplace=True)
    if state == 'All':
        df = odf[['mode', 'unlinked_passenger_trips']]. \
            groupby(['mode']).sum().reset_index()
    else:
        if agency == ' All ':
            df = odf[['state', 'mode', 'unlinked_passenger_trips']]. \
                groupby(['state', 'mode']).sum().reset_index()
            df = df.query("state == @state").reset_index()
        else:
            df = odf[['state', 'agency', 'mode', 'unlinked_passenger_trips']]. \
                groupby(['state', 'agency', 'mode']).sum().reset_index()
            df = df.query("state == @state and agency==@agency").reset_index(drop=True)
    return df


def statRidershipByYear(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statVrmByYear(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statVrhByYear(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statRidershipByRank(dataframe):
    df = dataframe[['percentile', 'fixed_route', 'demand_response', 'total']]
    df = df.dropna()
    df.columns = ['Percentile', 'Fixed-Route', 'Demand-response', 'Total']
    return df


def statVrmByRank(dataframe):
    df = dataframe[['percentile', 'fixed_route', 'demand_response', 'total']]
    df = df.dropna()
    df.columns = ['Percentile', 'Fixed-Route', 'Demand-response', 'Total']
    return df


def statVrhByRank(dataframe):
    df = dataframe[['percentile', 'fixed_route', 'demand_response', 'total']]
    df = df.dropna()
    df.columns = ['Percentile', 'Fixed-Route', 'Demand-response', 'Total']
    return df


def statCapitalFunding(dataframe):
    df = dataframe[['funding_source', '2015', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df.columns = ['Funding Source', '2015', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statOperatingFunding(dataframe):
    df = dataframe[['funding_source', '2015', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df.columns = ['Funding Source', '2015', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statVehiclesByMode(dataframe):
    df = dataframe[
        ['vehicle_type', 'demand_response', 'fixed_route', 'commuter_bus', 'vanpool', 'demand_response_taxi', 'total']]
    df = df.dropna()
    df.columns = ['Vehicle Type', 'Demand-Response', 'Fixed-Route', 'Commuter Bus', 'Vanpool', 'Demand-Response Taxi',
                  'Total']
    return df


def statFleetByMode(dataframe):
    df = dataframe[['mode', 'average_number_of_vehicles_per_agency']]
    df = df.dropna()
    df.columns = ['Mode', 'Average Number of Vehicles per Agency']
    return df


def statAdaAccessible(dataframe):
    df = dataframe[['vehicle_type', '2015', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['Vehicle Type', '2015', '2016', '2017', '2018', '2019']
    return df


def statVehicleAge(dataframe):
    df = dataframe[['vehicle_type', '2015', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['Vehicle Type', '2015', '2016', '2017', '2018', '2019']
    return df


def statVehicleLength(dataframe):
    df = dataframe[['vehicle_type', '2015', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['Vehicle Type', '2015', '2016', '2017', '2018', '2019']
    return df


def statSeatingCapacity(dataframe):
    df = dataframe[['vehicle_type', '2015', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['Vehicle Type', '2015', '2016', '2017', '2018', '2019']
    return df


def statVehicleOwnership(dataframe):
    df = dataframe[['ownership_type', 'bus', 'cutaway', 'van', 'minivan', 'auto', 'school_bus', 'over_the_road_bus',
                    'sports_utility_vehicle', 'total']]
    df = df.dropna()
    df.columns = ['Ownership Type', 'Bus', 'Cutaway', 'Van', 'Minivan', 'Auto', 'School Bus', 'Over-the-road bus',
                  'Sports Utility Vehicle', 'Total']
    return df


def statFundingSource(dataframe):
    df = dataframe[['funding_source', 'bus', 'cutaway', 'van', 'minivan', 'auto', 'school_bus', 'over_the_road_bus',
                    'sports_utility_vehicle', 'total']]
    df = df.dropna()
    df.columns = ['Funding Source', 'Bus', 'Cutaway', 'Van', 'Minivan', 'Auto', 'School Bus', 'Over-the-road bus',
                  'Sports Utility Vehicle', 'Total']
    return df


def statTripsPerMile(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statTripsPerHour(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statTripsMilesHoursPerVehicle(dataframe):
    df = dataframe[['performance_measure', 'fixed_route', 'demand_response', 'total']]
    df = df.dropna()
    df.columns = ['Performance Measure', 'Fixed-Route', 'Demand-Response', 'Total']
    return df


def statOperatingExpensePerTrip(dataframe):
    df = dataframe[['mode', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Mode', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statOperatingExpensePerVehicleMile(dataframe):
    df = dataframe[['mode', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Mode', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statOperatingExpensePerVehicleHour(dataframe):
    df = dataframe[['mode', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Mode', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statFareboxRecoveryRatio(dataframe):
    df = dataframe[['mode', '2016', '2017', '2018', '2019', 'change_2018_2019']]
    df = df.dropna()
    df.columns = ['Mode', '2016', '2017', '2018', '2019', '% Change 2018-2019']
    return df


def statPercentileTotal(dataframe):
    df = dataframe[['percentile', 'oe_per_trip', 'oe_per_vrm', 'oe_per_vrh', 'upt_per_vrm', 'upt_per_vrh',
                    'farebox_recovery_ratio']]
    df = df.dropna()
    df.columns = ['Percentile', 'OE Per Trip', 'OE Per VRM', 'OE Per VRH', 'UPT Per VRM', 'UPT Per VRH',
                  'Farebox Recovery Ratio']
    return df


def statPercentileFixedRoute(dataframe):
    df = dataframe[['percentile', 'oe_per_trip', 'oe_per_vrm', 'oe_per_vrh', 'upt_per_vrm', 'upt_per_vrh',
                    'farebox_recovery_ratio']]
    df = df.dropna()
    df.columns = ['Percentile', 'OE Per Trip', 'OE Per VRM', 'OE Per VRH', 'UPT Per VRM', 'UPT Per VRH',
                  'Farebox Recovery Ratio']
    return df


def statPercentileDemandResponse(dataframe):
    df = dataframe[['percentile', 'oe_per_trip', 'oe_per_vrm', 'oe_per_vrh', 'upt_per_vrm', 'upt_per_vrh',
                    'farebox_recovery_ratio']]
    df = df.dropna()
    df.columns = ['Percentile', 'OE Per Trip', 'OE Per VRM', 'OE Per VRH', 'UPT Per VRM', 'UPT Per VRH',
                  'Farebox Recovery Ratio']
    return df


def statAgenciesByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statRidershipByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statVrmByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statVrhByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statVehiclesByRegion(dataframe):
    df = dataframe[
        ['vehicle_type', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Type', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statPerformanceByRegion(dataframe):
    df = dataframe[
        ['performance_measures', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5',
         'fta_region_6', 'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Performance Measures', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4',
                  'FTA Region 5', 'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statTripsPerVRMByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statTripsPerVRHByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statOperatingPerTripByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statOperatingPerVRMByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statOperatingPerVRHByRegion(dataframe):
    df = dataframe[
        ['vehicle_mode', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5', 'fta_region_6',
         'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Vehicle Mode', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4', 'FTA Region 5',
                  'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statAgencyPerformanceByRegion(dataframe):
    df = dataframe[
        ['performance_measures', 'fta_region_1', 'fta_region_2', 'fta_region_3', 'fta_region_4', 'fta_region_5',
         'fta_region_6', 'fta_region_7', 'fta_region_8', 'fta_region_9', 'fta_region_10']]
    df = df.dropna()
    df.columns = ['Performance Measures', 'FTA Region 1', 'FTA Region 2', 'FTA Region 3', 'FTA Region 4',
                  'FTA Region 5', 'FTA Region 6', 'FTA Region 7', 'FTA Region 8', 'FTA Region 9', 'FTA Region 10']
    return df


def statRidershipByState(dataframe):
    df = dataframe[['state', 'total', 'fixed_route', 'demand_response', 'other']]
    df.columns = ['State', 'Total', 'Fixed-Route', 'Demand-Response', 'Other']
    return df


def statVrmByState(dataframe):
    df = dataframe[['state', 'total', 'fixed_route', 'demand_response', 'other']]
    df.columns = ['State', 'Total', 'Fixed-Route', 'Demand-Response', 'Other']
    return df


def statVrhByState(dataframe):
    df = dataframe[['state', 'total', 'fixed_route', 'demand_response', 'other']]
    df.columns = ['State', 'Total', 'Fixed-Route', 'Demand-Response', 'Other']
    return df


def statRidershipTotalYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statRidershipFRYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statRidershipDRYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statRidershipOtherYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statVrmTotalYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statVrmFrsYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statVrmDrsYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statVrmOtherYearlyByState(dataframe):
    df = dataframe[['state', '2016', '2017', '2018', '2019']]
    df = df.dropna()
    df.columns = ['State', '2016', '2017', '2018', '2019']
    return df


def statFinancialOnOperationsByState(dataframe):
    df = dataframe[
        ['state', 'directly_generated', 'local_government', 'state_government', 'federal_government', 'total']]
    #	df = df.dropna()
    df.columns = ['State', 'Directly Generated', 'Local Government', 'State Government', 'Federal Government', 'Total']
    return df


def statFinancialOnCapitalByState(dataframe):
    df = dataframe[
        ['state', 'directly_generated', 'local_government', 'state_government', 'federal_government', 'total']]
    #	df = df.dropna()
    df.columns = ['State', 'Directly Generated', 'Local Government', 'State Government', 'Federal Government', 'Total']
    return df


def statFleetStatisticsByState(dataframe):
    df = dataframe[['state', 'total_active_vehicles', 'ada_vehicles', 'average_vehicle_age', 'average_vehicle_length',
                    'average_vehicle_capacity', 'trips_per_vehicle', 'miles_per_vehicle', 'hours_per_vehicle']]
    #	df = df.dropna()
    df.columns = ['State', 'Total Active Vehicles', 'ADA Vehicles (%)', 'Average Vehicle Age',
                  'Average Vehicle Length (ft)', 'Average Vehicle Capacity', 'Trips Per Vehicle', 'Miles Per Vehicle',
                  'Hours Per Vehicle']
    return df


def statPerformanceMeasuresByState(dataframe):
    df = dataframe[['state', 'total_trips_per_vrm', 'fixed_route_trips_per_vrm', 'demand_response_trips_per_vrm',
                    'total_trips_per_vrh', 'fixed_route_trips_per_vrh', 'demand_response_trips_per_vrh',
                    'operating_expense_per_trip', 'operating_expense_per_vrm', 'operating_expense_per_vrh',
                    'farebox_recovery_ratio']]
    #	df = df.dropna()
    df.columns = ['State', 'Total Trips Per VRM', 'FR Trips Per VRM', 'DR Trips Per VRM', 'Total Trips Per VRH',
                  'FR Trips Per VRH', 'DR Trips Per VRH', 'OE Per Trip', 'OE Per VRM', 'OE Per VRH',
                  'Farebox Recovery Ratio']
    return df


def statPerformanceMeasuresMedianByState(dataframe):
    df = dataframe[['state', 'total_trips_per_vrm', 'fixed_route_trips_per_vrm', 'demand_response_trips_per_vrm',
                    'total_trips_per_vrh', 'fixed_route_trips_per_vrh', 'demand_response_trips_per_vrh',
                    'operating_expense_per_trip', 'operating_expense_per_vrm', 'operating_expense_per_vrh',
                    'farebox_recovery_ratio']]
    #	df = df.dropna()
    df.columns = ['State', 'Total Trips Per VRM', 'FR Trips Per VRM', 'DR Trips Per VRM', 'Total Trips Per VRH',
                  'FR Trips Per VRH', 'DR Trips Per VRH', 'OE Per Trip', 'OE Per VRM', 'OE Per VRH',
                  'Farebox Recovery Ratio']
    return df


def statAgencyPercentileRidershipByState(dataframe):
    df = dataframe[['state', 'number_of_agencies', '25th', '50th', '75th']]
    #	df = df.dropna()
    df.columns = ['State', 'Number of Agencies', '25th', '50th', '75th']
    return df


def statAgencyPercentileVrmByState(dataframe):
    df = dataframe[['state', 'number_of_agencies', '25th', '50th', '75th']]
    #	df = df.dropna()
    df.columns = ['State', 'Number of Agencies', '25th', '50th', '75th']
    return df


def statAgencyPercentileVrhByState(dataframe):
    df = dataframe[['state', 'number_of_agencies', '25th', '50th', '75th']]
    #	df = df.dropna()
    df.columns = ['State', 'Number of Agencies', '25th', '50th', '75th']
    return df


def statRidershipYearlyByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    #	df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statVrmYearlyByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    #	df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statVrhYearlyByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    #	df = df.dropna()
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statVehiclesByTribal(dataframe):
    df = dataframe[['vehicle_type', 'number_of_vehicles']]
    #	df = df.dropna()
    df.columns = ['Vehicle Type', 'Number of Vehicles']
    return df


def statFleetStatisticsByTribal(dataframe):
    df = dataframe[['number_of_vehicles', 'vehicle_ada', 'average_vehicle_age', 'average_vehicle_length',
                    'average_vehicle_capacity']]
    #	df = df.dropna()
    df.columns = ['Number of Vehicles', '% Vehicle ADA', 'Average Vehicle Age (years)', 'Average Vehicle Length (feet)',
                  'Average Vehicle Capacity']
    return df


def statTripsPerVehicleByTribal(dataframe):
    df = dataframe[['vehicle_mode', 'trips']]
    #	df = df.dropna()
    df.columns = ['Vehicle Mode', 'Trips']
    return df


def statVRMPerVehicleByTribal(dataframe):
    df = dataframe[['vehicle_mode', 'vehicle_revenue_miles']]
    #	df = df.dropna()
    df.columns = ['Vehicle Mode', 'Vehicle Revenue Miles']
    return df


def statVRHPerVehicleByTribal(dataframe):
    df = dataframe[['vehicle_mode', 'vehicle_revenue_hours']]
    #	df = df.dropna()
    df.columns = ['Vehicle Mode', 'Vehicle Revenue Hours']
    return df


def statTripsPerVrmByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statTripsPerVrhByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statOperatingExpensePerTripByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statOperatingExpensePerVrmByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statOperatingExpensePerVrhByTribal(dataframe):
    df = dataframe[['vehicle_mode', '2015', '2016', '2017', '2018', '2019']]
    df.columns = ['Vehicle Mode', '2015', '2016', '2017', '2018', '2019']
    return df


def statFareboxRecoveryRatioByTribal(dataframe):
    df = dataframe[['frr', '2015', '2016', '2017', '2018', '2019']]
    df.columns = ['Farebox Recovery Ratio', '2015', '2016', '2017', '2018', '2019']
    return df


def statPerformanceMeasureMedianByTribal(dataframe):
    df = dataframe[['performance_measure', 'median_value']]
    df.columns = ['Performance Measure', 'Median Value']
    return df


def statisticsForAgenciesRankedByVRM(dataframe):
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForDemandResponseRankedByVRM(dataframe):
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForFixedRouteRankedByVRM(dataframe):
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForAgenciesRankedByVRH(dataframe):
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForDemandResponseRankedByVRH(dataframe):
    # print(dataframe)
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    # print(df)
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForFixedRouteRankedByVRH(dataframe):
    # print(dataframe)
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    # print(df)
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForAgenciesRankedByRidership(dataframe):
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForDemandResponseRankedByRidership(dataframe):
    # print(dataframe)
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    # print(df)
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def statisticsForFixedRouteRankedByRidership(dataframe):
    # print(dataframe)
    df = dataframe[['percentile_rank', 'minimum', 'maximum', 'average_ridership', 'avg_vrm', 'avg_vrh', 'avg_upt_vrm',
                    'avg_upt_vrh', 'avg_op_ex_upt', 'avg_op_ex_vrm', 'avg_op_ex_vrh']]
    df = df.dropna()
    # print(df)
    df.columns = ['Percentile Rank', 'Minimum UPT', 'Maximum UPT', 'Avg UPT', 'Avg VRM', 'Avg VRH', 'Avg Trips Per VRM',
                  'Avg Trips Per VRH', 'Avg OE Per Trip', 'Avg OE Per VRM', 'Avg OE Per VRH']
    return df


def fleet_composition(dataframe, state='All', agency=None):
    """
    computes number of fleets by state
    dataframe: pandas dataframe
    state: str
    """
    if state == 'All':
        df = dataframe['vehicle_type'].value_counts().reset_index()

    else:
        if agency == ' All ':
            df = dataframe.query("state == @state").reset_index()
            df = df['vehicle_type'].value_counts().reset_index()

        else:
            df = dataframe.query("state == @state and agency_name==@agency").reset_index()
            df = df['vehicle_type'].value_counts().reset_index()

    df.columns = ['vehicle_type', 'count']
    return df


def generate_stats(dataframe, starting_year, ending_year, state='All', vehicle=' All ', agency=None):
    if state == 'All':
        if vehicle == ' All ':
            dataframe = dataframe
        else:
            dataframe = dataframe.query("vehicle_type == @vehicle")
    else:
        if agency == ' All ':
            if vehicle == ' All ':
                dataframe = dataframe.query("state == @state")
            else:
                dataframe = dataframe.query("state == @state and vehicle_type == @vehicle")
        else:
            if vehicle == ' All ':
                dataframe = dataframe.query("state == @state and agency_name==@agency")
            else:
                dataframe = dataframe.query("state == @state and vehicle_type == @vehicle and agency_name==@agency")

    dataframe = dataframe.loc[:, ('projected_retired_year', 'active_fleet_vehicles')].dropna(). \
        groupby('projected_retired_year').sum().reset_index()

    df_predicted = dataframe. \
        query('projected_retired_year >= @starting_year and projected_retired_year <= @ending_year').copy()

    df_backlog = DataFrame.from_dict({'projected_retired_year': ['backlog'],
                                      'active_fleet_vehicles': [
                                          dataframe.query('projected_retired_year < @starting_year')
                                          ['active_fleet_vehicles'].sum()]})

    data = concat([df_backlog, df_predicted]).reset_index(drop=True)
    return data


def replacement_cost(dataframe, starting_year, ending_year, state='All', vehicle=' All ', agency=None):
    if state == 'All':
        if vehicle == ' All ':
            dataframe = dataframe
        else:
            dataframe = dataframe.query("vehicle_type == @vehicle")
    else:
        if agency == ' All ':
            if vehicle == ' All ':
                dataframe = dataframe.query("state == @state")
            else:
                dataframe = dataframe.query("state == @state and vehicle_type == @vehicle")
        else:
            if vehicle == ' All ':
                dataframe = dataframe.query("state == @state and agency_name == @agency")
            else:
                dataframe = dataframe.query("state == @state and vehicle_type == @vehicle and agency_name==@agency")

    dataframe = dataframe.loc[:, ('projected_retired_year', 'total_fleet_cost')].dropna(). \
        groupby('projected_retired_year').sum().reset_index()

    df_predicted = dataframe. \
        query('projected_retired_year >= @starting_year and projected_retired_year <= @ending_year').copy()

    df_predicted.loc[:, 'projected_retired_year'] = df_predicted.loc[:, 'projected_retired_year'].astype(int)

    df_backlog = DataFrame.from_dict({'projected_retired_year': ['backlog'],
                                      'total_fleet_cost': [dataframe.query('projected_retired_year < @starting_year')
                                                           ['total_fleet_cost'].sum()]})

    data = concat([df_backlog, df_predicted]).reset_index(drop=True).copy()
    return data


def backlog(dataframe, state='All', agency=None):
    if state != 'All':
        if agency == ' All ':
            dataframe = dataframe.query("state == @state")
        else:
            dataframe = dataframe.query("state == @state and agency_name==@agency")

    df = dataframe.loc[dataframe.projected_retired_year < 2021].groupby(['vehicle_type'])[
        'active_fleet_vehicles'].sum().reset_index()
    df.columns = ['vehicle_type', 'count']
    return df


def backlog_cost(dataframe, state='All', agency=None):
    if state != 'All':
        if agency == ' All ':
            dataframe = dataframe.query("state == @state")
        else:
            dataframe = dataframe.query("state == @state and agency_name==@agency")

    df = dataframe.loc[dataframe.projected_retired_year < 2021].groupby(['vehicle_type'])[
        'total_fleet_cost'].sum().reset_index()
    return df


def make_state_agency_dict():
    in_df = read_csv('data/revenue_vehicle_condition.csv')

    d1 = (zip(in_df['State'], in_df['Agency Name']))

    res = defaultdict(set)
    for i, j in d1:
        res[i].add(j)

    for k, v in res.items():
        v.add(' All ')
        res[k] = sorted(v)

    res = OrderedDict(sorted(res.items()))
    res['All'] = [' All ']

    return res

def make_state_agency_dict2():
    tribe="Tribe"
    in_df = read_csv('data/revenue_vehicle_condition.csv')
    in_df = clean_names(in_df)
    in_df = in_df.query("reporting_module == @tribe").reset_index()
    d1 = (zip(in_df['state'], in_df['agency_name']))

    res = defaultdict(set)
    for i, j in d1:
        res[i].add(j)

    for k, v in res.items():
        v.add(' All ')
        res[k] = sorted(v)

    res = OrderedDict(sorted(res.items()))
    res['All'] = [' All ']

    return res

# US State, US Commonwealth and Territories dictionaries
states_dict = {
    'AL': 'Alabama',
    'AK': 'Alaska',
    'AZ': 'Arizona',
    'AR': 'Arkansas',
    'CA': 'California',
    'CO': 'Colorado',
    'CT': 'Connecticut',
    'DE': 'Delaware',
    'DC': 'District of Columbia',
    'FL': 'Florida',
    'GA': 'Georgia',
    'HI': 'Hawaii',
    'ID': 'Idaho',
    'IL': 'Illinois',
    'IN': 'Indiana',
    'IA': 'Iowa',
    'KS': 'Kansas',
    'KY': 'Kentucky',
    'LA': 'Louisiana',
    'ME': 'Maine',
    'MD': 'Maryland',
    'MA': 'Massachusetts',
    'MI': 'Michigan',
    'MN': 'Minnesota',
    'MS': 'Mississippi',
    'MO': 'Missouri',
    'MT': 'Montana',
    'NE': 'Nebraska',
    'NV': 'Nevada',
    'NH': 'New Hampshire',
    'NJ': 'New Jersey',
    'NM': 'New Mexico',
    'NY': 'New York',
    'NC': 'North Carolina',
    'ND': 'North Dakota',
    'OH': 'Ohio',
    'OK': 'Oklahoma',
    'OR': 'Oregon',
    'PA': 'Pennsylvania',
    'RI': 'Rhode Island',
    'SC': 'South Carolina',
    'SD': 'South Dakota',
    'TN': 'Tennessee',
    'TX': 'Texas',
    'UT': 'Utah',
    'VT': 'Vermont',
    'VA': 'Virginia',
    'WA': 'Washington',
    'WV': 'West Virginia',
    'WI': 'Wisconsin',
    'WY': 'Wyoming',
    'PR': 'Puerto Rico',
    'AS': 'American Samoa',
    'FM': 'Federated States of Micronesia',
    'GU': 'Guam',
    'MH': 'Marshall Islands',
    'MP': 'Northern Mariana Islands',
    'PW': 'Palau',
    'VI': 'Virgin Islands',
    'All': 'All'
}

vehicles_dict = {
    ' All ': ' All ',
    'Aerial Tramway': 'Aerial Tramway',
    'Articulated Bus': 'Articulated Bus',
    'Automobile': 'Automobile',
    'Bus': 'Bus',
    'Cutaway': 'Cutaway',
    'Ferryboat': 'Ferryboat',
    'Minivan': 'Minivan',
    'Over-the-road Bus': 'Over-the-road Bus',
    'School Bus': 'School Bus',
    'Sports Utility Vehicle': 'Sports Utility Vehicle',
    'Streetcar Rail': 'Streetcar Rail',
    'Van': 'Van'
}

vehicle_colors = {
    "Aerial Tramway": "#00876c",
    "Articulated Bus": "#3c986d",
    "Automobile": "#61a96e",
    "Bus": "#85b96f",
    "Cutaway": "#aac872",
    "Ferryboat": "#f7e382",
    "Minivan": "#f7c96c",
    "Over-the-road Bus": "#f5af5c",
    "School Bus": "#f19452",
    "Sports Utility Vehicle": "#ea784d",
    "Streetcar Rail": "#e15b4e",
    "Van": "#d43d51"}

mode_colors = {
    "RB": "#00876c",
    "MB": "#3c986d",
    "HR": "#61a96e",
    "DR": "#85b96f",
    "CB": "#aac872",
    "YR": "#f7e382",
    "VP": "#f7c96c",
    "LR": "#f5af5c",
    "CR": "#f19452",
    "DT": "#ea784d",
    "FB": "#ea784d",
    "TB": "#ea784d",
    "SR": "#ea784d",
    "AR": "#ea784d",
    "CC": "#ea784d",
    "MG": "#ea784d",
    "IP": "#ea784d",
    "PB": "#ea784d",

}
