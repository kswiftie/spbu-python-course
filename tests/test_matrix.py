import pytest
from project.linalg.matrix import Matrix


@pytest.mark.parametrize(
    "a, b, res",
    [
        (
            [
                [8, 3, 4, -1, -8, -10, -4, 2, -10, 4, -5],
                [-8, -5, 2, -10, 6, 9, 2, 7, 10, 2, 0],
                [-2, 10, 4, 8, -1, -4, 0, 5, 2, -6, -2],
                [10, 8, -7, -7, 4, -5, 1, 10, -2, -7, 5],
                [10, -9, 10, 3, 4, 8, 7, -3, 8, 1, -1],
                [-9, 3, 9, 8, -6, -10, 0, 10, -9, -3, -8],
                [-2, -5, -1, 3, 4, -9, 7, -8, -4, 5, 1],
            ],
            [
                [9, -2, -3, 0, 7, 9, -7, 4, -4, -2, 8],
                [-6, -5, 9, 10, -5, 3, -10, 2, 10, -7, 2],
                [0, -2, -6, 8, -3, -5, -5, -2, 10, 0, 2],
                [-3, 8, -2, -3, -4, 0, 9, -8, -7, -2, 9],
                [-5, -2, -9, -1, 4, -10, -7, 4, -7, -1, -6],
                [-4, 5, -8, 9, 6, -9, -4, -1, 1, 1, 9],
                [7, -4, -2, -10, 8, -5, 8, 10, 6, 1, -9],
            ],
            [
                [17, 1, 1, -1, -1, -1, -11, 6, -14, 2, 3],
                [-14, -10, 11, 0, 1, 12, -8, 9, 20, -5, 2],
                [-2, 8, -2, 16, -4, -9, -5, 3, 12, -6, 0],
                [7, 16, -9, -10, 0, -5, 10, 2, -9, -9, 14],
                [5, -11, 1, 2, 8, -2, 0, 1, 1, 0, -7],
                [-13, 8, 1, 17, 0, -19, -4, 9, -8, -2, 1],
                [5, -9, -3, -7, 12, -14, 15, 2, 2, 6, -8],
            ],
        ),
        (
            [
                [
                    3.150760743962218,
                    1.4312581605757657,
                    2.7957415830551504,
                    8.140421857750713,
                    -7.82423266045835,
                    -2.9189114268181022,
                    -0.8829398271685598,
                ],
                [
                    -7.74734308363298,
                    -4.775024438185563,
                    1.5759224722697525,
                    8.428715627877772,
                    6.8775519581914395,
                    4.086409255857607,
                    0.1971138249337976,
                ],
                [
                    -5.377673158475043,
                    -6.74276658524418,
                    2.335389844123405,
                    -0.07718919917246936,
                    -8.561278084035386,
                    -8.822006019773367,
                    7.018996956646937,
                ],
                [
                    -1.3056842004324043,
                    -9.31696224997959,
                    8.692881600759364,
                    6.047576911046836,
                    5.518776771865813,
                    8.915283061497032,
                    -6.534876178696685,
                ],
                [
                    5.0672016654965475,
                    -8.940315743343174,
                    3.0076876493485436,
                    -5.33719968595368,
                    -6.27903127702144,
                    2.2656348744499777,
                    1.4929863934040952,
                ],
                [
                    -3.5079027431930143,
                    2.0342086746082515,
                    2.5375275669300716,
                    6.472993127920937,
                    -4.498281472800112,
                    4.0612926846511925,
                    -4.9467238246915635,
                ],
                [
                    -4.447297965025532,
                    -0.433231077844491,
                    8.918072871183437,
                    -6.646970373457776,
                    9.35753332302222,
                    -8.68375730463362,
                    2.31207300901222,
                ],
            ],
            [
                [
                    2.8588051009519866,
                    6.633687881868514,
                    -9.669679456936969,
                    -7.301117683934999,
                    -5.425322842758962,
                    0.4559935617814954,
                    4.256700083462459,
                ],
                [
                    -1.6553574484359963,
                    9.536513715942366,
                    2.869765710036374,
                    -5.43352276763827,
                    4.12107822536381,
                    5.193401063892546,
                    -5.817182204286322,
                ],
                [
                    -6.261143911797886,
                    -3.088415131103992,
                    9.226726731729457,
                    5.338021140363638,
                    -8.052483594410667,
                    -5.7579888196003,
                    -6.151535513021598,
                ],
                [
                    9.646546509290129,
                    9.270734202655873,
                    4.569511486284528,
                    6.343623506677446,
                    -5.989536001687741,
                    8.794784679571116,
                    -2.0607070715969034,
                ],
                [
                    -1.6329072547710801,
                    6.48307386329796,
                    -7.31001174442242,
                    9.50340724015767,
                    0.6604980715002533,
                    -0.03881308103064285,
                    4.9102721064941,
                ],
                [
                    -1.0893638976023219,
                    -0.32430436620615843,
                    -7.1232604017071655,
                    -8.369157768828906,
                    0.8436855524879157,
                    2.807229919942751,
                    -7.447148265579477,
                ],
                [
                    0.19145318228668096,
                    -1.2550146899129508,
                    9.133074639320697,
                    1.4800600543567342,
                    -9.972783100329934,
                    -2.0989906049409557,
                    -1.8608312422611775,
                ],
            ],
            [
                [
                    6.009565844914205,
                    8.06494604244428,
                    -6.873937873881818,
                    0.8393041738157141,
                    -13.249555503217312,
                    -2.462917865036607,
                    3.373760256293899,
                ],
                [
                    -9.402700532068977,
                    4.761489277756803,
                    4.445688182306126,
                    2.9951928602395013,
                    10.99863018355525,
                    9.279810319750153,
                    -5.620068379352524,
                ],
                [
                    -11.638817070272928,
                    -9.831181716348173,
                    11.562116575852862,
                    5.260831941191169,
                    -16.613761678446053,
                    -14.579994839373667,
                    0.8674614436253396,
                ],
                [
                    8.340862308857725,
                    -0.04622804732371577,
                    13.262393087043892,
                    12.391200417724281,
                    -0.47075922982192786,
                    17.710067741068148,
                    -8.595583250293588,
                ],
                [
                    3.4342944107254674,
                    -2.4572418800452134,
                    -4.302324095073876,
                    4.166207554203991,
                    -5.618533205521187,
                    2.226821793419335,
                    6.403258499898195,
                ],
                [
                    -4.597266640795336,
                    1.709904308402093,
                    -4.585732834777094,
                    -1.896164640907969,
                    -3.6545959203121967,
                    6.868522604593943,
                    -12.39387209027104,
                ],
                [
                    -4.255844782738851,
                    -1.6882457677574418,
                    18.051147510504133,
                    -5.166910319101042,
                    -0.6152497773077137,
                    -10.782747909574574,
                    0.45124176675104266,
                ],
            ],
        ),
    ],
)
def test_matrix_sum(a, b, res):
    a, b = Matrix(a), Matrix(b)
    assert a + b == Matrix(res)


