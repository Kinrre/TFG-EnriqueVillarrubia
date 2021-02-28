<template>
  <div id="app" :style="style">
    <Board :boardSize="8" :fen="'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'"/>
    <!--<Board :boardSize="5" :fen="'bqkbn/ppppp/5/PPPPP/BQKBN'"/>-->
  </div>
</template>

<script>
import Board from './components/Board.vue'

export default {
  name: 'App',
  components: {
    Board
  },
  data() {
    return {
      style: {
        height: 'auto',
        width: '100%'
      }
    }
  },
  methods: {
    onResize() {
      // Set the size of the outter div to the viewport size
      this.style.height = innerHeight + 'px'
      this.style.width = innerWidth + 'px'
    }
  },
  mounted() {
    window.addEventListener('resize', this.onResize)

    // Resize first time
    this.onResize()
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.onResize)
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: white;
  background-color: rgb(49, 46, 43);
  overflow: hidden;
}
</style>
