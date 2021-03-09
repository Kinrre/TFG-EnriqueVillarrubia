import axios from 'axios'

export default {
  methods: {
    async getToken(username, password) {
      // Get token from the backend api
      var data = 'grant_type=password&username=' + username + '&password=' + password
      var response = await axios.post('http://localhost:8000/api/v1/auth/token', data)

      return response.data.access_token
    },
    async getTokenHeader(username, password) {
      // Build the Authorization header
      var token = await this.getToken(username, password)
      return {headers: {'Authorization': 'Bearer ' + token}}
    },
    async getGameMetaData(username, password, game_id) {
      // Return the room code, the boardSize and the fen string
      try {
        var authHeader = await this.getTokenHeader(username, password)
      } catch (error) {
        alert('invalid credentials')
        return
      }  

      var url = 'http://localhost:8000/api/v1/matches/?game_id=' + game_id

      try {
        var response = await axios.post(url, null, authHeader)
      } catch (error) {
        alert('game_id not found')
        return
      }

      var metadata = {
        room_code: response.data.room_code,
        boardSize: response.data.game.board_size,
        fen: response.data.game.fen
      }

      return metadata
    }
  }
}