@pytest.mark.parametrize(
    "a, b, res",
    [
        (
            [
                [-5, 8, -6, -1, 9, 7, -9, -10, -9],
                [-5, -1, 5, -4, -6, -9, -6, -6, -4],
                [5, 5, 6, 9, 7, 1, -9, -2, 9],
                [7, -6, -3, 8, -6, 4, 0, -1, -10],
                [7, 5, 1, -2, -4, -3, 6, 8, 9],
                [-10, 0, -8, -3, -3, 10, 6, -10, 3],
                [-7, -4, -8, 8, 0, 7, 6, 4, -6],
                [-8, -6, 7, -9, 9, 1, 6, -7, 5],
                [-7, -1, -1, 8, -3, -9, -9, 6, 5],
                [-6, 0, -1, -8, -5, -5, 1, 0, -2],
                [2, 7, 9, -3, -7, 9, 8, -1, -5],
                [0, -10, -5, 3, -1, 4, 0, -6, 10],
                [4, 0, -3, -5, -3, -6, 7, -9, 0],
                [-3, 0, 4, 1, 8, -8, -4, -4, -1],
            ],
            [
                [-10, -6],
                [9, -2],
                [5, -6],
                [0, 0],
                [-8, -6],
                [-5, -10],
                [5, 7],
                [8, -7],
                [8, 9],
            ],
            [
                [-212, -148],
                [49, 92],
                [-25, -96],
                [-199, -99],
                [193, 63],
                [8, 165],
                [-27, -12],
                [-2, 90],
                [168, 98],
                [109, 111],
                [91, -110],
                [-95, 148],
                [-38, 184],
                [-34, 17],
            ],
        ),
        (
            [
                [
                    -2.2377372,
                    2.4962028,
                    2.3706842,
                    -6.1641723,
                    -7.7244427,
                    6.9163574,
                    -3.5172153,
                ],
                [
                    -0.1231783,
                    8.7504083,
                    -9.3192284,
                    5.3913213,
                    -3.8243461,
                    -5.4981014,
                    3.6315429,
                ],
                [
                    -4.6085169,
                    -6.6119591,
                    4.2262321,
                    -7.4505959,
                    -2.7454212,
                    -5.9802176,
                    0.2512703,
                ],
                [
                    -5.2687429,
                    9.0644082,
                    -9.8138391,
                    5.2129308,
                    8.6160419,
                    4.3451935,
                    -4.6554018,
                ],
                [
                    2.1984573,
                    -7.5091841,
                    -9.7920768,
                    7.8810848,
                    1.1265284,
                    -5.7313989,
                    6.155259,
                ],
                [
                    0.1221676,
                    2.081951,
                    -7.4824826,
                    -0.6622015,
                    3.2673457,
                    6.370644,
                    2.5915962,
                ],
                [
                    4.2346841,
                    -1.5059308,
                    -0.9436938,
                    -0.8438108,
                    9.1540361,
                    3.9939651,
                    6.2639739,
                ],
            ],
            [
                [-1.4980047, -8.5072054, -0.918036],
                [5.9299124, 9.4434617, -7.456544],
                [-9.0532414, -9.5620221, -0.2883105],
                [5.3558574, -5.605461, 5.1978651],
                [1.1544469, -5.1492967, -9.6411583],
                [5.7039166, 0.9560253, 6.5583131],
                [-0.9948781, 3.5741401, -8.8319984],
            ],
            [
                [-2.29, 88.311, 101.614],
                [125.929, 169.988, -65.685],
                [-148.0, -12.564, -1.383],
                [217.773, 138.189, -46.282],
                [45.523, -29.441, -5.05],
                [113.888, 92.41, -29.53],
                [15.868, -57.423, -114.158],
            ],
        ),
    ],
)
def test_matrix_mul(a, b, res):
    a, b = Matrix(a), Matrix(b)
    assert [[round(x, 3) for x in y] for y in a @ b] == [
        [round(x, 3) for x in y] for y in res
    ]


