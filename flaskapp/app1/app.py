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
                                # dcc.Tab(
                                #     label='Revenue Vehicles Statistics',
                                #     style=tab_style,
                                #     selected_style=tab_selected_style,
                                #     children=[
                                #         html.H2(
                                #             'Small Urban & Rural Transit Systems Revenue Vehicles Fleet Information Reports'),
                                #         html.P(
                                #             'Reports are generated from National Transit Database (NTD) data based on 2019 reporting year, the most current data.',
                                #             style=paragraph_styles),
                                #         html.Br(),
                                #         dcc.Graph(id='revenue-vehicles', config={'displayModeBar': False},
                                #                   animate=True),
                                #         dcc.Graph(id='fleet-composition')
                                #     ]
                                # ),
                                # dcc.Tab(
                                #     label='Revenue Vehicles SGR Reports',
                                #     style=tab_style,
                                #     selected_style=tab_selected_style,
                                #     children=[
                                #         html.H2(
                                #             'Small Urban & Rural Transit Systems Revenue Vehicles State of Good Repair (SGR) Reports'),
                                #         html.P(
                                #             'The revenue vehicles State of Good Repair (SGR) reports are generated from the predicted results of machine learning model developed for small urban and rural transit systems. '
                                #             'The backlog is calculated from the projected retirement years, which were prior to 2021, and the projected vehicle replacements are calculated with the replacement of the same number of retired revenue vehicles. '
                                #             'The backlog and vehicle replacement costs are calculated from the vehicle cost data of the APTA public transportation vehicle database.',
                                #             style=paragraph_styles),
                                #         html.Br(),
                                #         dcc.Graph(id='number-replaced'),
                                #         dcc.Graph(id='replacement-cost')
                                #     ]
                                # ),
                                # dcc.Tab(label='Revenue Vehicles SGR Backlog Reports',
                                #         style=tab_style,
                                #         selected_style=tab_selected_style,
                                #         children=[
                                #             html.H2(
                                #                 'Small Urban & Rural Transit Systems Revenue Vehicles SGR Backlog Reports'),
                                #             html.P(
                                #                 'The revenue vehicles SGR Backlog are calculated from the projected retirement years, which were prior to 2021, and Backlog Costs are calculated from the APTA’s public transportation vehicle database. '
                                #                 'The reports show current backlog and backlog replacement cost by vehicle Type based on NTD data 2019 reporting year.',
                                #                 style=paragraph_styles),
                                #             html.Br(),
                                #             dcc.Graph(
                                #                 id='backlog-vehicles'),
                                #             dcc.Graph(
                                #                 id='backlog-cost-vehicles')
                                #         ]
                                #         ),
                                # dcc.Tab(
                                #     label=' Report Name ',
                                #     style=tab_style,
                                #     selected_style=tab_selected_style,
                                #     children=[
                                #         html.H2(
                                #             'Heading 2'),
                                #         html.P(
                                #             'Description',
                                #             style=paragraph_styles),
                                #         html.Br(),
                                #         dcc.Graph(
                                #             id='vehicle-revenue-miles'),
                                #         dcc.Graph(
                                #             id='vehicle-revenue-hours'),
                                #         dcc.Graph(
                                #             id='unlinked_passenger_trips'),
                                #         # html.Div(id='my-output'),
                                #         dcc.Graph(
                                #             id='vehicle-revenue-miles-table'),
                                #     ]
                                # ),
                                dcc.Tab(
                                    label=' Report Name ',
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
                                    label=' Report Name In table format',
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
                                            id='unlinked_passenger_trips-table'),
                                    ]
                                )
                            ],
                                style=tabs_styles)
                        ],
                    )
                ]
            )
        ]
    )
    return dash_app
