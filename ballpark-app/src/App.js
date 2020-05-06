// import React from 'react';
import React, { Component } from 'react';
import './App.css';
// import { Navbar, Jumbotron, Button } from 'react-bootstrap';
import Nav from 'react-bootstrap/Nav'
import { BrowserRouter } from 'react-router-dom';
import { Navbar, Button, Form, Col, Row} from 'react-bootstrap';
import Figure from 'react-bootstrap/Figure'
import 'bootstrap/dist/css/bootstrap.css';
import styles from './CompareButton.css';


let HME 
let AWY
let SEARCHINPUT

class App extends Component {

  constructor(props) {
    super(props)

    this.state = {
      homeTeam: null,
      awayTeam: null,
      predictionTable: [
        [0.53381564, 0.44348671, 0.35525779, 0.25101088, 0.32911323,
          0.323912, 0.58014366, 0.52952752, 0.44151939, 0.28076754, 0.42101708,
          0.24868299, 0.46667304, 0.42754784, 0.29464507, 0.36037679, 0.38111442, 0.55784127, 0.38793476, 0.29304615, 0.39060536, 0.4669181, 0.35130824, 0.33444937, 0.42496373, 0.44220127, 0.27442499, 0.44452377, 0.47236454, 0.36833853], [0.62198026, 0.53381564, 0.44188526, 0.32503332, 0.41345373, 0.40772967, 0.66504438, 0.61792266, 0.53183055, 0.35935494, 0.51097149, 0.32231437, 0.55699786, 0.51765006, 0.37509107, 0.44738635, 0.46945603, 0.6444882, 0.47663974, 0.37328664, 0.47944266, 0.55724079, 0.43762634, 0.41930267, 0.5150113, 0.53251891, 0.35210621, 0.53486092, 0.56262883, 0.45590024], [0.70410974, 0.62350524, 0.53381564, 0.41053553, 0.50481929, 0.49890622, 0.74170311, 0.70050923, 0.62163136, 0.44789453, 0.60177745, 0.40753319, 0.64519185, 0.60816687, 0.4646955, 0.53935519, 0.56135313, 0.72389832, 0.56843641, 0.46277923, 0.57118999, 0.6454172, 0.5295113, 0.51083506, 0.60564606, 0.62228146, 0.44008669, 0.62449088, 0.65040539, 0.54788406], [0.7964361, 0.73138765, 0.65309931, 0.53381564, 0.62632876, 0.62077669, 0.82521116, 0.79362976, 0.72981804, 0.57151622, 0.71302021, 0.53072345, 0.74935811, 0.71845981, 0.58801558, 0.6581292, 0.67784302, 0.81170133, 0.68410378, 0.58614761, 0.68652633, 0.74954299, 0.64917252, 0.63194462, 0.71631758, 0.73036288, 0.56375385, 0.73221216, 0.75362552, 0.66582151], [0.72773027, 0.65036515, 0.56258528, 0.43891656, 0.53381564, 0.52792504, 0.76333133, 0.72430463, 0.64854961, 0.47676931, 0.62926578, 0.43586013, 0.67132018, 0.63548131, 0.49368489, 0.56805959, 0.58972946, 0.74650787, 0.59668374, 0.4917589, 0.59938411, 0.67153739, 0.5583268, 0.53980028, 0.6330302, 0.64917955, 0.4688856, 0.6513198, 0.67634239, 0.57647433], [0.7323915, 0.65572427, 0.56839698, 0.44474967, 0.53969683, 0.53381564, 0.76757773, 0.72900267, 0.65392175, 0.48267273, 0.63476669, 0.4416846, 0.67651786, 0.64094262, 0.49959777, 0.57385365, 0.59543985, 0.75095764, 0.6023626, 0.49767138, 0.60505011, 0.67673329, 0.56415124, 0.54567023, 0.63850734, 0.65454719, 0.47477998, 0.65667201, 0.68149834, 0.58223852], [0.48689689, 0.3977337, 0.31347981, 0.2173593, 0.28903153, 0.28419541, 0.53381564, 0.48259551, 0.39582499, 0.24442854, 0.37601592, 0.21525381, 0.4203347, 0.38230956, 0.25715212, 0.31829401, 0.33788927, 0.51112609, 0.34436649, 0.25568292, 0.34690715, 0.42057461, 0.30977157, 0.29400259, 0.37981746, 0.39648639, 0.23863453, 0.39874043, 0.42591238, 0.32579959], [0.53809877, 0.44774116, 0.35921217, 0.25426249, 0.33292687, 0.3276948, 0.58433258, 0.53381564, 0.44577009, 0.28425833, 0.42522068, 0.25191459, 0.47096169, 0.43176801, 0.29823685, 0.36435594, 0.38518466, 0.56208473, 0.39203171, 0.29662664, 0.39471232, 0.47120701, 0.35524287, 0.33829366, 0.42917752, 0.44645328, 0.27786739, 0.44878015, 0.47665874, 0.37235442], [0.62385345, 0.53579966, 0.44385291, 0.32678531, 0.41538901, 0.40965687, 0.66681849, 0.61980367, 0.53381564, 0.36119293, 0.51296403, 0.32405874, 0.55896473, 0.51964097, 0.37696219, 0.44935877, 0.47144275, 0.64631329, 0.47862944, 0.37515416, 0.48143329, 0.55920744, 0.43958996, 0.42124567, 0.51700294, 0.53450363, 0.35392761, 0.53684435, 0.56459025, 0.4578791], [0.77058127, 0.70037909, 0.61777622, 0.49572479, 0.58999106, 0.58425746, 0.80210296, 0.76752255, 0.69870294, 0.53381564, 0.68081665, 0.49262009, 0.71962881, 0.68659836, 0.55062525, 0.62302265, 0.64366478, 0.78726747, 0.65024703, 0.54871786, 0.65279745, 0.71982742, 0.61368609, 0.5958006, 0.68432022, 0.69928467, 0.52593681, 0.70125991, 0.72421611, 0.63106205], [0.6432592, 0.55651884, 0.46457497, 0.34543662, 0.43582356, 0.43001684, 0.68512641, 0.63929755, 0.55454976, 0.38069753, 0.53381564, 0.34263363, 0.57946149, 0.54046281, 0.3967894, 0.47012059, 0.49231265, 0.66518219, 0.49951681, 0.39494656, 0.50232513, 0.5797014, 0.4602777, 0.44175062, 0.53783743, 0.55523264, 0.37326912, 0.55755541, 0.58501966, 0.47869235], [0.79844237, 0.73382076, 0.65590794, 0.53690523, 0.62923108, 0.62369623, 0.82699544, 0.7956566, 0.73226017, 0.57455509, 0.71555499, 0.53381564, 0.7516837, 0.72096534, 0.59102117, 0.66091825, 0.6805493, 0.81359236, 0.68678177, 0.5891573, 0.68919312, 0.75186744, 0.65199599, 0.63482875, 0.71883472, 0.73280189, 0.56680604, 0.73464051, 0.75592442, 0.6685794], [0.59975503, 0.51048644, 0.41896302, 0.3048616, 0.39097317, 0.38535586, 0.64390148, 0.59561397, 0.50849348, 0.33812022, 0.48759644, 0.30223583, 0.53381564, 0.49427828, 0.35343948, 0.42439573, 0.44624712, 0.62278373, 0.45337918, 0.35168059, 0.45616453, 0.53406065, 0.41476084, 0.39671919, 0.49163724, 0.50918448, 0.33107847, 0.51153617, 0.53949766, 0.43281478], [0.63710056, 0.54991051, 0.45793106, 0.33941644, 0.42926118, 0.42347627, 0.67933023, 0.63310952, 0.54793592, 0.37441434, 0.52715645, 0.33663718, 0.57293269, 0.53381564, 0.39040806, 0.46346602, 0.48563185, 0.6592015, 0.49283316, 0.38857576, 0.49564112, 0.57317358, 0.45364319, 0.43516783, 0.53118523, 0.54862069, 0.36703588, 0.55095006, 0.57851438, 0.47202454], [0.75838917, 0.68597655, 0.60166133, 0.47880541, 0.57351344, 0.56771824, 0.79113197, 0.75521953, 0.68425615, 0.51692889, 0.66592231, 0.47570672, 0.70576286, 0.67184377, 0.53381564, 0.60698823, 0.6279841, 0.77570402, 0.63469161, 0.53189756, 0.63729219, 0.70596728, 0.5975111, 0.57939, 0.66951, 0.6848532, 0.50902715, 0.68688078, 0.71048576, 0.61515836], [0.69944742, 0.61826141, 0.52826774, 0.40515536, 0.49925001, 0.49333718, 0.73741223, 0.69581468, 0.61637749, 0.4423922, 0.59642688, 0.40216552, 0.64007571, 0.60284549, 0.45915842, 0.53381564, 0.55586028, 0.71942355, 0.5629632, 0.45724548, 0.56572502, 0.6403025, 0.52395786, 0.50526713, 0.60031295, 0.61703105, 0.43460477, 0.6192524, 0.64532311, 0.54236005], [0.68043237, 0.5970689, 0.50607052, 0.38392108, 0.47703907, 0.4711418, 0.71983702, 0.67667604, 0.59514888, 0.42058621, 0.57485574, 0.38098758, 0.61934862, 0.58137663, 0.43717393, 0.51163814, 0.53381564, 0.70113231, 0.54097998, 0.43527887, 0.54376814, 0.61958071, 0.50174911, 0.48304673, 0.57880283, 0.59581489, 0.4128984, 0.59807913, 0.62472103, 0.5202237], [0.50963211, 0.41971113, 0.3333787, 0.23322955, 0.30807493, 0.30305599, 0.55636614, 0.50532769, 0.4177701, 0.26161456, 0.39758551, 0.2310157, 0.44264312, 0.40400642, 0.27490725, 0.33834788, 0.35852843, 0.53381564, 0.36518308, 0.27337393, 0.36779117, 0.44288604, 0.32954806, 0.31322921, 0.40146481, 0.41844278, 0.25555095, 0.42073462, 0.44828788, 0.34608628], [0.67413351, 0.5901167, 0.49886604, 0.37712782, 0.46985474, 0.46396749, 0.71398837, 0.67033901, 0.5881864, 0.4135797, 0.56779771, 0.37421469, 0.61253137, 0.5743467, 0.43009622, 0.50443535, 0.52663732, 0.6950586, 0.53381564, 0.42820849, 0.53661004, 0.61276502, 0.49454456, 0.47585425, 0.57176152, 0.58885595, 0.40593024, 0.59113243, 0.61794064, 0.51302702], [0.7597983, 0.68763406, 0.60350664, 0.48072866, 0.57539712, 0.56960831, 0.79240241, 0.75664121, 0.68591858, 0.51885282, 0.66763438, 0.47762892, 0.70736048, 0.67354037, 0.53573272, 0.60882491, 0.6297825, 0.77704185, 0.63647636, 0.53381564, 0.63907146, 0.70756425, 0.59936284, 0.58126668, 0.67121276, 0.68651392, 0.51095278, 0.68853568, 0.71206819, 0.61698095], [0.67166098, 0.58739686, 0.49605778, 0.37449275, 0.46705759, 0.4611749, 0.71168892, 0.66785188, 0.58546275, 0.41085793, 0.56503894, 0.37158783, 0.60986194, 0.57159819, 0.42734496, 0.50162713, 0.52383615, 0.69267247, 0.53101912, 0.4254603, 0.53381564, 0.61009617, 0.49173676, 0.47305325, 0.56900884, 0.58613362, 0.40322419, 0.58841464, 0.61528507, 0.5102202], [0.59951866, 0.5102404, 0.41872336, 0.30465299, 0.39073876, 0.38512269, 0.64367569, 0.59537681, 0.5082474, 0.33789991, 0.48735045, 0.30202823, 0.53357061, 0.49403217, 0.35321452, 0.42415524, 0.44600383, 0.6225524, 0.45313519, 0.35145614, 0.45592029, 0.53381564, 0.41452187, 0.39648357, 0.49139116, 0.50893842, 0.33086045, 0.51129015, 0.53925305, 0.43257309], [0.70769851, 0.6275545, 0.53811495, 0.41472524, 0.50914011, 0.50322787, 0.74500105, 0.70412331, 0.62568868, 0.45217304, 0.6059127, 0.41171366, 0.64913912, 0.61227852, 0.46899816, 0.54364709, 0.56560514, 0.72734002, 0.57267202, 0.46707963, 0.57541876, 0.64936333, 0.53381564, 0.51515381, 0.60976719, 0.62633599, 0.44435064, 0.62853586, 0.65432574, 0.55216247], [0.72293515, 0.64487241, 0.55665359, 0.43299803, 0.52782125, 0.52192274, 0.75895553, 0.71947244, 0.643044, 0.47076863, 0.6236334, 0.42995123, 0.66598757, 0.62988782, 0.48766973, 0.56214436, 0.58389361, 0.74192618, 0.59087818, 0.48574469, 0.59359094, 0.66620655, 0.5523833, 0.53381564, 0.62742114, 0.64367839, 0.46289636, 0.64583389, 0.67105134, 0.57058722], [0.63953997, 0.55252437, 0.46055508, 0.34178955, 0.4318518, 0.42605804, 0.68162763, 0.63556041, 0.55055187, 0.37689254, 0.52978945, 0.33900083, 0.57551605, 0.53644417, 0.39292562, 0.46609449, 0.48827163, 0.66157127, 0.49547437, 0.39108909, 0.49828259, 0.57575656, 0.45626332, 0.43776675, 0.53381564, 0.55123593, 0.36949408, 0.55356278, 0.58108866, 0.4746586], [0.62320443, 0.53511192, 0.44317052, 0.32617734, 0.41471774, 0.40898838, 0.66620393, 0.61915192, 0.53312752, 0.36055523, 0.51227325, 0.3234534, 0.55828302, 0.51895078, 0.37631304, 0.44867474, 0.47075384, 0.645681, 0.47793952, 0.37450626, 0.48074306, 0.5585258, 0.43890895, 0.42057174, 0.51631249, 0.53381564, 0.35329564, 0.53615682, 0.56391045, 0.45719287], [0.77612491, 0.70697402, 0.62521638, 0.50363185, 0.5976198, 0.59191909, 0.80707561, 0.77311833, 0.70531924, 0.54167764, 0.68765014, 0.50052678, 0.72596582, 0.69336381, 0.55843826, 0.63042178, 0.65088579, 0.79251647, 0.65740565, 0.55653732, 0.65993117, 0.72616165, 0.62115705, 0.6033939, 0.69111273, 0.70589357, 0.53381564, 0.70784353, 0.73048827, 0.63839498], [0.62099203, 0.53277006, 0.44084947, 0.32411237, 0.41243534, 0.4067156, 0.66410793, 0.61693036, 0.53078443, 0.35838838, 0.50992172, 0.32139745, 0.55596103, 0.51660106, 0.3741069, 0.44634797, 0.46840985, 0.64352509, 0.47559191, 0.37230438, 0.47839429, 0.55620408, 0.43659272, 0.41828014,
          0.51396195, 0.53147297, 0.35114846, 0.53381564, 0.56159481, 0.45485837], [0.59425734, 0.50477505, 0.41341082, 0.30004067, 0.38554577, 0.37995779, 0.63864483, 0.59009828, 0.50278148, 0.33302531, 0.48188903, 0.29743865, 0.52812483, 0.48856724, 0.34823519, 0.41882343, 0.44060753, 0.61740057, 0.44772233, 0.34648832, 0.45050157, 0.52837019, 0.4092251, 0.39126326, 0.48592738, 0.50347267, 0.3260374, 0.50582516, 0.53381564, 0.42721398], [0.69217128, 0.6101154, 0.51969322, 0.39689785, 0.4906566, 0.48474703, 0.73070132, 0.68848976, 0.60821676, 0.43392939, 0.58812533, 0.39392859, 0.63211822, 0.59458623, 0.45063408, 0.52525135, 0.54735756, 0.71243219, 0.55448748, 0.44872719, 0.55726074, 0.63234714, 0.51537687, 0.49667288, 0.59203666, 0.6088754, 0.42617707, 0.61111424, 0.63741591, 0.53381564]
      ],
      text: ' ',
      search: '',
      predictionResult: null
    }
  }

