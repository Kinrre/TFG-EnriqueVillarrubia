import axios from 'axios'
import Vue from 'vue'

import router from '../router'

const URL_GAME = 'http://localhost:8000/api/v1/matches/?game_id='
const URL_MATCH = 'http://localhost:8000/api/v1/matches/'

const HTTP_UNAUTHORIZED = 401
const HTTP_NOT_FOUND = 404

export default {
  state: {
    roomCode: null,
    isRoomCreated: false,

    boardSize: null,
    initialBoard: null,

    color: null,
    isActivePlayer: false,
  },
  getters: {
    getRoomCode(state) {
      return state.roomCode
    },
    isRoomCreated(state) {
      return state.isRoomCreated
    },
    getBoardSize(state) {
      return state.boardSize
    },
    getInitialBoard(state) {
      return state.initialBoard
    },
    isActivePlayer(state) {
      return state.isActivePlayer
    },
    getColor(state) {
      return state.color
    }
  },
  actions: {
    async createRoom(context, payload) {
      var url = URL_GAME + payload.gameId

      try {
        var response = await axios.post(url, null, payload.authHeader)
      } catch (error) {
        if (error.response.status == HTTP_UNAUTHORIZED) {
          // Remove token
          context.commit('setToken', null)

          // Go to login
          router.push('/login/')
        } else if (error.response.status == HTTP_NOT_FOUND) {
          Vue.swal('Game not found!', 'Check the game_id is valid.', 'error')
        }
        return
      }

      context.dispatch('commitRoom', response)
      context.commit('setColor', 'white')
    },
    async joinRoom(context, payload) {
      var url = URL_MATCH + '?room_code=' + payload.roomCode

      try {
        var response = await axios.get(url, payload.authHeader)
      } catch (error) {
        if (error.response.status == HTTP_UNAUTHORIZED) {
          // Remove token
          context.commit('setToken', null)

          // Go to login
          router.push('/login/')
        } else if (error.response.status == HTTP_NOT_FOUND) {
          Vue.swal('Room not found!', 'Check the invite link is valid.', 'error')

          // Go to home
          //router.push('/')
        }
        return
      }

      context.dispatch('commitRoom', response)
      context.commit('setColor', 'black')
    },
    commitRoom(context, response) {
      var roomInfo = {
        'roomCode': response.data.room_code,
        'boardSize': response.data.game.board_size,
        'initialBoard': response.data.game.initial_board
      }

      context.commit('setRoom', roomInfo)
    }
  },
  mutations: {
    setRoom(state, roomInfo) {
      state.roomCode = roomInfo.roomCode
      state.isRoomCreated = true
      state.boardSize = roomInfo.boardSize
      state.initialBoard = roomInfo.initialBoard
    },
    setColor(state, color) {
      state.color = color
    },
    setIsActivePlayer(state, active) {
      state.isActivePlayer = active
    },
  }
}
