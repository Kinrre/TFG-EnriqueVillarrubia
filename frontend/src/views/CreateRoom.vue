<template>
  <div class="home">
    <h1>Create a room</h1>
    <input type="text" placeholder="username" class="home-input" id="username" required="required">
    <input type="password" placeholder="password" class="home-input" id="password" required="required">
    <input type="number" placeholder="game_id" min="0" class="home-input" id="game_id" required="required">
    <button v-on:click="joinRoom" type="button" class="home-button">create room</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    async joinRoom() {
      // Create a room and join it 
      var username = document.getElementById('username').value
      var password = document.getElementById('password').value
      var gameId = document.getElementById('game_id').value

      if (!username || !password || !gameId) {
        this.$swal('Missing values!', 'Check that you have filled all the fields.', 'warning')
        return
      }

      await this.login()

      if (this.$store.getters.isAuthenticated) {
        await this.createRoom()
      }

      if (this.$store.getters.isRoomCreated) {
        this.redirectToRoom()
      }
    },
    getCredentials() {
      // Get the credentials from the user
      var username = document.getElementById('username').value
      var password = document.getElementById('password').value
      return {'username': username, 'password': password}
    },
    getGameId() {
      // Get the gameId from the user
      var gameId = document.getElementById('game_id').value
      return gameId
    },
    async login() {
      // Login into the backend
      var credentials = this.getCredentials()
      await this.$store.dispatch('login', credentials)
    },
    async createRoom() {
      // Create a room to play
      var gameId = this.getGameId()
      var authHeader = this.$store.getters.getAuthHeader
      var payload = {'gameId': gameId, 'authHeader': authHeader}
      await this.$store.dispatch('createRoom', payload)
    },
    redirectToRoom() {
      // Redirect to the room created
      var room = {
        name: 'Room',
        path: '/room/' + this.$store.getters.getRoomCode,
        params: {
          'roomCode': this.$store.getters.getRoomCode,
          'boardSize': this.$store.getters.getBoardSize,
          'initialBoard': this.$store.getters.getInitialBoard
        }
      }

      console.log(room)

      var title = 'Send your friends this link!'
      var body = 'http://localhost:8080/join-room/' + this.$store.getters.getRoomCode

      this.$swal(title, body)

      this.$router.push(room)
    }
  }
}
</script>

<style>
.home {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

.home-button {
  font-size: 2vmax;
  padding: 4px 8px;
  font-weight: 700;
  margin-top: 0.5vh;
}

.home-input {
  margin-bottom: 0.5vh;
  font-size: 1vmax;
}
</style>
