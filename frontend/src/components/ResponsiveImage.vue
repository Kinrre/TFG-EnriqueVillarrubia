<template>
  <div :style="div_size">
    <img :src="require('@/assets/' + name)" :style="img_size">
  </div>
</template>

<script>
export default {
  name: 'ResponsiveImage',
  props: {
    name: String
  },
  data() {
    return {
      div_size: {
        height: '100%',
        width: '100%'
      },
      img_size: {
        height: '100%',
        width: '100%',
        objectFit: 'contain' /* Preserve the aspect ratio */
      }
    }
  }
}
</script>

<style>

</style>
