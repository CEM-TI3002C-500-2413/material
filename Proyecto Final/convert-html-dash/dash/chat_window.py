html.Div(
    children=[
        html.Div(
            className="fixed bottom-5 right-5 z-10 flex h-[36rem] w-80 flex-col rounded-lg border-2 bg-white text-gray-700 shadow-xl",
            children=[
                html.Div(
                    className="flex justify-between rounded-t-lg p-4",
                    children=[
                        html.Div(
                            children=[
                                html.H4(
                                    className="inline-block text-xl font-semibold",
                                    children=["Asistente virtual"],
                                ),
                                dash_svg.Svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    fill="none",
                                    viewBox="0 0 24 24",
                                    stroke="currentColor",
                                    className="-mt-6 inline h-8 w-8",
                                    children=[
                                        dash_svg.Path(
                                            strokeLinecap="round",
                                            strokeLinejoin="round",
                                            d="M8.625 9.75a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H8.25m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0H12m4.125 0a.375.375 0 1 1-.75 0 .375.375 0 0 1 .75 0Zm0 0h-.375m-13.5 3.01c0 1.6 1.123 2.994 2.707 3.227 1.087.16 2.185.283 3.293.369V21l4.184-4.183a1.14 1.14 0 0 1 .778-.332 48.294 48.294 0 0 0 5.83-.498c1.585-.233 2.708-1.626 2.708-3.228V6.741c0-1.602-1.123-2.995-2.707-3.228A48.394 48.394 0 0 0 12 3c-2.392 0-4.744.175-7.043.513C3.373 3.746 2.25 5.14 2.25 6.741v6.018Z",
                                        )
                                    ],
                                ),
                            ]
                        ),
                        html.Button(
                            children=[
                                dash_svg.Svg(
                                    xmlns="http://www.w3.org/2000/svg",
                                    viewBox="0 0 24 24",
                                    fill="currentColor",
                                    className="inline h-8 w-8 rounded-full text-red-600 shadow-lg",
                                    children=[
                                        dash_svg.Path(
                                            fillRule="evenodd",
                                            d="M12 2.25c-5.385 0-9.75 4.365-9.75 9.75s4.365 9.75 9.75 9.75 9.75-4.365 9.75-9.75S17.385 2.25 12 2.25Zm-1.72 6.97a.75.75 0 1 0-1.06 1.06L10.94 12l-1.72 1.72a.75.75 0 1 0 1.06 1.06L12 13.06l1.72 1.72a.75.75 0 1 0 1.06-1.06L13.06 12l1.72-1.72a.75.75 0 1 0-1.06-1.06L12 10.94l-1.72-1.72Z",
                                            clipRule="evenodd",
                                        )
                                    ],
                                )
                            ]
                        ),
                    ],
                ),
                html.Div(
                    className="space-y-4 overflow-y-auto p-6",
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    className="rounded-lg bg-gradient-to-br from-sky-300 to-blue-500 p-4 text-white",
                                    children=[
                                        html.P(
                                            className="font-semibold",
                                            children=[
                                                """
                                                Lorem ipsum dolor sit amet consectetur adipisicing elit. In, optio quidem aspernatur ab deleniti sit iusto, illo ducimus sint id perferendis. Obcaecati facilis debitis cumque sequi consectetur quod, repudiandae dignissimos?
                                                Quia debitis esse omnis dolor similique. Ullam quo error accusamus, doloribus sapiente unde quisquam corporis rem magni facilis iusto alias vel distinctio rerum debitis atque assumenda libero, numquam cumque ea?
                                                """
                                            ],
                                        )
                                    ],
                                ),
                                html.Div(
                                    children=[
                                        html.P(
                                            className="text-xs font-semibold text-slate-800",
                                            children=["Asistente virtual"],
                                        )
                                    ]
                                ),
                            ]
                        ),
                        html.Div(
                            children=[
                                html.Div(
                                    className="rounded-lg bg-gradient-to-bl from-pink-300 to-orange-600 p-4 text-white",
                                    children=[
                                        html.P(
                                            className="font-semibold",
                                            children=[
                                                """
                                                Lorem ipsum dolor sit amet consectetur adipisicing elit. In, optio quidem aspernatur ab deleniti sit iusto, illo ducimus sint id perferendis. Obcaecati facilis debitis cumque sequi consectetur quod, repudiandae dignissimos?
                                                Quia debitis esse omnis dolor similique. Ullam quo error accusamus, doloribus sapiente unde quisquam corporis rem magni facilis iusto alias vel distinctio rerum debitis atque assumenda libero, numquam cumque ea?
                                                """
                                            ],
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="text-end",
                                    children=[
                                        html.P(
                                            className="text-xs font-semibold text-slate-800",
                                            children=["Usuario"],
                                        )
                                    ],
                                ),
                            ]
                        ),
                    ],
                ),
                html.Div(className="xp-4 rounded-b-lg p-4"),
            ],
        )
    ]
)
