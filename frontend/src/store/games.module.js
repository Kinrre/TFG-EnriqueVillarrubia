import axios from 'axios'

import router from '../router'

const URL_GAMES = 'http://localhost:8000/api/v1/games/?skip=0&limit=100'
const URL_ME_GAMES = 'http://localhost:8000/api/v1/users/me/games/?skip=0&limit=100'
const URL_USERS = 'http://localhost:8000/api/v1/users/id/'

const HTTP_UNAUTHORIZED = 401

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

        if (!cache[owner_id]) {
          let response_owner = await axios.get(URL_USERS + owner_id)
          cache[owner_id] = response_owner.data.username
        }

        games[i].username = cache[owner_id]
      }

      context.commit('setGames', games)
    },
    async getMeGames(context) {
      var authHeader = context.getters.getAuthHeader

      try {
        var response = await axios.get(URL_ME_GAMES, authHeader)
      } catch (error) {
        if (error.response.status == HTTP_UNAUTHORIZED) {
          // Remove token
          context.commit('setToken', null)

          // Go to login
          router.push('/login/')
        }
        return
      }

      var games = response.data
      
      for (let i = 0; i < games.length; i++) {
        games[i].username = context.getters.getUsername
      }

      context.commit('setGames', games)
    },
  },
  mutations: {
    setGames(state, games) {
      state.games = games
    }
  }
}
