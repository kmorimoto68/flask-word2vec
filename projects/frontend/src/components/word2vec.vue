<template>
  <div id='container'>
    <input v-model='keyword' @blur='getWord2vec()' placeholder='edit me' /><br />
    <div id='mynetwork'></div>
    <input v-model='positive' @blur='calcSubtraction()' placeholder='positive' /> - 
    <input v-model='negative' @blur='calcSubtraction()' placeholder='negative' /><br />
    <div v-for='(item, key) in results' :key='key'>
      {{ item.word }} : {{ item.value }}
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import vis from 'vis-network'

Vue.config.productionTip = false

export default {
  name: 'word2vec',
  data() {
    return {
      keyword: 'test',
      positive: '',
      negative: '',
      results: [],
      nodes: [],
      edges: [],
      options: {
        manipulation: {
            enabled: true,
            initiallyActive: true,
            addEdge: function(edgeData, callback) {
                callback(edgeData);
            }
        },
        nodes: {
            shape: "circle",
            /*scaling: {
              customScalingFunction: function(min, max, total, value) {
                return value / total;
              },
              min: 1,
              max: 50
            }*/
        }
      },
      container: '',
    }
  },
  computed: {
    graph_data() {
        return {
            nodes: this.nodes,
            edges: this.edges
        }
    }
  },
  mounted() {
      this.container = document.getElementById('mynetwork');
      this.network = new vis.Network(this.container, this.graph_data, this.options);
  },
  methods: {
    search(word) {
      this.keyword = word
      this.getWord2vec()
    },
    getWord2vec() {
      axios.get(`http://localhost:5000/ww?keyword=${this.keyword}`)
        .then(r =>  {
          this.results = r.data.results

          this.nodes.splice(0, this.nodes.length);
          this.edges.splice(0, this.edges.length);

          this.nodes.push({id: 0, label: this.keyword, color: '#F5A9A9'})
          for (const [key, value] of Object.entries(this.results)) {
            const index = +key + 1
            const node = {
              id: index,
              label: value.word.replace('[', '').replace(']', ''),
              color: '#F6CECE'
            }
            const edge = {
              from: 0,
              to: index,
              color: { color: '#ff0000', opacity: value.value }
            }
            this.nodes.push(node)
            this.edges.push(edge)
          }
          this.container = document.getElementById('mynetwork');
          this.network = new vis.Network(this.container, this.graph_data, this.options);
          const _this = this;
          this.network.on('click', function(properties) {
            var ids = properties.nodes;
            if (_this.nodes[ids]) {
              _this.search(_this.nodes[ids].label)
            }
          });
        })
    },
    calcSubtraction() {
      axios.get(`http://localhost:5000/calc?positive=${this.positive}&negative=${this.negative}`)
        .then(r =>  {
          this.results = r.data.results

          this.nodes.splice(0, this.nodes.length);
          this.edges.splice(0, this.edges.length);

          this.nodes.push({id: 0, label: this.keyword, color: '#F5A9A9'})
          for (const [key, value] of Object.entries(this.results)) {
            const index = +key + 1
            const node = {
              id: index,
              label: value.word.replace('[', '').replace(']', ''),
              color: '#F6CECE'
            }
            const edge = {
              from: 0,
              to: index,
              color: { color: '#ff0000', opacity: value.value }
            }
            this.nodes.push(node)
            this.edges.push(edge)
          }
          this.container = document.getElementById('mynetwork');
          this.network = new vis.Network(this.container, this.graph_data, this.options);
          const _this = this;
          this.network.on('click', function(properties) {
            var ids = properties.nodes;
            if (_this.nodes[ids]) {
              _this.search(_this.nodes[ids].label)
            }
          });
        })
    }
  },
  created: function () {
    this.getWord2vec()
  }
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>
  #container {
    padding: 20px;
  }
  #mynetwork {
      width: 600px;
      height: 600px;
      margin:  0 auto;
  }
</style>
