<template>
  <div class="container">
    <div class="row">
      <div class="blur"  style="width:30rem;  text-align: center;"  v-for='animal in animals' v-bind:key="animal.id">
        <div class="clear" >
          <center><h4 class="">{{animal.name}}</h4></center>
          <div class="">
            <figure class="">
              <div id="top-left" class="st-content"><div class="st base" ><span :class="animal.statusH">{{animal.status}}</span></div></div>
              <img class="rounded-pill border" v-bind:src="animal.thumbnail_url" :alt="animal.name" height="200" width="400" />
            </figure>      
            <p class="">{{animal.description.substring(0,200)+"..."}} <router-link v-bind:to="'/animals/'+animal.slug">read more</router-link></p>
          </div>  
        </div>               
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'Animals',
  data() {
    return{
      animals: [],
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
    
    getAnimals() {
      axios
        .get('api/v1/animals')
        .then(response => {
          this.animals = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getSpeciess() {
      axios
        .get('api/v1/animals/speciess')
        .then(response => {
          this.speciess = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getGenuss() {
      axios
        .get('api/v1/animals/genuss')
        .then(response => {
          this.genuss = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getFamilys() {
      axios
        .get('api/v1/animals/familys')
        .then(response => {
          this.familys = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getOrders() {
      axios
        .get('api/v1/animals/orders')
        .then(response => {
          this.orders = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getClasses() {
      axios
        .get('api/v1/animals/classes')
        .then(response => {
          this.classes = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getPhylums() {
      axios
        .get('api/v1/animals/phylums')
        .then(response => {
          this.phylums = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getKingdoms() {
      axios
        .get('api/v1/animals/kingdoms')
        .then(response => {
          this.kingdoms = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },
    getDomains() {
      axios
        .get('api/v1/animals/domains')
        .then(response => {
          this.domains = response.data
        })
        .catch(error =>{
          console.log(error)
        })
    },    
    // async Note() {
    //   const danger = document.getElementsByClassName("top-left-text");
    //   for (let i = 0; i < danger.length; i++){
    //     if (danger[i].textContent === "InDanger"){
    //       var ele = document.getElementById("top-left");
    //       ele.style.border= 'rgb(155, 5, 5) solid';          
    //       ele.style.backgroundColor= 'Red';

    //     } 
    //   }

    // }
     
  },
   mounted() {
    this.getAnimals(),
    this.getSpeciess(),
    this.getGenuss(),
    this.getFamilys(),
    this.getOrders(),
    this.getClasses(),
    this.getPhylums(),
    this.getKingdoms(),
    this.getDomains()
    // this.Note()
  }, 
  updated(){
  //  this.Note()
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
  border-radius: 25px;
}

.st{ 
  position: absolute;
  top: 75px;
  right: 30px;
  padding: 15px;
  border-top-right-radius: 35%;
  border-bottom-right-radius: 35%;
}
.st-content{
  height: 40px;
  width: 65%;
  position: relative; 
  width: 100%; 
  height: 100%; 
}
.st.base {
    background: #131313;
    color: #fff;
    opacity: 75%;
}

.st:before, .st:after {
    content: '';
    position: absolute;
    left: -9px;
    border-left: 10px solid transparent;
}
.st:before {
  content: attr(content);
    top: 0;
}
.st:after {
    bottom: 0;
}
.st.base:before {
    border-top: 27px solid #131313;
}
.st.base:after {
    border-bottom: 27px solid #131313;
}
.st span {
    display: block;
    font-size: 16px;
    font-weight: 600;
    top: 5px;
}

.EN {
 color: rgb(248, 4, 4);


}
.LC {
  color: rgb(14, 207, 241);
  text-align:center;

}
.EX {
 color: rgb(100, 82, 82);
  text-align:center;

}
.EW {
  color: rgb(63, 5, 5);

}
.CR {
 color: rgb(255, 0, 128);
  text-align:center;

}
.VU {
 color: rgb(255, 153, 0);
  text-align:center;

}
.NT {
 color: blueviolet;
  text-align:center;

}
.CD {
 color: blue;
  text-align:center;

}
.DD {
 color: whitesmoke;
  text-align:center;

}
.NE {
 color: rosybrown;
  text-align:center;

}
</style>