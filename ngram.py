#import requests
#import re
import pandas as pd

#response = requests.get("https://books.google.com/ngrams/graph?content=solution%2Csolutions%2Cpedant%2Cpedants%2Cvegetable%2Cvegetables&case_insensitive=on&year_start=1970&year_end=2010&corpus=17&smoothing=3&share=&direct_url=t4%3B%2Csolution%3B%2Cc0%3B%2Cs0%3B%3Bsolution%3B%2Cc0%3B%3BSolution%3B%2Cc0%3B%3BSOLUTION%3B%2Cc0%3B.t4%3B%2Csolutions%3B%2Cc0%3B%2Cs0%3B%3Bsolutions%3B%2Cc0%3B%3BSolutions%3B%2Cc0%3B%3BSOLUTIONS%3B%2Cc0%3B.t4%3B%2Cpedant%3B%2Cc0%3B%2Cs0%3B%3Bpedant%3B%2Cc0%3B%3BPedant%3B%2Cc0%3B%3BPEDANT%3B%2Cc0%3B.t4%3B%2Cpedants%3B%2Cc0%3B%2Cs0%3B%3Bpedants%3B%2Cc0%3B%3BPedants%3B%2Cc0%3B.t4%3B%2Cvegetable%3B%2Cc0%3B%2Cs0%3B%3Bvegetable%3B%2Cc0%3B%3BVegetable%3B%2Cc0%3B%3BVEGETABLE%3B%2Cc0%3B.t4%3B%2Cvegetables%3B%2Cc0%3B%2Cs0%3B%3Bvegetables%3B%2Cc0%3B%3BVegetables%3B%2Cc0%3B%3BVEGETABLES%3B%2Cc0")

