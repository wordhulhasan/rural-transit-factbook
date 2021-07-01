import dash
import dash_html_components as html
import dash_core_components as dcc

from util import states_dict, vehicles_dict, make_state_agency_dict


def init_dashboard(server):
    """Create a Plotly Dash dashboard."""
    external_stylesheets = ['https://www.w3schools.com/w3css/4/w3.css']
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=external_stylesheets
    )

    dash_app.config.suppress_callback_exceptions = True

    paragraph_styles = {
        'text-indent': '30px',
        'font-size': '16px'
    }

    tabs_styles = {
        'height': '65px',
    }

    tabs_styles_main = {
        'height': '44px',
        'borderBottom': '50px',
        'padding-top': '100px',
        'padding-left': '50px',
        'padding-right': '50px',
        'fontWeight': 'bold',
        'backgroundColor': '#FFFFFF',
        "margin-bottom": "20px"
    }

    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold',
        'color': 'black',
        'backgroundColor': '#969696'
    }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#000000',
        'color': 'white',
        'padding': '6px',
        'fontWeight': 'bold'
    }

    res = make_state_agency_dict()

    dash_app.layout = html.Div(
        children=[
            html.Div(
                className='row',
                children=[
                    html.Div(
                        className='nine columns div-for-charts bg-grey',
                        children=[
                            html.Br(),
                            html.Div(className='w3-xlarge w3-left',
                                     children=[
                                         html.A('Home',
                                                className="w3-button w3-grey w3-round-xlarge w3-center",
                                                id='submit-val',
                                                href='/')
                                     ],
                                     style={'padding-left': '105px'}
                                     ),
                            dcc.Tabs([
                                dcc.Tab(
                                    label='Revenue Vehicles Statistics',
                                    style=tab_style,
                                    selected_style=tab_selected_style,

                                    children=[
                                        html.H2(
                                            'Small Urban & Rural Transit Systems Revenue Vehicles Fleet Information Reports'),
                                        html.P(
                                            'Reports are generated from National Transit Database (NTD) data based on 2019 reporting year, the most current data.',
                                            style=paragraph_styles),
                                        html.Br(),

                                        html.Hr(),
                                        html.H3('State'),
                                        dcc.Dropdown(
                                            id='state-selector',
                                            options=[{'label': states_dict[k], 'value': k} for k in res.keys()],
                                            value='All',
                                            placeholder='Select a state...',
                                            style = {'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
                                        ),
                                        html.Hr(),
                                        html.H3('Transit Agency'),
                                        dcc.Dropdown(
                                            id='agency-dropdown',
                                            placeholder='Select a transit agency...',
                                            style={'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
                                        ),

                                        dcc.Graph(id='revenue-vehicles', config={'displayModeBar': False},
                                                  animate=True),
                                        dcc.Graph(id='fleet-composition')
                                    ]
                                ),
                                dcc.Tab(
                                    label=' Operating Statistics ',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.H2(
                                            'Operating Statistics of Rural Transit Systems'),
                                        html.P(
                                            'Source: National Transit Database',
                                            style=paragraph_styles),
                                        html.Br(),
                                        dcc.Tabs([
                                            dcc.Tab(
                                                label=' Operating Statistics in 2019 (Chart) ',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.H2(
                                                        ''),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    html.Hr(),
                                                    html.H3('State'),
                                                    dcc.Dropdown(
                                                        id='state-selector-2',
                                                        options=[{'label': states_dict[k], 'value': k} for k in
                                                                 res.keys()],
                                                        value='All',
                                                        placeholder='Select a state...',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Hr(),
                                                    html.H3('Transit Agency'),
                                                    dcc.Dropdown(
                                                        id='agency-dropdown-2',
                                                        placeholder='Select a transit agency...',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    dcc.Graph(
                                                        id='vehicle-revenue-miles'),
                                                    dcc.Graph(
                                                        id='vehicle-revenue-hours'),
                                                    dcc.Graph(
                                                        id='unlinked_passenger_trips'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label=' Operating Statistics in 2019 (Table)',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.H2(
                                                        ''),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    html.Hr(),
                                                    html.H3('State'),
                                                    dcc.Dropdown(
                                                        id='state-selector-3',
                                                        options=[{'label': states_dict[k], 'value': k} for k in
                                                                 res.keys()],
                                                        value='All',
                                                        placeholder='Select a state...',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Hr(),
                                                    html.H3('Transit Agency'),
                                                    dcc.Dropdown(
                                                        id='agency-dropdown-3',
                                                        placeholder='Select a transit agency...',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.P(
                                                        'Ridership',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='unlinked_passenger_trips-table'),
                                                    html.P(
                                                        'Vehicle Revenue Miles',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vehicle-revenue-miles-table'),
                                                    html.Br(),
                                                    html.Br(),
                                                    html.P(
                                                        'Vehicle Revenue Hours',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vehicle-revenue-hours-table'),
                                                    html.Br(),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label=' Rural Transit Operating Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.H2(
                                                        ''),
                                                    html.P(
                                                        'Source: National Transit Database, 2015–2019',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    html.P(
                                                        'Ridership (millions)',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridership_by_year-table'),
                                                    html.Br(),
                                                    html.Br(),
                                                    html.P(
                                                        'Vehicle Revenue Miles (millions)',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrm_by_year-table'),
                                                    html.Br(),
                                                    html.Br(),
                                                    html.P(
                                                        'Vehicle Revenue Hours (millions)',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrh_by_year-table')
                                                ]
                                            ),
                                            dcc.Tab(
                                                label=' Operating Statistics Percentile Rankings',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.H2(
                                                        ''),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    html.P(
                                                        'Ridership Percentile Rankings for Rural Transit Agencies',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridership_by_rank-table'),
                                                    html.Br(),
#                                                    html.Br(),
                                                    html.P(
                                                        'Vehicle Miles Percentile Rankings for Rural Transit Agencies',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrm_by_rank-table'),
                                                    html.Br(),
#                                                    html.Br(),
                                                    html.P(
                                                        'Vehicle Hours Percentile Rankings for Rural Transit Agencies',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrh_by_rank-table')
                                                ]
                                            ),
                                        ], style=tabs_styles),
                                    ]
                                ),
                                dcc.Tab(
                                    label=' Fleet Statistics ',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.H2(
                                            'Key Statistics on Small Urban & Rural Transit Vehicles'),
                                        html.P(
                                            'Source: National Transit Database',
                                            style=paragraph_styles),
                                        html.Br(),
                                        dcc.Tabs([
                                            dcc.Tab(
                                                label='Vehicles by Mode',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='vehicle_by_mode-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Fleet Size by Mode',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='fleet_by_mode-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='ADA Accessible in %',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='adaAccessible-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Avg. Vehicle Age',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='vehicleAge-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Avg. Vehicle Length',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='vehicleLenght-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Avg. Seating Capacity',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='seatingCapacity-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Vehicle Ownership',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P(
                                                        'OOPA - Owned Outright by a Public Agency',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'OOPE - Owned Outright by a Private Entity',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'TLPA - True Lease by a Public Agency',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'LRPA - Leased or Borrowed from Related Parties by a Public Agency',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'TLPE - True Lease by a Private Entity',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'LPPA - Lease under Lease Purchase Agreement by a Public Agency ',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'LRPE - Leased or Borrowed from Related Parties by a Private Entity',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='vehicleOwnership-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Funding Source',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='fundingSource-table'),
                                                ]
                                            ),
                                        ], style=tabs_styles),

                                    ]
                                ),
                                dcc.Tab(
                                    label=' Performance Measures ',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.H2(
                                            ''),
                                        html.P(
                                            '',
                                            style=paragraph_styles),
                                        html.Br(),
                                        dcc.Tabs([
                                            dcc.Tab(
                                                label='Trips per Vehicle Revenue Mile',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='tripsPerMile-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Trips per Vehicle Revenue Hour',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='tripsPerHour-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Trips, Miles, and Hours per Vehicle',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='tripsMilesHoursPerVehicle-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Key Performance Measures by Year',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Operating Expense per Trip',style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingExpensePerTrip-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense per Vehicle Mile', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingExpensePerVehicleMile-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense per Vehicle Hour',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingExpensePerVehicleHour-table'),
                                                    html.Br(),
                                                    html.P('Farebox Recovery Ratio',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='fareboxRecoveryRatio-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Performance Measures Percentiles',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Total', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='percentileTotal-table'),
                                                    html.Br(),
                                                    html.P('Fixed-route',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='percentileFixedRoute-table'),
                                                    html.Br(),
                                                    html.P('Demand-response',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='percentileDemandResponse-table'),
                                                    html.Br(),
                                                    html.P('Note:',
                                                           style=paragraph_styles),
                                                    html.P('OE - Operating Expense, VRM - Vehicle Revenue Mile, VRH - Vehicle Revenue Hour, UPT - Unlinked Passenger Trips',
                                                           style=paragraph_styles),

                                                ]
                                            ),
                                        ], style=tabs_styles),

                                    ]
                                ),
                                dcc.Tab(
                                    label=' Percentile Rank',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.H3(
                                            ''),
                                        html.Br(),
                                        html.Br(),

                                        dcc.Tabs([
                                            dcc.Tab(
                                                label='Statistics For Agencies',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='stat-dropdown-upt',
                                                        options=[
                                                            {
                                                                'label': 'Ranked by Ridership',
                                                                'value': 'ridership'},
                                                            {
                                                                'label': 'Ranked by Vehicle Revenue Hours',
                                                                'value': 'vrh'},
                                                            {
                                                                'label': 'Ranked by Vehicle Revenue Miles',
                                                                'value': 'vrm'}
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='statisticsRankedByAgencies-table'),
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'Note: VRH - Vehicle Revenue Hours, VRM - Vehicle Revenue Miles, UPT - Unlinked Passenger Trips, OE - Operating Expenses',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Statistics For Fixed Route Service',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='stat-dropdown-vrm',
                                                        options=[
                                                            {
                                                                'label': 'Ranked by Ridership',
                                                                'value': 'ridership'},
                                                            {
                                                                'label': 'Ranked by Vehicle Revenue Hours',
                                                                'value': 'vrh'},
                                                            {
                                                                'label': 'Ranked by Vehicle Revenue Miles',
                                                                'value': 'vrm'}
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='statisticsRankedByMB-table'),
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'Note: VRH - Vehicle Revenue Hours, VRM - Vehicle Revenue Miles, UPT - Unlinked Passenger Trips, OE - Operating Expenses',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Statistics For Demand Response Service',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='stat-dropdown-vrh',
                                                        options=[
                                                            {
                                                                'label': 'Ranked by Ridership',
                                                                'value': 'ridership'},
                                                            {
                                                                'label': 'Ranked by Vehicle Revenue Hours',
                                                                'value': 'vrh'},
                                                            {
                                                                'label': 'Ranked by Vehicle Revenue Miles',
                                                                'value': 'vrm'}
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),

                                                    dcc.Graph(
                                                        id='statisticsRankedByDemandResponse-table'),
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'Note: VRH - Vehicle Revenue Hours, VRM - Vehicle Revenue Miles, UPT - Unlinked Passenger Trips, OE - Operating Expenses',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                        ], style=tabs_styles),
                                    ]
                                ),
                                dcc.Tab(
                                    label=' Regional Statistics ',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.H2(
                                            ''),
                                        html.P(
                                            '',
                                            style=paragraph_styles),
                                        html.Br(),
                                        dcc.Tabs([
                                            dcc.Tab(
                                                label='Transit Agencies by Region',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='agenciesByRegion-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Fleet Statistics by Region',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='vehiclesByRegion-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Operating Statistics by Region',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Ridership', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridershipByRegion-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Miles',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                       id='vrmByRegion-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Hours',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrhByRegion-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Performance Measures by Region',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Key Performance Measures', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='performanceByRegion-table'),
                                                    html.Br(),
                                                    html.P('Trips per Vehicle Revenue Miles',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='tripsPerVRMByRegion-table'),
                                                    html.Br(),
                                                    html.P('Trips per Vehicle Revenue Hours',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='tripsPerVRHByRegion-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense per Trip',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingPerTripByRegion-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense per Vehicle Revenue Miles',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingPerVRMByRegion-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense per Vehicle Revenue Hours',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingPerVRHByRegion-table'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Median Agency Performance Measures',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='agencyPerformanceByRegion-table'),
                                                    html.Br(),
                                                    html.P('Note: VRM = Vehicle Revenue Miles, VRH = Vehicle Revenue Hours',
                                                           style=paragraph_styles),
                                                ]
                                            ),
                                        ], style=tabs_styles),

                                    ]
                                ),
                            ],
                                vertical=True,
                                style=tabs_styles_main),
                        ],
                    )
                ]
            )
        ]
    )
    return dash_app
