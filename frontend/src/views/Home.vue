<template>
  <div>
    <center>
            <div class="row container-md m-5  rounded">            
                <div class="col">
                    <br><br>
                    <center><router-link aria-current="page"  to="/animals"><h3 class="animal_main">Animals in Syria</h3></router-link></center>              
                    <p class="animal_text">
                        Wild animal life is sparse. Wolves, hyenas, foxes, badgers, wild boar, and jackals can still be found in remote areas. Deer, bears, squirrels, and such small carnivores as martens and polecats are also found, while desert animals include gazelles and jerboas (nocturnal jumping rodents). Vipers, lizards, and chameleons are common in the desert. Eagles, buzzards, kites, and falcons frequent the mountains. Harmful insects include mosquitoes, sandflies, grasshoppers, and occasionally locusts. The mule is the beast of burden in the mountains, and the camel on the steppe. Other domesticated animals include horses, donkeys, cattle, sheep, goats, and chickens. Bees also are kept.
                    </p>
                    <small><a href="https://www.britannica.com/place/Syria/The-winds" class="float-end" style="color: cornsilk;">(Britannica)</a></small>
                </div>             
                <div class="col-6">
                    <img src="../assets/img/animalsSyria.png" class="float-end">
                </div>                       
            </div>
        </center>
        <center>
            <div class="row container-md m-5  rounded">              
                <div class="col-6">
                    <img src="../assets/img/animalsSyria.png" class="float-end">
                </div>             
                <div class="col">
                    <center><router-link aria-current="page"  to="/plants"><h3 class="animal_main">Plants in Syria</h3></router-link></center>              
                    <p class="animal_text">
                      Yew, lime, and fir trees grow on the mountain slopes. The date palm is found in the Euphrates valley. In both coastal and inland regions, plants include grains, olive trees, grapevines, apricot trees, oaks, and poplars. Lemon and orange trees grow along the coast. Garigue, a degenerate Mediterranean scrub, and maquis, a thick scrubby underbrush, cover many slopes.
Forests make up only a very small percentage of the country’s total area and are primarily found in the mountains, especially in the Al-Anṣariyyah Mountains. Glossy-leaved and thorny drought-resistant shrubs such as myrtle, boxwood, turpentine, broom, arbutus, and wild olive abound to the south. Excessive exploitation of the forests for their wood has largely turned them into scrub. A reforestation project has been undertaken in the mountains north of Latakia, however, and some forests are protected by the government. Commercially important forest plants include sumac, which is used as a spice, wild pistachio, which is important for its oil-rich fruit, laurel, which is used in the production of cosmetics, and mulberry, whose leaves are fed to silkworms. Pine tree branches are used for smoking tobacco leaves. Other useful plants are winter vegetables such as khubbayzah, a kind of spinach; ʿakkūb, a flowering plant; and truffles. Licorice is widely exploited for its root, which is used in the pharmaceutical industry.
The steppe is characterized by the absence of natural tree cover, except for some sparsely distributed hawthorns. All other trees—such as those in the orchards of Damascus and Aleppo and along the banks of the Orontes and Euphrates rivers—are cultivated.
For a brief period before June, the land is covered with a variety of flowering and grassy plants. Under the implacable sun of June, however, the plants soon wither, casting off their seeds onto the dry ground.
                    </p>
                    <small><a href="https://www.britannica.com/place/Syria/The-winds" class="float-end" style="color: cornsilk;">(Britannica)</a></small>
                </div>                     
            </div>
        </center>
  </div>
</template>

<script>
// @ is an alias to /src


export default {
  name: 'Home',
  components: {
    
  }
}
</script>
<style scoped>
.row{
    padding-top: 15px;
    padding-bottom: 15px;
}
</style>
