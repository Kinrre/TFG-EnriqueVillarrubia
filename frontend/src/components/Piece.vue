<template>
  <div :style="piece_style"></div>
</template>

<script>
export default {
  name: 'Piece',
  props: {
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
      piece_style: {
        height: this.props_style.size + '%',
        width: this.props_style.size + '%',
        position: 'absolute',
        transform: 'translate(' + this.props_style.offsetX + '%, ' + this.props_style.offsetY + '%)',
        backgroundImage: this.getPiece(),
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'contain',
        pointerEvents: 'none'
      }
    }
  },
  methods: {
    getPiece() {
      return 'url(' + require('@/assets/pieces/' + this.props_style.color + '/' + this.props_style.color + '_' + this.props_style.piece + '.png') + ')'
    }
  }
}
</script>

<style>
</style>
