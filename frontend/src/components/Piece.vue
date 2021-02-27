<template>
  <div :style="style"></div>
</template>

<script>
export default {
  name: 'Piece',
  props: {
    boardSize: Number,
    props_style: {
      piece: String,
      color: String,
      size: Number,
      offsetX: Number,
      offsetY: Number
    }
  },
  data() {
    return {
      dragging: false,
      style: {
        height: this.props_style.size + '%',
        width: this.props_style.size + '%',
        position: 'absolute',
        transform: 'translate(' + this.props_style.offsetX + '%, ' + this.props_style.offsetY + '%)',
        backgroundImage: this.getPiece(),
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'contain',
        userSelect: 'none',
        willChange: 'transform', // Performance boost
        cursor: 'grab'
      }
    }
  },
  methods: {
    onMouseDown(event) {
      // Ensure we only execute in the clicked component
      if (event.target.__vue__._uid != this._uid) return

      // Change the cursor to grab and tell that we are grabbing the piece
      this.dragging = true
      this.style.cursor = 'grabbing'

      // Center the piece into the cursor
      this.movePiece(event)
    },
    onMouseMove(event) {
      // Ensure we are dragging the component
      if (!this.dragging) return

      // Move the piece
      this.movePiece(event)
    },
    onMouseUp() {
      // Undo the cursor and tell that ww are not grabbing the piece
      this.dragging = false
      this.style.cursor = 'grab'

      // Center the piece into a square
      this.correctPosition()
    },
    movePiece(event) {
      // Ensure that we have a parent element
      if (!event.target.parentElement) return

      // Get the bounds of the board
      var boardBounds = event.target.parentElement.getBoundingClientRect()

      // Calculate the new raw offsets positions centering the piece into the mouse
      var rawOffsetX = event.clientX - boardBounds.left - this.$el.clientWidth / 2
      var rawOffsetY = event.clientY - boardBounds.top - this.$el.clientHeight / 2

      // Calculating the new relative offsets
      var offsetX = rawOffsetX * 100 / this.$el.clientWidth
      var offsetY = rawOffsetY * 100 / this.$el.clientHeight

      // Ensure that we are not outside the limits of the board
      var checkedOffsets = this.checkBounds(offsetX, offsetY)
      offsetX = checkedOffsets[0]
      offsetY = checkedOffsets[1]

      // Update the position
      this.style.transform = 'translate(' + offsetX + '%, ' + offsetY + '%)'
    },
    checkBounds(offsetX, offsetY) {
      // Check the bounds of the board size
      var limit = 100 * (this.boardSize - 1)

      // Check the X axis
      if (offsetX > limit) {
        offsetX = limit
      } else if (offsetX < 0) {
        offsetX = 0
      }
      
      // Check the Y axis
      if (offsetY > limit) {
        offsetY = limit
      } else if (offsetY < 0) {
        offsetY = 0
      }

      return [offsetX, offsetY]
    },
    correctPosition() {
      // Correct the position of a piece centering in a square
      var offsets = this.style.transform.match(/[+-]?\d+(\.\d+)?/g)
      var offsetX = offsets[0]
      var offsetY = offsets[1]

      offsetX = Math.round(offsetX / 100) * 100
      offsetY = Math.round(offsetY / 100) * 100

      // Update the position
      this.style.transform = 'translate(' + offsetX + '%, ' + offsetY + '%)'
    },
    getPiece() {
      // Get the piece background image
      return 'url(' + require('@/assets/pieces/' + this.props_style.color + '/' + this.props_style.color + '_' + this.props_style.piece + '.png') + ')'
    }
  },
  mounted() {
    window.addEventListener('mousedown', this.onMouseDown)
    window.addEventListener('mousemove', this.onMouseMove)
    window.addEventListener('mouseup', this.onMouseUp)
  },
  beforeDestroy() {
    window.removeEventListener('mousedown', this.onMouseDown)
    window.removeEventListener('mousemove', this.onMouseMove)
    window.removeEventListener('mouseup', this.onMouseUp)
  }
}
</script>

<style>
</style>
