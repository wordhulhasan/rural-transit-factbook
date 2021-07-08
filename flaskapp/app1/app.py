import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

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
        'padding-top': '40px',
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

    tab_style_sub = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold',
        'color': 'blue',
        'backgroundColor': '#969696',
        'height':'40px',
        'width': '130px',
    }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#000000',
        'color': 'white',
        'padding': '6px',
        'fontWeight': 'bold'
    }


    tab_selected_style_sub = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#000000',
        'color': 'white',
        'padding': '6px',
        'fontWeight': 'bold',
        'height':'40px',
        'width': '130px',
    }

    res = make_state_agency_dict()

    dash_app.layout = html.Div(
        children=[
            dbc.Nav(
                children=[
                    # dbc.Label("NDSU Upper Great Plains Transportation Institute",
                    #           style={"color": "white"}),
                    dbc.NavLink("NDSU Upper Great Plains Transportation Institute   |    Small Urban and Rural Transit Center on Mobility", href="/",
                                style={"align": "center", "color": "white"}),
                ],
                style={"background-color": "#006400", "padding": "20px"}

            ),
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
                                                style={'padding': '8px 65px'},
                                                href='/')
                                     ],
                                     style={'padding-left': '47px'}
                                     ),
                            dcc.Tabs([
                                dcc.Tab(
                                    label='Rural Fleet Information',
                                    style=tab_style,
                                    selected_style=tab_selected_style,

                                    children=[
                                        html.Br(),
                                        html.H2(
                                            'Small Urban & Rural Transit Systems Revenue Vehicles Fleet Information Reports'),
                                        html.P(
                                            '',
                                            style=paragraph_styles),
                                        html.Br(),

                                        html.H3('State'),
                                        dcc.Dropdown(
                                            id='state-selector',
                                            options=[{'label': states_dict[k], 'value': k} for k in res.keys()],
                                            value='All',
                                            placeholder='Select a state...',
                                            style = {'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
                                        ),
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
                                            ''),
                                        html.P(
                                            '',
                                            style=paragraph_styles),
                                        html.Br(),
                                        dcc.Tabs([
                                            dcc.Tab(
                                                label='Operating Statistics in 2019',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.Br(),
                                                    dcc.Tabs([
                                                        dcc.Tab(
                                                            label=' Chart ',
                                                            style=tab_style_sub,
                                                            selected_style=tab_selected_style_sub,
                                                            children=[
                                                                #                                                   html.H2(
                                                                #                                                        ''),
                                                                #                                                    html.P(
                                                                #                                                        'Source: National Transit Database, 2019',
                                                                #                                                        style=paragraph_styles),
                                                                html.Br(),
                                                                html.H3('State'),
                                                                dcc.Dropdown(
                                                                    id='state-selector-2',
                                                                    options=[{'label': states_dict[k], 'value': k} for k
                                                                             in
                                                                             res.keys()],
                                                                    value='All',
                                                                    placeholder='Select a state...',
                                                                    style={'width': '60%', 'margin': '0 0 0',
                                                                           'padding-left': '100px'}
                                                                ),
                                                                html.H3('Transit Agency'),
                                                                dcc.Dropdown(
                                                                    id='agency-dropdown-2',
                                                                    placeholder='Select a transit agency...',
                                                                    style={'width': '60%', 'margin': '0 0 0',
                                                                           'padding-left': '100px'}
                                                                ),
                                                                html.H3('Performance Measure'),
                                                                dcc.Dropdown(
                                                                    id='op-stat-dropdown',
                                                                    options=[
                                                                        {
                                                                            'label': 'Vehicle Revenue Miles',
                                                                            'value': 'vrm'},
                                                                        {
                                                                            'label': 'Vehicle Revenue Hours',
                                                                            'value': 'vrh'},
                                                                        {
                                                                            'label': 'Unlinked Passenger Trips',
                                                                            'value': 'utp'}
                                                                    ],
                                                                    value='ridership',
                                                                    style={'width': '60%', 'margin': '0 0 0',
                                                                           'padding-left': '100px'}
                                                                ),
                                                                html.Br(),

                                                                dcc.Graph(
                                                                    id='op-stat'),
                                                                # dcc.Graph(
                                                                #     id='vehicle-revenue-hours'),
                                                                # dcc.Graph(
                                                                #     id='unlinked_passenger_trips'),
                                                            ]
                                                        ),
                                                        dcc.Tab(
                                                            label=' Table ',
                                                            style=tab_style_sub,
                                                            selected_style=tab_selected_style_sub,
                                                            children=[
                                                                #                                                    html.H2(
                                                                #                                                        ''),
                                                                #                                                    html.P(
                                                                #                                                        'Source: National Transit Database, 2019',
                                                                #                                                        style=paragraph_styles),
                                                                html.Br(),
                                                                html.H3('State'),
                                                                dcc.Dropdown(
                                                                    id='state-selector-3',
                                                                    options=[{'label': states_dict[k], 'value': k} for k
                                                                             in
                                                                             res.keys()],
                                                                    value='All',
                                                                    placeholder='Select a state...',
                                                                    style={'width': '60%', 'margin': '0 0 0',
                                                                           'padding-left': '100px'}
                                                                ),
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
                                                    ], style=tabs_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label=' Rural Transit Operating Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id = 'operating-stat-dropdown-ridership',
                                                        options=[
                                                            {
                                                                'label':'Ridership (millions)',
                                                                'value':'ridership'},
                                                            {'label':'Vehicle Revenue Miles (millions)',
                                                             'value':'vrm'},
                                                            {'label':'Vehicle Revenue Hours (millions)',
                                                             'value':'vrh'}
                                                        ],
                                                        value='ridership',
                                                        style={'width':'60%', 'margin':'0 0 0', 'padding-left':'100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='ridership_by_year-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label=' Operating Statistics Percentile Rankings',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
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
                                            ''),
                                        html.P(
                                            '',
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
                                                    dcc.Graph(
                                                        id='vehicleOwnership-table'),
                                                    html.Br(),
                                                    html.P(
                                                        'Note:',
                                                        style=paragraph_styles),
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
                                        html.P(
                                            '',
                                            style=paragraph_styles),
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
                                dcc.Tab(
                                    label=' State Statistics ',
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
                                                label='Operating Statistics by State',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Ridership', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridershipByState-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Miles',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrmByState-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Hours',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrhByState-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Rural Transit Ridership by State',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Total (million trips)', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridershipTotalYearlyByState-table'),
                                                    html.Br(),
                                                    html.P('Fixed-Route Service (million trips)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridershipFRYearlyByState-table'),
                                                    html.Br(),
                                                    html.P('Demand-Response Service (million trips)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridershipDRYearlyByState-table'),
                                                    html.Br(),
                                                    html.P('Other Service (million trips)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridershipOtherYearlyByState-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Rural Transit Vehicle Revenue Miles of Service by State',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Total (million miles)', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrmTotalYearlyByState-table'),
                                                    html.Br(),
                                                    html.P('Fixed-Route Service (million miles)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrmFrsYearlyByState-table'),
                                                    html.Br(),
                                                    html.P('Demand-Response Service (million miles)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrmDrsYearlyByState-table'),
                                                    html.Br(),
                                                    html.P('Other Service (million trips)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrmOtherYearlyByState-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='State Financial Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Funds Expended on Operations by Source', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='financialOnOperationsByState-table'),
                                                    html.Br(),
                                                    html.P('Funds Expended on Capital by Source',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='financialOnCapitalByState-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='State Fleet Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='fleetStatisticsByState-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='State Performance Measures, Averages',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='performanceMeasuresByState-table'),
                                                    html.Br(),
                                                    html.P('Note:',style=paragraph_styles),
                                                    html.P('VRM - Vehicle Revenue Mile,VRH - Vehicle Revenue Hour, FR - Fixed-Route, DR - Demand-Response, OE - Operating Expense',
                                                           style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='State Performance Measures, Median Agency Values',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='performanceMeasuresMedianByState-table'),
                                                    html.Br(),
                                                    html.P('Note:', style=paragraph_styles),
                                                    html.P(
                                                        'VRM - Vehicle Revenue Mile,VRH - Vehicle Revenue Hour, FR - Fixed-Route, DR - Demand-Response, OE - Operating Expense',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Transit Agency Percentiles for Operating Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Ridership Percentile',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='agencyPercentileRidershipByState-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Miles Percentile',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='agencyPercentileVrmByState-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Hours Percentile',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='agencyPercentileVrhByState-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                        ], style=tabs_styles),

                                    ]
                                ),
                                dcc.Tab(
                                    label=' Tribal Transit Statistics ',
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
                                                label='Tribal Transit Operating Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Ridership (thousand rides)', style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='ridershipYearlyByTribal-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Miles (thousand miles)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrmYearlyByTribal-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Hours (thousand hours)',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrhYearlyByTribal-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Tribal Transit Vehicles Information',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='vehiclesByTribal-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Tribal Transit Fleet Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='fleetStatisticsByTribal-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Operating Statistics by Vehicle Mode',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Trips per Vehicle',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='tripsPerVehicleByTribal-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Miles per Vehicle',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrmPerVehicleByTribal-table'),
                                                    html.Br(),
                                                    html.P('Vehicle Revenue Hours per Vehicle',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='vrhPerVehicleByTribal-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Tribal Transit Performance Measures',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    html.P('Trips per Vehicle Revenue Mile',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='tripsPerVrmByTribal-table'),
                                                    html.Br(),
                                                    html.P('Trips per Vehicle Revenue Hour',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='tripsPerVrhByTribal-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense Per Trip',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingExpensePerTripByTribal-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense per Vehicle Revenue Mile',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingExpensePerVrmByTribal-table'),
                                                    html.Br(),
                                                    html.P('Operating Expense per Vehicle Revenue Hour',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='operatingExpensePerVrhByTribal-table'),
                                                    html.Br(),
                                                    html.P('Farebox Recovery Ratio',
                                                           style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='fareboxRecoveryRatioByTribal-table'),
                                                    html.Br(),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Tribal Transit Performance Measures, Median Agency Values',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='performanceMeasureMedianByTribal-table'),
                                                    html.Br(),
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
