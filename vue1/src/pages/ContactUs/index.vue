<template lang="html">
  <section class="df-feedback">
    <div class="main-wrapper">
      <div class="main">
        <div class="ContactUsBackground">
          <div class="declaration">
          <div class="main-wrapper">
            <div class="declaration1">


            <div style="width:100%;text-align:center"><br/>
              <div class="ContactUsDiv"style="text-align:center">
               Comments
             </div>
              <el-form :rules="rules">
              <el-input v-model="input" placeholder="Name" style="display:inline-table; width: 70%;"></el-input>
              <br/><br/>
              <el-input v-model="input1" placeholder="E-mail" style="display:inline-table; width: 70%;"></el-input>
              <br/><br/>
              <el-input type="textarea" :rows="4" placeholder="Add your comments here" v-model="input2" style="display:inline-table; width: 70%;"></el-input> <br/><br/>
              <el-button type="primary" @click="submit()" style=" margin: 2px;">Submit</el-button>

            </el-form>
            </div>

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
  name: 'Commment',
  data () {
    return {
      input: '',
      input1: '',
      input2: ''
    }
  },
  methods: {
    submit () {
      this.$http.get('api/submitcomment', {params: {name: this.input, email: this.input1, comments: this.input2}})
     // this.$http.get('http://127.0.0.1:8000/api/submitcomment?email=' + this.input1)
     // this.$http.get('http://127.0.0.1:8000/api/submitcomment?comments=' + this.input2)
        .then((response) => {
          var res = JSON.parse(response.bodyText)
          if (res.error_num === 0) {
            this.$message.error('success')
          } else {
            this.$message.error('failed')
            console.log(res['msg'])
          }
        })
    }
  }
}
</script>
