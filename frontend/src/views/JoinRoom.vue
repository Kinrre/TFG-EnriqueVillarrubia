<template>
  <div class="home">
    <h1>Tester</h1>
    <input type="text" placeholder="username" class="home-input" id="username" required="required">
    <input type="password" placeholder="password" class="home-input" id="password" required="required">
    <button v-on:click="joinRoom" type="button" class="home-button">join room</button>
  </div>
</template>

<script>
export default {
  name: 'Home',
  methods: {
    async joinRoom() {
      // Join a room
      var username = document.getElementById('username').value
      var password = document.getElementById('password').value

      if (!username || !password) {
        this.$swal('Missing values!', 'Check that you have filled all the fields.', 'warning')
        return
      }

      await this.login()

      if (this.$store.getters.isAuthenticated) {
        await this.registerRoom()
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
    async login() {
      // Login into the backend
      var credentials = this.getCredentials()
      await this.$store.dispatch('login', credentials)
    },
    async registerRoom() {
      var roomCode = window.location.href.substring(window.location.href.lastIndexOf('/') + 1)
      var payload = {'roomCode': roomCode}
      await this.$store.dispatch('joinRoom', payload)
    },
    redirectToRoom() {
      // Redirect to the room created
      var credentials = this.getCredentials()
      var room = {
        name: 'Room',
        path: '/room/' + this.$store.getters.getRoomCode,
        params: {
          'roomCode': this.$store.getters.getRoomCode,
          'boardSize': this.$store.getters.getBoardSize,
          'fen': this.$store.getters.getFen,
          'playerName': credentials.username
        }
      }

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
