import json

import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import plotly.figure_factory as ff
from util import vehicle_colors, revenue_vehicles, fleet_composition, \
    generate_stats, \
    replacement_cost, backlog, backlog_cost, make_state_agency_dict, vehicle_revenue_miles, mode_colors, \
    vehicle_revenue_hours, unlinked_passenger_trips, \
    statisticsForAgenciesRankedByVRM, statisticsForDemandResponseRankedByVRM, statisticsForFixedRouteRankedByVRM, \
    statisticsForAgenciesRankedByVRH, statisticsForDemandResponseRankedByVRH, statisticsForFixedRouteRankedByVRH, \
    statisticsForAgenciesRankedByRidership, statisticsForDemandResponseRankedByRidership, \
    statisticsForFixedRouteRankedByRidership, statVehiclesByMode, statFleetByMode, statAdaAccessible, statVehicleAge,\
	statVehicleLength, statSeatingCapacity, statVehicleOwnership, statFundingSource, \
	statRidershipByYear, statVrmByYear, statVrhByYear, statRidershipByRank, statVrmByRank, statVrhByRank, \
    statTripsPerMile, statTripsPerHour, statTripsMilesHoursPerVehicle, statOperatingExpensePerTrip, \
    statOperatingExpensePerVehicleMile, statOperatingExpensePerVehicleHour, statFareboxRecoveryRatio, \
    statPercentileTotal, statPercentileFixedRoute, statPercentileDemandResponse, \
    statAgenciesByRegion, statRidershipByRegion, statVrmByRegion, statVrhByRegion, statVehiclesByRegion, \
    statPerformanceByRegion, statTripsPerVRMByRegion,  statTripsPerVRHByRegion, statOperatingPerTripByRegion, \
    statOperatingPerVRMByRegion, statOperatingPerVRHByRegion, statAgencyPerformanceByRegion, \
    statRidershipByState, statVrmByState, statVrhByState, statRidershipTotalYearlyByState, \
    statRidershipFRYearlyByState, statRidershipDRYearlyByState, statRidershipOtherYearlyByState, \
    statVrmTotalYearlyByState, statVrmFrsYearlyByState, statVrmDrsYearlyByState, statVrmOtherYearlyByState, \
    statFinancialOnOperationsByState, statFinancialOnCapitalByState, statFleetStatisticsByState, \
    statPerformanceMeasuresByState, statPerformanceMeasuresMedianByState

from .data import init_data


