html.Div(
    className="bg-gray-50",
    children=[
        html.Main(
            className="mx-auto min-h-screen max-w-7xl px-4 py-10",
            children=[
                html.Section(
                    className="mb-10 flex flex-col rounded-lg bg-white p-6 text-gray-700 shadow-lg",
                    children=[
                        html.H2(
                            className="mb-4 text-4xl font-semibold",
                            children=["Predicción para un restaurante"],
                        ),
                        html.Form(
                            action="3",
                            method="post",
                            className="space-y-6",
                            children=[
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Tipo de comida"],
                                        ),
                                        html.Select(
                                            id="food-type",
                                            name="food-type",
                                            className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                                            children=[
                                                html.Option(
                                                    value="mexican",
                                                    children=["Mexican"],
                                                ),
                                                html.Option(
                                                    value="thai", children=["Thai"]
                                                ),
                                                html.Option(
                                                    value="italian",
                                                    children=["Italian"],
                                                ),
                                                html.Option(
                                                    value="american",
                                                    children=["American"],
                                                ),
                                                html.Option(
                                                    value="chinese",
                                                    children=["Chinese"],
                                                ),
                                                html.Option(
                                                    value="indian", children=["Indian"]
                                                ),
                                                html.Option(
                                                    value="japanese",
                                                    children=["Japanese"],
                                                ),
                                                html.Option(
                                                    value="mediterranean",
                                                    children=["Mediterranean"],
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Área de fumadores"],
                                        ),
                                        html.Div(
                                            className="flex items-center space-x-4",
                                            children=[
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["Sí"],
                                                        )
                                                    ]
                                                ),
                                                html.Div(
                                                    children=[
                                                        html.Label(
                                                            className="ml-2 text-gray-700",
                                                            children=["No"],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Estado"],
                                        ),
                                        html.Select(
                                            id="state",
                                            name="state",
                                            className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                                            children=[
                                                html.Option(
                                                    value="AL", children=["Alabama"]
                                                ),
                                                html.Option(
                                                    value="AK", children=["Alaska"]
                                                ),
                                                html.Option(
                                                    value="AZ", children=["Arizona"]
                                                ),
                                                html.Option(
                                                    value="AR", children=["Arkansas"]
                                                ),
                                                html.Option(
                                                    value="CA", children=["California"]
                                                ),
                                                html.Option(
                                                    value="CO", children=["Colorado"]
                                                ),
                                                html.Option(
                                                    value="CT", children=["Connecticut"]
                                                ),
                                                html.Option(
                                                    value="DE", children=["Delaware"]
                                                ),
                                                html.Option(
                                                    value="FL", children=["Florida"]
                                                ),
                                                html.Option(
                                                    value="GA", children=["Georgia"]
                                                ),
                                                html.Option(
                                                    value="HI", children=["Hawaii"]
                                                ),
                                                html.Option(
                                                    value="ID", children=["Idaho"]
                                                ),
                                                html.Option(
                                                    value="IL", children=["Illinois"]
                                                ),
                                                html.Option(
                                                    value="IN", children=["Indiana"]
                                                ),
                                                html.Option(
                                                    value="IA", children=["Iowa"]
                                                ),
                                                html.Option(
                                                    value="KS", children=["Kansas"]
                                                ),
                                                html.Option(
                                                    value="KY", children=["Kentucky"]
                                                ),
                                                html.Option(
                                                    value="LA", children=["Louisiana"]
                                                ),
                                                html.Option(
                                                    value="ME", children=["Maine"]
                                                ),
                                                html.Option(
                                                    value="MD", children=["Maryland"]
                                                ),
                                                html.Option(
                                                    value="MA",
                                                    children=["Massachusetts"],
                                                ),
                                                html.Option(
                                                    value="MI", children=["Michigan"]
                                                ),
                                                html.Option(
                                                    value="MN", children=["Minnesota"]
                                                ),
                                                html.Option(
                                                    value="MS", children=["Mississippi"]
                                                ),
                                                html.Option(
                                                    value="MO", children=["Missouri"]
                                                ),
                                                html.Option(
                                                    value="MT", children=["Montana"]
                                                ),
                                                html.Option(
                                                    value="NE", children=["Nebraska"]
                                                ),
                                                html.Option(
                                                    value="NV", children=["Nevada"]
                                                ),
                                                html.Option(
                                                    value="NH",
                                                    children=["New Hampshire"],
                                                ),
                                                html.Option(
                                                    value="NJ", children=["New Jersey"]
                                                ),
                                                html.Option(
                                                    value="NM", children=["New Mexico"]
                                                ),
                                                html.Option(
                                                    value="NY", children=["New York"]
                                                ),
                                                html.Option(
                                                    value="NC",
                                                    children=["North Carolina"],
                                                ),
                                                html.Option(
                                                    value="ND",
                                                    children=["North Dakota"],
                                                ),
                                                html.Option(
                                                    value="OH", children=["Ohio"]
                                                ),
                                                html.Option(
                                                    value="OK", children=["Oklahoma"]
                                                ),
                                                html.Option(
                                                    value="OR", children=["Oregon"]
                                                ),
                                                html.Option(
                                                    value="PA",
                                                    children=["Pennsylvania"],
                                                ),
                                                html.Option(
                                                    value="RI",
                                                    children=["Rhode Island"],
                                                ),
                                                html.Option(
                                                    value="SC",
                                                    children=["South Carolina"],
                                                ),
                                                html.Option(
                                                    value="SD",
                                                    children=["South Dakota"],
                                                ),
                                                html.Option(
                                                    value="TN", children=["Tennessee"]
                                                ),
                                                html.Option(
                                                    value="TX", children=["Texas"]
                                                ),
                                                html.Option(
                                                    value="UT", children=["Utah"]
                                                ),
                                                html.Option(
                                                    value="VT", children=["Vermont"]
                                                ),
                                                html.Option(
                                                    value="VA", children=["Virginia"]
                                                ),
                                                html.Option(
                                                    value="WA", children=["Washington"]
                                                ),
                                                html.Option(
                                                    value="WV",
                                                    children=["West Virginia"],
                                                ),
                                                html.Option(
                                                    value="WI", children=["Wisconsin"]
                                                ),
                                                html.Option(
                                                    value="WY", children=["Wyoming"]
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["City"],
                                        )
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Price Range"],
                                        ),
                                        html.Select(
                                            id="price-range",
                                            name="price-range",
                                            className="mt-2 w-full rounded-md border border-gray-300 p-3 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500",
                                            children=[
                                                html.Option(value="$", children=["$"]),
                                                html.Option(
                                                    value="$$", children=["$$"]
                                                ),
                                                html.Option(
                                                    value="$$$", children=["$$$"]
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    className="flex justify-center",
                                    children=[
                                        html.Button(
                                            type="submit",
                                            className="inline-block rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white shadow-lg hover:from-pink-300 hover:to-orange-600",
                                            children=["Enviar"],
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Section(
                    className="mb-10 flex flex-col rounded-lg bg-white p-6 text-gray-700 shadow-lg",
                    children=[
                        html.H2(
                            className="mb-4 text-4xl font-semibold",
                            children=["Predicción usando un archivo"],
                        ),
                        html.P(
                            className="mb-4 text-lg",
                            children=[
                                "Subir un archivo csv con los campos:",
                                html.Span(
                                    className="font-semibold text-sky-500",
                                    children=[
                                        "Food Type, Smoker Area, State, City, Price Range"
                                    ],
                                ),
                            ],
                        ),
                        html.Form(
                            action="#",
                            method="post",
                            encType="multipart/form-data",
                            className="space-y-6",
                            children=[
                                html.Div(
                                    children=[
                                        html.Label(
                                            className="block text-lg font-medium text-gray-700",
                                            children=["Archivo csv"],
                                        )
                                    ]
                                ),
                                html.Div(
                                    className="flex justify-center",
                                    children=[
                                        html.Button(
                                            type="submit",
                                            className="inline-block rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white shadow-lg hover:from-pink-300 hover:to-orange-600",
                                            children=["Subir archivo"],
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    ],
)
