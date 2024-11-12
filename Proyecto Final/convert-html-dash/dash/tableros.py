html.Div(
    className="bg-gray-50",
    children=[
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen",
            children=[
                html.Section(
                    className="flex flex-col bg-white shadow-lg mb-10 p-6 rounded-lg text-gray-700",
                    children=[
                        html.H2(
                            className="mb-4 font-semibold text-4xl",
                            children=["Ejemplo de un video"],
                        ),
                        html.Iframe(
                            className="aspect-video",
                            src="https://www.youtube.com/embed/TtkFsfOP9QI?si=54tx-j7w-2nN5P1P",
                            title="YouTube video player",
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share",
                            referrerPolicy="strict-origin-when-cross-origin",
                        ),
                    ],
                ),
                html.Section(
                    className="flex flex-col bg-white shadow-lg p-6 rounded-lg text-gray-700",
                    children=[
                        html.H2(
                            className="mb-4 font-semibold text-4xl",
                            children=["Ejemplo de inserción de tablero"],
                        ),
                        html.Iframe(
                            className="h-[800px]",
                            src="https://public.tableau.com/views/TableroRetoIndividual/Dashboard2?:showVizHome=no&:embed=true",
                        ),
                    ],
                ),
            ],
        )
    ],
)
