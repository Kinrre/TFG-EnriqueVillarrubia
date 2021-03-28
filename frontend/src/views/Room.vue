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
  methods: {
    movePiece(position) {
      // Move the piece to the new position
      var board = this.$children[0]
      var pieces = board.$children

      // Index zero are the coordinates, so we start in the index one
      for (var i = 1; i < pieces.length; i++) {
        var piece = pieces[i]

        // Only move the piece in the 'fromPosition' to 'toPosition'
        if (position.fromPosition == piece.getStyle().transform) {
          piece.getStyle().transform = position.toPosition
          piece.capturePiece()
        }
      }
    }
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
    },
    move(position) {
      // Change the turn for the active player
      if (this.$store.getters.isActivePlayer) {
        this.$store.commit('setIsActivePlayer', false)
        return
      }

      // Change the turn for the NOT active player
      this.$store.commit('setIsActivePlayer', true)

      // Move the piece to the new position
      this.movePiece(position)
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