def init_callbacks(dash_app):
    # callbacks
    data1, data2, data3, dataRidershipByYear, dataVrmByYear, dataVrhByYear, dataRidershipByRank, dataVrmByRank, dataVrhByRank, \
	dataVehiclesByMode, dataFleetByMode, dataAdaAccessible, dataVehicleAge, dataVehicleLength, \
	dataSeatingCapacity, dataVehicleOwnership, dataFundingSource, dataTripsPerMile, dataTripsPerHour, dataTripsMilesHoursPerVehicle, \
    dataOperatingExpensePerTrip, dataOperatingExpensePerVehicleMile, dataOperatingExpensePerVehicleHour, dataFareboxRecoveryRatio, \
    dataPercentileTotal, dataPercentileFixedRoute, dataPercentileDemandResponse, \
    dataAgenciesByRegion, dataRidershipByRegion, dataVrmByRegion, dataVrhByRegion, dataVehiclesByRegion, \
    dataPerformanceByRegion, dataTripsPerVRMByRegion, dataTripsPerVRHByRegion, dataOperatingPerTripByRegion, \
    dataOperatingPerVRMByRegion, dataOperatingPerVRHByRegion, dataAgencyPerformanceByRegion, \
    dataRidershipByState, dataVrmByState, dataVrhByState, \
    dataRidershipTotalYearlyByState, dataRidershipFRYearlyByState, dataRidershipDRYearlyByState, dataRidershipOtherYearlyByState, \
    dataVrmTotalYearlyByState, dataVrmFrsYearlyByState, dataVrmDrsYearlyByState, dataVrmOtherYearlyByState, \
    dataFinancialOnOperationsByState, dataFinancialOnCapitalByState, \
    dataFleetStatisticsByState, \
    dataPerformanceMeasuresByState, \
    dataPerformanceMeasuresMedianByState,\
    dataStatforAgenciesRankedByVRM, datastatForDemandResponseRankedByVRM, datastatForFixedRouteRankedByVRM, \
    dataStatforAgenciesRankedByVRH, datastatForDemandResponseRankedByVRH, datastatForFixedRouteRankedByVRH, \
    dataStatforAgenciesRankedByRidership, datastatForDemandResponseRankedByRidership, datastatForFixedRouteRankedByRidership \
        = init_data()

    res = make_state_agency_dict()

    @dash_app.callback(
        Output('agency-dropdown', 'options'),
        [Input('state-selector', 'value')])
    def set_cities_options(selected_state):
        return [{'label': i, 'value': i} for i in res[selected_state]]

    @dash_app.callback(
        Output('agency-dropdown-2', 'options'),
        [Input('state-selector-2', 'value')])
    def set_cities_options(selected_state):
        return [{'label': i, 'value': i} for i in res[selected_state]]

    @dash_app.callback(
        Output('agency-dropdown-3', 'options'),
        [Input('state-selector-3', 'value')])
    def set_cities_options(selected_state):
        return [{'label': i, 'value': i} for i in res[selected_state]]

    @dash_app.callback(
        Output('agency-dropdown', 'value'),
        [Input('agency-dropdown', 'options')])
    def set_cities_value(available_options):
        return available_options[0]['value']

    @dash_app.callback(
        Output('agency-dropdown-2', 'value'),
        [Input('agency-dropdown-2', 'options')])
    def set_cities_value(available_options):
        return available_options[0]['value']

    @dash_app.callback(
        Output('agency-dropdown-3', 'value'),
        [Input('agency-dropdown-3', 'options')])
    def set_cities_value(available_options):
        return available_options[0]['value']

    @dash_app.callback(Output('revenue-vehicles', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def update_revenue_vehicles(state, agency):
        df = revenue_vehicles(data1, state, agency)

        fig = px.bar(df, x='vehicle_type', y='active_fleet_vehicles', text='active_fleet_vehicles',
                     color='vehicle_type',
                     color_discrete_map=vehicle_colors, title='Number of Revenue Vehicles',
                     labels={"vehicle_type": "Vehicle Type", "active_fleet_vehicles": "Number of Revenue Vehicles"},
                     template='simple_white',
                     )

        fig.update_traces(textposition='outside')
        fig.update_layout(
            font_color="black",
            title_font_color="black",
            legend_title_font_color="black",
            margin=dict(l=100, r=50, t=150, b=50),
            height=600,
            hovermode='x',
            autosize=True
        )
        return fig

    @dash_app.callback(Output('fleet-composition', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def update_fleet_composition(state, agency):
        df = fleet_composition(data1, state, agency)

        fig = px.pie(df, values='count', names='vehicle_type', color='vehicle_type', color_discrete_map=vehicle_colors,
                     title='Percent of Revenue Vehicles', template='simple_white')

        fig.update_layout(
            font_color="black",
            title_font_color="black",
            legend_title_font_color="black",
            uniformtext_minsize=16,
            uniformtext_mode='hide',
            margin=dict(l=100, r=50, t=150, b=50),
            height=700,
            hovermode='x',
            autosize=True
        )
        return fig

    @dash_app.callback(Output('op-stat', 'figure'),
                       [Input('state-selector-2', 'value'),
                        Input('agency-dropdown-2', 'value'),
                        Input('op-stat-dropdown','value')])
    def vrm(state, agency, opStat):
        if opStat == "vrm":
            df = vehicle_revenue_miles(data3, state, agency)
            fig = px.bar(df, x='mode', y='vehicle_revenue_miles', text='vehicle_revenue_miles',
                         color='mode',
                         color_discrete_map=mode_colors, title='Vehicle Revenue Miles',
                         labels={"mode": "mode", "vehicle_revenue_miles": "Vehicle Revenue Miles"},
                         template='simple_white',
                         )

            fig.update_traces(textposition='outside')
            fig.update_layout(
                font_color="black",
                title_font_color="black",
                legend_title_font_color="black",
                margin=dict(l=100, r=50, t=150, b=50),
                height=600,
                hovermode='x',
                autosize=True
            )
        elif opStat == "vrh":
            df = vehicle_revenue_hours(data3, state, agency)
            fig = px.bar(df, x='mode', y='vehicle_revenue_hours', text='vehicle_revenue_hours',
                         color='mode',
                         color_discrete_map=mode_colors, title='Vehicle Revenue Hours',
                         labels={"mode": "mode", "vehicle_revenue_hours": "Vehicle Revenue Hours"},
                         template='simple_white',
                         )

            fig.update_traces(textposition='outside')
            fig.update_layout(
                font_color="black",
                title_font_color="black",
                legend_title_font_color="black",
                margin=dict(l=100, r=50, t=150, b=50),
                height=600,
                hovermode='x',
                autosize=True
            )
        else:
            df = unlinked_passenger_trips(data3, state, agency)
            fig = px.bar(df, x='mode', y='unlinked_passenger_trips', text='unlinked_passenger_trips',
                         color='mode',
                         color_discrete_map=mode_colors, title='Unlinked Passenger Trips',
                         labels={"mode": "mode", "unlinked_passenger_trips": "unlinked_passenger_trips"},
                         template='simple_white',
                         )

            fig.update_traces(textposition='outside')
            fig.update_layout(
                font_color="black",
                title_font_color="black",
                legend_title_font_color="black",
                margin=dict(l=100, r=50, t=150, b=50),
                height=600,
                hovermode='x',
                autosize=True
            )
        return fig

    @dash_app.callback(Output('ridership_by_year-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rby(state, agency):
        df = statRidershipByYear(dataRidershipByYear)
        fig = ff.create_table(df)
        return fig
		
    @dash_app.callback(Output('vrm_by_year-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrmby(state, agency):
        df = statVrmByYear(dataVrmByYear)
        fig = ff.create_table(df)
        return fig
		
    @dash_app.callback(Output('vrh_by_year-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrhby(state, agency):
        df = statVrhByYear(dataVrhByYear)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('ridership_by_rank-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rbr(state, agency):
        df = statRidershipByRank(dataRidershipByRank)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrm_by_rank-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrmbr(state, agency):
        df = statVrmByRank(dataVrmByRank)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrh_by_rank-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrhbr(state, agency):
        df = statVrhByRank(dataVrhByRank)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vehicle_by_mode-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vbm(state, agency):
        df = statVehiclesByMode(dataVehiclesByMode)
#        df_sample = df[['vehicle_type', 'vehicle_revenue_miles']]
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('fleet_by_mode-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vbm(state, agency):
        df = statFleetByMode(dataFleetByMode)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('adaAccessible-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def ada(state, agency):
        df = statAdaAccessible(dataAdaAccessible)
        fig = ff.create_table(df)
        return fig
		
    @dash_app.callback(Output('vehicleAge-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def age(state, agency):
        df = statVehicleAge(dataVehicleAge)
        fig = ff.create_table(df)
        return fig
		
    @dash_app.callback(Output('vehicleLenght-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def length(state, agency):
        df = statVehicleLength(dataVehicleLength)
        fig = ff.create_table(df)
        return fig
		
    @dash_app.callback(Output('seatingCapacity-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def seating(state, agency):
        df = statSeatingCapacity(dataSeatingCapacity)
        fig = ff.create_table(df)
        return fig
	
    @dash_app.callback(Output('vehicleOwnership-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def ownership(state, agency):
        df = statVehicleOwnership(dataVehicleOwnership)
        fig = ff.create_table(df)
        return fig
		
    @dash_app.callback(Output('fundingSource-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def funding(state, agency):
        df = statFundingSource(dataFundingSource)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('tripsPerMile-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def tpm(state, agency):
        df = statTripsPerMile(dataTripsPerMile)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('tripsPerHour-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def tph(state, agency):
        df = statTripsPerHour(dataTripsPerHour)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('tripsMilesHoursPerVehicle-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def tmhpv(state, agency):
        df = statTripsMilesHoursPerVehicle(dataTripsMilesHoursPerVehicle)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('operatingExpensePerTrip-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def oept(state, agency):
        df = statOperatingExpensePerTrip(dataOperatingExpensePerTrip)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('operatingExpensePerVehicleMile-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def oepvm(state, agency):
        df = statOperatingExpensePerVehicleMile(dataOperatingExpensePerVehicleMile)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('operatingExpensePerVehicleHour-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def oepvh(state, agency):
        df = statOperatingExpensePerVehicleHour(dataOperatingExpensePerVehicleHour)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('fareboxRecoveryRatio-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def frr(state, agency):
        df = statFareboxRecoveryRatio(dataFareboxRecoveryRatio)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('percentileTotal-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def pt(state, agency):
        df = statPercentileTotal(dataPercentileTotal)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('percentileFixedRoute-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def pfr(state, agency):
        df = statPercentileFixedRoute(dataPercentileFixedRoute)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('percentileDemandResponse-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def pdr(state, agency):
        df = statPercentileDemandResponse(dataPercentileDemandResponse)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('agenciesByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def abr(state, agency):
        df = statAgenciesByRegion(dataAgenciesByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('ridershipByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rbr(state, agency):
        df = statRidershipByRegion(dataRidershipByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrmByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrmbr(state, agency):
        df = statVrmByRegion(dataVrmByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrhByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrhbr(state, agency):
        df = statVrhByRegion(dataVrhByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vehiclesByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vbr(state, agency):
        df = statVehiclesByRegion(dataVehiclesByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('performanceByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def pbr(state, agency):
        df = statPerformanceByRegion(dataPerformanceByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('tripsPerVRMByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def tpvrmbr(state, agency):
        df = statTripsPerVRMByRegion(dataTripsPerVRMByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('tripsPerVRHByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def tpvrhbr(state, agency):
        df = statTripsPerVRHByRegion(dataTripsPerVRHByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('operatingPerTripByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def optbr(state, agency):
        df = statOperatingPerTripByRegion(dataOperatingPerTripByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('operatingPerVRMByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def opvrmbr(state, agency):
        df = statOperatingPerVRMByRegion(dataOperatingPerVRMByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('operatingPerVRHByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def opvrhbr(state, agency):
        df = statOperatingPerVRHByRegion(dataOperatingPerVRHByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('agencyPerformanceByRegion-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def apbr(state, agency):
        df = statAgencyPerformanceByRegion(dataAgencyPerformanceByRegion)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('ridershipByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rbs(state, agency):
        df = statRidershipByState(dataRidershipByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrmByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rbvrm(state, agency):
        df = statVrmByState(dataVrmByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrhByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rbvrh(state, agency):
        df = statVrhByState(dataVrhByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('ridershipTotalYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rtybs(state, agency):
        df = statRidershipTotalYearlyByState(dataRidershipTotalYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('ridershipFRYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rfrybs(state, agency):
        df = statRidershipFRYearlyByState(dataRidershipFRYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('ridershipDRYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rdrybs(state, agency):
        df = statRidershipDRYearlyByState(dataRidershipDRYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('ridershipOtherYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def rorybs(state, agency):
        df = statRidershipOtherYearlyByState(dataRidershipOtherYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrmTotalYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vtybs(state, agency):
        df = statVrmTotalYearlyByState(dataVrmTotalYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrmFrsYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vfybs(state, agency):
        df = statVrmFrsYearlyByState(dataVrmFrsYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrmDrsYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vdybs(state, agency):
        df = statVrmDrsYearlyByState(dataVrmDrsYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vrmOtherYearlyByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def voybs(state, agency):
        df = statVrmOtherYearlyByState(dataVrmOtherYearlyByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('financialOnOperationsByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def foobs(state, agency):
        df = statFinancialOnOperationsByState(dataFinancialOnOperationsByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('financialOnCapitalByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def focbs(state, agency):
        df = statFinancialOnCapitalByState(dataFinancialOnCapitalByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('fleetStatisticsByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def fsbs(state, agency):
        df = statFleetStatisticsByState(dataFleetStatisticsByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('performanceMeasuresByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def pmbs(state, agency):
        df = statPerformanceMeasuresByState(dataPerformanceMeasuresByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('performanceMeasuresMedianByState-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def pmmbs(state, agency):
        df = statPerformanceMeasuresMedianByState(dataPerformanceMeasuresMedianByState)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('vehicle-revenue-miles-table', 'figure'),
                       [Input('state-selector-3', 'value'),
                        Input('agency-dropdown-3', 'value')])
    def vrm(state, agency):
        df = vehicle_revenue_miles(data3, state, agency)
        df_sample = df[['mode', 'vehicle_revenue_miles']]
        fig = ff.create_table(df_sample)
        return fig

    @dash_app.callback(Output('vehicle-revenue-hours-table', 'figure'),
                       [Input('state-selector-3', 'value'),
                        Input('agency-dropdown-3', 'value')])
    def vrh(state, agency):
        df = vehicle_revenue_hours(data3, state, agency)
        df_sample = df[['mode', 'vehicle_revenue_hours']]
        fig = ff.create_table(df_sample)
        return fig

    @dash_app.callback(Output('unlinked_passenger_trips-table', 'figure'),
                       [Input('state-selector-3', 'value'),
                        Input('agency-dropdown-3', 'value')])
    def vrh(state, agency):
        df = unlinked_passenger_trips(data3, state, agency)
        df_sample = df[['mode', 'unlinked_passenger_trips']]
        fig = ff.create_table(df_sample)
        print(df_sample)
        return fig

    @dash_app.callback(Output('statisticsRankedByMB-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value'),
                        Input('stat-dropdown-vrm', 'value')]
                       )
    def statRankedByFixedRoute(state, agency, statdropdown):
        if statdropdown == "ridership":
            df = statisticsForFixedRouteRankedByRidership(datastatForFixedRouteRankedByRidership)
        elif statdropdown == "vrh":
            df = statisticsForFixedRouteRankedByVRH(datastatForFixedRouteRankedByVRH)
        else:
            df = statisticsForFixedRouteRankedByVRM(datastatForFixedRouteRankedByVRM)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('statisticsRankedByDemandResponse-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value'),
                        Input('stat-dropdown-vrh', 'value')]
                       )
    def statRankedByVRH(state, agency, statdropdown):
        if statdropdown == "ridership":
            df = statisticsForDemandResponseRankedByRidership(datastatForDemandResponseRankedByRidership)
        elif statdropdown == "vrh":
            df = statisticsForDemandResponseRankedByVRH(datastatForDemandResponseRankedByVRH)
        else:
            df = statisticsForDemandResponseRankedByVRM(datastatForDemandResponseRankedByVRM)
        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('statisticsRankedByAgencies-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value'),
                        Input('stat-dropdown-upt', 'value')]
                       )
    def statRankedByAgencies(state, agency, statdropdown):
        if statdropdown == "ridership":
            df = statisticsForAgenciesRankedByRidership(dataStatforAgenciesRankedByRidership)
        elif statdropdown == "vrh":
            df = statisticsForAgenciesRankedByVRH(dataStatforAgenciesRankedByVRH)
        else:
            df = statisticsForAgenciesRankedByVRM(dataStatforAgenciesRankedByVRM)

        fig = ff.create_table(df)
        return fig

    @dash_app.callback(Output('number-replaced', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('vehicle-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def update_replaced(state, vehicle, agency):
        df = generate_stats(data2, 2021, 2032, state, vehicle, agency)

        colors = ['#bababa', ] * (len(df))
        colors[0] = '#ffcc00'

        layout = go.Layout(title='Number of Revenue Vehicles Replaced',
                           xaxis=dict(title='Year',
                                      type='category'),
                           yaxis=dict(title='Number of Revenue Vehicles Replaced'),
                           font_color="black",
                           title_font_color="black",
                           legend_title_font_color="black",
                           margin=dict(l=100, r=50, t=150, b=50),
                           height=550,
                           hovermode='x',
                           autosize=True,
                           template='simple_white'
                           )

        fig = go.Figure(data=[go.Bar(
            x=list(df.projected_retired_year.astype('str')),
            y=df.active_fleet_vehicles,
            marker_color=colors,  # marker color can be a single color value or an iterable
            text=df.active_fleet_vehicles,
            textposition='auto',
        )], layout=layout)

        fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        return fig

    @dash_app.callback(Output('replacement-cost', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('vehicle-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def update_replacement_cost(state, vehicle, agency):
        df = replacement_cost(data2, 2021, 2032, state, vehicle, agency)

        colors = ['#bababa', ] * (len(df))
        colors[0] = '#ffcc00'

        layout = go.Layout(title='Backlog and Replacement Cost (Million)',
                           xaxis=dict(title='Year',
                                      type='category'),
                           yaxis=dict(title='Revenue Vehicles Replacement Cost (Million)',
                                      tickprefix='$'),
                           font_color="black",
                           title_font_color="black",
                           legend_title_font_color="black",
                           margin=dict(l=100, r=50, t=150, b=50),
                           height=550,
                           hovermode='x',
                           autosize=True,
                           template='simple_white')

        fig = go.Figure(data=[go.Bar(
            x=list(df.projected_retired_year.astype('str')),
            y=df.total_fleet_cost,
            marker_color=colors,
            text=df.total_fleet_cost,  # marker color can be a single color value or an iterable,
            textposition='auto',
        )], layout=layout)

        fig.update_traces(texttemplate='$%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

        return fig

    @dash_app.callback(Output('backlog-vehicles', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def update_backlog(state, agency):
        df = backlog(data2, state, agency)

        fig = px.bar(df, x='vehicle_type', y='count', color='vehicle_type', text='count',
                     title='Backlog by Vehicle Type',
                     color_discrete_map=vehicle_colors,
                     labels={"vehicle_type": "Vehicle Type",
                             "count": "Number of Revenue Vehicles (Backlog)"
                             },
                     template='simple_white'
                     )

        fig.update_traces(textposition='outside')
        fig.update_layout(
            font_color="black",
            title_font_color="black",
            legend_title_font_color="black",
            margin=dict(l=100, r=50, t=150, b=50),
            height=600,
            hovermode='x',
            autosize=True
        )

        return fig

    @dash_app.callback(Output('backlog-cost-vehicles', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def update_backlog_cost(state, agency):
        df = backlog_cost(data2, state, agency)

        fig = px.bar(df, x='vehicle_type', y='total_fleet_cost', text='total_fleet_cost',
                     title='Backlog Cost by Vehicle Type',
                     color='vehicle_type',
                     color_discrete_map=vehicle_colors,
                     labels={
                         "vehicle_type": "Vehicle Type",
                         "total_fleet_cost": "Backlog (Million)"
                     },
                     template='simple_white'
                     )

        fig.update_traces(texttemplate='$%{text:.2s}', textposition='outside')
        fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
        fig.update_layout(
            font_color="black",
            title_font_color="black",
            legend_title_font_color="black",
            margin=dict(l=100, r=50, t=150, b=50),
            height=600,
            hovermode='x',
            autosize=True
        )

        return fig

    @dash_app.callback(Output('tabs-example-content', 'children'),
                       [Input('tabs-example', 'value')])
    def render_content(tab):
        if tab == 'tab-1':
            return html.Div([
                html.H3('Tab content 1')
            ])
        elif tab == 'tab-2':
            return html.Div([
                html.H3('Tab content 2')
            ])
