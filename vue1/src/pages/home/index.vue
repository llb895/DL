<template lang="html">
  <section class="df-feedback">
    <div class="main-wrapper">
      <div class="main">
        <div class="ContactUsBackground">
          <div class="declaration">
          <div class="main-wrapper">

            <div style="width:100%;text-align:center">
            <el-row display="margin-top:10px">
            <el-input v-model="input" placeholder="请输入 batch" style="display:inline-table; width: 50%; float:left"></el-input>
            <el-input v-model="input1" placeholder="请输入 seq_len" style="display:inline-table; width: 50%;"></el-input><br/>
              <el-button type="primary" @click="home_submit()" style="float:left; margin: 2px;">提交</el-button>
            </el-row>

<br/>


              <div>output:{{m}}</div>
              <div>hn:{{f}}</div>
              <div>cn:{{g}}</div>

            </div>

            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="stylus" scoped>
@import '../../common/stylus/common'

.df-feedback
  margin-top 10px

  .main-wrapper
    fj(center)

    .main
      width 80%

      .declaration
        padding 40px
        border 1px solid black
        border-radius 10px
        box-shadow 0 1px 1px rgba(0, 0, 0, .2)
        line-height 1.5em
        color black

      .declaration1
        width 500px
        height 390px
        border 1px solid black
        border-radius 10px
        box-shadow 0 1px 1px rgba(0, 0, 0, .2)
        line-height 1.5em
        color black
</style>

<script>
export default {
  name: 'DANQ',
  data () {
    return {
      input: '',
      input1: '',
      m: '',
      f: '',
      g: ''
    }
  },
  methods: {
    home_submit () {
      this.$http.get('http://127.0.0.1:8000/api/home_submit', {params: {a: this.input, b: this.input1}})
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.m = res['m']
            this.f = res['f']
            this.g = res['g']
            console.log(res['msg'])
          } else {
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
