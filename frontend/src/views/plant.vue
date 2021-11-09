<template>
    <div class="body">
        <div class="head">
            <h1 class="float-start name"  >{{plant.name}}</h1>
            <small class="float-start status" :class="plant.status">{{plant.statusH}}</small>
        </div>
        <small class="tree float-end">{{plant.tree}}</small><br>
        <img :src="plant.image_url" :alt="plant.name" class="img"><br>
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
                {{plant.description}}
                <small class="float-end ">
                    <a class="source" :href="plant.link">
                        ({{plant.source}}) 
                    </a>                    
                </small>                
            </p>                                   
        </div>        
    </div>
</template>


<script>
import axios from 'axios'
import VueQRCodeComponent from 'vue-qrcode-component'


export default {
    name:'Plant',
    components: {
        'qr-code': VueQRCodeComponent
    },
    data(){
        return {
           plant: {
           }, 
        }
    },
    mounted(){
        this.getPlant()
    },
    
    methods: {
        getPlant(){
            const plant_slug = this.$route.params.plant_slug

            axios
                .get(`/api/v1/plants/${plant_slug}`)
                .then(response => {
                    this.plant = response.data
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
    position: relative;
    margin-left: -20px;
    margin-top: 4%;
    margin-bottom: 4%;
}
.tree{
    color: aquamarine;
    margin-right: 15px;
    margin-top: 15px;
}
.description{
    color: bisque;
    margin: 15px;
    background-color: rgba(9, 41, 13, 0.363);
    text-align: justify;
    border-radius: 35px;
    text-indent: 50px;
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
 color: rgb(255, 136, 0);

}
.LC {
 color: black;
  text-align:center;

}
.EX {
 color: black;
  text-align:center;

}
.EW {
  color: red;

}
.CR {
 color: black;
  text-align:center;

}
.VU {
 color: black;
  text-align:center;

}
.NT {
 color: black;
  text-align:center;

}
.CD {
 color: black;
  text-align:center;

}
.DD {
 color: black;
  text-align:center;

}
.NE {
 color: black;
  text-align:center;

}
</style>