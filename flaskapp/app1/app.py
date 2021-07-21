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
        'font-size': '.9em'
    }

    tabs_styles_main = {
        'height': '44px',
        'borderBottom': '50px',
        'padding-top': '40px',
        'padding-left': '50px',
        'padding-right': '50px',
        'fontWeight': 'bold',
        'backgroundColor': '#FFFFFF',
        "margin-bottom": "20px",
        'font-size': '.9em'
    }

    tab_style = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold',
        'color': 'black',
        'backgroundColor': '#969696',
        'font-size': '.9em'
    }

    tab_style_sub = {
        'borderBottom': '1px solid #d6d6d6',
        'padding': '6px',
        'fontWeight': 'bold',
        'color': 'blue',
        'backgroundColor': '#969696',
        'height': '40px',
        'width': '260px',
    }

    tab_selected_style = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#000000',
        'color': 'white',
        'padding': '6px',
        'fontWeight': 'bold',
        'font-size': '.9em'
    }

    tab_selected_style_sub = {
        'borderTop': '1px solid #d6d6d6',
        'borderBottom': '1px solid #d6d6d6',
        'backgroundColor': '#000000',
        'color': 'white',
        'padding': '6px',
        'fontWeight': 'bold',
        'height': '40px',
        'width': '260px',
    }

    res = make_state_agency_dict()

    dash_app.layout = html.Div(
        children=[
            dbc.Nav(
                children=[
                    # dbc.Label("NDSU Upper Great Plains Transportation Institute",
                    #           style={"color": "white"}),
                    dbc.NavLink(
                        "NDSU Upper Great Plains Transportation Institute   |    Small Urban and Rural Transit Center on Mobility (SURCOM)",
                        href="/",
                        style={"align": "center", "color": "white"}),
                    html.A('Home',
                        className="w3-button w3-grey w3-round-xlarge w3-center",
                        id='submit-val',
                        style={'padding': '8px 65px','float':'right'},
                        href="/",
                    )
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
                            # html.Div(className='w3-xlarge w3-left',
                            #          children=[
                            #              html.A('Home',
                            #                     className="w3-button w3-grey w3-round-xlarge w3-center",
                            #                     id='submit-val',
                            #                     style={'padding': '8px 65px'},
                            #                     href='/')
                            #          ],
                            #          style={'padding-left': '47px'}
                            #          ),
                            dcc.Tabs([
#                                dcc.Tab(
#                                    label='National Rural Transit Fleet Information',
##                                    style=tab_style,
#                                    selected_style=tab_selected_style,
#                                    children=[
#                                        html.Br(),
##                                        html.H2(
##                                            'Small Urban & Rural Transit Systems Revenue Vehicles Fleet Information Reports'),
#                                        html.P(
#                                            '',
#                                            style=paragraph_styles),
#                                        html.Br(),
#                                        html.H3('State'),
#                                        dcc.Dropdown(
#                                            id='state-selector',
#                                            options=[{'label': states_dict[k], 'value': k} for k in res.keys()],
#                                            value='All',
#                                            placeholder='Select a state...',
#                                            style = {'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
#                                        ),
#                                        html.H3('Transit Agency'),
#                                        dcc.Dropdown(
#                                            id='agency-dropdown',
#                                            placeholder='Select a transit agency...',
#                                            style={'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
#                                        ),
#                                        dcc.Graph(id='revenue-vehicles', config={'displayModeBar': False},
#                                                  animate=True),
#                                        dcc.Graph(id='fleet-composition')
#                                    ]
#                                ),
                                dcc.Tab(
                                    label='National Rural Transit Fleet Information',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.Br(),
                                        html.Br(),
                                        html.H3('State'),
                                        dcc.Dropdown(
                                            id='state-selector',
                                            options=[{'label': states_dict[k], 'value': k} for k in res.keys()],
                                            value='All',
                                            placeholder='Select a state...',
                                            style={'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
                                        ),
                                        html.H3('Transit Agency'),
                                        dcc.Dropdown(
                                            id='agency-dropdown',
                                            placeholder='Select a transit agency...',
                                            style={'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
                                        ),
                                        html.Br(),
                                        dcc.Graph(id='revenue-vehicles', config={'displayModeBar': False},
                                                  animate=True),
                                    ]
                                ),
                                dcc.Tab(
                                    label=' Rural Transit Financial Statistics',
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
                                                label='Rural Transit Financial Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='source-of-funding-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Capital Funding',
                                                                'value': 'capital'},
                                                            {
                                                                'label': 'Operating Funding',
                                                                'value': 'operating'}
                                                        ],
                                                        value='capital',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='source_of_funding-table'),
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2015-2019',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                        ], style=tabs_styles),
                                    ]
                                ),
                                dcc.Tab(
                                    label=' Rural Transit Operating Statistics ',
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
                                                label='Operating Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
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
                                                               'padding-left': '100px'},
                                                    ),
                                                    html.Br(),
                                                    html.Br(),
                                                    dcc.Tabs([
                                                        dcc.Tab(
                                                            label=' Chart ',
                                                            style=tab_style_sub,
                                                            selected_style=tab_selected_style_sub,
                                                            children=[
                                                                html.Br(),

                                                                dcc.Graph(
                                                                    id='op-stat'),
                                                            ]
                                                        ),
                                                        dcc.Tab(
                                                            label=' Table ',
                                                            style=tab_style_sub,
                                                            selected_style=tab_selected_style_sub,
                                                            children=[
                                                                html.Br(),
                                                                dcc.Graph(
                                                                    id='op-stat-table'),
                                                                # html.P(
                                                                #     'Vehicle Revenue Miles',
                                                                #     style=paragraph_styles),
                                                                # dcc.Graph(
                                                                #     id='vehicle-revenue-miles-table'),
                                                                # html.Br(),
                                                                # html.Br(),
                                                                # html.P(
                                                                #     'Vehicle Revenue Hours',
                                                                #     style=paragraph_styles),
                                                                # dcc.Graph(
                                                                #     id='vehicle-revenue-hours-table'),
                                                                # html.Br(),
                                                                # html.Br(),
                                                            ]
                                                        ),
                                                    ], style=tabs_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Operating Statistics (Yearly)',
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label=' Operating Statistics Percentile Rankings',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                        html.Br(),
                                        dcc.Dropdown(
                                            id='operating-stat-per-rank-dropdown',
                                            options=[
                                                {
                                                    'label': 'Ridership Percentile Rankings for Rural Transit Agencies',
                                                    'value': 'ridership'},
                                                {
                                                    'label': 'Vehicle Miles Percentile Rankings for Rural Transit Agencies',
                                                    'value': 'vrm'},
                                                {
                                                    'label': 'Vehicle Hours Percentile Rankings for Rural Transit Agencies',
                                                    'value': 'vrh'}
                                            ],
                                            value='ridership',
                                            style={'width': '60%', 'margin': '0 0 0', 'padding-left': '100px'}
                                        ),
                                        html.Br(),
                                        dcc.Graph(
                                            id='ridership_by_rank-table'
                                        ),
                                        html.Br(),
                                        html.P(
                                            'Source: National Transit Database, 2019',
                                            style=paragraph_styles),
                                    ]
                                            ),
                                      ], style=tabs_styles),
                                 ]
                               ),
                                dcc.Tab(
                                    label=' Rural Transit Fleet Statistics ',
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    html.P(
                                                        'Note:',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'RAFP - Rural Area Formula Program',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'EMSID - Enhanced Mobility of Seniors & Individuals with Disabilities',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'OFF - Other Federal Funds',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'NFPF - Non-Federal Public Funds',
                                                        style=paragraph_styles),
                                                    html.P(
                                                        'NFPRF - Non-Federal Private Funds',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                        ], style=tabs_styles),

                                    ]
                                ),
                                dcc.Tab(
                                    label=' Rural Transit Performance Measures ',
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2015-2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2015-2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Key Performance Measures by Year',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='kpm-by-year-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Operating Expense per Trip',
                                                                'value': 'operating_trip'},
                                                            {
                                                                'label': 'Operating Expense per Vehicle Mile',
                                                                'value': 'operating_mile'},
                                                            {
                                                                'label': 'Operating Expense per Vehicle Hour',
                                                                'value': 'operating_hour'},
                                                            {
                                                                'label': 'Farebox Recovery Ratio',
                                                                'value': 'frr'}
                                                        ],
                                                        value='operating_trip',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='kpm-by-year-table'),
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2016-2019',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Performance Measures Percentiles',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='performance-percentile-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Total',
                                                                'value': 'total'},
                                                            {
                                                                'label': 'Fixed-route',
                                                                'value': 'fr'},
                                                            {
                                                                'label': 'Demand-response',
                                                                'value': 'dr'},
                                                        ],
                                                        value='total',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='performance-percentile-table'),
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    html.P('Note:',
                                                           style=paragraph_styles),
                                                    html.P(
                                                        'OE - Operating Expense, VRM - Vehicle Revenue Mile, VRH - Vehicle Revenue Hour, UPT - Unlinked Passenger Trips',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                        ], style=tabs_styles),

                                    ]
                                ),
                                dcc.Tab(
                                    label=' Rural Transit Percentile Rank',
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
                                                        'Note: VRH - Vehicle Revenue Hours, VRM - Vehicle Revenue Miles, UPT - Unlinked Passenger Trips, OE - Operating Expenses, Avg-Average',
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
                                    label=' Rural Transit Regional Statistics ',
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
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
                                                    html.Br(),
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Operating Statistics by Region',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='region-operating-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Ridership',
                                                                'value': 'ridership'},
                                                            {
                                                                'label': 'Vehicle Revenue Miles',
                                                                'value': 'vrm'},
                                                            {
                                                                'label': 'Vehicle Revenue Hours',
                                                                'value': 'vrh'},
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='region-operating-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2019',
                                                           style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Performance Measures by Region',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='region-performance-measures-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Key Performance Measures',
                                                                'value': 'kpm'},
                                                            {
                                                                'label': 'Trips per Vehicle Revenue Miles',
                                                                'value': 'trip_vrm'},
                                                            {
                                                                'label': 'Trips per Vehicle Revenue Hours',
                                                                'value': 'trips_vrh'},
                                                            {
                                                                'label': 'Operating Expense per Trip',
                                                                'value': 'oe_trip'},
                                                            {
                                                                'label': 'Operating Expense per Vehicle Revenue Miles',
                                                                'value': 'oe_vrm'},
                                                            {
                                                                'label': 'Operating Expense per Vehicle Revenue Hours',
                                                                'value': 'oe_vrh'},
                                                        ],
                                                        value='kpm',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='region-performance-measures-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2019',
                                                           style=paragraph_styles),
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
                                                    html.P(
                                                        'Source: National Transit Database, 2019',
                                                        style=paragraph_styles),
                                                    html.P('Note: VRM - Vehicle Revenue Miles, VRH - Vehicle Revenue Hours, OE - Operating Expense, FRR - Farebox Recovery Ratio',
                                                           style=paragraph_styles),
                                                ]
                                            ),
                                        ], style=tabs_styles),

                                    ]
                                ),
                                dcc.Tab(
                                    label=' Rural Transit State Statistics ',
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
                                                    dcc.Dropdown(
                                                        id='operating-statistics-dropdown',
                                                        options=[
                                                            {
                                                                'label':'Ridership',
                                                                'value':'ridership'},
                                                            {
                                                                'label': 'Vehicle Revenue Miles',
                                                                'value': 'vrm'},
                                                            {
                                                                'label': 'Vehicle Revenue Hours',
                                                                'value': 'vrh'},
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0','padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='operating-statistics-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2019', style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Rural Transit Ridership by State (Yearly)',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='state-ridership-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Total (million trips)',
                                                                'value': 'total'},
                                                            {
                                                                'label': 'Fixed-Route Service (million trips)',
                                                                'value': 'fr'},
                                                            {
                                                                'label': 'Demand-Response Service (million trips)',
                                                                'value': 'dr'},
                                                            {
                                                                'label': 'Other Service (million trips)',
                                                                'value': 'other'},
                                                        ],
                                                        value='total',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='state-ridership-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2016-2019', style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Rural Transit Vehicle Revenue Miles of Service by State (Yearly)',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='state-vrm-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Total (million miles)',
                                                                'value': 'total'},
                                                            {
                                                                'label': 'Fixed-Route Service (million miles)',
                                                                'value': 'fr'},
                                                            {
                                                                'label': 'Demand-Response Service (million miles)',
                                                                'value': 'dr'},
                                                            {
                                                                'label': 'Other Service (million miles)',
                                                                'value': 'other'},
                                                        ],
                                                        value='total',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='state-vrm-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2016-2019', style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='State Financial Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='state-financial-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Funds Expended on Operations by Source',
                                                                'value': 'operations'},
                                                            {
                                                                'label': 'Funds Expended on Capital by Source',
                                                                'value': 'capital'},
                                                        ],
                                                        value='operations',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='state-financial-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2019', style=paragraph_styles),
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
                                                    html.P('Source: National Transit Database, 2019',
                                                           style=paragraph_styles),
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
                                                    html.P('Source: National Transit Database, 2019',
                                                           style=paragraph_styles),
                                                    html.P('Note: VRM - Vehicle Revenue Mile,VRH - Vehicle Revenue Hour, FR - Fixed-Route, DR - Demand-Response, OE - Operating Expense',
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
                                                    html.P('Source: National Transit Database, 2019',
                                                           style=paragraph_styles),
                                                    html.P('Note: VRM - Vehicle Revenue Mile,VRH - Vehicle Revenue Hour, FR - Fixed-Route, DR - Demand-Response, OE - Operating Expense',
                                                        style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Transit Agency Percentiles for Operating Statistics',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='state-percentile-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Ridership Percentile',
                                                                'value': 'ridership'},
                                                            {
                                                                'label': 'Vehicle Revenue Miles Percentile',
                                                                'value': 'vrm'},
                                                            {
                                                                'label': 'Vehicle Revenue Hours Percentile',
                                                                'value': 'vrh'},
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='state-percentile-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2019', style=paragraph_styles),
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
                                                    dcc.Dropdown(
                                                        id='tribal-operating-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Ridership (thousand rides)',
                                                                'value': 'ridership'},
                                                            {
                                                                'label': 'Vehicle Revenue Miles (thousand miles)',
                                                                'value': 'vrm'},
                                                            {
                                                                'label': 'Vehicle Revenue Hours (thousand hours)',
                                                                'value': 'vrh'},
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='tribal-operating-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2015-2019',
                                                           style=paragraph_styles),
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
                                                    html.P('Source: National Transit Database, 2019',
                                                           style=paragraph_styles),
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
                                                    html.P('Source: National Transit Database, 2019',
                                                           style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Operating Statistics by Vehicle Mode',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='tribal-operatingByMode-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Trips per Vehicle',
                                                                'value': 'ridership'},
                                                            {
                                                                'label': 'Vehicle Revenue Miles per Vehicle',
                                                                'value': 'vrm'},
                                                            {
                                                                'label': 'Vehicle Revenue Hours per Vehicle',
                                                                'value': 'vrh'},
                                                        ],
                                                        value='ridership',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='tribal-operatingByMode-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2019', style=paragraph_styles),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Tribal Transit Performance Measures',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.Br(),
                                                    dcc.Dropdown(
                                                        id='tribal-performance-dropdown',
                                                        options=[
                                                            {
                                                                'label': 'Trips per Vehicle Revenue Mile',
                                                                'value': 'trips_vrm'},
                                                            {
                                                                'label': 'Trips per Vehicle Revenue Hour',
                                                                'value': 'trips_vrh'},
                                                            {
                                                                'label': 'Operating Expense Per Trip',
                                                                'value': 'oe_trip'},
                                                            {
                                                                'label': 'Operating Expense per Vehicle Revenue Mile',
                                                                'value': 'oe_vrm'},
                                                            {
                                                                'label': 'Operating Expense per Vehicle Revenue Hour',
                                                                'value': 'oe_vrh'},
                                                            {
                                                                'label': 'Farebox Recovery Ratio',
                                                                'value': 'farebox'},
                                                        ],
                                                        value='trips_vrm',
                                                        style={'width': '60%', 'margin': '0 0 0',
                                                               'padding-left': '100px'}
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='tribal-performance-table'),
                                                    html.Br(),
                                                    html.P('Source: National Transit Database, 2015-2019', style=paragraph_styles),
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
                                                    html.P('Source: National Transit Database, 2019',
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
