import axios from 'axios'
import Vue from 'vue'

const URL_GAME = 'http://localhost:8000/api/v1/matches/?game_id='
const URL_MATCH = 'http://localhost:8000/api/v1/matches/'
const HTTP_NOT_FOUND = 404

export default {
  state: {
    roomCode: null,
    isRoomCreated: false,

    isActivePlayer: false,

    boardSize: null,
    fen: null,

    player1: null,
    player2: null
  },
  getters: {
    getRoomCode(state) {
      return state.roomCode
    },
    isRoomCreated(state) {
      return state.isRoomCreated
    },
    isActivePlayer(state) {
      return state.isActivePlayer
    },
    getBoardSize(state) {
      return state.boardSize
    },
    getFen(state) {
      return state.fen
    }
  },
  actions: {
    async createRoom(context, payload) {
      var url = URL_GAME + payload.gameId

      try {
        var response = await axios.post(url, null, payload.authHeader)
      } catch (error) {
        if (error.response.status == HTTP_NOT_FOUND) {
          Vue.swal('Game not found!', 'Check the game_id is valid.', 'error')
        }
        return
      }

      context.dispatch('commitRoom', response)
    },
    async joinRoom(context, payload) {
      var url = URL_MATCH + '?room_code=' + payload.roomCode

      try {
        var response = await axios.get(url)
      } catch (error) {
        if (error.response.status == HTTP_NOT_FOUND) {
          Vue.swal('Room not found!', 'Check the invite link is valid.', 'error')
        }
        return
      }

      context.dispatch('commitRoom', response)
    },
    commitRoom(context, response) {
      var roomInfo = {
        'roomCode': response.data.room_code,
        'boardSize': response.data.game.board_size,
        'fen': response.data.game.fen
      }

      context.commit('setRoom', roomInfo)
    }
  },
  mutations: {
    setRoom(state, roomInfo) {
      state.roomCode = roomInfo.roomCode
      state.isRoomCreated = true
      state.boardSize = roomInfo.boardSize
      state.fen = roomInfo.fen
    }
  }
}
