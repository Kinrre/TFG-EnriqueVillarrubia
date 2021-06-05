<template>
    <tr>
      <td>{{ name }}</td>
      <td>{{ author }}</td>
      <td>{{ boardSize }}</td>
      <td>{{ maxMovements }}</td>
      <td>{{ is_trained }}</td>
      <td><button v-on:click="createRoom" type="button" class="transparent">▶️</button></td>
    </tr>
</template>

<script>
export default {
  name: 'Game',
  props: {
    props_style: {
      id: Number,
      name: String,
      author: String,
      boardSize: Number,
      maxMovements: Number,
      is_trained: Boolean
    }
  },
  data() {
    return {
      id: this.props_style.id,
      name: this.props_style.name,
      author: this.props_style.username,
      boardSize: this.props_style.board_size + 'x' + this.props_style.board_size,
      maxMovements: this.props_style.maximum_movements,
      is_trained: this.props_style.is_trained ? "✔️" : "❌"
    }
  },
  methods: {
    async createRoom() {
      // Create a room to play
      var authHeader = this.$store.getters.getAuthHeader
      var payload = {'gameId': this.id, 'authHeader': authHeader}
      await this.$store.dispatch('createRoom', payload)

      if (this.$store.getters.isAuthenticated) {
        this.redirectToRoom()
      }
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

      var title = 'Send your friends this link!'
      var body = 'http://localhost:8080/join-room/' + this.$store.getters.getRoomCode

      this.$swal(title, body)

      this.$router.push(room)
    }
  }
}
</script>

<style>
.transparent {
  background-color: transparent;
  background-repeat: no-repeat;
  border: none;
  overflow: hidden;
  outline: none;
}
</style>