data = [{"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [0.00014675098233851713, 0.00014726754068306036, 0.00014635450090357457, 0.0001454912464039028, 0.0001447346809300143, 0.00014444658651362782, 0.00014225549268433366, 0.00014119276579549478, 0.00013883409535862614, 0.00013778156474992493, 0.00013693367964151548, 0.00013576516565600677, 0.00013301275219289112, 0.00013260850982987904, 0.0001298555725465381, 0.00012918807622749488, 0.00012821244290859925, 0.00012516849333873582, 0.00012355601493904293, 0.00012299288482608972, 0.00012059608632495967, 0.0001196432478829073, 0.00011804709760911335, 0.00011609706153389457, 0.00011608583783332245, 0.00011555004914498568, 0.00011362268147812366, 0.00011193122876258191, 0.00011095491504420352, 0.00010879645505415933, 0.00010650281184812878, 0.00010316305388511995, 0.000100073699562537, 9.725423834489837e-05, 9.368600836166608e-05, 8.972170092290201e-05, 8.56380141190779e-05, 7.165424275561754e-05, 6.866128237940454e-05, 6.41955901073743e-05, 5.789116306686992e-05], "ngram": "solution (All)"}, {"type": "EXPANSION", "timeseries": [0.00013538969869841821, 0.00013569392613135278, 0.00013467725269341221, 0.00013381116150412709, 0.00013261104426679334, 0.00013191355433913747, 0.00012967042234127542, 0.0001285180395435808, 0.00012625687356506075, 0.0001248609135343161, 0.00012372954993874634, 0.0001222975947062618, 0.00011936397952792634, 0.00011870162623901186, 0.00011598535638768226, 0.00011474172788439319, 0.00011374346753914974, 0.00011082741340422737, 0.0001092204121440383, 0.00010884182016265445, 0.00010627890047284641, 0.00010523091935153519, 0.00010344832428797548, 0.000101405090910183, 0.0001011041593821054, 0.00010044471335796905, 9.83512873062864e-05, 9.69229409487785e-05, 9.584479890431144e-05, 9.411835240566038e-05, 9.206770170879151e-05, 8.896572191068637e-05, 8.626700374796721e-05, 8.369501613612686e-05, 8.050590674559186e-05, 7.715822825308091e-05, 7.386364865981574e-05, 6.183834089564957e-05, 5.9401012549642473e-05, 5.5592825810890643e-05, 5.042336124461144e-05], "parent": "solution (All)", "ngram": "solution"}, {"type": "EXPANSION", "timeseries": [9.64737751019129e-06, 9.77531890384853e-06, 9.904838407237548e-06, 9.855234306347224e-06, 1.01620271379943e-05, 1.0446449128461868e-05, 1.0505981143588932e-05, 1.0575632586551365e-05, 1.04757790333159e-05, 1.0586067479120434e-05, 1.0758006413068091e-05, 1.0986810074038139e-05, 1.120090954438118e-05, 1.1386408524621011e-05, 1.1403808847327518e-05, 1.1892588580459623e-05, 1.1975989894251273e-05, 1.2017473116949467e-05, 1.2054363521331521e-05, 1.1877938829586907e-05, 1.2016155129198783e-05, 1.2025123136741708e-05, 1.2249769237574323e-05, 1.2483881229335176e-05, 1.2661724602886742e-05, 1.269925685067262e-05, 1.2920244574031261e-05, 1.2786560416446133e-05, 1.2997715852439537e-05, 1.267971869570569e-05, 1.2444634194253013e-05, 1.2310300007811747e-05, 1.2052061850096965e-05, 1.1841336864953128e-05, 1.1503787391120568e-05, 1.0934899624511932e-05, 1.0193704253781886e-05, 8.49349615756572e-06, 8.016390665943618e-06, 7.455674949596869e-06, 6.385654273799446e-06], "parent": "solution (All)", "ngram": "Solution"}, {"type": "EXPANSION", "timeseries": [1.7139061299076275e-06, 1.7982956478590496e-06, 1.7724098029248125e-06, 1.8248505934285016e-06, 1.961609525226647e-06, 2.0865830460284736e-06, 2.0790891994693084e-06, 2.0990936653626183e-06, 2.1014427602494834e-06, 2.3345837364883792e-06, 2.446123289701063e-06, 2.480760875706827e-06, 2.447863120583601e-06, 2.5204750662461654e-06, 2.4664073115283306e-06, 2.5537597626420653e-06, 2.492985475198241e-06, 2.3236068175590063e-06, 2.2812392736731065e-06, 2.2731258338483584e-06, 2.30103072291448e-06, 2.387205394630395e-06, 2.3490040835635488e-06, 2.208089394376397e-06, 2.3199538483303125e-06, 2.406078936344004e-06, 2.351149597806008e-06, 2.2217273973572967e-06, 2.1124002874525364e-06, 1.9983839527932493e-06, 1.9904759450842642e-06, 1.8870319666218296e-06, 1.7546339644728244e-06, 1.7178853438183848e-06, 1.676314224953655e-06, 1.6285730453091674e-06, 1.5806612054802827e-06, 1.322405702402258e-06, 1.2438791638184437e-06, 1.147089346886787e-06, 1.0821475484590337e-06], "parent": "solution (All)", "ngram": "SOLUTION"}, {"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [4.6104599604746e-05, 4.676404903420917e-05, 4.685611936376214e-05, 4.702275780183689e-05, 4.7294261313319505e-05, 4.6906035842247154e-05, 4.6925727994156266e-05, 4.684135447925136e-05, 4.6170038087568954e-05, 4.616740605862496e-05, 4.6239295418867444e-05, 4.6297283379967015e-05, 4.623344861849026e-05, 4.6543307608512153e-05, 4.585850559481384e-05, 4.5814248429516215e-05, 4.55383297435219e-05, 4.478556478813646e-05, 4.4552358580014175e-05, 4.4935749055444566e-05, 4.4457147055254616e-05, 4.4824368095370506e-05, 4.493101550094382e-05, 4.4801622574855825e-05, 4.499629680562326e-05, 4.529453156822325e-05, 4.4959089214963956e-05, 4.4788056405715384e-05, 4.4705064267093674e-05, 4.440386419446441e-05, 4.374892703903502e-05, 4.253062740693687e-05, 4.148567407469273e-05, 4.034788172394396e-05, 3.9062749993133495e-05, 3.639425523260798e-05, 3.37449913294969e-05, 2.8048376267163026e-05, 2.6707925402528567e-05, 2.437391399610078e-05, 2.1089708756250047e-05], "ngram": "solutions (All)"}, {"type": "EXPANSION", "timeseries": [4.230323975207284e-05, 4.288046984584071e-05, 4.298054591345135e-05, 4.3028020237605756e-05, 4.327453383926435e-05, 4.291029784196455e-05, 4.290426919136995e-05, 4.27893916951559e-05, 4.219591833784112e-05, 4.2162655258185365e-05, 4.234181791876576e-05, 4.23612015895612e-05, 4.22556721397476e-05, 4.249295099206003e-05, 4.185626156478455e-05, 4.1750673907310034e-05, 4.144554778966787e-05, 4.068090441121187e-05, 4.040062672824466e-05, 4.074862434728337e-05, 4.027000509917603e-05, 4.0503296207004625e-05, 4.045186246262996e-05, 4.017477528707657e-05, 4.0222646930487826e-05, 4.0303743714633e-05, 3.976364626266461e-05, 3.944880258391744e-05, 3.921484364712212e-05, 3.883315782461848e-05, 3.8122494255990856e-05, 3.693355029099621e-05, 3.599022290602859e-05, 3.486697096377611e-05, 3.3709733543219045e-05, 3.1422987896283825e-05, 2.919021920076505e-05, 2.4304798249171915e-05, 2.3151098806314014e-05, 2.111679386871401e-05, 1.8467533209332032e-05], "parent": "solutions (All)", "ngram": "solutions"}, {"type": "EXPANSION", "timeseries": [3.1662763717577036e-06, 3.251861426178948e-06, 3.2561022559699873e-06, 3.269984907612005e-06, 3.294247530253155e-06, 3.2711228803756446e-06, 3.293122777644645e-06, 3.3229414059730644e-06, 3.240971734287866e-06, 3.2543889249479563e-06, 3.2594274281499177e-06, 3.307978464103404e-06, 3.3456798454218576e-06, 3.419158409607397e-06, 3.380233270685754e-06, 3.4398455487202488e-06, 3.4760192063134e-06, 3.490019707896863e-06, 3.5367688074724616e-06, 3.5791792275371596e-06, 3.589611943815336e-06, 3.730281085673986e-06, 3.885853792391052e-06, 4.027224284592583e-06, 4.173261459072819e-06, 4.381115591708554e-06, 4.60657975054346e-06, 4.751491490294159e-06, 4.904154073821181e-06, 5.005534668660923e-06, 5.092229652551136e-06, 5.077335702350995e-06, 5.005459765275841e-06, 5.0098303420652106e-06, 4.910482078100488e-06, 4.557546714879988e-06, 4.1834002136706005e-06, 3.437557260050588e-06, 3.276390733238562e-06, 3.005649659826304e-06, 2.4017211330829014e-06], "parent": "solutions (All)", "ngram": "Solutions"}, {"type": "EXPANSION", "timeseries": [6.350834809154549e-07, 6.317177621895098e-07, 6.194711943408038e-07, 7.247526566191352e-07, 7.25479943801994e-07, 7.246151199069573e-07, 7.283360251416784e-07, 7.290213781223949e-07, 7.331480154399677e-07, 7.503618754916326e-07, 6.38050071951771e-07, 6.281033263024125e-07, 6.320966333208032e-07, 6.311982068447313e-07, 6.220107593435387e-07, 6.237289734859328e-07, 6.167627475406334e-07, 6.146406690277217e-07, 6.149630442970582e-07, 6.079454806240392e-07, 5.975300122632429e-07, 5.907908026918969e-07, 5.932992459228055e-07, 5.996230031866747e-07, 6.003884160626123e-07, 6.096722618817044e-07, 5.888632017558848e-07, 5.877623315037843e-07, 5.860665461503751e-07, 5.651717011850061e-07, 5.34203130493032e-07, 5.197414135896647e-07, 4.899914033882981e-07, 4.7108041810263656e-07, 4.4253437181396293e-07, 4.1372062144416434e-07, 3.713719150612503e-07, 3.0602075794052196e-07, 2.8043586297599177e-07, 2.514704675604662e-07, 2.2045441383511388e-07], "parent": "solutions (All)", "ngram": "SOLUTIONS"}, {"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [3.981210465811569e-07, 3.82262086612295e-07, 3.678964516038811e-07, 3.5328602897487044e-07, 3.191010298577078e-07, 3.074572587001358e-07, 2.8760469944488776e-07, 2.737187360340216e-07, 2.6064193807208624e-07, 2.5428443028203365e-07, 2.459427445589135e-07, 2.3120179780995134e-07, 2.2039729662732504e-07, 2.1169971226824608e-07, 2.1024895890953132e-07, 2.0613644867241628e-07, 1.9337188127727905e-07, 1.9019531349862007e-07, 1.852859373231906e-07, 1.7558435074148194e-07, 1.7416092374616147e-07, 1.6654408395235164e-07, 1.6086134684607195e-07, 1.5945162659284202e-07, 1.6009708937923607e-07, 1.5996524728643739e-07, 1.5908788018683036e-07, 1.621904304035685e-07, 1.645733091233075e-07, 1.645646216281398e-07, 1.8024984275008142e-07, 1.8414621995508996e-07, 1.8899189854363184e-07, 1.9955682103603832e-07, 2.0929102698527148e-07, 2.506788600824856e-07, 2.9657767759110646e-07, 2.5912878382732577e-07, 2.6618548136051834e-07, 2.8068728470387326e-07, 2.9450597438529513e-07], "ngram": "pedant (All)"}, {"type": "EXPANSION", "timeseries": [3.4352907363199847e-07, 3.3174644045175226e-07, 3.191286263396857e-07, 3.0674792737629885e-07, 2.8124512750439733e-07, 2.6982016062707513e-07, 2.5320110198988134e-07, 2.4313624586674063e-07, 2.311133978797183e-07, 2.2502647060004426e-07, 2.1806643043679026e-07, 2.0386792495433577e-07, 1.921711612697306e-07, 1.8281390217517973e-07, 1.8241290433707036e-07, 1.7791462271686343e-07, 1.6861528706613171e-07, 1.6554655246636685e-07, 1.6146511378727674e-07, 1.556672332623878e-07, 1.552107826390576e-07, 1.475062418876405e-07, 1.4318702312721143e-07, 1.4103082029188435e-07, 1.4158974741868796e-07, 1.3986064776158207e-07, 1.3794180883256297e-07, 1.3661622842521736e-07, 1.36857559190113e-07, 1.36718252211462e-07, 1.4440853135511134e-07, 1.4679072535273008e-07, 1.5153688082136796e-07, 1.5846568146571371e-07, 1.6868750053942806e-07, 2.0673081938379516e-07, 2.488723903785025e-07, 2.2214749760353568e-07, 2.286970541831579e-07, 2.4218904570716404e-07, 2.581902798226565e-07], "parent": "pedant (All)", "ngram": "pedant"}, {"type": "EXPANSION", "timeseries": [5.3055202897667186e-08, 4.787549450213646e-08, 4.6026770246972624e-08, 4.379386681867865e-08, 3.535490630416202e-08, 3.504272072518688e-08, 3.1865377638138984e-08, 2.8059562546494428e-08, 2.756231129045058e-08, 2.7491780280846408e-08, 2.620757426947356e-08, 2.579062220929375e-08, 2.4821481251332704e-08, 2.5350593751178556e-08, 2.4109142999455864e-08, 2.3770093575998478e-08, 2.047096168768446e-08, 2.057106370959413e-08, 1.968968899035417e-08, 1.778983779335671e-08, 1.7045333271832012e-08, 1.6656692786958567e-08, 1.610597826535403e-08, 1.6445432698170796e-08, 1.646575828065774e-08, 1.752986023006997e-08, 1.8412820220906464e-08, 2.1587995264431877e-08, 2.3723154234695746e-08, 2.3660834815229592e-08, 2.5124456166330285e-08, 2.512194236763727e-08, 2.5267356968632678e-08, 2.645492967547268e-08, 2.64684594242226e-08, 2.9079238318883782e-08, 3.281391463311982e-08, 2.9125766179812932e-08, 3.027466040824341e-08, 3.082065838100334e-08, 3.12810755076498e-08], "parent": "pedant (All)", "ngram": "Pedant"}, {"type": "EXPANSION", "timeseries": [1.5367700514912208e-09, 2.6401516584062535e-09, 2.741055017222808e-09, 2.744234779892908e-09, 2.5009960491484406e-09, 2.59437734787379e-09, 2.538219816867431e-09, 2.5229276207865733e-09, 1.966228901917333e-09, 1.7661794011430182e-09, 1.6687398526496873e-09, 1.5432506463218333e-09, 3.4046541062617207e-09, 3.5352163418878035e-09, 3.726911573005103e-09, 4.451732379554382e-09, 4.285632523462876e-09, 4.077697322659089e-09, 4.131134545559689e-09, 2.1272796857374487e-09, 1.9048078352718837e-09, 2.38114927775257e-09, 1.5683454535064811e-09, 1.975373602786894e-09, 2.0415836798903797e-09, 2.5747392947853396e-09, 2.7332511333609334e-09, 3.986206713919265e-09, 3.9925956984987465e-09, 4.185534601448231e-09, 1.0716855228639791e-08, 1.2233552234722619e-08, 1.2187660753631185e-08, 1.463620989485191e-08, 1.4135067021620834e-08, 1.4868802379806669e-08, 1.4891372579484141e-08, 7.855520043977191e-09, 7.213766769117076e-09, 7.677580615705893e-09, 5.034619054988809e-09], "parent": "pedant (All)", "ngram": "PEDANT"}, {"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [2.5834086558873537e-07, 2.471608055998331e-07, 2.3235263535426043e-07, 2.2077245910777167e-07, 2.0315241387537852e-07, 1.88002449417825e-07, 1.7394580797969184e-07, 1.5608527219918802e-07, 1.4565494397901698e-07, 1.3885519197945738e-07, 1.3656790225675358e-07, 1.2514502615143132e-07, 1.1782768316592751e-07, 1.130421647716722e-07, 1.1385919553217961e-07, 1.1058555411074572e-07, 1.0773733708343716e-07, 1.00687013647262e-07, 1.0038840742814565e-07, 9.833112134062715e-08, 9.941127242031809e-08, 9.345143687460628e-08, 8.963310379631448e-08, 8.969120018116022e-08, 8.806285732378325e-08, 8.810264416427215e-08, 8.664309384239946e-08, 8.168960022710995e-08, 8.041022019662186e-08, 7.820903746846852e-08, 7.78503129897753e-08, 8.269459326827797e-08, 8.203162822033912e-08, 8.520485954883432e-08, 8.934001950931605e-08, 1.1009143279545291e-07, 1.4156222105654592e-07, 1.2889484901634773e-07, 1.3230404527497797e-07, 1.4085601902635857e-07, 1.5158461141862034e-07], "ngram": "pedants (All)"}, {"type": "EXPANSION", "timeseries": [2.3535163151677807e-07, 2.2453721157944528e-07, 2.1187685443161777e-07, 2.0159340863301622e-07, 1.8610327044500862e-07, 1.7340057110816686e-07, 1.6144233378716827e-07, 1.4484691287667113e-07, 1.3622197160754824e-07, 1.2953909487935432e-07, 1.2735111454276193e-07, 1.1659419994560136e-07, 1.0967259912929097e-07, 1.0482280592733722e-07, 1.0497839956055291e-07, 1.0119327242819054e-07, 9.870910438231866e-08, 9.21748305618816e-08, 9.165580142475197e-08, 8.938119679312098e-08, 9.017903274915235e-08, 8.524463522365164e-08, 8.182445502110827e-08, 8.16917895869145e-08, 7.992062478479056e-08, 8.01072396987885e-08, 7.887951320688963e-08, 7.44664703233866e-08, 7.291040304835406e-08, 7.108715597122942e-08, 7.073696904415425e-08, 7.537592594530906e-08, 7.494108901693965e-08, 7.80690788206227e-08, 8.218185953978718e-08, 1.0211130633105573e-07, 1.318153165032397e-07, 1.2024020382536298e-07, 1.23794987890354e-07, 1.3181603861767143e-07, 1.4188948505022836e-07], "parent": "pedants (All)", "ngram": "pedants"}, {"type": "EXPANSION", "timeseries": [2.29892340719573e-08, 2.2623594020387826e-08, 2.0475780922642645e-08, 1.9179050474755447e-08, 1.7049143430369895e-08, 1.4601878309658138e-08, 1.250347419252356e-08, 1.1238359322516902e-08, 9.432972371468753e-09, 9.316097100103044e-09, 9.21678771399164e-09, 8.550826205829968e-09, 8.155084036636545e-09, 8.219358844334984e-09, 8.880795971626704e-09, 9.392281682555189e-09, 9.028232701118505e-09, 8.512183085380393e-09, 8.732606003393682e-09, 8.949924547506174e-09, 9.232239671165741e-09, 8.206801650954633e-09, 7.808648775206199e-09, 7.99941059424571e-09, 8.142232538992694e-09, 7.995404465483652e-09, 7.763580635509828e-09, 7.223129903723345e-09, 7.4998171482678e-09, 7.121881497239104e-09, 7.113343945621052e-09, 7.3186673229689146e-09, 7.0905392033994625e-09, 7.135780728211622e-09, 7.158159969528859e-09, 7.98012646439718e-09, 9.746904553306227e-09, 8.654645190984768e-09, 8.509057384623967e-09, 9.039980408687142e-09, 9.695126368391982e-09], "parent": "pedants (All)", "ngram": "Pedants"}, {"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [1.0227811138463494e-05, 1.0371146328225224e-05, 1.0682463861636885e-05, 1.0813102700727281e-05, 1.1151824821808987e-05, 1.1279623777227242e-05, 1.1445278837689849e-05, 1.1790475708396895e-05, 1.2010607361747003e-05, 1.2196538741753621e-05, 1.2468715120966018e-05, 1.2610362444677645e-05, 1.2855735442534363e-05, 1.2833229939295573e-05, 1.2791550854477203e-05, 1.273982578758088e-05, 1.2472577805868112e-05, 1.2211160527694379e-05, 1.2136178355603988e-05, 1.2002066845135622e-05, 1.2015324240824807e-05, 1.2018603375249118e-05, 1.2162734285376634e-05, 1.2448199230772972e-05, 1.2692345446144568e-05, 1.278503079049642e-05, 1.2764687003904587e-05, 1.2797532505715024e-05, 1.2644360428534386e-05, 1.2416611909316089e-05, 1.2157724691113409e-05, 1.1796432102885645e-05, 1.1563896208599544e-05, 1.1418331865797882e-05, 1.1247434837205869e-05, 1.1360131239257498e-05, 1.1510853425988898e-05, 9.817156367830648e-06, 9.644644957044571e-06, 9.372821961051158e-06, 8.980057788932072e-06], "ngram": "vegetable (All)"}, {"type": "EXPANSION", "timeseries": [8.628930345366825e-06, 8.7318103396683e-06, 8.971298181374246e-06, 9.053626074871448e-06, 9.297756670483587e-06, 9.343208928060318e-06, 9.44932552166782e-06, 9.70775506305342e-06, 9.837722765431473e-06, 9.936353308148682e-06, 1.011278124808866e-05, 1.0197336190945602e-05, 1.0377633121346922e-05, 1.036539509056768e-05, 1.0298671960689327e-05, 1.0265612607846769e-05, 1.0047604259203321e-05, 9.856848009803798e-06, 9.783744124953436e-06, 9.687216074131097e-06, 9.689989123476802e-06, 9.726182984845114e-06, 9.827107403128008e-06, 1.0049807705010088e-05, 1.0224507864872326e-05, 1.0290087629982736e-05, 1.0292247290116003e-05, 1.0301588970053541e-05, 1.0186341179568054e-05, 1.0042747297640225e-05, 9.886641497100104e-06, 9.65135326883423e-06, 9.503073670202866e-06, 9.382504166361677e-06, 9.292465360236487e-06, 9.47819392292461e-06, 9.698983636293893e-06, 8.29909017089189e-06, 8.178408734238474e-06, 7.998196088010445e-06, 7.75077296566451e-06], "parent": "vegetable (All)", "ngram": "vegetable"}, {"type": "EXPANSION", "timeseries": [1.401658494160074e-06, 1.4259751651479745e-06, 1.4859435850667069e-06, 1.515505199936992e-06, 1.59130416120336e-06, 1.6615870046215214e-06, 1.714521025470666e-06, 1.795171377645082e-06, 1.8712367883771158e-06, 1.947825775719788e-06, 2.0405134039590067e-06, 2.093906784596454e-06, 2.154499400473599e-06, 2.151518564070492e-06, 2.1762564626572256e-06, 2.175737303592281e-06, 2.1493853442474834e-06, 2.1004413091369704e-06, 2.1118961025682178e-06, 2.0855263755947817e-06, 2.0999114635092804e-06, 2.0713949392562166e-06, 2.1129647263608476e-06, 2.174478952708471e-06, 2.2432956419444442e-06, 2.2757989362227297e-06, 2.258621244826437e-06, 2.27932108438316e-06, 2.2494090379560864e-06, 2.1815153559145983e-06, 2.087050006593927e-06, 1.973343744664037e-06, 1.8944515107120554e-06, 1.874927631563748e-06, 1.8042823057839996e-06, 1.740105939721356e-06, 1.6676866932487298e-06, 1.3952885475581361e-06, 1.3470278001174545e-06, 1.2561068388095009e-06, 1.1151129797326575e-06], "parent": "vegetable (All)", "ngram": "Vegetable"}, {"type": "EXPANSION", "timeseries": [1.972222989365946e-07, 2.133608234089479e-07, 2.2522209519593162e-07, 2.4397142591884145e-07, 2.627639901220391e-07, 2.748278445454032e-07, 2.8143229055136286e-07, 2.8754926769839327e-07, 3.016478079384147e-07, 3.123596578851513e-07, 3.154204689183514e-07, 3.1911946913559017e-07, 3.236029207138407e-07, 3.1631628465739983e-07, 3.1662243113065157e-07, 2.9847587614183014e-07, 2.7558820241730633e-07, 2.5387120875361037e-07, 2.405381280823349e-07, 2.2932439540974364e-07, 2.2542365383872364e-07, 2.2102545114778748e-07, 2.2266215588777933e-07, 2.2391257305441415e-07, 2.2454193932779682e-07, 2.1914422429095533e-07, 2.1381846896214744e-07, 2.1662245127832387e-07, 2.086102110102469e-07, 1.9234925576126572e-07, 1.8403318741937775e-07, 1.717350893873767e-07, 1.6637102768462292e-07, 1.609000678724572e-07, 1.5068717118538189e-07, 1.4183137661153262e-07, 1.4418309644627569e-07, 1.227776493806232e-07, 1.1920842268864362e-07, 1.1851903423121257e-07, 1.1417184353490484e-07], "parent": "vegetable (All)", "ngram": "VEGETABLE"}, {"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [1.1943574765638232e-05, 1.2116544158402576e-05, 1.260937307989707e-05, 1.2962530330388029e-05, 1.354622504834424e-05, 1.3984385997137646e-05, 1.4385101152925019e-05, 1.4795077829278724e-05, 1.5319589936422873e-05, 1.571694662873467e-05, 1.6035469022719034e-05, 1.6528456727980612e-05, 1.6896838624396488e-05, 1.7082499673343978e-05, 1.7216551453559858e-05, 1.7213741943221195e-05, 1.6941460972118095e-05, 1.680027021474676e-05, 1.6500020598592918e-05, 1.6397963810683386e-05, 1.6453276554021352e-05, 1.6572587832846306e-05, 1.6686805827654488e-05, 1.7116445338924026e-05, 1.7486002686187673e-05, 1.7909224940889805e-05, 1.8098841232066274e-05, 1.8270088655672873e-05, 1.8172950441502117e-05, 1.8393502959465226e-05, 1.8234392726412807e-05, 1.793782742660304e-05, 1.774585610446268e-05, 1.763438057115049e-05, 1.7378422790719537e-05, 1.7059528238811644e-05, 1.64741956731567e-05, 1.3925231004106666e-05, 1.3440479567824088e-05, 1.2669579078306015e-05, 1.158737917705821e-05], "ngram": "vegetables (All)"}, {"type": "EXPANSION", "timeseries": [1.0757203654065961e-05, 1.0885088522627484e-05, 1.1294003646374525e-05, 1.1601866909976316e-05, 1.2102750198599616e-05, 1.2443490309773811e-05, 1.2771738251363526e-05, 1.3103877920782128e-05, 1.3566167451374764e-05, 1.392180391641367e-05, 1.4169669676838176e-05, 1.4601989538017993e-05, 1.4981130594346073e-05, 1.5170465823237983e-05, 1.5338190938304512e-05, 1.536081085110449e-05, 1.5135574098426982e-05, 1.504138318913257e-05, 1.478626693694553e-05, 1.4687048081084089e-05, 1.4741365313446814e-05, 1.4855991529267548e-05, 1.496848718878547e-05, 1.537088701297762e-05, 1.573759579644372e-05, 1.6154571702437742e-05, 1.6375738986036075e-05, 1.6569657028802404e-05, 1.6518009683100638e-05, 1.674419373947395e-05, 1.6638041155861822e-05, 1.6403919549442696e-05, 1.6248593445717624e-05, 1.613417303555512e-05, 1.5924435761657412e-05, 1.5647377300151027e-05, 1.5126673913203246e-05, 1.2794515636674727e-05, 1.2351454794649422e-05, 1.1642822028079535e-05, 1.067389644049399e-05], "parent": "vegetables (All)", "ngram": "vegetables"}, {"type": "EXPANSION", "timeseries": [9.856654230588902e-07, 1.0324485401724815e-06, 1.0991036181925058e-06, 1.121161387475565e-06, 1.1860537694831561e-06, 1.2720851470606119e-06, 1.3359073299008223e-06, 1.3989349554321961e-06, 1.446586127583162e-06, 1.4921203858518441e-06, 1.5698469236927589e-06, 1.6279849432976334e-06, 1.6137188530202756e-06, 1.6165082732706132e-06, 1.5936773739407987e-06, 1.5705435154294328e-06, 1.5314143248750561e-06, 1.497897203859923e-06, 1.4646593789231183e-06, 1.468819001664607e-06, 1.4701542698146243e-06, 1.480549242062677e-06, 1.4837717929237572e-06, 1.5070044940200335e-06, 1.5117571885119624e-06, 1.5189012693943887e-06, 1.499940286261595e-06, 1.4803450117791987e-06, 1.4403515089205548e-06, 1.4474931698974354e-06, 1.4041908116269042e-06, 1.3467298458635923e-06, 1.3122668990815458e-06, 1.3066407810973551e-06, 1.2713514771738638e-06, 1.2325596766718912e-06, 1.1688014995213183e-06, 9.778405163680354e-07, 9.41811265420256e-07, 8.869550356394029e-07, 7.921487679141137e-07], "parent": "vegetables (All)", "ngram": "Vegetables"}, {"type": "EXPANSION", "timeseries": [2.0070568851338066e-07, 1.990070956026102e-07, 2.162658153300375e-07, 2.3950203293614844e-07, 2.5742108026146783e-07, 2.6881054030322306e-07, 2.7745557166066905e-07, 2.922649530643996e-07, 3.068363574649473e-07, 3.030223264691553e-07, 2.959524221880981e-07, 2.984822466649868e-07, 3.0198917703013907e-07, 2.9552557683538385e-07, 2.846831413145472e-07, 2.8238757668727234e-07, 2.744725488160579e-07, 2.60989821754265e-07, 2.490942827242699e-07, 2.4209672793468986e-07, 2.4175697075991464e-07, 2.3604706151607907e-07, 2.3454684594526043e-07, 2.385538319263755e-07, 2.3664970123198665e-07, 2.357519690576737e-07, 2.2316195976860138e-07, 2.2008661509127186e-07, 2.1458924948092317e-07, 2.018160500938393e-07, 1.9216075892407908e-07, 1.8717803129675303e-07, 1.8499575966351195e-07, 1.9356675449801385e-07, 1.8263555188825974e-07, 1.795912619887271e-07, 1.7872026043213346e-07, 1.5287485106390314e-07, 1.4721350775441047e-07, 1.3980201458707596e-07, 1.2133396865010582e-07], "parent": "vegetables (All)", "ngram": "VEGETABLES"}, {"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [2.487950779617165e-06, 2.397005170706734e-06, 2.3990536757168e-06, 2.3433708921264236e-06, 2.2681429011787e-06, 2.2755325167013647e-06, 2.3779636388253167e-06, 2.3422336400561306e-06, 2.348511234373518e-06, 2.3359394129483595e-06, 2.4401302215640693e-06, 2.406242190642973e-06, 2.3647428208611084e-06, 2.40704562415317e-06, 2.4082133833758235e-06, 2.3755440910885487e-06, 2.298220543650586e-06, 2.1678139684614247e-06, 2.0866587579096825e-06, 2.024271162883094e-06, 1.8317234058429221e-06, 1.8009490142998985e-06, 1.8627938734385097e-06, 1.8620313494263234e-06, 1.865651709311221e-06, 1.9334106795554362e-06, 1.928812834149442e-06, 1.8677876893389924e-06, 1.8204287291569341e-06, 1.722015752595293e-06, 1.7095231620142419e-06, 1.6653422125756379e-06, 1.5932472257063068e-06, 1.5937739974753688e-06, 1.5737274519724207e-06, 1.4892457428520143e-06, 1.457164460459483e-06, 1.21612977237768e-06, 1.1618447848249502e-06, 1.0733711027555159e-06, 9.255306461231072e-07], "ngram": "datum (All)"}, {"type": "EXPANSION", "timeseries": [2.2497463305626297e-06, 2.1676463802577927e-06, 2.168673972846591e-06, 2.1131869191646857e-06, 2.046040744322194e-06, 2.038536828357402e-06, 2.101536681818418e-06, 2.0588332095680277e-06, 2.051918743615845e-06, 2.0252313431358615e-06, 2.0940091677143106e-06, 2.0484162145554104e-06, 2.003948371306511e-06, 2.0185166574395097e-06, 2.013506592187956e-06, 1.9831812291418567e-06, 1.9199100701631063e-06, 1.8284630576610134e-06, 1.7585679513233896e-06, 1.7084716513896377e-06, 1.5671762087419796e-06, 1.5353585760229699e-06, 1.5763778427364222e-06, 1.5599437931866435e-06, 1.547699769486956e-06, 1.5952297352279338e-06, 1.5963058785928297e-06, 1.5524339005423826e-06, 1.5008678084476351e-06, 1.4237823669256095e-06, 1.420705432662674e-06, 1.3866602038043702e-06, 1.314216579625541e-06, 1.2956708457880138e-06, 1.2485527106166825e-06, 1.194997358717436e-06, 1.1714180589349001e-06, 9.703430399505514e-07, 9.15807627658675e-07, 8.534856647202105e-07, 7.361664557947734e-07], "parent": "datum (All)", "ngram": "datum"}, {"type": "EXPANSION", "timeseries": [1.74509512618215e-07, 1.6859822835613158e-07, 1.714516623489241e-07, 1.722231469817156e-07, 1.730402609772292e-07, 1.855441606072158e-07, 1.8624696045727823e-07, 1.9556922633715397e-07, 2.030021428416668e-07, 2.1043181318093828e-07, 2.1273299921631406e-07, 2.1753537688644948e-07, 2.0898482132127227e-07, 2.2021281357150917e-07, 2.0816984504433223e-07, 2.0658837586649626e-07, 1.9700338376489007e-07, 1.8820832232384938e-07, 1.8442335252594993e-07, 1.8255413587147424e-07, 1.8068014233969215e-07, 1.8266071119147194e-07, 2.0212837625877e-07, 2.192157840649348e-07, 2.3929922170801934e-07, 2.596524930303141e-07, 2.583253961217581e-07, 2.5222480612033647e-07, 2.7624452262183953e-07, 2.588718116060461e-07, 2.535806881301791e-07, 2.448018656358337e-07, 2.4888500555724544e-07, 2.6999265807197456e-07, 2.9359398467931896e-07, 2.6521478600573444e-07, 2.650279680795263e-07, 2.288557437525794e-07, 2.3191049554801188e-07, 2.0554394950522691e-07, 1.758162753162651e-07], "parent": "datum (All)", "ngram": "Datum"}, {"type": "EXPANSION", "timeseries": [6.36949364363204e-08, 6.076056209280978e-08, 5.892804052128516e-08, 5.7960825980022234e-08, 4.906189587927656e-08, 5.1451527736747134e-08, 9.017999654962036e-08, 8.783120415094864e-08, 9.359034791600607e-08, 1.0027625663155959e-07, 1.3338805463344476e-07, 1.402905992011126e-07, 1.5180962823332527e-07, 1.6831615314215143e-07, 1.865369461435356e-07, 1.857744860801956e-07, 1.8130708972259007e-07, 1.5114258847656208e-07, 1.43667454060343e-07, 1.3324537562198202e-07, 8.386705476125047e-08, 8.292972708545676e-08, 8.428765444331735e-08, 8.287177217474501e-08, 7.865271811624552e-08, 7.852845129718844e-08, 7.418155943485414e-08, 6.312898267627329e-08, 4.331639808745942e-08, 3.936157406363756e-08, 3.5237041221388865e-08, 3.388014313543408e-08, 3.014564052352041e-08, 2.8110493615380553e-08, 3.158075667641924e-08, 2.903359812884381e-08, 2.071843344505656e-08, 1.6930988674549293e-08, 1.412666161826337e-08, 1.434148853007855e-08, 1.3547915012068756e-08], "parent": "datum (All)", "ngram": "DATUM"}, {"type": "CASE_INSENSITIVE", "parent": "", "timeseries": [0.0002703418529108603, 0.0002744256269579637, 0.0002833675513708537, 0.00028938148794363126, 0.00030342796389959403, 0.00031577267171607157, 0.0003286149481677317, 0.0003365006092021109, 0.00034787814885411147, 0.0003531975666451867, 0.0003620478104754251, 0.00037103261027888427, 0.0003807393924424624, 0.00038568396757909795, 0.0003872899402007793, 0.00038828445511691304, 0.0003883139357380319, 0.00039082952194543656, 0.0003875549436997971, 0.0003863033929779444, 0.0003801075182699216, 0.00038056736346853934, 0.00037885686404998917, 0.00037618139075285787, 0.00037001157962939554, 0.0003683931931846019, 0.0003634691415105148, 0.00036258576587247906, 0.0003628993040690278, 0.00036696940284335663, 0.0003698617202059852, 0.0003606822786618328, 0.0003525375644975222, 0.00034122109455633363, 0.00032968868900492713, 0.0003023926548654085, 0.0002720991696410887, 0.00021966525952978245, 0.0002066792779563305, 0.00018640142998265218, 0.0001601471151388978], "ngram": "data (All)"}, {"type": "EXPANSION", "timeseries": [0.00023316742226597853, 0.00023612065997440367, 0.00024330222368007526, 0.0002477815412151228, 0.00025938753346313855, 0.0002682046366057226, 0.0002781918446999043, 0.00028391401117135374, 0.00029181420437193343, 0.00029539678611659577, 0.00030195489775256386, 0.0003081790346186608, 0.00031543621610450955, 0.0003191575773858598, 0.0003201724237961961, 0.00032147200545296073, 0.00032137285701797476, 0.0003233465499111584, 0.0003207101919023054, 0.0003208832931704819, 0.0003159405563824943, 0.00031642332656442055, 0.0003153861824622644, 0.0003134850953106901, 0.00030915081983299127, 0.0003082410008313933, 0.0003040696194927607, 0.0003035961084866098, 0.0003046350944454649, 0.00030894135124981403, 0.00031179379688442817, 0.0003045843041036278, 0.00029864303152342994, 0.0002899315981526992, 0.00028076917182521096, 0.0002578016137704253, 0.00023217549148414816, 0.00018785355080451285, 0.0001769001925519357, 0.00015944692422635852, 0.00013691007916349918], "parent": "data (All)", "ngram": "data"}, {"type": "EXPANSION", "timeseries": [2.9435407668643165e-05, 3.065772834816016e-05, 3.214142573900366e-05, 3.356819122148279e-05, 3.569899594627454e-05, 3.821219693885983e-05, 4.041306082009604e-05, 4.208004247630015e-05, 4.4562177728429173e-05, 4.5971516166381275e-05, 4.7184523282339796e-05, 4.9106677449474644e-05, 5.110389507275873e-05, 5.2275335162578684e-05, 5.3021094832469574e-05, 5.32301959797873e-05, 5.350552705099939e-05, 5.4621513949574106e-05, 5.4767311147380883e-05, 5.441509503205972e-05, 5.3987466214623835e-05, 5.455982474294225e-05, 5.446356850110793e-05, 5.433146465553104e-05, 5.3578056914765125e-05, 5.3504334313661926e-05, 5.339311558470529e-05, 5.358838045919713e-05, 5.334042050110709e-05, 5.350184177846781e-05, 5.390628367812107e-05, 5.21838701388333e-05, 5.0392530933355116e-05, 4.797201108885929e-05, 4.584399825294635e-05, 4.185284394355092e-05, 3.754555889047749e-05, 2.993713522820534e-05, 2.8076492223287158e-05, 2.5445683786529116e-05, 2.2045036985218758e-05], "parent": "data (All)", "ngram": "Data"}, {"type": "EXPANSION", "timeseries": [7.73902297623863e-06, 7.647238635399845e-06, 7.9239019517748e-06, 8.031755507025601e-06, 8.34143449018094e-06, 9.355838171489137e-06, 1.0010042647731357e-05, 1.0506555554457009e-05, 1.1501766753748857e-05, 1.182926436220961e-05, 1.2908389440521465e-05, 1.3746898210748831e-05, 1.4199281265194128e-05, 1.425105503065944e-05, 1.4096421572113676e-05, 1.3582253684165022e-05, 1.3435551669057791e-05, 1.2861458084704022e-05, 1.2077440650110865e-05, 1.1005004775402735e-05, 1.0179495672803438e-05, 9.584212161176506e-06, 9.00711308661682e-06, 8.364830786636698e-06, 7.282702881639125e-06, 6.647858039546658e-06, 6.006406433048791e-06, 5.401276926672186e-06, 4.923789122455803e-06, 4.526209815074773e-06, 4.1616396434359814e-06, 3.914104419371662e-06, 3.502002040737092e-06, 3.317485314775175e-06, 3.075518926769811e-06, 2.7381971514322297e-06, 2.378119266463078e-06, 1.8745734970642452e-06, 1.7025931811076589e-06, 1.50882196976454e-06, 1.1919989901798544e-06], "parent": "data (All)", "ngram": "DATA"}]

stats = {}
for stat in data:
    if stat["type"] == "CASE_INSENSITIVE":
        ngram = stat["ngram"]
        stats[ngram] = stat["timeseries"]

df = pd.DataFrame(data=stats)
df.to_csv("data.csv")