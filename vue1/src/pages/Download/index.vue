<template lang="html">
  <section class="df-feedback">
    <div class="main-wrapper">
      <div class="main">
        <div class="helpBackground">
          <div class="declaration">
              <table class=table11_6 align="center">
                <tr>
                  <th></th><th>File Name</th><th>Description</th><th>Release Dtae</th><th>Size</th>
                </tr>
                <tr>
                  <td><img src='./download.jpg' class="download_image" /></td><td>xxx.zip</td><td><a href="https://github.com/llb895/DL">Source code + example data</a></td><td>2021/7/4</td><td>SAMPLE</td>
                </tr>
                <tr>
                  <td><img src='./download.jpg' class="download_image" /><td>xxx-whole.zip</td><td><a href="https://github.com/llb895/DL">Source code + whole data</a></td><td>2021/7/4</td><td>SAMPLE</td>
                </tr>
                <tr>
                  <td><img src='./download.jpg' class="download_image" /><td>SAMPLE</td><td>SAMPLE</td><td>SAMPLE</td><td>SAMPLE</td>
                </tr>
                <tr>
                  <td><img src='./download.jpg' class="download_image" /><td>SAMPLE</td><td>SAMPLE</td><td>SAMPLE</td><td>SAMPLE</td>
                </tr>
              </table>

          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<style lang="stylus" scoped>
@import '../../common/stylus/common'

td{
    text-align:center;
  }

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
        box-shadow 0px 1px 1px rgba(0, 0, 0, .2)
        line-height 1.5em
        color black
</style>
