<template>
  <div :style="board_style">
    <Piece v-for="piece in pieces" v-bind:props_style="piece.props_style" :key="piece.id"/>
  </div>
</template>

<script>
import Piece from './Piece.vue'

export default {
  name: 'Board',
  components: {
    Piece
  },
  props: {
    boardSize: Number,
    fen: String
  },
  data() {
    return {
      board_style: {
        height: 'auto',
        width: '100%',
        position: 'relative',
        margin: 'auto',
        backgroundImage: this.getBoard(),
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'contain',
        pointerEvents: 'none'
      },
      pieces: {}
    }
  },
  created() {
    this.pieces = this.piecesFromFen()
  },
  methods: {
    onResize() {
      // Ensure the div is a perfect square
      if (innerHeight > innerWidth) {
        this.board_style.height = innerWidth + 'px'
        this.board_style.width = innerWidth + 'px'
      } else {
        this.board_style.height = innerHeight + 'px'
        this.board_style.width = innerHeight + 'px'
      }
    },
    isLower(character) {
      return (character === character.toLowerCase()) && (character !== character.toUpperCase())
    },
    getBoard() {
      return 'url(' + require('@/assets/boards/' + this.boardSize + 'x' + this.boardSize + '_board.png') + ')'
    },
    piecesFromFen() {
      var pieces = []
      var row = 0, column = 0

      for (let piece_type = 0; piece_type < this.fen.length; piece_type++) {
        var piece = {props_style: {}}, char_piece
        char_piece = this.fen.charAt(piece_type)
        
        if (parseInt(char_piece)) {
          column += parseInt(char_piece)
        } else if (char_piece == '/') {
          row += 1
          column = 0
        } else {
          piece.props_style.piece = char_piece
          piece.props_style.color = this.isLower(char_piece) ? 'black' : 'white'
          piece.props_style.size = 100 / this.boardSize
          piece.props_style.offsetX = 100 * column
          piece.props_style.offsetY = 100 * row
          pieces.push(piece)

          column += 1
        }
      }

      return pieces;
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
