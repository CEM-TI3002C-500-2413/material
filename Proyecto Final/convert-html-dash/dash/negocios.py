html.Div(
    className="bg-gray-50",
    children=[
        html.Main(
            className="mx-auto min-h-screen max-w-7xl px-4 py-10 text-gray-700",
            children=[
                html.Section(
                    className="flex flex-col rounded-lg bg-white p-6 shadow-lg",
                    children=[
                        html.Div(
                            className="mb-4 flex justify-center",
                            children=[
                                html.Button(
                                    className="rounded-r-lg bg-blue-600 px-4 text-white hover:bg-blue-700 focus:outline-none focus:ring focus:ring-blue-300",
                                    children=["Buscar"],
                                )
                            ],
                        ),
                        html.Ul(
                            className="mb-4 space-y-4",
                            children=[
                                html.Li(
                                    className="flex flex-col items-center justify-between rounded-lg bg-white p-4 shadow-md md:flex-row",
                                    children=[
                                        html.Span(
                                            className="text-lg font-semibold text-gray-700",
                                            children=["Restaurante 1"],
                                        ),
                                        html.Button(
                                            className="rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white hover:from-pink-300 hover:to-orange-600",
                                            children=["Ver restaurante"],
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="flex flex-col items-center justify-between rounded-lg bg-white p-4 shadow-md md:flex-row",
                                    children=[
                                        html.Span(
                                            className="text-lg font-semibold text-gray-700",
                                            children=["Restaurante 2"],
                                        ),
                                        html.Button(
                                            className="rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white hover:from-pink-300 hover:to-orange-600",
                                            children=["Ver restaurante"],
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="flex flex-col items-center justify-between rounded-lg bg-white p-4 shadow-md md:flex-row",
                                    children=[
                                        html.Span(
                                            className="text-lg font-semibold text-gray-700",
                                            children=["Restaurante 3"],
                                        ),
                                        html.Button(
                                            className="rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white hover:from-pink-300 hover:to-orange-600",
                                            children=["Ver restaurante"],
                                        ),
                                    ],
                                ),
                                html.Li(
                                    className="flex flex-col items-center justify-between rounded-lg bg-white p-4 shadow-md md:flex-row",
                                    children=[
                                        html.Span(
                                            className="text-lg font-semibold text-gray-700",
                                            children=["Restaurante 4"],
                                        ),
                                        html.Button(
                                            className="rounded-lg bg-gradient-to-br from-teal-400 to-blue-500 px-6 py-3 font-semibold text-white hover:from-pink-300 hover:to-orange-600",
                                            children=["Ver restaurante"],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="text-center",
                            children=[
                                html.H2(
                                    className="mb-4 text-6xl font-bold",
                                    children=["Restaurante"],
                                )
                            ],
                        ),
                        html.P(
                            className="mb-4 text-justify",
                            children=[
                                """
                                Lorem ipsum dolor sit amet consectetur adipisicing elit. Minus obcaecati assumenda fugit corporis exercitationem mollitia, quibusdam delectus, modi asperiores explicabo vel dolores adipisci maxime, placeat tenetur culpa vero est ullam?
                                Eligendi eius illum alias et, blanditiis sunt beatae praesentium porro reprehenderit, voluptate laborum explicabo delectus odit quasi repudiandae aliquid a, consequatur saepe fugiat inventore? Ratione veniam dolore sed! Sed, recusandae.
                                Suscipit cum quibusdam culpa nihil odit praesentium quia animi numquam, nulla quis eaque voluptatibus repellat porro, magni mollitia rem ipsam! Delectus cum non libero corrupti reiciendis officia optio eos ipsa.
                                Voluptatibus amet possimus ducimus in dolorem sunt ex maxime, libero, qui culpa id rerum quam. Doloribus, deleniti dignissimos. Doloribus illo odit pariatur reprehenderit voluptates. Beatae dolorem quasi praesentium impedit provident.
                                Hic repellendus iste cupiditate. Totam commodi quod veniam, earum asperiores velit obcaecati libero quos consequuntur sed ad eius nostrum officia exercitationem quia. Eligendi ratione eaque iste delectus praesentium, ad quas?
                                """
                            ],
                        ),
                        html.Img(
                            className="mb-4 rounded-lg shadow-lg",
                            src="/images/pexels-amar-28056778.jpg",
                            alt="Foto de la fachada de Loretta Café",
                        ),
                        html.Div(
                            className="mb-4 rounded-lg p-6 text-center shadow-lg",
                            children=[
                                html.H3(
                                    className="mb-4 text-4xl font-semibold",
                                    children=["Indicadores"],
                                ),
                                html.Div(
                                    className="grid grid-cols-1 gap-6 md:grid-cols-4",
                                    children=[
                                        html.Div(
                                            className="rounded-lg p-6 shadow-lg",
                                            children=[
                                                html.H4(
                                                    className="mb-2 text-xl font-semibold",
                                                    children=["Personal registrado"],
                                                ),
                                                html.P(
                                                    className="mb-2 text-6xl font-bold",
                                                    children=[
                                                        "14",
                                                        dash_svg.Svg(
                                                            xmlns="http://www.w3.org/2000/svg",
                                                            fill="none",
                                                            viewBox="0 0 24 24",
                                                            stroke="currentColor",
                                                            className="inline h-14 w-14",
                                                            children=[
                                                                dash_svg.Path(
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z",
                                                                )
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                html.P(
                                                    children=[
                                                        "Cuentas activas en el mes"
                                                    ]
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="rounded-lg p-6 shadow-lg",
                                            children=[
                                                html.H4(
                                                    className="mb-2 text-xl font-semibold",
                                                    children=["Propinas obtenidas"],
                                                ),
                                                html.P(
                                                    className="mb-2 text-6xl font-bold text-green-700",
                                                    children=["+12%"],
                                                ),
                                                html.P(
                                                    children=["Respecto al mes pasado"]
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="rounded-lg p-6 shadow-lg",
                                            children=[
                                                html.H4(
                                                    className="mb-2 text-xl font-semibold",
                                                    children=["Promedio"],
                                                ),
                                                html.P(
                                                    className="mb-2 text-6xl font-bold",
                                                    children=["$120"],
                                                ),
                                                html.P(children=["Por propina"]),
                                            ],
                                        ),
                                        html.Div(
                                            className="rounded-lg p-6 shadow-lg",
                                            children=[
                                                html.H4(
                                                    className="mb-2 text-xl font-semibold",
                                                    children=["Método de pago"],
                                                ),
                                                html.P(
                                                    className="mb-2 text-6xl font-bold",
                                                    children=[
                                                        dash_svg.Svg(
                                                            xmlns="http://www.w3.org/2000/svg",
                                                            fill="none",
                                                            viewBox="0 0 24 24",
                                                            stroke="currentColor",
                                                            className="inline h-14 w-14",
                                                            children=[
                                                                dash_svg.Path(
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    d="M2.25 8.25h19.5M2.25 9h19.5m-16.5 5.25h6m-6 2.25h3m-3.75 3h15a2.25 2.25 0 0 0 2.25-2.25V6.75A2.25 2.25 0 0 0 19.5 4.5h-15a2.25 2.25 0 0 0-2.25 2.25v10.5A2.25 2.25 0 0 0 4.5 19.5Z",
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                ),
                                                html.P(children=["Tarjeta de crédito"]),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="mb-4 rounded-lg p-6 text-center shadow-lg",
                            children=[
                                html.H3(
                                    className="mb-4 text-4xl font-semibold",
                                    children=["Propinas del mes"],
                                ),
                                html.Img(
                                    className="rounded-lg",
                                    src="/images/newplot.png",
                                    alt="Gráfica de líneas con las propinas del mes",
                                ),
                            ],
                        ),
                    ],
                )
            ],
        )
    ],
)
