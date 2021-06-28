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
    statisticsForFixedRouteRankedByRidership, statVehiclesByMode, statFleetByMode, statAdaAccessible, statVehicleAge

from .data import init_data


def init_callbacks(dash_app):
    # callbacks
    data1, data2, data3, dataVehiclesByMode, dataFleetByMode,\
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
        Output('agency-dropdown', 'value'),
        [Input('agency-dropdown', 'options')])
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

    @dash_app.callback(Output('vehicle-revenue-miles', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrm(state, agency):
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
		
    @dash_app.callback(Output('vehicle-revenue-miles-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrm(state, agency):
        df = vehicle_revenue_miles(data3, state, agency)
        df_sample = df[['mode', 'vehicle_revenue_miles']]
        fig = ff.create_table(df_sample)
        return fig

    @dash_app.callback(Output('vehicle-revenue-hours', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrh(state, agency):
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
        return fig

    @dash_app.callback(Output('vehicle-revenue-hours-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrh(state, agency):
        df = vehicle_revenue_hours(data3, state, agency)
        df_sample = df[['mode', 'vehicle_revenue_hours']]
        fig = ff.create_table(df_sample)
        return fig

    @dash_app.callback(Output('unlinked_passenger_trips', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
    def vrh(state, agency):
        df = unlinked_passenger_trips(data3, state, agency)
        fig = px.bar(df, x='mode', y='unlinked_passenger_trips', text='unlinked_passenger_trips',
                     color='mode',
                     color_discrete_map=mode_colors, title='Vehicle Revenue Hours',
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

    @dash_app.callback(Output('unlinked_passenger_trips-table', 'figure'),
                       [Input('state-selector', 'value'),
                        Input('agency-dropdown', 'value')])
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
