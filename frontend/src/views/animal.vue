<template>
    <div class="body">
        <div class="head">
            <h1 class="float-start name"  >{{animal.name}}</h1>
            <small class="float-start status" :class="animal.statusH">{{animal.status}}</small>
        </div>
        <small class="tree float-end">{{animal.tree}}</small>
        <center>
            <div style="position:static">            
                <img :src="animal.image_url" :alt="animal.name" class="img">
            </div>
        </center>
        
        <div class="description">
            <center class="float-end qr">
                <qr-code 
                    :text='find_url()'
                    size="100"                         
                    error-level="H"
                    class="mt-2"
                    >                    
                </qr-code>  
                <span class="mb-5">
                    <small>
                        keep reading on other device
                    </small>
                </span>                
            </center>            
            <p class="p">
                {{animal.description}}
                <small class="float-end ">
                    <a class="source" :href="animal.link">
                        ({{animal.source}}) 
                    </a>                    
                </small>                
            </p>                                   
        </div>
        <div id="carouselExampleFade" class="carousel slide carousel-fade" data-bs-ride="carousel">
            <div class="carousel-inner">
                <div class="carousel-item active">
                <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                <img src="..." class="d-block w-100" alt="...">
                </div>
                <div class="carousel-item">
                <img src="..." class="d-block w-100" alt="...">
                </div>
            </div>
            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
            </button>
            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleFade" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
            </button>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import VueQRCodeComponent from 'vue-qrcode-component'
import bootstrap from 'bootstrap'


export default {
    
    name:'Animal',
    components: {
        'qr-code': VueQRCodeComponent
    },
    data(){
        return {
           animal: {
           }, 
        }
    },
    mounted(){
        this.getAnimal()
    },
    
    methods: {      
        getAnimal(){
            const animal_slug = this.$route.params.animal_slug

            axios
                .get(`/api/v1/animals/${animal_slug}`)
                .then(response => {
                    this.animal = response.data
                })
                .catch(error => {
                    console.log(error)
                })
        },
        find_url() {
            var curr_url = window.location.href;
            return curr_url
        }
    }
}

</script>
<style scoped>
.body{
    border-radius: 25px;
    height: 100%;
    color: whitesmoke;
    text-align: center;
    position: relative;
}
.head{
    margin: 2px;
}
.img{
    height:500px;
    width:750px;
    border-radius: 5px 250px;
    position: inherit;
    margin-left: 15%;
    margin-right: 15%;
    
}
.tree{
    color: aquamarine;
    margin: 30px;
}
.description{
    height: 250px;
    color: bisque;
    margin: 30px;
    background-color: rgba(9, 41, 13, 0.363);
    text-align: justify;
    border-radius: 35px;
    text-indent: 50px;
    position: relative;
}
.source{
    color: brown;
}
.p{
    
    padding: 2%;
}

.name{
    color:rosybrown;
    padding-left: 15px;
    padding-top: 15px;
}
.status{
    padding-top: 15px;
}
.qr {
    height: 150px;
    width: 200px;
    border: green dotted;
    margin: 10px;
    margin-top: 30px;
    color: burlywood;
    border-radius: 35px;
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
.slider {
    width: 500px;
    height: 300px;
    background-color: yellow;
    margin-left: auto;
    margin-right: auto;
    margin-top: 0px;
    text-align: center;
    overflow: hidden;
}
.image-container {
    width: 1500px;
    background-color: pink;
    height: 300px;
    clear: both;
    position: relative;
    -webkit-transition: left 2s;
    -moz-transition: left 2s;
    -o-transition: left 2s;
    transition: left 2s;
}

</style>