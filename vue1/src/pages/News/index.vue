<template lang="html">
  <section class="df-feedback">
    <div class="main-wrapper">
      <div class="main">
        <div class="helpBackground">
          <div class="declaration">

            <table class=newsTable_table>
                  <th class="newsTable_th">Issue:</th>
            </table>
            <div class="news_date">
              &nbsp;Aug 20 2019<br/>
            </div>
            <div class="news_content">
              &nbsp;We are updating a new GPU for our web server, the find motif section has been temporarily disabled.<br/>
              &nbsp;Please build DESSO from source code: https://github.com/viyjy/DESSO
            </div><br/>


            <table class=newsTable_table>
                  <th class="newsTable_th">Updates:</th>
            </table>
            <div class="news_date">
              &nbsp;Jul 22 2019<br/>
            </div>
            <div class="news_content">
              &nbsp;The manuscript “Prediction of Regulatory Motifs from Human ChIP-Sequencing Data using a Deep Learning Framework” has been<br/>
              &nbsp;officially accepted by Nucleic Acids Research! https://doi.org/10.1093/nar/gkz672
            </div><br/>

            <table class=newsTable_table>
                  <th class="newsTable_th">Updates: explanations</th>
            </table>
            <div class="news_date">
              &nbsp;Apr 21 2019<br/>
            </div>
            <div class="news_content">
              &nbsp;Added explanations next to various sections titles.
            </div><br/>

            <table class=newsTable_table>
                  <th class="newsTable_th">Updates: FAQ</th>
            </table>
            <div class="news_date">
              &nbsp;Sep 2 2018<br/>
            </div>
            <div class="news_content">
              &nbsp;Updated the DESSO FAQ page.
            </div><br/>


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
        box-shadow 0px 1px 1px rgba(0, 0, 0, .2)
        line-height 1.5em
        color black
</style>
