<template>
  <div class="home">
    <h1>Tester</h1>
    <input type="text" placeholder="username" class="home-input" id="username" required="required">
    <input type="password" placeholder="password" class="home-input" id="password" required="required">
    <input type="number" placeholder="game_id" min="0" class="home-input" id="game_id" required="required">
    <button v-on:click="createRoom" type="button" class="home-button">create room</button>
  </div>
</template>

<script>
import Client from '../mixins/Client.js'

export default {
  name: 'Home',
  mixins: [Client],
  methods: {
    async createRoom() {
      // Create a room and join it 
      var username = document.getElementById('username').value
      var password = document.getElementById('password').value
      var game_id = document.getElementById('game_id').value

      if (!username) return
      if (!password) return
      if (!game_id) return

      var roomMetaData = await this.getGameMetaData(username, password, game_id)

      if (!roomMetaData) return

      var room = {
        name: 'Room',
        path: '/room/' + roomMetaData.roomCode,
        params: roomMetaData
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
