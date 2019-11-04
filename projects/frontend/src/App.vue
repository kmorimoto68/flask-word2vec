<template>
  <div id='app'>
    <img alt='Vue logo' src='./assets/logo.png' style='height: 50px' />
    <word2vec />
  </div>
</template>

<script>
import word2vec from './components/word2vec.vue'

export default {
  name: 'app',
  components: {
    word2vec
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
