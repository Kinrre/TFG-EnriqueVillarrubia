import axios from 'axios'

const URL_GAMES = 'http://localhost:8000/api/v1/games/?skip=0&limit=100'
const URL_USERS = 'http://localhost:8000/api/v1/users/id/'

export default {
  state: {
    games: null
  },
  getters: {
    getGames(state) {
      return state.games
    }
  },
  actions: {
    async getGames(context) {
      var response = await axios.get(URL_GAMES)
      var games = response.data
      var cache = {}
      
      for (let i = 0; i < games.length; i++) {
        let game = games[i]
        let owner_id = game.owner_id

        if (!cache.owner_id) {
          let response_owner = await axios.get(URL_USERS + owner_id)
          cache.owner_id = response_owner.data.username
        }

        games[i].username = cache.owner_id
      }

      context.commit('setGames', games)
    }
  },
  mutations: {
    setGames(state, games) {
      state.games = games
    }
  }
}
