import http from "http"
import express from "express";
import mongoose from "mongoose";


const app = express();
const PORT = 3000

// ranking data 
// 1 to 100 ranking
// {username: STRING, score: INT, timestamp: INT}
// let ranking = []

// users array
//  { username: STRING , highestScore: INT, games: [{ id: INT, score: INT, timestamp: STRING }] }
// let users = []

app.use(express.json());
app.use(express.urlencoded({ extended: true }));


mongoose
  .connect("mongodb://127.0.0.1:27017/task-manager", {
    useNewUrlParser: true,
    useCreateIndex: true,
  })
  .then(() => {
    console.log("Connected to MongoDB");
  })
  .catch((err) => {
    console.log(err);
  });

const UserSchema = new mongoose.Schema({
  username: String,
  highestScore: Number,
  games: Array,
});

const RankingSchema = new mongoose.Schema({
  id: Number,
  username: String,
  score: Number,
})

const User = mongoose.model("User", UserSchema);
const Ranking = mongoose.model("Ranking", RankingSchema);

function documentation(req, res) {
  res.send('Typing Test for the Developer');
}

async function loadRanking() {
  return await Ranking.find({})
}

async function updateRanking(id, data) {
  const records = new Ranking({
    id: id,
    username: data.username,
    score: data.score
  });
  await records.save()
    .catch((err) => {
      console.log("Error : " + err);
    });
}

async function deleteRanking(id) {
  await Ranking.findOneAndDelete({ "id": id })
}


async function rankingSystem(data) {
  let ranking = await loadRanking()
  updateRanking(ranking.length !== undefined ? ranking.length : 0, data)
}

// see the 1 to 10 ranking 
async function showRanking(req, res) {
  let ranking = await loadRanking()
  let newRank = ranking.sort(function (a, b) {
    return b.score - a.score;
  }).map(function (e, i) {
    var record = new Object();
    record.id = e.id
    record.username = e.username;
    record.score = e.score;
    record.rank = i + 1
    return record;
  });
  if (newRank.length > 10) {
    newRank.map(record => {
      if (record.rank > 10) {
        deleteRanking(record.id)
      }
    })
  }
  res.send(newRank)
}

async function makeUser(data) {
  const me = new User({
    username: data.username,
    highestScore: data.highestScore,
    games: data.games
  });
  await me.save()
    .catch((err) => {
      console.log("Error : " + err);
    });
}

async function loadUser(username) {
  const user = await User.findOne({ "username": username })

  return user
}

async function updateUser(username, data) {
  await User.findOneAndUpdate({ "username": username }, { "games": data.games, "highestScore": data.highestScore })
}

// post ranking data {username, score}
async function addData(req, res) {
  let data = req.body
  if (data === undefined || data === null || data.username === undefined || data.score === undefined || data.timestamp === undefined) {
    res.send({ ok: false })
    return
  }

  // let indexOfUser
  // users.map((user, index) => {
  //   if (user.username === data.username) {
  //     existUser = user
  //     indexOfUser = index
  //     users.splice(index, 1);
  //     return
  //   }
  // })

  let existUser = await loadUser(data.username)

  let game = {
    id: existUser?.games?.length !== undefined ? existUser.games.length : 0,
    score: data.score,
  }

  if (game.id !== 0) {
    if (existUser.highestScore < data.score) {
      existUser.highestScore = data.score
    }
    existUser?.games?.push(game)

    await updateUser(existUser.username, existUser)

  } else {
    existUser = {
      username: data.username,
      highestScore: data.score,
      games: [game]
    }
    await makeUser(existUser)
  }

  rankingSystem(data)

  res.send({ ok: true })
}

// get the user's profile
async function userInformation(req, res) {
  const { username } = req.params
  res.send({ ok: false, user: await loadUser(username) })

}

app.get('/', documentation);
app.get('/ranking', showRanking);
app.post('/addData', addData);
app.get('/user/:username', userInformation)


const httpServer = http.createServer(app);

const handleListen = () => console.log(`Listening on http://localhost:${PORT}`);
httpServer.listen(PORT, handleListen);


// OLD RANKING SYSTEM
// let indexOfData = null
  // if (ranking.length === 0) {
  //   ranking.push(data)
  //   return
  // }
  // ranking.map((record, index) => {
  //   if (record.score <= data.score) {
  //     indexOfData = indexOfData < index ? indexOfData : index
  //   }
  // })\
// let newRanking = []

//     ranking.map((record, index) => {
//       if (index < indexOfData) {
//         newRanking.push(record)
//       }
//     })
//     newRanking.push(data)
//     ranking.map((record, index) => {
//       if (index >= indexOfData) {
//         newRanking.push(record)
//       }
//     })

//     if (newRanking.length > 10) {
//       newRanking.pop()
//     }
//     ranking = newRanking