<template>
  <div class="home">
    <h1>Tester</h1>
    <input type="text" placeholder="username" class="home-input" id="username" required="required">
    <input type="password" placeholder="password" class="home-input" id="password" required="required">
    <button v-on:click="createRoom" type="button" class="home-button">join room</button>
  </div>
</template>

<script>
import Client from '../mixins/Client.js'

export default {
  name: 'Home',
  mixins: [Client],
  methods: {
    async createRoom() {
      // Join a created room
      var username = document.getElementById('username').value
      var password = document.getElementById('password').value

      if (!username) return
      if (!password) return

      var gameId = 'a'
      var roomMetaData = await this.getGameMetaDataJoin(gameId)
      

      if (!roomMetaData) return

      // update player2

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
