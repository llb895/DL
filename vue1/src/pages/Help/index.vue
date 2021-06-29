<template lang="html">
  <section class="df-feedback">
    <div class="main-wrapper">
      <div class="main">
        <div class="helpBackground">
          <div class="declaration">
            <div class="help_headline">
             1. What is DESSO (DEep Sequence and Shape mOtif) and what can it provide for users?<br/>
            </div>
            DESSO is a database/web server that provides all identified sequence and shape motifs from a homonymous framework developed by us.
            This framework contains a deep learning model for motif pattern learning and a novel statistical model for motif instance identification.
            The performance of this framework was evaluated on the 690 ENCODE ChIP-seq
            <br/><br/>
            <div style="border:1px solid rgba(204,204,204,0.38)"></div>
            <br/>
            <div class="help_headline">
            2. What is DNA sequence motif?<br/>
            </div>
            A DNA motif is a region of DNA that regulates the expression of downstream genes located on that same molecule of DNA, i.e., a chromosome.
            This concept is equivalent to a DNA cis-regulatory element or cis-element. It contains the transcription factor binding sites (TFBSs) and
            other conserved functional elements in the five intergenic regions of genes.
            <br/><br/>
            <div style="border:1px solid rgba(204,204,204,0.38)"></div>
            <br/>
            <div class="help_headline">
            3. What is DNA shape?<br/>
            </div>
            DNA shape represents three-dimensional structure information of the corresponding DNA sequences and play an important role in TF-DNA recognition.
            Four distinct DNA shape features (i.e., Minor Groove Width (MGW), Propeller Twist (ProT), Helix Twist (HelT), and Roll) can be computationally
            derived from DNA sequences based on the Monte Carlo simulation.
            <br/><br/>
            <div style="border:1px solid rgba(204,204,204,0.38)"></div>
            <br/>
             <div class="help_headline">
            4. What is shape motif?<br/>
            </div>
           Shape motif indicates conserved DNA shape patterns that are involved in TF-shape readouts recognition. Shape motifs are conserved in shape level
            but not necessarily in sequence level.
            <br/><br/>
            <div style="border:1px solid rgba(204,204,204,0.38)"></div>
            <br/>
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
