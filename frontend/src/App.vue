<template>
  <div class="container-fluid">          
    <nav class="navbar navbar-expand-lg navbar-dark bg-transparent ">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">SWL</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                      <router-link class="nav-link active" aria-current="page"  to="/">Home</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link active" aria-current="page"  to="/plants">Plants</router-link>
                    </li>
                    <li class="nav-item">
                        <router-link class="nav-link active" aria-current="page"  to="/animals">Animals</router-link>
                    </li>
                    <li class="nav-item">
                      <router-link class="nav-link active" aria-current="page"  to="/about">About</router-link>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                        Menu
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="#">Action</a></li>
                        <li><a class="dropdown-item" href="#">Another action</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">Something else here</a></li>
                        </ul>
                    </li>
                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>    
  <router-view/><br>
    <footer class="footer fix-bottom">
      <big class="copy">Copyrights &copy;2021 <a class="copy" href="#">Safirasoft</a></big>
    </footer>
  </div>
</template>

<script>
  import axios from 'axios'

  export default{
    name:'Home',
    methods:{
        
    }
   
  }
  
</script>


<style lang="scss">
@import '../node_modules/bootstrap/scss/bootstrap.scss';
@import "bootstrap";

.body {
  background: rgb(17,82,7);
background: linear-gradient(90deg, rgba(17,82,7,1) 0%, rgba(144,180,50,1) 72%, rgba(156,240,143,1) 100%);
}
.animal_main {
  color: gold;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
    Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  font-style: italic;
  font-weight: bolder;
  font-size: x-large;
}
.animal_text {
  color: cornsilk;
  font-family: cursive;
}
.dropdown-item {
  color: cornsilk;
}
.dropdown-item :hover {
  color: seagreen;
}
.dropdown-menu {
  background-color: seagreen;
}
.footer{
  text-align: center;
  margin-top: 15px;
}
.copy{
  color: wheat;
}
p{
  color: whitesmoke;
}
h4{
  color: gold;
}

</style>
