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
        'height': '44px'
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
                        className='three columns div-user-controls',
                        children=[
                            html.Hr(),
                            html.H3('State'),
                            dcc.Dropdown(
                                id='state-selector',
                                options=[{'label': states_dict[k], 'value': k} for k in res.keys()],
                                value='All',
                                placeholder='Select a state...'
                            ),
                            html.Hr(),
                            html.H3('Transit Agency'),
                            dcc.Dropdown(
                                id='agency-dropdown',
                                placeholder='Select a transit agency...'
                            ),

                            html.Hr(),
                            html.H3('Vehicle Type'),
                            html.Div(
                                className='div-for-vehicle-dropdown',
                                children=[
                                    dcc.Dropdown(
                                        id='vehicle-selector',
                                        options=[{'label': k, 'value': v} for k, v in vehicles_dict.items()],
                                        value=' All ',
                                        className='vehicle-selector',
                                        placeholder='Select a vehicle type...'
                                    ),
                                ],
                            ),
                            html.Br(),
                            html.Div(className='w3-xlarge w3-center',
                                     children=[
                                         html.A('Home',
                                                className="w3-button w3-grey w3-round-xlarge w3-center",
                                                id='submit-val',
                                                href='/')
                                     ]
                                     )
                        ],
                    ),
                    html.Div(
                        className='nine columns div-for-charts bg-grey',
                        children=[
                            dcc.Tabs([

                                dcc.Tab(
                                    label=' Services ',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.H2(
                                            'Heading'),
                                        html.P(
                                            'Description',
                                            style=paragraph_styles),
                                        html.Br(),
                                        dcc.Tabs([
                                            dcc.Tab(
                                                label=' Transit Services in Chart ',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.H2(
                                                        'Heading 2'),
                                                    html.P(
                                                        'Description',
                                                        style=paragraph_styles),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='vehicle-revenue-miles'),
                                                    dcc.Graph(
                                                        id='vehicle-revenue-hours'),
                                                    dcc.Graph(
                                                        id='unlinked_passenger_trips'),
                                                ]
                                            ),
                                            dcc.Tab(
                                                label=' Transit Services in table format',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
                                                    html.H2(
                                                        'Heading 2'),
                                                    html.P(
                                                        'Description',
                                                        style=paragraph_styles),
                                                    html.Br(),
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

                                                    html.P(
                                                        'Unlinked Passenger Trips',
                                                        style=paragraph_styles),
                                                    dcc.Graph(
                                                        id='unlinked_passenger_trips-table')
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
                                            'Transit agencies are categorized into ten groups based on percentiles for vehicle revenue miles, vehicle revenue hours, or ridership. The first group is the smallest 10% of agencies, the second group the next smallest 10%, etc.'),
										html.Br(),
                                        html.P(
                                            'Note: VRH - Vehicle Revenue Hours, VRM - Vehicle Revenue Miles, UPT - Unlinked Passenger Trips, OE - Operating Expenses',
                                            style=paragraph_styles),
                                        html.P(
                                            'Source: National Transit Database, 2019',
                                            style=paragraph_styles),
                                        html.Br(),

                                        dcc.Tabs([
                                            dcc.Tab(
                                                label='Statistics For Agencies',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
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
                                                        value='ridership'
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='statisticsRankedByAgencies-table'),

                                                ]
                                            ),
                                            dcc.Tab(
                                                label='Statistics For Fixed Route Service',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[

                                                    dcc.Dropdown(
                                                        id ='stat-dropdown-vrm',
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
                                                        value='ridership'
                                                    ),
                                                    html.Br(),
                                                    dcc.Graph(
                                                        id='statisticsRankedByMB-table'),

                                                ]
                                            ),											
                                            dcc.Tab(
                                                label='Statistics For Demand Response Service',
                                                style=tab_style,
                                                selected_style=tab_selected_style,
                                                children=[
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
                                                        value='ridership'
                                                    ),
                                                    html.Br(),

                                                    dcc.Graph(
                                                        id='statisticsRankedByDemandResponse-table'),
                                                ]
                                            ),
                                        ], style=tabs_styles),
                                    ]
                                ),
                            ],
                                style=tabs_styles)
                        ],
                    )
                ]
            )
        ]
    )
    return dash_app
