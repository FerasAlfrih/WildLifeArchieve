9<template>
  <div class="container">
    <div class="row">
      <div class="blur"  style="width:30rem;  text-align: center;"  v-for='plant in plants' v-bind:key="plant.id">
        <div class="clear" >
          <center><h3 class="">{{plant.name}}</h3></center>
          <div class="">
            <figure class="">
              <img class="rounded-pill border" v-bind:src="plant.thumbnail_url" :alt="plant.name" height="200" width="400" />
              <div id="top-left " :class="plant.status"><p class="top-left-text" >{{plant.statusH}}</p></div> 
            </figure>      
            <p class="">{{plant.description.substring(0,200)+"..."}} <router-link v-bind:to="'/plants/'+plant.slug">read more</router-link></p>
          </div>  
        </div>               
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Plants',
  data() {
    return{
      plants: [],
      speciess:[],
      genuss:[],
      familys:[],
      orders:[],
      classes:[],
      phylums:[],
      kingdoms:[],
      domains:[],
    }    
  },
 
  methods: {
    
    getPlants() {
      axios
        .get('api/v1/plants')
        .then(response => {
          this.plants = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getSpeciess() {
      axios
        .get('api/v1/plants/speciess')
        .then(response => {
          this.speciess = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getGenuss() {
      axios
        .get('api/v1/plants/genuss')
        .then(response => {
          this.genuss = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getFamilys() {
      axios
        .get('api/v1/plants/familys')
        .then(response => {
          this.familys = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getOrders() {
      axios
        .get('api/v1/plants/orders')
        .then(response => {
          this.orders = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getClasses() {
      axios
        .get('api/v1/plants/classes')
        .then(response => {
          this.classes = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getPhylums() {
      axios
        .get('api/v1/plants/phylums')
        .then(response => {
          this.phylums = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getKingdoms() {
      axios
        .get('api/v1/plants/kingdoms')
        .then(response => {
          this.kingdoms = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getDomains() {
      axios
        .get('api/v1/plants/domains')
        .then(response => {
          this.domains = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },  
  },
   mounted() {
    this.getPlants(),
    this.getSpeciess(),
    this.getGenuss(),
    this.getFamilys(),
    this.getOrders(),
    this.getClasses(),
    this.getPhylums(),
    this.getKingdoms(),
    this.getDomains()
  }
}

</script>
<style scoped>
.blur { 
  width: 400;
  height: 500;
  position: relative;
  border: 5px ;
  padding: 10px;
  margin: 25px;
  border-radius: 35px;
}

.clear {
  width: 460px;
  height: 350px;
  position: relative;
  color: rgb(206, 241, 214);
  border-radius: 25px;
}
.EN {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: rgb(248, 4, 248);
  color: gold;
  border: gold solid;
  border-radius: 50%;  
  opacity:60% ;

}
.LC {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: blue;
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.EX {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: black;
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.EW {
  height: 110px;
  width: 110px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color:rgb(252, 4, 4);
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.CR {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: rgb(255, 0, 0);
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.VU {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: rgb(255, 102, 0);
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.NT {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: rgb(183, 0, 255);
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.CD {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: rgb(61, 16, 167);
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.DD {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: rgb(255, 166, 0);
  color: rgb(8, 8, 8);
  border: rgb(8, 8, 8) solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}
.NE {
  height: 100px;
  width: 100px;
  position: absolute;
  top: 50px;
  left: 50px;  
  background-color: rgb(17, 141, 48);
  color: gold;
  border: gold solid;
  border-radius: 50%;
  opacity:60% ;
  text-align:center;

}

.top-left-text{
  transform: rotate(-30deg);  
  text-align: center;
  position: absolute;
  top: 32%;
  left: 17%;
  height: 100px;
  width: 100px;
  opacity: 100%; 
  font-size: 80%;
}
</style>