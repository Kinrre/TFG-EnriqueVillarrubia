<template>
  <div :style="style">
    <Coordinates :boardSize="boardSize"/>
    <Piece v-for="piece in pieces" v-bind:id="piece.id" v-bind:boardSize="boardSize" v-bind:props_style="piece" :key="piece.id"/>
  </div>
</template>

<script>
import Coordinates from './Coordinates.vue'
import Piece from './Piece.vue'

export default {
  name: 'Board',
  components: {
    Coordinates,
    Piece
  },
  props: {
    boardSize: Number,
    fen: String
  },
  data() {
    return {
      style: {
        height: 'auto',
        width: '100%',
        position: 'relative',
        margin: 'auto',
        backgroundImage: this.getBoard(),
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'contain',
        userSelect: 'none'
      },
      pieces: this.piecesFromFen()
    }
  },
  methods: {
    onResize() {
      // Ensure the div is a perfect square
      if (innerHeight > innerWidth) {
        this.style.height = innerWidth + 'px'
        this.style.width = innerWidth + 'px'
      } else {
        this.style.height = innerHeight + 'px'
        this.style.width = innerHeight + 'px'
      }
    },
    isLower(character) {
      // Check if a character is lowercase
      return (character === character.toLowerCase()) && (character !== character.toUpperCase())
    },
    getBoard() {
      // Get the board background image
      return 'url(' + require('@/assets/boards/' + this.boardSize + 'x' + this.boardSize + '_board.png') + ')'
    },
    piecesFromFen() {
      // Create pieces components from a fen string
      var pieces = []
      var row = 0, column = 0, id = 0

      for (let piece_type = 0; piece_type < this.fen.length; piece_type++) {
        var piece = {}, char_piece
        char_piece = this.fen.charAt(piece_type)
        
        if (parseInt(char_piece)) {
          column += parseInt(char_piece)
        } else if (char_piece == '/') {
          row += 1
          column = 0
        } else {
          piece.id = id
          piece.piece = char_piece
          piece.color = this.isLower(char_piece) ? 'black' : 'white'
          piece.size = 100 / this.boardSize
          piece.offsetX = 100 * column
          piece.offsetY = 100 * row
          pieces.push(piece)

          column += 1
          id += 1
        }
      }

      return pieces
    },
    removePiece(index) {
      // Remove a piece given his index
      this.pieces.splice(index, 1)
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
</style>
