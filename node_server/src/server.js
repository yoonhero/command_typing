import http from "http"
import express from "express";

const app = express();
const PORT = 3000

// ranking data 
// 1 to 100 ranking
// {username: STRING, score: INT, timestamp: INT}
let ranking = []

// users array
//  { username: STRING , highestScore: INT, games: [{ id: INT, score: INT, timestamp: STRING }] }
let users = []

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

function documentation(req, res) {
  res.send('Typing Test for the Developer');
}

function rankingSystem(data) {
  let indexOfData = null
  if (ranking.length === 0) {
    ranking.push(data)
    return
  }
  ranking.map((record, index) => {
    if (record.score <= data.score) {
      indexOfData = indexOfData < index ? indexOfData : index
    }
  })
  if (indexOfData !== null) {
    let newRanking = []
    ranking.map((record, index) => {
      if (index < indexOfData) {
        newRanking.push(record)
      }
    })
    newRanking.push(data)
    ranking.map((record, index) => {
      if (index >= indexOfData) {
        newRanking.push(record)
      }
    })

    if (newRanking.length > 10) {
      newRanking.pop()
    }
    ranking = newRanking
  } else {
    ranking.push(data)
  }
}

// see the 1 to 10 ranking 
function showRanking(req, res) {
  res.send(ranking)
}

// post ranking data {username, score}
function addData(req, res) {
  let data = req.body
  if (data === undefined || data === null || data.username === undefined || data.score === undefined || data.timestamp === undefined) {
    res.send({ ok: false })
    return
  }

  let existUser = {}
  let game = {}
  let indexOfUser

  users.map((user, index) => {
    if (user.username === data.username) {
      existUser = user
      indexOfUser = index
      users.splice(index, 1);
      return
    }
  })

  game = {
    id: existUser?.games?.length !== undefined ? existUser.games.length : 0,
    score: data.score,
    timestamp: data.timestamp
  }

  if (game.id !== 0) {
    if (existUser.highestScore < data.score) {
      existUser.highestScore = data.score
    }
    existUser?.games?.push(game)
    users.push(existUser)
  } else {
    existUser = {
      username: data.username,
      highestScore: data.score,
      games: [game]
    }
    users.push(existUser)
  }

  rankingSystem(data)

  res.send({ ok: true })
}

// get the user's profile
function userInformation(req, res) {
  const { username } = req.params
  users.map((user) => {
    if (user.username == username) {
      res.send({ ok: true, user })
      return
    }
  })
  res.send({ ok: false })

}

app.get('/', documentation);
app.get('/ranking', showRanking);
app.post('/addData', addData);
app.get('/user/:username', userInformation)


const httpServer = http.createServer(app);

const handleListen = () => console.log(`Listening on http://localhost:${PORT}`);
httpServer.listen(PORT, handleListen);