  submitHome = event => {
    var homeTeam = event.target.value;
    console.log(homeTeam)
    this.setState({
      homeTeam
    })
  }

  submitAway = event => {
    var awayTeam = event.target.value;
    console.log(awayTeam)
    this.setState({
      awayTeam
    })
  }

  compareButton = () => {
    this.setState({
      text: 'Home Team % chance of winning : ' + this.state.predictionTable[HME][AWY]//this.state.predictionResult
    });
  }

  updateSearch = event => {
    this.setState({
      search: event.target.value
    });
  }

  searchButton = () => {
    this.setState({
      SEARCHINPUT: this.state.SearchInput  
    })
    console.log(SEARCHINPUT)
  }


  render() {

    console.log("RENDER")

    const {
      predictionTable,
      homeTeam,
      awayTeam,
    } = this.state

    console.log(homeTeam)
    console.log(awayTeam)

    let predictionResult = 0
    if (homeTeam != null && awayTeam != null) {
      HME = homeTeam
      AWY = awayTeam
      predictionResult = predictionTable[homeTeam][awayTeam]
      console.log("PRED RESULT: " + predictionResult)
    }

    return (


      <div style={{backgroundColor: '#D3D3D3'}}>
        <div>
          <Navbar bg="dark" variant="dark" sticky="top">
              <Nav inline className="mr-auto" style={{ padding: 15 }}>
                <Navbar.Brand className="mr-sm-4 navbar-brand" href="#home" style={{ width: 100, height: 30 }}>Ballpark Bookie</Navbar.Brand>
                <Button className="mr-sm-4" variant="primary" href="#home" style={{ width: 100, height: 30 }}>Home</Button>
                <Button className="mr-sm-4" variant="danger" href="#home" style={{ width: 100, height: 30 }}>Big Predictions</Button>
                <Button className="mr-sm-4" color="#002D72" href="#home" style={{ width: 100, height: 30 }}>$$$</Button>
              </Nav>
              <Form inline style={{ padding: 15 }}>
                <input value={this.state.search} onChange={this.updateSearch} placeholder="Search"style={{ width: 100, height: 30 }}/>
                <Button className="ml-lg-4" variant="danger" style={{ width: 75, height: 30 }} onClick={this.searchButton}>Search</Button>
              </Form>
          </Navbar>
        </div>
        <div style={{backgroundColor: '#D3D3D3'}} >
          <Row>
            <Col md="3">
              <BrowserRouter>
                <div className="col-lg-9">
                  <div>
                    <h2>Schedules</h2></div>
                  <div>
                    <a href="https://www.mlb.com/dbacks/schedule">
                      <h5 className="text-dark"><u>Arizona Diamondbacks</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/braves/schedule">
                      <h5 className="text-dark"><u>Atlanta Braves</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/orioles/schedule">
                      <h5 className="text-dark"><u>Baltimore Orioles</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/redsox/schedule">
                      <h5 className="text-dark"><u>Boston Red Sox</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/whitesox/schedule">
                      <h5 className="text-dark"><u>Chicago White Sox</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/cubs/schedule">
                      <h5 className="text-dark"><u>Chicago Cubs</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/reds/schedule">
                      <h5 className="text-dark"><u>Cincinnati Reds</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/indians/schedule">
                      <h5 className="text-dark"><u>Cleveland Indians</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/rockies/schedule">
                      <h5 className="text-dark"><u>Colorado Rockies</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/tigers/schedule">
                      <h5 className="text-dark"><u>Detroit Tigers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/astros/schedule">
                      <h5 className="text-dark"><u>Houston Astros</u></h5></a></div>
                  <div className="  ">
                    <a href="https://www.mlb.com/royals/schedule">
                      <h5 className="text-dark"><u>Kansas City Royals</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/angels/schedule">
                      <h5 className="text-dark"><u>Los Angeles Angels</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/dodgers/schedule">
                      <h5 className="text-dark"><u>Los Angeles Dodgers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/marlins/schedule">
                      <h5 className="text-dark"><u>Miami Marlins</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/brewers/schedule">
                      <h5 className="text-dark"><u>Milwaukee Brewers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/twins/schedule">
                      <h5 className="text-dark"><u>Minnesota Twins</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/yankees/schedule">
                      <h5 className="text-dark"><u>New York Yankees</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/mets/schedule">
                      <h5 className="text-dark"><u>New York Mets</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/athletics/schedule">
                      <h5 className="text-dark"><u>Oakland Athletics</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/phillies/schedule">
                      <h5 className="text-dark"><u>Philadelphia Phillies</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/pirates/schedule">
                      <h5 className="text-dark"><u>Pittsburgh Pirates</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/padres/schedule">
                      <h5 className="text-dark"><u>San Diego Padres</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/giants/schedule">
                      <h5 className="text-dark"><u>San Fransisco Giants</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/mariners/schedule">
                      <h5 className="text-dark"><u>Seattle Mariners</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/cardinals/schedule">
                      <h5 className="text-dark"><u>St. Louis Cardinals</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/rays/schedule">
                      <h5 className="text-dark"><u>Tampa Bay Rays</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/rangers/schedule">
                      <h5 className="text-dark"><u>Texas Rangers</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/bluejays/schedule">
                      <h5 className="text-dark"><u>Toronto Blue Jays</u></h5></a></div>
                  <div>
                    <a href="https://www.mlb.com/nationals/schedule">
                      <h5 className="text-dark"><u>Washington Nationals</u></h5></a></div>
                </div>
              </BrowserRouter>
            </Col>
            <Col>
              <div className="col-lg-9 mx-auto">
                <Row>
                  <div style={{ padding: 40 }} >
                    <select as={Col} md="6" className="TeamOne-Select" onChange={this.submitHome}>
                      <option>Pick Home One</option>
                      <option value="29">Arizona Diamondbacks</option>
                      <option value="19">Atlanta Braves</option>
                      <option value="0">Baltimore Orioles</option>
                      <option value="2">Boston Red Sox</option>
                      <option value="8">Chicago White Sox</option>
                      <option value="20">Chicago Cubs</option>
                      <option value="24">Cincinnati Reds</option>
                      <option value="5">Cleveland Indians</option>
                      <option value="27">Colorado Rockies</option>
                      <option value="6">Detroit Tigers</option>
                      <option value="11">Houston Astros</option>
                      <option value="7">Kansas City Royals</option>
                      <option value="13">Los Angeles Angels</option>
                      <option value="26">Los Angeles Dodgers</option>
                      <option value="17">Miami Marlins</option>
                      <option value="23">Milwaukee Brewers</option>
                      <option value="9">Minnesota Twins</option>
                      <option value="3">New York Yankees</option>
                      <option value="16">New York Mets</option>
                      <option value="14">Oakland Athletics</option>
                      <option value="18">Philadelphia Phillies</option>
                      <option value="21">Pittsburgh Pirates</option>
                      <option value="28">San Diego Padres</option>
                      <option value="25">San Fransisco Giants</option>
                      <option value="12">Seattle Mariners</option>
                      <option value="22">St. Louis Cardinals</option>
                      <option value="4">Tampa Bay Rays</option>
                      <option value="10">Texas Rangers</option>
                      <option value="1">Toronto Blue Jays</option>
                      <option value="15">Washington Nationals</option>
                    </select>
                  </div>
                  <Row>
                  <div style={{ padding: 40 }}>
                    <div className="CompareButton" />
                      <Button backgroundColor="#002D72" type="compare" onClick={this.compareButton} >
                        Calculate
                      </Button>
                  </div>
                </Row>
                  {/*<Form>
                    <Form.Group as={Col} md="6" controlId="team1">
                      <Form.Label>Team One</Form.Label>
                      <Form.Control type="team" placeholder="Enter Team One" />
                    </Form.Group>
                    <Form.Group as={Col} md="6" controlId="team2">                    
                      <Form.Label>Team Two</Form.Label>
                      <Form.Control type="team" placeholder="Enter Team Two" />
                    </Form.Group>
                  </Form>*/}
                  <div style={{ padding: 40 }}>
                    <select as={Col} md="6" className="TeamTwo-Select" onChange={this.submitAway}>
                      <option>Pick Away Two</option>
                      <option value="29">Arizona Diamondbacks</option>
                      <option value="19">Atlanta Braves</option>
                      <option value="0">Baltimore Orioles</option>
                      <option value="2">Boston Red Sox</option>
                      <option value="8">Chicago White Sox</option>
                      <option value="20">Chicago Cubs</option>
                      <option value="24">Cincinnati Reds</option>
                      <option value="5">Cleveland Indians</option>
                      <option value="27">Colorado Rockies</option>
                      <option value="6">Detroit Tigers</option>
                      <option value="11">Houston Astros</option>
                      <option value="7">Kansas City Royals</option>
                      <option value="13">Los Angeles Angels</option>
                      <option value="26">Los Angeles Dodgers</option>
                      <option value="17">Miami Marlins</option>
                      <option value="23">Milwaukee Brewers</option>
                      <option value="9">Minnesota Twins</option>
                      <option value="3">New York Yankees</option>
                      <option value="16">New York Mets</option>
                      <option value="14">Oakland Athletics</option>
                      <option value="18">Philadelphia Phillies</option>
                      <option value="21">Pittsburgh Pirates</option>
                      <option value="28">San Diego Padres</option>
                      <option value="25">San Fransisco Giants</option>
                      <option value="12">Seattle Mariners</option>
                      <option value="22">St. Louis Cardinals</option>
                      <option value="4">Tampa Bay Rays</option>
                      <option value="10">Texas Rangers</option>
                      <option value="1">Toronto Blue Jays</option>
                      <option value="15">Washington Nationals</option>
                    </select>
                  </div>
                </Row>
                <Row>
                <div style={{ padding: 40 }}>
                  <Figure.Image style={{ padding: 10 }} width={150} height={150} alt="150x150" src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/San_Francisco_Giants_Cap_Insignia.svg/350px-San_Francisco_Giants_Cap_Insignia.svg.png" />
                </div>

                <div style={{ padding: 55
                 }}>

                </div>
                

                <div style={{ padding: 40 }}>
                  <Figure.Image style={{ padding: 10 }} width={150} height={150} alt="150x150" src="https://content.sportslogos.net/logos/54/63/full/4813_los_angeles_dodgers-primary-1972.png" />
                </div>
                </Row>
                <Row>
                  <h1>{this.state.text}</h1>
                </Row>
              </div>
              <Figure.Image style={{ padding: 10 }} width={850} height={300} alt="850x300" src="https://i0.wp.com/sportleaguemaps.com/wp-content/uploads/2020-MLB-Map.png?w=1324&ssl=1" />
            </Col>
          </Row>
        </div>
      </div>
    );
  }
}

export default App;