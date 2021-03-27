<template>
  <div class="room">
    <Board :boardSize="boardSize" :fen="fen"/>
  </div>
</template>

<script>
import Board from '../components/Board.vue'

export default {
  name: 'Room',
  components: {
    Board
  },
  computed: {
    boardSize() {
      return this.$route.params.boardSize
    },
    fen() {
      return this.$route.params.fen
    },
  },
  sockets: {
    connect() {
      var color = this.$store.getters.getColor
      var roomCode = this.$route.params.roomCode
      this.$socket.emit('join', roomCode)

      if (color == 'black') {
        var data = {'roomCode': roomCode, 'playerName': this.$route.params.playerName}
        this.$socket.emit('room_completed', data)
      }
    },
    roomCompleted(playerName) {
      var color = this.$store.getters.getColor

      if (color == 'white') {
        this.$store.commit('setIsActivePlayer', true)
        
        var title = playerName + ' has joined the game!'
        var body = 'Enjoy the game!'
        this.$swal(title, body, 'success')
      }
    }
  },
  created() {
    // Ensure the room has been properly created
    if (this.boardSize == null || this.fen == null) this.$router.push('/')
  },
  mounted() {
    this.$socket.connect()
  }
}
</script>

<style>
</style>