@pytest.mark.parametrize(
    "a, res",
    [
        ([[-1, 0, 0], [1, 9, 2], [6, -7, 10]], [[-1, 1, 6], [0, 9, -7], [0, 2, 10]]),
        (
            [
                [
                    2.5283248,
                    -4.8624507,
                    -4.7038006,
                    0.3421778,
                    7.3514607,
                    -3.8274414,
                    7.2612634,
                    4.979486,
                    -1.7357245,
                    -9.6468335,
                    -9.2860831,
                ],
                [
                    -9.8698376,
                    -7.4551573,
                    9.2011299,
                    8.033886,
                    -5.4370666,
                    -9.3849644,
                    0.2988726,
                    -9.5501509,
                    -3.1199985,
                    -8.746493,
                    -6.1659248,
                ],
                [
                    6.9617862,
                    9.376941,
                    8.2711871,
                    0.9140624,
                    -5.0291993,
                    -7.0172479,
                    -5.5715747,
                    -6.1595622,
                    4.3720126,
                    1.614952,
                    -7.2235466,
                ],
                [
                    9.1849525,
                    2.1624836,
                    -0.1776206,
                    -9.8695998,
                    8.5475859,
                    9.9643153,
                    9.5895183,
                    -3.8389814,
                    3.497442,
                    8.1891971,
                    -5.1574211,
                ],
                [
                    -8.3766806,
                    5.6476089,
                    -2.8630811,
                    -7.3210128,
                    -6.8860712,
                    5.1324381,
                    9.9135237,
                    -3.9654722,
                    9.29575,
                    -3.8326753,
                    1.7598569,
                ],
                [
                    5.1334684,
                    -6.2304619,
                    -5.6971372,
                    5.0209441,
                    -5.1301941,
                    -3.3438787,
                    -3.9291827,
                    -6.7716238,
                    1.2531566,
                    8.5734029,
                    4.9105732,
                ],
                [
                    7.6800291,
                    -2.6375596,
                    9.4887364,
                    3.705962,
                    9.0132434,
                    4.1392715,
                    -1.509901,
                    -0.0959989,
                    8.1925902,
                    -9.5242947,
                    6.0741902,
                ],
                [
                    6.5787444,
                    8.4387942,
                    1.6398929,
                    0.2461451,
                    0.1187901,
                    -3.0061366,
                    -0.5829605,
                    2.3126771,
                    -2.1741217,
                    -0.7457311,
                    -3.5559353,
                ],
                [
                    -0.3670228,
                    -5.9921866,
                    -5.2943566,
                    1.4689932,
                    -5.4278887,
                    5.5444918,
                    -4.8432178,
                    -1.6058498,
                    4.0781111,
                    -5.9523647,
                    -4.4663757,
                ],
                [
                    0.8472695,
                    -5.9804946,
                    -1.4465567,
                    -3.910595,
                    9.2567123,
                    -0.9826849,
                    1.4275037,
                    -3.1933302,
                    6.6365312,
                    5.1251309,
                    5.8288419,
                ],
                [
                    -2.5138311,
                    -1.0419937,
                    -0.774828,
                    0.4986884,
                    4.7750773,
                    -9.5170037,
                    1.9801867,
                    -8.4407695,
                    -2.737738,
                    -8.2152199,
                    4.1969263,
                ],
            ],
            [
                [
                    2.5283248,
                    -9.8698376,
                    6.9617862,
                    9.1849525,
                    -8.3766806,
                    5.1334684,
                    7.6800291,
                    6.5787444,
                    -0.3670228,
                    0.8472695,
                    -2.5138311,
                ],
                [
                    -4.8624507,
                    -7.4551573,
                    9.376941,
                    2.1624836,
                    5.6476089,
                    -6.2304619,
                    -2.6375596,
                    8.4387942,
                    -5.9921866,
                    -5.9804946,
                    -1.0419937,
                ],
                [
                    -4.7038006,
                    9.2011299,
                    8.2711871,
                    -0.1776206,
                    -2.8630811,
                    -5.6971372,
                    9.4887364,
                    1.6398929,
                    -5.2943566,
                    -1.4465567,
                    -0.774828,
                ],
                [
                    0.3421778,
                    8.033886,
                    0.9140624,
                    -9.8695998,
                    -7.3210128,
                    5.0209441,
                    3.705962,
                    0.2461451,
                    1.4689932,
                    -3.910595,
                    0.4986884,
                ],
                [
                    7.3514607,
                    -5.4370666,
                    -5.0291993,
                    8.5475859,
                    -6.8860712,
                    -5.1301941,
                    9.0132434,
                    0.1187901,
                    -5.4278887,
                    9.2567123,
                    4.7750773,
                ],
                [
                    -3.8274414,
                    -9.3849644,
                    -7.0172479,
                    9.9643153,
                    5.1324381,
                    -3.3438787,
                    4.1392715,
                    -3.0061366,
                    5.5444918,
                    -0.9826849,
                    -9.5170037,
                ],
                [
                    7.2612634,
                    0.2988726,
                    -5.5715747,
                    9.5895183,
                    9.9135237,
                    -3.9291827,
                    -1.509901,
                    -0.5829605,
                    -4.8432178,
                    1.4275037,
                    1.9801867,
                ],
                [
                    4.979486,
                    -9.5501509,
                    -6.1595622,
                    -3.8389814,
                    -3.9654722,
                    -6.7716238,
                    -0.0959989,
                    2.3126771,
                    -1.6058498,
                    -3.1933302,
                    -8.4407695,
                ],
                [
                    -1.7357245,
                    -3.1199985,
                    4.3720126,
                    3.497442,
                    9.29575,
                    1.2531566,
                    8.1925902,
                    -2.1741217,
                    4.0781111,
                    6.6365312,
                    -2.737738,
                ],
                [
                    -9.6468335,
                    -8.746493,
                    1.614952,
                    8.1891971,
                    -3.8326753,
                    8.5734029,
                    -9.5242947,
                    -0.7457311,
                    -5.9523647,
                    5.1251309,
                    -8.2152199,
                ],
                [
                    -9.2860831,
                    -6.1659248,
                    -7.2235466,
                    -5.1574211,
                    1.7598569,
                    4.9105732,
                    6.0741902,
                    -3.5559353,
                    -4.4663757,
                    5.8288419,
                    4.1969263,
                ],
            ],
        ),
    ],
)
def test_matrix_transposition(a, res):
    a = Matrix(a)
    assert a.transpose() == Matrix(res)
