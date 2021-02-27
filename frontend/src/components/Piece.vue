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
      // Undo the cursor
      this.dragging = false
      this.style.cursor = 'grab'
    },
    movePiece(event) {
      // Get the bounds of the board
      var board_bounds = event.target.parentElement.getBoundingClientRect()

      // Calculate the new offsets positions centering the piece into the mouse
      var offsetX = event.clientX - board_bounds.left - this.$el.clientWidth / 2
      var offsetY = event.clientY - board_bounds.top - this.$el.clientHeight / 2

      // Update the position
      this.style.transform = 'matrix(1, 0, 0, 1, ' + offsetX + ', ' + offsetY + ')'

      return [offsetX, offsetY]
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
