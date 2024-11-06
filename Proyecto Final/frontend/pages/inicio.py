import dash
from dash import html, dcc

dash.register_page(__name__,
                   path="/",
                   title="Sitio de administración de TipOn",
                   name="inicio")

layout = html.Div(
    className="bg-gray-50",
    children=[
        html.Header(
            className="bg-blue-600 drop-shadow-lg px-2 py-20 text-center text-white",
            children=[
                html.H2(
                    className="mb-4 text-4xl md:text-6xl",
                    children=["Sitio de administración de TipOn"],
                ),
                html.P(
                    className="mb-6",
                    children=[
                        "Éste es el sitio principal de administración del sistema de propinas de TipOn"
                    ],
                ),
                dcc.Link(
                    className="inline-block bg-white hover:bg-blue-400 shadow-lg hover:shadow-gray-700 px-6 py-3 rounded-lg font-semibold text-blue-500 text-xl hover:text-white",
                    href="/",
                    children=["Inicio"],
                ),
            ],
        ),
        html.Main(
            className="mx-auto px-4 py-10 max-w-7xl min-h-screen",
            children=[
                html.Section(
                    className="flex md:flex-row flex-col items-center bg-white shadow-xl mb-10 p-6 rounded-lg text-gray-700",
                    children=[
                        html.Div(
                            className="mb-4 md:mb-0 md:pr-6 md:w-1/2 text-center md:text-left",
                            children=[
                                html.H2(
                                    className="mb-4 font-bold text-4xl",
                                    children=["Acerca del sitio"],
                                ),
                                html.P(
                                    className="text-justify",
                                    children=[
                                        """
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Error, fugit repellendus maxime ducimus ut nostrum quidem porro rem ipsa cupiditate incidunt quisquam consequatur minima aliquid quod officia nemo voluptatibus? Temporibus!
                                        Facilis natus eveniet dolor ad blanditiis doloremque. Aut, libero dolor! Minima, aut in? Amet impedit at repudiandae sed dolorum cupiditate ratione, ad commodi. Facere quae voluptates, ducimus dolores libero a.
                                        """
                                    ],
                                ),
                            ],
                        ),
                        html.Img(
                            className="shadow-lg rounded-lg md:w-1/2",
                            src=dash.get_asset_url("images/pexels-elevate-1267320.jpg"),
                            alt="Chef sirviendo platillos",
                        ),
                    ],
                ),
                html.Section(
                    className="flex flex-col items-center bg-white shadow-xl mb-10 p-6 rounded-lg text-gray-700",
                    children=[
                        html.H2(
                            className="mb-4 font-bold text-4xl", children=["Propósito"]
                        ),
                        html.P(
                            className="text-justify",
                            children=[
                                """
                                Lorem ipsum dolor, sit amet consectetur adipisicing elit. Mollitia, laborum rerum? Aperiam ab maiores necessitatibus sint ipsa repellat doloremque saepe nobis, modi ipsam cupiditate architecto excepturi deserunt, fugit eum? Nemo?
                                Rem deleniti qui et perspiciatis temporibus facere? Sit aliquid vero autem sunt. Alias iste eligendi iusto aliquam voluptate dignissimos! Numquam dolorum mollitia totam iste. Laborum eaque dicta voluptas consequuntur earum.
                                Possimus incidunt ad, aut commodi doloremque, voluptas illum recusandae quasi ipsum suscipit mollitia magnam voluptates tenetur nam at! Aliquam quo sit rerum at, ipsam asperiores quasi in exercitationem incidunt! Quidem!
                                Quia reprehenderit iusto voluptatem. Quas sunt qui incidunt doloribus nostrum pariatur atque ipsam dolorem magnam et voluptas eos voluptate esse, mollitia vitae animi. Eaque recusandae ad incidunt molestias asperiores exercitationem.
                                Recusandae consectetur aperiam quis iste veniam impedit, culpa ratione repellendus dicta hic aut optio provident velit architecto error quisquam iure porro perspiciatis voluptatum animi a distinctio? Aut veniam quia natus.
                                """
                            ],
                        ),
                    ],
                ),
                html.Section(
                    className="flex md:flex-row flex-col items-center bg-white shadow-xl mb-10 p-6 rounded-lg text-gray-700",
                    children=[
                        html.Img(
                            className="shadow-lg rounded-lg md:w-1/2",
                            src=dash.get_asset_url("images/pexels-evonics-1058277.jpg"),
                            alt="Restaurante-bar lleno de noche",
                        ),
                        html.Div(
                            className="mb-4 md:mb-0 md:pl-6 md:w-1/2",
                            children=[
                                html.H2(
                                    className="mb-4 font-bold text-4xl text-center md:text-left",
                                    children=["Negocios"],
                                ),
                                html.P(
                                    className="text-justify",
                                    children=[
                                        """
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit, nam provident ratione enim laudantium tempora nobis laborum harum aliquid iure! Ad sequi ducimus reprehenderit alias necessitatibus deserunt illum, tenetur earum.
                                        Non eligendi distinctio porro. Maiores quidem harum quo veniam, excepturi repellendus blanditiis commodi doloribus similique? Veniam suscipit consectetur corporis vel quisquam, nobis ducimus, quasi, reiciendis officia rem iure minus excepturi.
                                        Nostrum magni, magnam asperiores soluta reiciendis mollitia pariatur nesciunt? Voluptas, blanditiis accusamus nostrum libero a molestias cumque! Totam quam consequuntur nisi eum assumenda? Ducimus reiciendis perspiciatis molestiae nisi provident porro.
                                        """
                                    ],
                                ),
                                html.Div(
                                    className="mb-4 text-center",
                                    children=[
                                        dcc.Link(
                                            className="inline-block bg-gradient-to-br from-teal-400 hover:from-pink-300 to-blue-500 hover:to-orange-600 shadow-lg mt-6 px-6 py-3 rounded-lg font-semibold text-white",
                                            href="/negocios",
                                            children=["Ver negocios"],
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Section(
                    className="flex md:flex-row flex-col items-center bg-white shadow-xl mb-10 p-6 rounded-lg text-gray-700",
                    children=[
                        html.Div(
                            className="mb-4 md:mb-0 md:pr-6 md:w-1/2",
                            children=[
                                html.H2(
                                    className="mb-4 font-bold text-4xl text-center md:text-left",
                                    children=["Tableros"],
                                ),
                                html.P(
                                    className="text-justify",
                                    children=[
                                        """
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit, nam provident ratione enim laudantium tempora nobis laborum harum aliquid iure! Ad sequi ducimus reprehenderit alias necessitatibus deserunt illum, tenetur earum.
                                        Non eligendi distinctio porro. Maiores quidem harum quo veniam, excepturi repellendus blanditiis commodi doloribus similique? Veniam suscipit consectetur corporis vel quisquam, nobis ducimus, quasi, reiciendis officia rem iure minus excepturi.
                                        Nostrum magni, magnam asperiores soluta reiciendis mollitia pariatur nesciunt? Voluptas, blanditiis accusamus nostrum libero a molestias cumque! Totam quam consequuntur nisi eum assumenda? Ducimus reiciendis perspiciatis molestiae nisi provident porro.
                                        """
                                    ],
                                ),
                                html.Div(
                                    className="mb-4 text-center",
                                    children=[
                                        dcc.Link(
                                            className="inline-block bg-gradient-to-br from-teal-400 hover:from-pink-300 to-blue-500 hover:to-orange-600 shadow-lg mt-6 px-6 py-3 rounded-lg font-semibold text-white",
                                            href="/tableros",
                                            children=["Ver tableros"],
                                        )
                                    ],
                                ),
                            ],
                        ),
                        html.Img(
                            className="shadow-lg rounded-lg md:w-1/2",
                            src=dash.get_asset_url("images/pexels-pixabay-262978.jpg"),
                            alt="Restaurante-bar lleno de noche",
                        ),
                    ],
                ),
                html.Section(
                    className="flex md:flex-row flex-col items-center bg-white shadow-xl mb-10 p-6 rounded-lg text-gray-700",
                    children=[
                        html.Img(
                            className="shadow-lg rounded-lg md:w-1/2",
                            src=dash.get_asset_url("images/pexels-wildlittlethingsphoto-696218.jpg"),
                            alt="Restaurante-bar lleno de noche",
                        ),
                        html.Div(
                            className="mb-4 md:mb-0 md:pl-6 md:w-1/2",
                            children=[
                                html.H2(
                                    className="mb-4 font-bold text-4xl text-center md:text-left",
                                    children=["Predicción"],
                                ),
                                html.P(
                                    className="text-justify",
                                    children=[
                                        """
                                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit, nam provident ratione enim laudantium tempora nobis laborum harum aliquid iure! Ad sequi ducimus reprehenderit alias necessitatibus deserunt illum, tenetur earum.
                                        Non eligendi distinctio porro. Maiores quidem harum quo veniam, excepturi repellendus blanditiis commodi doloribus similique? Veniam suscipit consectetur corporis vel quisquam, nobis ducimus, quasi, reiciendis officia rem iure minus excepturi.
                                        Nostrum magni, magnam asperiores soluta reiciendis mollitia pariatur nesciunt? Voluptas, blanditiis accusamus nostrum libero a molestias cumque! Totam quam consequuntur nisi eum assumenda? Ducimus reiciendis perspiciatis molestiae nisi provident porro.
                                        """
                                    ],
                                ),
                                html.Div(
                                    className="mb-4 text-center",
                                    children=[
                                        dcc.Link(
                                            className="inline-block bg-gradient-to-br from-teal-400 hover:from-pink-300 to-blue-500 hover:to-orange-600 shadow-lg mt-6 px-6 py-3 rounded-lg font-semibold text-white",
                                            href="/predicciones",
                                            children=["Ver predicciones"],
                                        )
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)