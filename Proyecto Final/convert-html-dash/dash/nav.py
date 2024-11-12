html.Nav(
    className="flex md:flex-row flex-col justify-between items-center bg-gradient-to-b from-cyan-500 to-blue-600 px-6 py-8",
    children=[
        html.Div(
            className="flex",
            children=[
                html.A(
                    href="/index.html",
                    children=[
                        html.Img(
                            className="w-52",
                            src="/images/logo.png",
                            alt="Logo de TipOn",
                        )
                    ],
                )
            ],
        ),
        html.Div(
            className="flex space-x-4 font-semibold text-white text-xl",
            children=[
                html.A(
                    href="/index.html",
                    className="hover:text-blue-200 hover:underline",
                    children=["Inicio"],
                ),
                html.A(
                    href="/negocios.html",
                    className="hover:text-blue-200 hover:underline",
                    children=["Negocios"],
                ),
                html.A(
                    href="/tableros.html",
                    className="hover:text-blue-200 hover:underline",
                    children=["Tableros"],
                ),
                html.A(
                    href="predicción.html",
                    className="hover:text-blue-200 hover:underline",
                    children=["Predicción"],
                ),
            ],
        ),
    ],
)
