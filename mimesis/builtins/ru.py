"""Specific data provider for Russia (ru)."""

import typing as t
from datetime import datetime

from mimesis.builtins.base import BaseSpecProvider
from mimesis.enums import Gender
from mimesis.locales import Locale
from mimesis.types import Seed

__all__ = ["RussiaSpecProvider"]


class RussiaSpecProvider(BaseSpecProvider):
    """Class that provides special data for Russia (ru)."""
    def __init__(self, seed: Seed = None) -> None:
        """Initialize attributes."""
        super().__init__(locale=Locale.RU, seed=seed)
        self._load_datafile(self._datafile)
        self._current_year = str(datetime.now().year)
        # Local tax office code. Used in tax-related identifiers - KPP, INN, OGRN.
        # Tax offices on contested territories between Ukraine and Russia are not included.
        self._tax_office_codes: t.Final[t.Sequence[str, ...]] = (
            "0001", "0002", "0003", "0004", "0005", "0006", "0007", "0008", "0009", "0010",
            "0019", "0023", "0100", "0101", "0102", "0103", "0104", "0105", "0106", "0107",
            "0108", "0109", "0110", "0200", "0201", "0202", "0203", "0204", "0205", "0206",
            "0207", "0208", "0209", "0210", "0211", "0212", "0213", "0214", "0215", "0216",
            "0217", "0218", "0219", "0220", "0221", "0222", "0223", "0224", "0225", "0226",
            "0227", "0228", "0229", "0230", "0231", "0232", "0233", "0234", "0235", "0236",
            "0237", "0238", "0239", "0240", "0241", "0242", "0243", "0244", "0245", "0246",
            "0247", "0248", "0249", "0250", "0251", "0252", "0253", "0254", "0255", "0256",
            "0257", "0258", "0259", "0260", "0261", "0262", "0263", "0264", "0265", "0266",
            "0267", "0268", "0269", "0270", "0271", "0272", "0273", "0274", "0275", "0276",
            "0277", "0278", "0279", "0280", "0300", "0301", "0302", "0303", "0304", "0305",
            "0306", "0307", "0308", "0309", "0310", "0311", "0312", "0313", "0314", "0315",
            "0316", "0317", "0318", "0319", "0320", "0321", "0322", "0323", "0324", "0325",
            "0326", "0327", "0400", "0401", "0402", "0403", "0404", "0405", "0406", "0407",
            "0408", "0409", "0410", "0411", "0500", "0501", "0502", "0503", "0504", "0505",
            "0506", "0507", "0508", "0509", "0510", "0511", "0512", "0513", "0514", "0515",
            "0516", "0517", "0518", "0519", "0520", "0521", "0522", "0523", "0524", "0525",
            "0526", "0527", "0528", "0529", "0530", "0531", "0532", "0533", "0534", "0535",
            "0536", "0537", "0538", "0539", "0540", "0541", "0542", "0543", "0544", "0545",
            "0546", "0547", "0548", "0549", "0550", "0552", "0553", "0554", "0560", "0561",
            "0562", "0570", "0571", "0572", "0573", "0600", "0601", "0602", "0603", "0604",
            "0605", "0606", "0607", "0608", "0700", "0701", "0702", "0703", "0704", "0705",
            "0706", "0707", "0708", "0709", "0710", "0711", "0712", "0713", "0714", "0715",
            "0716", "0717", "0718", "0719", "0720", "0721", "0722", "0723", "0724", "0725",
            "0726", "0800", "0801", "0802", "0803", "0804", "0805", "0806", "0807", "0808",
            "0809", "0810", "0811", "0812", "0813", "0814", "0815", "0816", "0817", "0900",
            "0901", "0902", "0903", "0904", "0905", "0906", "0907", "0908", "0909", "0910",
            "0911", "0912", "0913", "0914", "0915", "0916", "0917", "0918", "0919", "0920",
            "1000", "1001", "1002", "1003", "1004", "1005", "1006", "1007", "1011", "1012",
            "1013", "1014", "1015", "1016", "1017", "1018", "1019", "1020", "1021", "1031",
            "1032", "1033", "1034", "1035", "1036", "1037", "1038", "1039", "1040", "1100",
            "1101", "1102", "1103", "1104", "1105", "1106", "1107", "1108", "1109", "1110",
            "1111", "1112", "1113", "1114", "1115", "1116", "1117", "1118", "1119", "1120",
            "1121", "1122", "1123", "1200", "1201", "1202", "1203", "1204", "1205", "1206",
            "1207", "1208", "1209", "1210", "1211", "1212", "1213", "1214", "1215", "1216",
            "1217", "1218", "1219", "1220", "1221", "1222", "1223", "1224", "1225", "1226",
            "1300", "1301", "1302", "1303", "1304", "1305", "1306", "1307", "1308", "1309",
            "1310", "1311", "1312", "1313", "1314", "1315", "1316", "1317", "1318", "1319",
            "1320", "1321", "1322", "1323", "1324", "1325", "1326", "1327", "1328", "1400",
            "1401", "1402", "1403", "1404", "1405", "1406", "1407", "1408", "1409", "1410",
            "1411", "1412", "1413", "1414", "1415", "1416", "1417", "1418", "1419", "1420",
            "1421", "1422", "1423", "1424", "1425", "1426", "1427", "1428", "1429", "1430",
            "1431", "1432", "1433", "1434", "1435", "1436", "1437", "1438", "1439", "1440",
            "1441", "1442", "1443", "1444", "1445", "1446", "1447", "1448", "1449", "1450",
            "1500", "1501", "1502", "1503", "1504", "1505", "1506", "1507", "1508", "1509",
            "1510", "1511", "1512", "1513", "1514", "1515", "1516", "1517", "1600", "1601",
            "1602", "1603", "1604", "1605", "1606", "1607", "1608", "1609", "1610", "1611",
            "1612", "1613", "1614", "1615", "1616", "1617", "1618", "1619", "1620", "1621",
            "1622", "1623", "1624", "1625", "1626", "1627", "1628", "1629", "1630", "1631",
            "1632", "1633", "1634", "1635", "1636", "1637", "1638", "1639", "1640", "1641",
            "1642", "1643", "1644", "1645", "1646", "1647", "1648", "1649", "1650", "1651",
            "1652", "1653", "1654", "1655", "1656", "1657", "1658", "1659", "1660", "1661",
            "1662", "1663", "1664", "1665", "1667", "1668", "1669", "1670", "1671", "1672",
            "1673", "1674", "1675", "1676", "1677", "1679", "1681", "1682", "1683", "1684",
            "1685", "1686", "1687", "1688", "1689", "1690", "1691", "1700", "1701", "1702",
            "1703", "1704", "1705", "1706", "1707", "1708", "1709", "1710", "1711", "1712",
            "1713", "1714", "1715", "1716", "1717", "1718", "1719", "1720", "1721", "1722",
            "1723", "1724", "1800", "1801", "1802", "1803", "1804", "1805", "1806", "1807",
            "1808", "1809", "1810", "1811", "1812", "1813", "1814", "1815", "1816", "1817",
            "1818", "1819", "1820", "1821", "1822", "1823", "1824", "1825", "1826", "1827",
            "1828", "1829", "1830", "1831", "1832", "1833", "1834", "1835", "1836", "1837",
            "1838", "1839", "1840", "1841", "1900", "1901", "1902", "1903", "1904", "1905",
            "1906", "1907", "1908", "1909", "1910", "1911", "2000", "2001", "2002", "2003",
            "2004", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
            "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023",
            "2024", "2025", "2026", "2027", "2028", "2029", "2031", "2032", "2033", "2034",
            "2035", "2036", "2100", "2101", "2102", "2103", "2104", "2105", "2106", "2107",
            "2108", "2109", "2110", "2111", "2112", "2113", "2114", "2115", "2116", "2117",
            "2118", "2119", "2120", "2121", "2122", "2123", "2124", "2125", "2126", "2127",
            "2128", "2129", "2130", "2131", "2132", "2133", "2134", "2135", "2136", "2137",
            "2138", "2139", "2200", "2201", "2202", "2203", "2204", "2205", "2206", "2207",
            "2208", "2209", "2210", "2211", "2217", "2221", "2222", "2223", "2224", "2225",
            "2226", "2227", "2231", "2232", "2233", "2234", "2235", "2236", "2237", "2238",
            "2239", "2240", "2241", "2242", "2243", "2244", "2245", "2246", "2247", "2248",
            "2249", "2250", "2251", "2252", "2253", "2254", "2255", "2256", "2257", "2258",
            "2259", "2260", "2261", "2262", "2263", "2264", "2265", "2266", "2267", "2268",
            "2269", "2270", "2271", "2272", "2273", "2274", "2275", "2276", "2277", "2278",
            "2279", "2280", "2281", "2282", "2283", "2284", "2285", "2286", "2287", "2288",
            "2289", "2290", "2291", "2300", "2301", "2302", "2303", "2304", "2305", "2306",
            "2307", "2308", "2309", "2310", "2311", "2312", "2313", "2314", "2315", "2316",
            "2317", "2318", "2319", "2320", "2321", "2322", "2323", "2324", "2325", "2326",
            "2327", "2328", "2329", "2330", "2331", "2332", "2333", "2334", "2335", "2336",
            "2337", "2338", "2339", "2340", "2341", "2342", "2343", "2344", "2345", "2346",
            "2347", "2348", "2349", "2350", "2351", "2352", "2353", "2354", "2355", "2356",
            "2357", "2358", "2359", "2360", "2361", "2362", "2363", "2364", "2365", "2366",
            "2367", "2368", "2369", "2370", "2371", "2372", "2373", "2374", "2375", "2376",
            "2377", "2378", "2400", "2401", "2402", "2403", "2404", "2405", "2406", "2407",
            "2408", "2409", "2410", "2411", "2412", "2413", "2414", "2415", "2416", "2417",
            "2418", "2419", "2420", "2421", "2422", "2423", "2424", "2425", "2426", "2427",
            "2428", "2429", "2430", "2431", "2432", "2433", "2434", "2435", "2436", "2437",
            "2438", "2439", "2440", "2441", "2442", "2443", "2444", "2445", "2446", "2447",
            "2448", "2449", "2450", "2451", "2452", "2453", "2454", "2455", "2456", "2457",
            "2458", "2459", "2460", "2461", "2462", "2463", "2464", "2465", "2466", "2467",
            "2468", "2469", "2470", "2500", "2501", "2502", "2503", "2504", "2505", "2506",
            "2507", "2508", "2509", "2510", "2511", "2512", "2513", "2514", "2515", "2516",
            "2517", "2518", "2520", "2521", "2522", "2523", "2524", "2525", "2526", "2527",
            "2528", "2529", "2530", "2531", "2532", "2533", "2534", "2535", "2536", "2537",
            "2538", "2539", "2540", "2542", "2543", "2600", "2601", "2602", "2603", "2604",
            "2605", "2606", "2607", "2608", "2609", "2610", "2611", "2612", "2613", "2614",
            "2615", "2616", "2617", "2618", "2619", "2620", "2621", "2622", "2623", "2624",
            "2625", "2626", "2627", "2628", "2629", "2630", "2631", "2632", "2633", "2634",
            "2635", "2636", "2641", "2642", "2643", "2644", "2645", "2646", "2647", "2648",
            "2649", "2650", "2651", "2654", "2700", "2702", "2703", "2704", "2705", "2706",
            "2707", "2708", "2709", "2710", "2711", "2712", "2713", "2714", "2715", "2716",
            "2717", "2718", "2719", "2720", "2721", "2722", "2723", "2724", "2725", "2726",
            "2727", "2728", "2800", "2801", "2802", "2803", "2804", "2805", "2806", "2807",
            "2808", "2809", "2810", "2811", "2812", "2813", "2814", "2815", "2816", "2817",
            "2818", "2819", "2820", "2821", "2822", "2823", "2824", "2825", "2826", "2827",
            "2828", "2829", "2900", "2901", "2902", "2903", "2904", "2905", "2906", "2907",
            "2908", "2909", "2910", "2911", "2912", "2913", "2914", "2915", "2916", "2917",
            "2918", "2919", "2920", "2921", "2922", "2923", "2924", "2925", "2926", "2927",
            "2928", "2929", "2930", "2931", "2932", "2983", "3000", "3001", "3002", "3003",
            "3004", "3005", "3006", "3007", "3008", "3009", "3010", "3011", "3012", "3013",
            "3014", "3015", "3016", "3017", "3018", "3019", "3020", "3021", "3022", "3023",
            "3024", "3025", "3100", "3101", "3102", "3103", "3104", "3105", "3106", "3107",
            "3108", "3109", "3110", "3111", "3112", "3113", "3114", "3115", "3116", "3117",
            "3118", "3119", "3120", "3121", "3122", "3123", "3124", "3125", "3126", "3127",
            "3128", "3129", "3130", "3200", "3201", "3202", "3203", "3204", "3205", "3206",
            "3207", "3208", "3209", "3210", "3211", "3212", "3213", "3214", "3215", "3216",
            "3217", "3218", "3219", "3220", "3221", "3222", "3223", "3224", "3225", "3226",
            "3227", "3228", "3229", "3230", "3231", "3232", "3233", "3234", "3235", "3241",
            "3242", "3243", "3244", "3245", "3246", "3247", "3248", "3249", "3250", "3251",
            "3252", "3253", "3254", "3255", "3256", "3257", "3300", "3301", "3302", "3303",
            "3304", "3305", "3306", "3307", "3308", "3309", "3310", "3311", "3312", "3313",
            "3314", "3315", "3316", "3317", "3318", "3319", "3320", "3321", "3322", "3323",
            "3324", "3325", "3326", "3327", "3328", "3329", "3332", "3334", "3335", "3336",
            "3337", "3338", "3339", "3340", "3400", "3401", "3402", "3403", "3404", "3405",
            "3406", "3407", "3408", "3409", "3410", "3411", "3412", "3413", "3414", "3415",
            "3416", "3417", "3418", "3419", "3420", "3421", "3422", "3423", "3424", "3425",
            "3426", "3427", "3428", "3429", "3430", "3431", "3432", "3433", "3434", "3435",
            "3436", "3437", "3438", "3439", "3441", "3442", "3443", "3444", "3445", "3446",
            "3447", "3448", "3451", "3452", "3453", "3454", "3455", "3456", "3457", "3458",
            "3459", "3460", "3461", "3500", "3501", "3502", "3503", "3504", "3505", "3506",
            "3507", "3508", "3509", "3510", "3511", "3512", "3513", "3514", "3515", "3516",
            "3517", "3518", "3519", "3520", "3521", "3522", "3523", "3524", "3525", "3526",
            "3527", "3528", "3529", "3530", "3531", "3532", "3533", "3534", "3535", "3536",
            "3537", "3538", "3539", "3600", "3601", "3602", "3603", "3604", "3605", "3606",
            "3607", "3608", "3609", "3610", "3611", "3612", "3613", "3614", "3615", "3616",
            "3617", "3618", "3619", "3620", "3621", "3622", "3623", "3624", "3625", "3626",
            "3627", "3628", "3629", "3630", "3631", "3632", "3650", "3651", "3652", "3661",
            "3662", "3663", "3664", "3665", "3666", "3667", "3668", "3700", "3701", "3702",
            "3703", "3704", "3705", "3706", "3707", "3708", "3709", "3710", "3711", "3712",
            "3713", "3714", "3715", "3716", "3717", "3718", "3719", "3720", "3721", "3722",
            "3723", "3724", "3725", "3726", "3727", "3728", "3729", "3730", "3731", "3732",
            "3733", "3734", "3800", "3801", "3802", "3803", "3804", "3805", "3806", "3807",
            "3808", "3809", "3810", "3811", "3812", "3813", "3814", "3815", "3816", "3817",
            "3818", "3819", "3820", "3821", "3822", "3823", "3824", "3825", "3826", "3827",
            "3828", "3829", "3830", "3831", "3832", "3833", "3834", "3835", "3836", "3837",
            "3838", "3839", "3840", "3841", "3842", "3843", "3844", "3845", "3846", "3847",
            "3848", "3849", "3850", "3851", "3852", "3853", "3900", "3901", "3902", "3903",
            "3904", "3905", "3906", "3907", "3908", "3909", "3910", "3911", "3912", "3913",
            "3914", "3915", "3916", "3917", "3918", "3919", "3920", "3921", "3922", "3923",
            "3924", "3925", "3926", "3927", "3928", "4000", "4001", "4002", "4003", "4004",
            "4005", "4006", "4007", "4008", "4009", "4010", "4011", "4012", "4013", "4014",
            "4015", "4016", "4017", "4018", "4019", "4020", "4021", "4022", "4023", "4024",
            "4025", "4026", "4027", "4028", "4029", "4100", "4101", "4102", "4103", "4104",
            "4105", "4106", "4107", "4108", "4109", "4141", "4177", "4182", "4200", "4201",
            "4202", "4203", "4204", "4205", "4206", "4207", "4208", "4209", "4210", "4211",
            "4212", "4213", "4214", "4215", "4216", "4217", "4218", "4219", "4220", "4221",
            "4222", "4223", "4224", "4225", "4226", "4227", "4228", "4229", "4230", "4231",
            "4232", "4233", "4234", "4235", "4236", "4237", "4238", "4239", "4240", "4241",
            "4242", "4243", "4244", "4245", "4246", "4247", "4248", "4249", "4250", "4251",
            "4252", "4253", "4254", "4300", "4301", "4302", "4303", "4304", "4305", "4306",
            "4307", "4308", "4309", "4310", "4311", "4312", "4313", "4314", "4315", "4316",
            "4317", "4318", "4319", "4320", "4321", "4322", "4323", "4324", "4325", "4326",
            "4327", "4328", "4329", "4330", "4331", "4332", "4333", "4334", "4335", "4336",
            "4337", "4338", "4339", "4340", "4341", "4342", "4343", "4345", "4346", "4347",
            "4348", "4349", "4350", "4351", "4400", "4401", "4402", "4403", "4404", "4405",
            "4406", "4407", "4408", "4409", "4410", "4411", "4412", "4413", "4414", "4415",
            "4416", "4417", "4418", "4419", "4420", "4421", "4422", "4423", "4424", "4425",
            "4426", "4427", "4428", "4429", "4430", "4431", "4432", "4433", "4434", "4435",
            "4436", "4437", "4438", "4439", "4441", "4442", "4443", "4444", "4500", "4501",
            "4502", "4503", "4504", "4505", "4506", "4507", "4508", "4509", "4510", "4511",
            "4512", "4513", "4514", "4515", "4516", "4517", "4518", "4519", "4520", "4521",
            "4522", "4523", "4524", "4525", "4526", "4600", "4601", "4602", "4603", "4604",
            "4605", "4606", "4607", "4608", "4609", "4610", "4611", "4612", "4613", "4614",
            "4615", "4616", "4617", "4618", "4619", "4620", "4621", "4622", "4623", "4624",
            "4625", "4626", "4627", "4628", "4629", "4630", "4631", "4632", "4633", "4634",
            "4635", "4700", "4701", "4702", "4703", "4704", "4705", "4706", "4707", "4708",
            "4709", "4710", "4711", "4712", "4713", "4714", "4715", "4716", "4717", "4718",
            "4719", "4720", "4721", "4722", "4723", "4724", "4725", "4726", "4727", "4728",
            "4800", "4801", "4802", "4803", "4804", "4805", "4806", "4807", "4808", "4809",
            "4810", "4811", "4812", "4813", "4814", "4815", "4816", "4817", "4818", "4819",
            "4820", "4821", "4822", "4823", "4824", "4825", "4826", "4827", "4828", "4900",
            "4901", "4902", "4903", "4904", "4905", "4906", "4907", "4908", "4909", "4910",
            "4911", "4912", "5000", "5001", "5002", "5003", "5004", "5005", "5006", "5007",
            "5008", "5009", "5010", "5011", "5012", "5013", "5014", "5015", "5016", "5017",
            "5018", "5019", "5020", "5021", "5022", "5023", "5024", "5025", "5026", "5027",
            "5028", "5029", "5030", "5031", "5032", "5033", "5034", "5035", "5036", "5037",
            "5038", "5039", "5040", "5041", "5042", "5043", "5044", "5045", "5046", "5047",
            "5048", "5049", "5050", "5051", "5052", "5053", "5054", "5055", "5056", "5070",
            "5071", "5072", "5073", "5074", "5075", "5076", "5077", "5078", "5079", "5081",
            "5088", "5089", "5099", "5100", "5101", "5102", "5103", "5104", "5105", "5106",
            "5107", "5108", "5109", "5110", "5111", "5112", "5113", "5114", "5115", "5116",
            "5117", "5118", "5190", "5191", "5192", "5193", "5199", "5200", "5201", "5202",
            "5203", "5204", "5205", "5206", "5207", "5208", "5209", "5210", "5211", "5212",
            "5213", "5214", "5215", "5216", "5217", "5218", "5219", "5220", "5221", "5222",
            "5223", "5224", "5225", "5226", "5227", "5228", "5229", "5230", "5231", "5232",
            "5233", "5234", "5235", "5236", "5237", "5238", "5239", "5240", "5243", "5244",
            "5245", "5246", "5247", "5248", "5249", "5250", "5251", "5252", "5253", "5254",
            "5256", "5257", "5258", "5259", "5260", "5261", "5262", "5263", "5270", "5275",
            "5277", "5300", "5301", "5302", "5303", "5304", "5305", "5306", "5307", "5308",
            "5309", "5310", "5311", "5312", "5313", "5314", "5315", "5316", "5317", "5318",
            "5319", "5320", "5321", "5322", "5331", "5332", "5333", "5334", "5335", "5336",
            "5337", "5338", "5400", "5401", "5402", "5403", "5404", "5405", "5406", "5407",
            "5408", "5409", "5410", "5411", "5413", "5414", "5415", "5416", "5417", "5418",
            "5419", "5420", "5421", "5422", "5423", "5424", "5425", "5426", "5427", "5428",
            "5429", "5430", "5431", "5432", "5433", "5434", "5435", "5436", "5437", "5438",
            "5439", "5440", "5441", "5442", "5443", "5444", "5445", "5446", "5447", "5448",
            "5451", "5452", "5453", "5456", "5460", "5461", "5462", "5463", "5464", "5465",
            "5466", "5467", "5468", "5469", "5470", "5471", "5472", "5473", "5474", "5475",
            "5476", "5477", "5483", "5485", "5487", "5500", "5501", "5502", "5503", "5504",
            "5505", "5506", "5507", "5508", "5509", "5510", "5511", "5512", "5513", "5514",
            "5515", "5516", "5517", "5518", "5519", "5520", "5521", "5522", "5523", "5524",
            "5525", "5526", "5527", "5528", "5529", "5530", "5531", "5532", "5533", "5534",
            "5535", "5536", "5537", "5538", "5539", "5540", "5541", "5542", "5543", "5544",
            "5600", "5601", "5602", "5603", "5604", "5605", "5606", "5607", "5608", "5609",
            "5610", "5611", "5612", "5613", "5614", "5615", "5616", "5617", "5618", "5619",
            "5620", "5621", "5622", "5623", "5624", "5625", "5626", "5627", "5628", "5629",
            "5630", "5631", "5632", "5633", "5634", "5635", "5636", "5637", "5638", "5639",
            "5640", "5641", "5642", "5643", "5644", "5645", "5646", "5647", "5648", "5649",
            "5650", "5651", "5652", "5653", "5654", "5655", "5658", "5659", "5660", "5661",
            "5700", "5701", "5702", "5703", "5704", "5705", "5706", "5707", "5708", "5709",
            "5710", "5711", "5712", "5713", "5714", "5715", "5716", "5717", "5718", "5719",
            "5720", "5721", "5722", "5723", "5724", "5725", "5726", "5727", "5731", "5732",
            "5733", "5734", "5735", "5736", "5737", "5738", "5739", "5740", "5741", "5742",
            "5743", "5744", "5745", "5746", "5747", "5748", "5749", "5751", "5752", "5753",
            "5754", "5800", "5801", "5802", "5803", "5804", "5805", "5806", "5807", "5808",
            "5809", "5810", "5811", "5812", "5813", "5814", "5815", "5816", "5817", "5818",
            "5819", "5820", "5821", "5822", "5823", "5824", "5825", "5826", "5827", "5828",
            "5829", "5830", "5831", "5832", "5833", "5834", "5835", "5836", "5837", "5838",
            "5900", "5901", "5902", "5903", "5904", "5905", "5906", "5907", "5908", "5910",
            "5911", "5912", "5913", "5914", "5915", "5916", "5917", "5918", "5919", "5920",
            "5921", "5930", "5931", "5932", "5933", "5934", "5935", "5936", "5937", "5938",
            "5939", "5940", "5941", "5942", "5943", "5944", "5945", "5946", "5947", "5948",
            "5949", "5950", "5951", "5952", "5953", "5954", "5955", "5956", "5957", "5958",
            "5959", "5960", "5981", "6000", "6001", "6002", "6003", "6004", "6005", "6006",
            "6007", "6008", "6009", "6010", "6011", "6012", "6013", "6014", "6015", "6016",
            "6017", "6018", "6019", "6020", "6021", "6022", "6023", "6024", "6025", "6026",
            "6027", "6028", "6029", "6030", "6031", "6032", "6033", "6034", "6035", "6036",
            "6037", "6100", "6101", "6102", "6103", "6104", "6105", "6106", "6107", "6108",
            "6109", "6110", "6111", "6112", "6113", "6114", "6115", "6116", "6117", "6118",
            "6119", "6120", "6121", "6122", "6123", "6124", "6125", "6126", "6127", "6128",
            "6129", "6130", "6131", "6132", "6133", "6134", "6135", "6136", "6137", "6138",
            "6139", "6140", "6141", "6142", "6143", "6144", "6145", "6146", "6147", "6148",
            "6149", "6150", "6151", "6152", "6153", "6154", "6155", "6161", "6162", "6163",
            "6164", "6165", "6166", "6167", "6168", "6171", "6172", "6173", "6174", "6175",
            "6176", "6177", "6178", "6179", "6180", "6181", "6182", "6183", "6185", "6186",
            "6187", "6188", "6189", "6190", "6191", "6192", "6193", "6194", "6195", "6196",
            "6200", "6201", "6202", "6203", "6204", "6205", "6206", "6207", "6208", "6209",
            "6210", "6211", "6212", "6213", "6214", "6215", "6216", "6217", "6218", "6219",
            "6220", "6221", "6222", "6223", "6224", "6225", "6226", "6227", "6228", "6229",
            "6230", "6231", "6232", "6233", "6234", "6300", "6310", "6311", "6312", "6313",
            "6314", "6315", "6316", "6317", "6318", "6319", "6320", "6321", "6322", "6323",
            "6324", "6325", "6326", "6330", "6335", "6340", "6345", "6350", "6355", "6357",
            "6361", "6362", "6363", "6364", "6365", "6366", "6367", "6368", "6369", "6370",
            "6371", "6372", "6373", "6374", "6375", "6376", "6377", "6378", "6379", "6380",
            "6381", "6382", "6383", "6384", "6385", "6386", "6387", "6400", "6401", "6402",
            "6404", "6405", "6406", "6407", "6408", "6409", "6410", "6411", "6412", "6413",
            "6414", "6415", "6416", "6417", "6418", "6419", "6420", "6421", "6422", "6423",
            "6424", "6425", "6426", "6427", "6428", "6430", "6431", "6432", "6433", "6434",
            "6435", "6436", "6437", "6438", "6439", "6440", "6441", "6442", "6443", "6444",
            "6445", "6446", "6447", "6448", "6449", "6450", "6451", "6452", "6453", "6454",
            "6455", "6456", "6457", "6500", "6501", "6502", "6503", "6504", "6505", "6506",
            "6507", "6508", "6509", "6510", "6511", "6512", "6513", "6514", "6515", "6516",
            "6517", "6518", "6600", "6601", "6602", "6603", "6604", "6605", "6606", "6607",
            "6608", "6609", "6610", "6611", "6612", "6613", "6614", "6615", "6616", "6617",
            "6618", "6619", "6620", "6621", "6622", "6623", "6624", "6625", "6626", "6627",
            "6628", "6629", "6630", "6631", "6632", "6633", "6634", "6635", "6636", "6637",
            "6638", "6639", "6640", "6641", "6642", "6643", "6644", "6645", "6646", "6647",
            "6648", "6649", "6650", "6651", "6652", "6653", "6654", "6655", "6656", "6657",
            "6658", "6659", "6660", "6661", "6662", "6663", "6664", "6665", "6666", "6667",
            "6668", "6669", "6670", "6671", "6672", "6673", "6674", "6675", "6676", "6677",
            "6678", "6679", "6680", "6681", "6682", "6683", "6684", "6685", "6686", "6700",
            "6701", "6702", "6703", "6704", "6705", "6706", "6707", "6708", "6709", "6710",
            "6711", "6712", "6713", "6714", "6715", "6716", "6717", "6718", "6719", "6720",
            "6722", "6723", "6724", "6725", "6726", "6727", "6728", "6729", "6730", "6731",
            "6732", "6733", "6800", "6801", "6802", "6803", "6804", "6805", "6806", "6807",
            "6808", "6809", "6810", "6811", "6812", "6813", "6814", "6815", "6816", "6817",
            "6818", "6819", "6820", "6821", "6822", "6823", "6824", "6825", "6826", "6827",
            "6828", "6829", "6830", "6831", "6832", "6833", "6900", "6901", "6902", "6903",
            "6904", "6905", "6906", "6907", "6908", "6909", "6910", "6911", "6912", "6913",
            "6914", "6915", "6916", "6917", "6918", "6919", "6920", "6921", "6922", "6923",
            "6924", "6925", "6926", "6927", "6928", "6929", "6930", "6931", "6932", "6933",
            "6934", "6935", "6936", "6937", "6938", "6939", "6940", "6941", "6942", "6943",
            "6944", "6945", "6946", "6947", "6949", "6950", "6952", "7000", "7001", "7002",
            "7003", "7004", "7005", "7006", "7007", "7008", "7009", "7010", "7011", "7012",
            "7013", "7014", "7015", "7016", "7017", "7018", "7019", "7020", "7021", "7022",
            "7023", "7024", "7025", "7026", "7027", "7028", "7029", "7030", "7031", "7100",
            "7101", "7102", "7103", "7104", "7105", "7106", "7107", "7111", "7112", "7113",
            "7114", "7115", "7116", "7117", "7118", "7121", "7122", "7123", "7124", "7125",
            "7126", "7127", "7128", "7129", "7130", "7131", "7132", "7133", "7134", "7135",
            "7136", "7141", "7142", "7143", "7144", "7145", "7146", "7147", "7148", "7149",
            "7150", "7151", "7152", "7153", "7154", "7155", "7200", "7201", "7202", "7203",
            "7204", "7205", "7206", "7207", "7208", "7209", "7210", "7211", "7212", "7213",
            "7214", "7215", "7216", "7217", "7218", "7219", "7220", "7221", "7222", "7223",
            "7224", "7225", "7226", "7227", "7228", "7229", "7230", "7231", "7232", "7300",
            "7301", "7302", "7303", "7304", "7305", "7306", "7307", "7308", "7309", "7310",
            "7311", "7312", "7313", "7314", "7315", "7316", "7317", "7318", "7319", "7320",
            "7321", "7322", "7323", "7324", "7325", "7326", "7327", "7328", "7329", "7400",
            "7401", "7402", "7403", "7404", "7405", "7406", "7407", "7408", "7409", "7410",
            "7411", "7412", "7413", "7414", "7415", "7416", "7417", "7418", "7419", "7420",
            "7421", "7422", "7423", "7424", "7425", "7426", "7427", "7428", "7429", "7430",
            "7431", "7432", "7433", "7434", "7435", "7436", "7437", "7438", "7439", "7440",
            "7441", "7442", "7443", "7444", "7445", "7446", "7447", "7448", "7449", "7450",
            "7451", "7452", "7453", "7454", "7455", "7456", "7457", "7458", "7459", "7460",
            "7500", "7501", "7502", "7503", "7504", "7505", "7506", "7507", "7508", "7509",
            "7510", "7511", "7512", "7513", "7514", "7515", "7516", "7517", "7518", "7519",
            "7520", "7521", "7522", "7523", "7524", "7525", "7526", "7527", "7528", "7529",
            "7530", "7531", "7532", "7533", "7534", "7535", "7536", "7537", "7538", "7580",
            "7600", "7601", "7602", "7603", "7604", "7605", "7606", "7607", "7608", "7609",
            "7610", "7611", "7612", "7613", "7614", "7615", "7616", "7617", "7618", "7619",
            "7620", "7621", "7622", "7623", "7624", "7625", "7626", "7627", "7628", "7700",
            "7701", "7702", "7703", "7704", "7705", "7706", "7707", "7708", "7709", "7710",
            "7711", "7712", "7713", "7714", "7715", "7716", "7717", "7718", "7719", "7720",
            "7721", "7722", "7723", "7724", "7725", "7726", "7727", "7728", "7729", "7730",
            "7731", "7732", "7733", "7734", "7735", "7736", "7737", "7738", "7739", "7740",
            "7741", "7742", "7743", "7744", "7745", "7746", "7747", "7748", "7749", "7750",
            "7751", "7800", "7801", "7802", "7803", "7804", "7805", "7806", "7807", "7808",
            "7809", "7810", "7811", "7812", "7813", "7814", "7815", "7816", "7817", "7818",
            "7819", "7820", "7821", "7822", "7823", "7824", "7825", "7826", "7827", "7830",
            "7831", "7832", "7833", "7834", "7835", "7836", "7837", "7838", "7839", "7840",
            "7841", "7842", "7843", "7844", "7845", "7846", "7847", "7848", "7849", "7850",
            "7851", "7852", "7853", "7900", "7901", "7902", "7903", "7904", "7905", "7906",
            "7907", "8000", "8001", "8002", "8003", "8100", "8101", "8102", "8103", "8104",
            "8105", "8106", "8107", "8200", "8201", "8202", "8203", "8204", "8300", "8301",
            "8400", "8401", "8402", "8403", "8404", "8500", "8501", "8502", "8503", "8504",
            "8505", "8506", "8600", "8601", "8602", "8603", "8604", "8605", "8606", "8607",
            "8608", "8609", "8610", "8611", "8612", "8613", "8614", "8615", "8616", "8617",
            "8618", "8619", "8620", "8621", "8622", "8623", "8624", "8625", "8700", "8701",
            "8702", "8703", "8704", "8705", "8706", "8707", "8708", "8709", "8800", "8801",
            "8802", "8803", "8900", "8901", "8902", "8903", "8904", "8905", "8906", "8907",
            "8908", "8909", "8910", "8911", "8912", "8913", "8914", "9000", "9001", "9002",
            "9003", "9004", "9005", "9100", "9101", "9102", "9103", "9104", "9105", "9106",
            "9107", "9108", "9109", "9110", "9111", "9112", "9500", "9705", "9800", "9900",
            "9901", "9909", "9951", "9952", "9953", "9954", "9955", "9956", "9957", "9958"
        )

    class Meta:
        """The name of the provider."""

        name: t.Final[str] = "russia_provider"

    def generate_sentence(self) -> str:
        """Generate sentence from the parts.

        :return: Sentence.
        """
        sentences = self.extract(["sentence"])
        sentence = [
            self.random.choice(sentences[k]) for k in ("head", "p1", "p2", "tail")
        ]
        return " ".join(sentence)

    def patronymic(self, gender: t.Optional[Gender] = None) -> str:
        """Generate random patronymic name.

        :param gender: Gender of person.
        :return: Patronymic name.

        :Example:
            Алексеевна.
        """
        gender = self.validate_enum(gender, Gender)
        patronymics: t.List[str] = self.extract(["patronymic", str(gender)])
        return self.random.choice(patronymics)

    def passport_series(self, year: t.Optional[int] = None) -> str:
        """Generate random series of passport.

        :param year: Year of manufacture.
        :type year: int or None
        :return: Series.

        :Example:
            02 15.
        """
        if not year:
            year = self.random.randint(10, int(self._current_year[2:]))

        region = self.random.randint(1, 99)
        return f"{region:02d} {year}"

    def passport_number(self) -> int:
        """Generate random passport number.

        :return: Number.

        :Example:
            560430
        """
        return self.random.randint(100000, 999999)

    def series_and_number(self) -> str:
        """Generate a random passport number and series.

        :return: Series and number.

        :Example:
            57 16 805199.
        """
        series = self.passport_series()
        number = self.passport_number()
        return f"{series} {number}"

    def snils(self) -> str:
        """Generate snils with special algorithm.

        :return: SNILS.

        :Example:
            41917492600.
        """
        numbers = []
        control_codes = []

        for i in range(0, 9):
            numbers.append(self.random.randint(0, 9))

        for i in range(9, 0, -1):
            control_codes.append(numbers[9 - i] * i)

        control_code = sum(control_codes)
        code = "".join(map(str, numbers))

        if control_code in (100, 101):
            snils = code + "00"
            return snils

        if control_code < 100:
            snils = code + str(control_code)
            return snils

        if control_code > 101:
            control_code = control_code % 101
            if control_code == 100:
                control_code = 0
            snils = code + f"{control_code:02}"
            return snils

    def inn(self) -> str:
        """Generate random, but valid ``INN``.

        :return: INN.
        """

        def control_sum(nums: t.List[int], t: str) -> int:
            digits_dict = {
                "n2": [7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
                "n1": [3, 7, 2, 4, 10, 3, 5, 9, 4, 6, 8],
            }
            number = 0
            digits = digits_dict[t]

            for i, _ in enumerate(digits, start=0):
                number += nums[i] * digits[i]
            return number % 11 % 10

        numbers = []
        for x in range(0, 10):
            numbers.append(self.random.randint(1 if x == 0 else 0, 9))

        n2 = control_sum(numbers, "n2")
        numbers.append(n2)
        n1 = control_sum(numbers, "n1")
        numbers.append(n1)
        return "".join(map(str, numbers))

    def ogrn(self) -> str:
        """Generate random valid ``OGRN``.

        :return: OGRN.

        :Example:
            4715113303725.
        """
        numbers = []
        for _ in range(0, 12):
            numbers.append(self.random.randint(1 if _ == 0 else 0, 9))

        ogrn = "".join(map(str, numbers))
        check_sum = str(int(ogrn) % 11 % 10)

        return f"{ogrn}{check_sum}"

    def bic(self) -> str:
        """Generate random ``BIC`` (Bank ID Code).

        :return: BIC.

        :Example:
            044025575.
        """
        country_code = "04"
        code = f"{self.random.randint(1, 10):02}"
        bank_number = f"{self.random.randint(0, 99):02}"
        bank_office = f"{self.random.randint(50, 999):03}"
        bic = country_code + code + bank_number + bank_office
        return bic

    def kpp(self) -> str:
        """Generate random ``KPP``.

        :return: 'KPP'.

        :Example:
            560058652.
        """
        tax_code = self.random.choice(self._tax_office_codes)
        reg_code = f"{self.random.randint(1, 99):02}"
        reg_number = f"{self.random.randint(1, 999):03}"
        kpp = tax_code + reg_code + reg_number
        return kpp
