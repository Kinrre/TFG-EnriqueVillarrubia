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
      console.log('socket connected')
    }
  }
}
</script>

<style>
</style>
